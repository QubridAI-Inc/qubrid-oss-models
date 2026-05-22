#!/usr/bin/env python3
"""
Prompt Studio — generate HTML/CSS/JS from a prompt via Qwen3.7-Max on Qubrid.

Part of One Click Apps. Stdlib only.

  python app.py
"""

from __future__ import annotations

import http.client
import json
import ssl
import sys
import threading
import urllib.error
import urllib.request
import webbrowser
from http import HTTPStatus
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

PORT = 7848
QUBRID_CHAT_URL = "https://platform.qubrid.com/v1/chat/completions"
MODEL = "Qwen/Qwen3.7-Max"
DEFAULT_MAX_TOKENS = 16384
MAX_TOKENS_CAP = 32768
MIN_MAX_TOKENS = 1024
APP_DIR = Path(__file__).resolve().parent

SYSTEM_PROMPT = """You are an expert front-end developer. The user will describe a UI, page, widget, or interactive experience.

Your job: output ONE complete, self-contained HTML document that implements their request.

Rules:
- Start with <!DOCTYPE html> and include <html>, <head>, and <body>.
- Put ALL CSS in a <style> tag in <head>. Put ALL JavaScript in a <script> tag before </body>.
- Do NOT use external URLs: no CDN links, no Google Fonts, no npm, no import maps.
- Use only vanilla HTML, CSS, and JavaScript.
- Make it visually polished: thoughtful layout, color, typography (system fonts), spacing, and subtle animation where appropriate.
- The result must run offline in a browser iframe with zero network dependencies.
- Output ONLY the HTML document. No markdown fences, no explanation before or after."""


class PromptStudioHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(APP_DIR), **kwargs)

    def log_message(self, format: str, *args) -> None:
        if args and isinstance(args[0], str) and args[0].startswith(("GET /api", "POST /api")):
            return
        super().log_message(format, *args)

    def end_headers(self) -> None:
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self) -> None:
        self.send_response(HTTPStatus.NO_CONTENT)
        self.end_headers()

    def do_GET(self) -> None:
        if self.path == "/favicon.ico":
            self.send_response(HTTPStatus.NO_CONTENT)
            self.end_headers()
            return
        if self.path in ("/", "/index.html"):
            self.path = "/index.html"
        super().do_GET()

    def do_POST(self) -> None:
        if self.path != "/api/generate":
            self.send_error(HTTPStatus.NOT_FOUND, "Not found")
            return

        length = int(self.headers.get("Content-Length", 0))
        try:
            payload = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            self._json_response(HTTPStatus.BAD_REQUEST, {"error": "Invalid JSON body"})
            return

        api_key = (payload.get("api_key") or "").strip()
        prompt = (payload.get("prompt") or "").strip()

        if not api_key:
            self._json_response(HTTPStatus.BAD_REQUEST, {"error": "API key is required"})
            return
        if not prompt:
            self._json_response(HTTPStatus.BAD_REQUEST, {"error": "Prompt is required"})
            return

        max_tokens = int(payload.get("max_tokens", DEFAULT_MAX_TOKENS))
        max_tokens = max(MIN_MAX_TOKENS, min(MAX_TOKENS_CAP, max_tokens))

        body = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            "max_tokens": max_tokens,
            "temperature": float(payload.get("temperature", 0.6)),
        }

        use_stream = payload.get("stream", True)

        try:
            if use_stream:
                self._stream_generate(api_key, body, max_tokens)
            else:
                self._json_generate(api_key, body, max_tokens)
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            try:
                parsed = json.loads(detail)
            except json.JSONDecodeError:
                parsed = {"error": detail or exc.reason}
            self._json_response(exc.code, parsed)
        except urllib.error.URLError as exc:
            self._json_response(
                HTTPStatus.BAD_GATEWAY,
                {"error": f"Could not reach Qubrid API: {exc.reason}"},
            )

    def _json_generate(self, api_key: str, body: dict, max_tokens: int) -> None:
        upstream = self._call_qubrid(api_key, body)
        choice = (upstream.get("choices") or [{}])[0]
        raw = (choice.get("message") or {}).get("content", "")
        self._json_response(
            HTTPStatus.OK,
            {
                "raw": raw,
                "model": upstream.get("model", MODEL),
                "usage": upstream.get("usage"),
                "finish_reason": choice.get("finish_reason"),
                "max_tokens": max_tokens,
            },
        )

    def _stream_generate(self, api_key: str, body: dict, max_tokens: int) -> None:
        stream_body = {**body, "stream": True}
        data = json.dumps(stream_body).encode("utf-8")

        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache, no-store")
        self.send_header("Connection", "keep-alive")
        self.send_header("X-Accel-Buffering", "no")
        self.end_headers()

        finish_reason = None
        usage = None
        model = MODEL

        def emit(event: dict) -> None:
            payload = f"data: {json.dumps(event, ensure_ascii=False)}\n\n".encode("utf-8")
            self.wfile.write(payload)
            self.wfile.flush()

        def process_upstream_line(line: str) -> None:
            nonlocal finish_reason, usage, model
            if not line or line == "data: [DONE]":
                return
            if not line.startswith("data: "):
                return
            try:
                chunk = json.loads(line[6:])
            except json.JSONDecodeError:
                return

            if chunk.get("model"):
                model = chunk["model"]
            if chunk.get("usage"):
                usage = chunk["usage"]

            for choice in chunk.get("choices") or []:
                if choice.get("finish_reason"):
                    finish_reason = choice["finish_reason"]
                delta = choice.get("delta") or {}
                content = delta.get("content")
                if content:
                    emit({"type": "delta", "content": content})

        try:
            parsed = urlparse(QUBRID_CHAT_URL)
            ctx = ssl.create_default_context()
            conn = http.client.HTTPSConnection(
                parsed.hostname,
                parsed.port or 443,
                timeout=300,
                context=ctx,
            )
            try:
                path = parsed.path or "/v1/chat/completions"
                conn.request(
                    "POST",
                    path,
                    body=data,
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json",
                        "Accept": "text/event-stream",
                    },
                )
                res = conn.getresponse()
                if res.status >= 400:
                    detail = res.read().decode("utf-8", errors="replace")
                    try:
                        parsed_err = json.loads(detail)
                        err = parsed_err.get("error", parsed_err)
                        if isinstance(err, dict):
                            err = err.get("message", str(err))
                    except json.JSONDecodeError:
                        err = detail or res.reason
                    emit({"type": "error", "error": str(err)})
                    return

                buf = b""
                while True:
                    chunk = res.read(1024)
                    if not chunk:
                        break
                    buf += chunk
                    while b"\n" in buf:
                        raw_line, buf = buf.split(b"\n", 1)
                        line = raw_line.decode("utf-8", errors="replace").strip()
                        process_upstream_line(line)

                tail = buf.decode("utf-8", errors="replace").strip()
                if tail:
                    process_upstream_line(tail)
            finally:
                conn.close()

            emit(
                {
                    "type": "done",
                    "finish_reason": finish_reason,
                    "usage": usage,
                    "model": model,
                    "max_tokens": max_tokens,
                }
            )
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            try:
                parsed = json.loads(detail)
                err = parsed.get("error", parsed)
                if isinstance(err, dict):
                    err = err.get("message", str(err))
            except json.JSONDecodeError:
                err = detail or exc.reason
            emit({"type": "error", "error": str(err)})
        except urllib.error.URLError as exc:
            emit({"type": "error", "error": f"Could not reach Qubrid API: {exc.reason}"})
        except (BrokenPipeError, ConnectionResetError):
            pass

    def _call_qubrid(self, api_key: str, body: dict) -> dict:
        data = json.dumps(body).encode("utf-8")
        req = urllib.request.Request(
            QUBRID_CHAT_URL,
            data=data,
            method="POST",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
        )
        with urllib.request.urlopen(req, timeout=300) as res:
            return json.loads(res.read().decode("utf-8"))

    def _json_response(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", PORT), PromptStudioHandler)
    url = f"http://127.0.0.1:{PORT}/"

    print()
    print("  Qwen3.7-Max - Prompt Studio")
    print("  ---------------------------")
    print(f"  Running at  {url}")
    print("  Press Ctrl+C to stop")
    print()

    threading.Timer(0.8, lambda: webbrowser.open(url)).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Shutting down.")
        server.shutdown()
        sys.exit(0)


if __name__ == "__main__":
    main()
