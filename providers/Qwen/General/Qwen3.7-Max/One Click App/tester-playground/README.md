# Tester / Playground — Qwen3.7-Max

Part of **[One Click Apps](../README.md)** for this model.

A **local** chat web app for **[Qwen/Qwen3.7-Max](https://huggingface.co/Qwen/Qwen3.7-Max)** on the [Qubrid platform](https://platform.qubrid.com). No `npm install`, no `pip install` — only **Python 3** (standard library).

You run a small server on your machine, open a browser, paste your Qubrid API key, and chat. Your key never leaves your machine except when the local server forwards requests to Qubrid.

---

## Table of contents

- [Who this is for](#who-this-is-for)
- [Prerequisites](#prerequisites)
- [Quick start](#quick-start)
- [First-time walkthrough](#first-time-walkthrough)
- [How it works](#how-it-works)
- [Configuration](#configuration)
- [Security and privacy](#security-and-privacy)
- [Verify it works](#verify-it-works)
- [Troubleshooting](#troubleshooting)
- [Limitations](#limitations)
- [Files in this folder](#files-in-this-folder)

---

## Who this is for

| Audience | Experience |
|:---------|:-----------|
| Developers trying Qwen3.7-Max on Qubrid | Run one command, chat in the browser |
| Repo visitors cloning this registry | Copy the folder, add an API key, demo in minutes |
| Non-developers | Use **`run.bat`** (Windows) or **`run.sh`** (macOS/Linux) if Python is already installed |

This is **not** a hosted website. Users must start the app locally (see [Limitations](#limitations)).

---

## Prerequisites

Before you start, confirm all of the following.

### 1. Python 3.8 or newer

Check from a terminal:

```bash
python --version
# or
python3 --version
```

You should see `Python 3.8.x` or higher (3.10+ recommended).

**Install Python**

| OS | Link / notes |
|:---|:-------------|
| Windows | [python.org/downloads](https://www.python.org/downloads/) — enable **“Add python.exe to PATH”** during install |
| macOS | `brew install python` or python.org installer |
| Linux | `sudo apt install python3` (Debian/Ubuntu) or your distro package |

No virtual environment or `pip install` is required for this app.

### 2. Qubrid API key

- Sign in at **[platform.qubrid.com](https://platform.qubrid.com)**
- Create or copy an API key with access to **`Qwen/Qwen3.7-Max`**
- Ensure the account has quota / billing if your org requires it

### 3. Network access

The app must reach:

```text
https://platform.qubrid.com/v1/chat/completions
```

Corporate proxies or offline machines will block chat until connectivity is fixed.

### 4. A modern browser

Chrome, Edge, Firefox, or Safari (recent versions). JavaScript must be enabled.

### 5. Free local port (default `7847`)

Nothing else should be using port **7847** on your machine. See [Port already in use](#port-already-in-use) if startup fails.

---

## Quick start

Choose **one** way to launch.

### Option A — Windows (double-click style)

1. Open the `tester-playground` folder in File Explorer.
2. Double-click **`run.bat`**.
3. If Windows SmartScreen appears, choose **Run anyway** (script only starts Python locally).
4. Browser opens to `http://127.0.0.1:7847/` — paste your API key and chat.

### Option B — macOS / Linux

```bash
cd "One Click App/tester-playground"
chmod +x run.sh   # first time only
./run.sh
```

### Option C — Manual (all platforms)

```bash
cd "One Click App/tester-playground"
python app.py
```

On some systems use `python3` instead of `python`.

**From the repo root (Windows PowerShell):**

```powershell
cd "providers\Qwen\General\Qwen3.7-Max\One Click App\tester-playground"
python app.py
```

When the server is running you should see:

```text
  Qwen3.7-Max - Tester / Playground
  -----------------------------
  Running at  http://127.0.0.1:7847/
  Press Ctrl+C to stop
```

Leave that terminal window open while you use the app. Press **Ctrl+C** to stop.

---

## First-time walkthrough

1. **Start the server** using [Quick start](#quick-start) above.
2. **Browser** opens (or go to **http://127.0.0.1:7847/** manually).
3. **Modal — “Connect to Qubrid”**  
   Paste your API key → **Save & start**.  
   The key is stored in the browser’s **session storage** (cleared when you close the tab/browser).
4. **Status bar** should show: `Connected · model Qwen/Qwen3.7-Max`.
5. **Send a message** — e.g. `Say hello in one sentence.`
6. **Reply** appears under “Qwen3.7-Max”; token usage may show at the bottom.
7. Optional: click a **starter chip** (support summary, explain topic, code helper).
8. Optional: **Clear chat** resets history; **API key** reopens settings (temperature, max tokens).

---

## How it works

```text
Browser (index.html)
    │  POST /api/chat  { api_key, message, messages, ... }
    ▼
Local Python server (app.py)  — 127.0.0.1:7847
    │  POST https://platform.qubrid.com/v1/chat/completions
    ▼
Qubrid API  —  model: Qwen/Qwen3.7-Max
```

| File | Role |
|:-----|:-----|
| `app.py` | Serves `index.html` and proxies chat to Qubrid (`urllib`, stdlib only) |
| `index.html` | Chat UI (HTML/CSS/JS, no build step) |
| `run.bat` | Windows launcher — checks Python, runs `app.py` |
| `run.sh` | macOS/Linux launcher |

This mirrors the [Python SDK example](../Python/chat.py) but adds a UI and **multi-turn** conversation history.

**API details (proxied by `app.py`):**

| Setting | Default |
|:--------|--------:|
| Base URL | `https://platform.qubrid.com/v1` |
| Endpoint | `/chat/completions` |
| Model | `Qwen/Qwen3.7-Max` |
| Max tokens | 500 (slider in UI) |
| Temperature | 0.7 (slider in UI) |

---

## Configuration

### Change the port

Edit `PORT` at the top of `app.py`:

```python
PORT = 7847
```

Restart the server and open `http://127.0.0.1:<PORT>/`.

### Adjust model parameters

Use the **API key** modal sliders (temperature, max tokens) or edit the defaults in `index.html` / the payload in `app.py`.

---

## Security and privacy

| Topic | Behavior |
|:------|:---------|
| API key storage | Browser `sessionStorage` only (not written to disk by the app) |
| Key transmission | Browser → `localhost` → Qubrid (not sent to other domains) |
| Production use | This is a **local demo**; do not expose `app.py` to the public internet without hardening |
| HTTPS | Local server uses HTTP on loopback only |

Treat your API key like a password. Revoke it on the platform if it is leaked.

---

## Verify it works

### UI smoke test (no API key)

1. Start the app.
2. Confirm the chat page loads and the API key modal appears.
3. **Send** should stay disabled until a key is saved.

### Full test (with API key)

1. Save a valid Qubrid key.
2. Send: `Say hello in one sentence.`
3. Expect an assistant reply within a few seconds and status **Ready**.

### Optional — terminal check (server running)

**Windows PowerShell:**

```powershell
# Page should return StatusCode 200
Invoke-WebRequest http://127.0.0.1:7847/ -UseBasicParsing

# Should fail with "API key is required" (proves /api/chat exists)
Invoke-WebRequest http://127.0.0.1:7847/api/chat -Method POST `
  -ContentType "application/json" -Body '{"message":"hi"}' -UseBasicParsing
```

**macOS / Linux:**

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:7847/
curl -s -X POST http://127.0.0.1:7847/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"hi"}'
```

Second request should return JSON mentioning the missing API key.

---

## Troubleshooting

### App will not start

| Symptom | Cause | Fix |
|:--------|:------|:----|
| `'python' is not recognized` | Python not installed or not on PATH | Install Python; enable PATH on Windows; reopen terminal |
| `UnicodeEncodeError` on startup (older copy) | Windows console + Unicode in `print` | Use the latest `app.py` (ASCII-only banner) |
| `run.bat` closes immediately | Python missing or crash on start | Run `run.bat` from cmd to read errors; install Python |
| Address already in use / port error | Port **7847** taken | Change `PORT` in `app.py` or stop the other process |

### Browser / UI issues

| Symptom | Cause | Fix |
|:--------|:------|:----|
| Blank page / cannot connect | Server not running | Start `python app.py` or `run.bat`; keep terminal open |
| Browser did not open | `webbrowser` blocked or headless | Open **http://127.0.0.1:7847/** manually |
| Send button disabled | No API key saved | Click **API key** → paste key → **Save & start** |
| `Network error — is python app.py running?` | Server stopped or wrong port | Restart app; match URL port to `PORT` in `app.py` |

### API / chat errors

| Symptom | Cause | Fix |
|:--------|:------|:----|
| `API key is required` | Empty key in request | Save key in modal again |
| `401` / `403` / Unauthorized | Invalid or expired key | Create a new key on [platform.qubrid.com](https://platform.qubrid.com) |
| `Could not reach Qubrid API` | No internet, firewall, proxy | Check network; allow `platform.qubrid.com` |
| Model not found / 404 | Model ID or access not enabled on account | Confirm `Qwen/Qwen3.7-Max` on your Qubrid account |
| Rate limit / 429 | Too many requests | Wait and retry; check platform limits |
| Empty or error bubble in chat | Upstream error body | Read the red status text; check terminal for details |
| Very slow replies | Model load or long `max_tokens` | Reduce max tokens; retry later |

### Windows-specific

| Symptom | Fix |
|:--------|:----|
| Folder path has spaces | Quote paths: `cd "One Click App/tester-playground"` |
| SmartScreen blocks `run.bat` | More info → Run anyway (script only runs local Python) |
| Multiple Python versions | Try `py -3 app.py` or full path to the correct `python.exe` |

### macOS / Linux-specific

| Symptom | Fix |
|:--------|:----|
| `Permission denied` on `run.sh` | Run `chmod +x run.sh` once |
| `python` points to Python 2 | Use `python3 app.py` or `./run.sh` |

### Port already in use

1. Find what uses 7847 (Windows):  
   `netstat -ano | findstr :7847`
2. Stop that process, **or** change `PORT` in `app.py` and restart.
3. Open the new URL in the browser.

### Still stuck?

1. Confirm Python: `python --version`
2. Confirm server prints `Running at http://127.0.0.1:7847/`
3. Test with a minimal message after saving the key.
4. Compare with the standalone script: [../Python/chat.py](../Python/chat.py) (replace `QUBRID_API_KEY` with your real key).

---

## Limitations

| Limitation | Detail |
|:-----------|:-------|
| **Local only** | Users must run Python; closing the terminal stops the app |
| **Not hosted** | Opening files on GitHub does not run the app — clone/download + start server |
| **One user per instance** | Default server is for local demo, not multi-user production |
| **Session API key** | Key cleared when browser session ends (unless you save again) |
| **Depends on Qubrid** | Outages, model availability, and pricing are controlled by the platform |

For a “zero install” experience you would need hosted deployment (out of scope for this folder).

---

## Files in this folder

| File | Description |
|:-----|:------------|
| `app.py` | Local HTTP server + Qubrid API proxy |
| `index.html` | Chat user interface |
| `run.bat` | Windows one-click launcher |
| `run.sh` | macOS/Linux launcher |
| `README.md` | This documentation |

---

**Model:** `Qwen/Qwen3.7-Max` · **Platform:** [Qubrid](https://platform.qubrid.com) · **All apps:** [../README.md](../README.md) · **Model docs:** [../../README.md](../../README.md)
