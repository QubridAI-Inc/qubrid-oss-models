#!/usr/bin/env python3
"""
Tester / Playground — local chat UI for Qwen3.7-Max on Qubrid.

Part of One Click Apps. No pip installs required (stdlib only).

  python app.py
"""

from __future__ import annotations

import json
import sys
import threading
import urllib.error
import urllib.request
import webbrowser
from http import HTTPStatus
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

PORT = 7847
QUBRID_CHAT_URL = "https://platform.qubrid.com/v1/chat/completions"
MODEL = "Qwen/Qwen3.7-Max"
APP_DIR = Path(__file__).resolve().parent


class QubridAppHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(APP_DIR), **kwargs)

    def log_message(self, format: str, *args) -> None:
        if args and isinstance(args[0], str) and args[0].startswith("GET /api"):
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
        if self.path != "/api/chat":
            self.send_error(HTTPStatus.NOT_FOUND, "Not found")
            return

        length = int(self.headers.get("Content-Length", 0))
        try:
            payload = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            self._json_response(HTTPStatus.BAD_REQUEST, {"error": "Invalid JSON body"})
            return

        api_key = (payload.get("api_key") or "").strip()
        message = (payload.get("message") or "").strip()
        history = payload.get("messages") or []

        if not api_key:
            self._json_response(HTTPStatus.BAD_REQUEST, {"error": "API key is required"})
            return
        if not message:
            self._json_response(HTTPStatus.BAD_REQUEST, {"error": "Message is required"})
            return

        messages = list(history) if isinstance(history, list) else []
        messages.append({"role": "user", "content": message})

        body = {
            "model": MODEL,
            "messages": messages,
            "max_tokens": int(payload.get("max_tokens", 500)),
            "temperature": float(payload.get("temperature", 0.7)),
        }

        try:
            upstream = self._call_qubrid(api_key, body)
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            try:
                parsed = json.loads(detail)
            except json.JSONDecodeError:
                parsed = {"error": detail or exc.reason}
            self._json_response(exc.code, parsed)
            return
        except urllib.error.URLError as exc:
            self._json_response(
                HTTPStatus.BAD_GATEWAY,
                {"error": f"Could not reach Qubrid API: {exc.reason}"},
            )
            return

        choice = (upstream.get("choices") or [{}])[0]
        reply = (choice.get("message") or {}).get("content", "")
        self._json_response(
            HTTPStatus.OK,
            {
                "reply": reply,
                "model": upstream.get("model", MODEL),
                "usage": upstream.get("usage"),
                "messages": messages + [{"role": "assistant", "content": reply}],
            },
        )

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
        with urllib.request.urlopen(req, timeout=120) as res:
            return json.loads(res.read().decode("utf-8"))

    def _json_response(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", PORT), QubridAppHandler)
    url = f"http://127.0.0.1:{PORT}/"

    print()
    print("  Qwen3.7-Max - Tester / Playground")
    print("  -----------------------------")
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
