# Prompt Studio - Qwen3.7-Max

Part of **[One Click Apps](../README.md)**.

Describe any UI in plain English - **Qwen3.7-Max** builds a complete **HTML + CSS + JavaScript** page, streams the source into an IDE-style editor, and renders a **live preview** in your browser.

**No npm. No pip. No API key in the repo.** Paste your key once, write a prompt, click Generate.

| | |
|---|---|
| **URL (local)** | `http://127.0.0.1:7848/` |
| **Port** | `7848` (Tester / Playground uses `7847`) |
| **Model** | `Qwen/Qwen3.7-Max` |
| **Platform** | [Qubrid](https://platform.qubrid.com) |

---

## Table of contents

- [Who this is for](#who-this-is-for)
- [Prerequisites](#prerequisites)
- [Quick start (3 steps)](#quick-start-3-steps)
- [First-time walkthrough](#first-time-walkthrough)
- [What you should see](#what-you-should-see)
- [How it works](#how-it-works)
- [Configuration](#configuration)
- [Security and privacy](#security-and-privacy)
- [Verify it works](#verify-it-works)
- [Troubleshooting](#troubleshooting)
- [Limitations](#limitations)
- [Files in this folder](#files-in-this-folder)

---

## Who this is for

| Audience | What you get |
|:---------|:-------------|
| **Developers** | Fast UI prototypes from a text prompt on Qubrid |
| **Repo visitors** | Clone → run `run.bat` → paste key → generate |
| **Non-developers** | Double-click **`run.bat`** (Windows) if Python is installed |

This is a **local app** on your computer - not a public website. You must start it once per session (see [Quick start](#quick-start-3-steps)).

---

## Prerequisites

Check these **before** you run the app.

### 1. Python 3.8+

```bash
python --version
```

| OS | Install |
|:---|:--------|
| **Windows** | [python.org/downloads](https://www.python.org/downloads/) - check **“Add python.exe to PATH”** |
| **macOS** | `brew install python` or python.org installer |
| **Linux** | `sudo apt install python3` (Debian/Ubuntu) or your package manager |

No `pip install` and no virtual environment required.

### 2. Qubrid API key

1. Sign in at **[platform.qubrid.com](https://platform.qubrid.com)**
2. Create or copy an API key
3. Confirm your account can use **`Qwen/Qwen3.7-Max`** (quota / billing if required)

### 3. Internet access

The app calls:

```text
https://platform.qubrid.com/v1/chat/completions
```

VPNs, proxies, or offline networks can block generation.

### 4. Modern browser

Chrome, Edge, Firefox, or Safari (recent). JavaScript enabled.

### 5. Port 7848 available

If another app uses **7848**, startup fails - see [Port already in use](#port-already-in-use).

---

## Quick start (3 steps)

### Step 1 - Start the app

| Platform | Action |
|:---------|:-------|
| **Windows** | Double-click **`run.bat`** in this folder |
| **macOS / Linux** | `chmod +x run.sh && ./run.sh` |
| **Manual** | `python app.py` (or `python3 app.py`) |

**Windows PowerShell from repo root:**

```powershell
cd "providers\Qwen\General\Qwen3.7-Max\One Click App\prompt-studio"
python app.py
```

Keep the terminal window **open** while you use the app.

You should see:

```text
  Qwen3.7-Max - Prompt Studio
  ---------------------------
  Running at  http://127.0.0.1:7848/
  Press Ctrl+C to stop
```

Your browser may open automatically. If not, go to **http://127.0.0.1:7848/** manually.

### Step 2 - Paste API key

1. Modal: **Connect to Qubrid** (or click **API key** in the header)
2. Paste your key → **Save**
3. Status should show you are ready to generate

The key is stored in **session storage** only (cleared when you close the browser tab).

### Step 3 - Generate

1. Write a prompt (or click an **example** chip)
2. Adjust **Max output tokens** if needed (default **16,384**)
3. Click **Generate preview** or press **Ctrl+Enter**
4. Watch code stream in **Source**, then open **Live preview** when done
5. Optional: **Download HTML**

---

## First-time walkthrough

| Step | Action | Success signal |
|:-----|:-------|:----------------|
| 1 | Start `run.bat` or `python app.py` | Terminal shows `Running at http://127.0.0.1:7848/` |
| 2 | Open `http://127.0.0.1:7848/` | Prompt Studio UI loads |
| 3 | Save API key | **Generate preview** button enabled |
| 4 | Prompt: *"A hello world card with a gradient button that shows an alert when clicked."* | Short, fast test |
| 5 | Click **Generate preview** | **Source** tab opens; text appears; status shows **chars / lines / chunks** increasing |
| 6 | Click **Live preview** | Rendered page in iframe; button works |
| 7 | Click a link in the preview (if any) | Opens in a **new browser tab**, not inside Prompt Studio |

---

## What you should see

### While generating

- App switches to the **Source** tab (IDE-style editor with line numbers)
- Tab title **generated.html** shows a green streaming dot
- Status bar under the prompt shows: `Streaming · X chars · Y lines · Z chunks`
- **Z (chunks)** should increase during generation - that means tokens are arriving live
- Plain text streams first; **syntax highlighting** applies when generation finishes

### When finished

- Status: `Complete - switch to Live preview tab` (or token usage line)
- **Source** shows highlighted HTML
- **Live preview** tab shows the rendered page (updates in the background during streaming)
- **Download HTML** is enabled

### Preview links

Links inside the preview **do not** reload Prompt Studio. They open in a **new tab** (`target="_blank"`). In-page `#` anchors stay in the preview.

---

## How it works

```text
Browser (index.html)
    │  POST /api/generate  { api_key, prompt, stream: true, max_tokens, temperature }
    ▼
Local Python server (app.py)  - 127.0.0.1:7848
    │  Streamed POST → https://platform.qubrid.com/v1/chat/completions
    ▼
Qwen/Qwen3.7-Max  -  returns HTML document (system prompt: single file, no external URLs)
    │
    ├─► Source tab  -  live text, then syntax highlight
    └─► Preview     -  sandboxed iframe (srcdoc), offline-safe
```

| Setting | Default |
|:--------|--------:|
| Max output tokens | 16,384 (slider up to 32,768) |
| Temperature | 0.6 |
| Streaming | On (SSE) |

---

## Configuration

### Change the port

Edit `PORT` in `app.py` (default `7848`), restart, open the new URL.

### Max output tokens

Use the slider next to the prompt:

| Symptom | Suggested value |
|:--------|:------------------|
| Small widget / card | 8,192 – 16,384 |
| Full landing page | 16,384 – 24,576 |
| Large page + heavy CSS/JS | 24,576 – 32,768 |

If output stops mid-`<style>` or mid-tag, increase tokens and **regenerate**. A red status appears when the API returns `finish_reason: length`.

### Temperature

Lower (0.3–0.5) = more consistent layout. Higher (0.7–0.9) = more creative variation.

---

## Security and privacy

| Topic | Behavior |
|:------|:---------|
| API key | Browser session only; sent to `localhost`, then to Qubrid |
| Generated code | Runs in a **sandboxed** iframe (`allow-scripts` only) |
| Production | Local demo - do not expose `app.py` to the public internet without hardening |

Revoke keys on the platform if leaked.

---

## Verify it works

### Without an API key

1. Start the server
2. Open `http://127.0.0.1:7848/` - page loads, **Generate** disabled until key saved

### With an API key

1. Save key → enter a one-line prompt → **Generate preview**
2. **Source** fills with `<!DOCTYPE html>…`
3. **Live preview** renders the page

### Terminal check (server running)

**PowerShell:**

```powershell
# Page loads
(Invoke-WebRequest http://127.0.0.1:7848/ -UseBasicParsing).StatusCode   # expect 200

# API rejects missing key (proves proxy works)
Invoke-WebRequest http://127.0.0.1:7848/api/generate -Method POST `
  -ContentType "application/json" -Body '{"prompt":"test"}' -UseBasicParsing
# expect error: API key is required
```

---

## Troubleshooting

### App will not start

| Symptom | Fix |
|:--------|:----|
| `'python' is not recognized` | Install Python; enable PATH on Windows; reopen terminal |
| `run.bat` closes instantly | Open Command Prompt in this folder, run `run.bat`, read the error |
| Window shows error then pauses | Read the message; usually missing Python |

### Page will not load

| Symptom | Fix |
|:--------|:----|
| Blank / cannot connect | Confirm terminal shows `Running at http://127.0.0.1:7848/` - keep it open |
| Old broken UI | **Hard refresh**: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac) |
| Wrong port | Match browser URL to `PORT` in `app.py` |

### Port already in use

```powershell
netstat -ano | findstr :7848
```

Stop the listed PID, or change `PORT` in `app.py` and restart.

**Windows:** close other terminals running `python app.py` for Prompt Studio.

### API key / Generate button

| Symptom | Fix |
|:--------|:----|
| **Generate preview** disabled | Click **API key** → paste key → **Save** |
| `401` / `403` / Unauthorized | New key from [platform.qubrid.com](https://platform.qubrid.com) |
| `API key is required` in status | Save key again; do not use quotes around the key |

### Generation fails or errors

| Symptom | Fix |
|:--------|:----|
| `Network error - is python app.py running?` | Start server; keep terminal open |
| `Could not reach Qubrid API` | Check internet / firewall / VPN |
| Model not found | Confirm `Qwen/Qwen3.7-Max` on your account |
| Rate limit / 429 | Wait and retry |

### Streaming / Source tab

| Symptom | Fix |
|:--------|:----|
| Cursor blinks, no text for a long time, then all at once | **Chunks** stayed at 0 - Qubrid may batch the response; UI still works; wait for completion |
| **Chunks** increase, text grows line by line | Normal - streaming is working |
| `/* Waiting for first token… */` for 30s+ | Slow model or network; wait or retry |
| Stops mid-CSS or mid-HTML | Raise **Max output tokens** (try 24k–32k) → **Generate preview** again |
| Red status mentions **truncated** / `length` | Increase max tokens slider |

### Live preview

| Symptom | Fix |
|:--------|:----|
| Blank preview | Open **Source** - if empty, generation failed; if full HTML exists, click **Live preview** again |
| Clicking a link reloads Prompt Studio inside preview | Hard refresh page (`Ctrl+Shift+R`) - you need the latest `index.html` + `app.py` |
| Link should open new tab | Expected after fix; external `http` links open in new tab |
| Preview looks broken | Model may have truncated output - increase tokens; check **Source** for incomplete `</html>` |
| Buttons / JS do not work | Preview allows scripts in sandbox; incomplete JS from truncation is a common cause |

### HTML / download

| Symptom | Fix |
|:--------|:----|
| Markdown in **Source** (` ```html `) | Reprompt: *"Output only a full HTML document starting with <!DOCTYPE html>"* |
| **Download HTML** disabled | Wait until generation finishes and HTML is parsed |
| Downloaded file broken | Open **Source** - ensure `</html>` is present; regenerate with more tokens |

### Running both One Click Apps

| App | Port |
|:----|-----:|
| Tester / Playground | 7847 |
| Prompt Studio | 7848 |

Run each in its own terminal. Do not use the same port twice.

### Windows-specific

| Symptom | Fix |
|:--------|:----|
| Path with spaces | Quote paths: `cd "One Click App\prompt-studio"` |
| SmartScreen blocks `run.bat` | More info → Run anyway |
| Multiple Python versions | Try `py -3 app.py` |

### macOS / Linux-specific

| Symptom | Fix |
|:--------|:----|
| `Permission denied` on `run.sh` | `chmod +x run.sh` |
| Use `python3` | `python3 app.py` |

### Still stuck?

1. `python --version` → 3.8+
2. Terminal shows `Running at http://127.0.0.1:7848/`
3. Hard refresh browser
4. Valid API key saved (Generate enabled)
5. Short test prompt (hello-world card)
6. Compare with [Tester / Playground](../tester-playground/) - if chat works there, your key and network are fine

---

## Limitations

| Limitation | Detail |
|:-----------|:-------|
| **Local only** | Must run `python app.py` or `run.bat` - GitHub does not host this UI |
| **Not one-click on GitHub** | Clone/download the repo first |
| **Streaming depends on API** | Some responses arrive in one batch; UI still shows progress when chunks arrive |
| **Complex apps** | Very large pages may need max tokens at 32k and simpler prompts |
| **Generated quality** | Varies by prompt; iterate temperature and wording |

---

## Files in this folder

| File | Purpose |
|:-----|:--------|
| `app.py` | Local server, streaming proxy to Qubrid |
| `index.html` | Prompt UI, IDE source view, live preview |
| `run.bat` | Windows launcher (checks Python) |
| `run.sh` | macOS/Linux launcher |
| `README.md` | This guide |

---

**All apps:** [../README.md](../README.md) · **Model docs:** [../../README.md](../../README.md) · **Chat tester:** [../tester-playground/README.md](../tester-playground/README.md)
