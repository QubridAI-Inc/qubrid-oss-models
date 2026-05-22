# One Click Apps — Qwen3.7-Max

Runnable local demos for **Qwen/Qwen3.7-Max** on [Qubrid](https://platform.qubrid.com). Each app lives in its own folder — add new ones alongside the existing apps without changing the model docs above.

No monorepo build step: every app is **Python stdlib + static HTML**, launched with `run.bat`, `run.sh`, or `python app.py` inside that app’s folder.

---

## Available apps

| App | Folder | Description | Default port |
|:-----|:-------|:------------|-------------:|
| **Tester / Playground** | [`tester-playground/`](./tester-playground/) | Interactive chat UI to try the model with your API key | `7847` |
| **Prompt Studio** | [`prompt-studio/`](./prompt-studio/) | Prompt → streamed HTML/CSS/JS → IDE source + live preview ([full guide](./prompt-studio/README.md)) | `7848` |

Pick an app → open its **README** for step-by-step setup and troubleshooting.

### Quick launch

| App | Windows | Terminal |
|:----|:--------|:---------|
| Tester / Playground | [`tester-playground/run.bat`](./tester-playground/run.bat) | `cd tester-playground && python app.py` |
| Prompt Studio | [`prompt-studio/run.bat`](./prompt-studio/run.bat) | `cd prompt-studio && python app.py` |

---

## Adding a new app

1. Create a new folder under `One Click App/`, e.g. `my-new-app/`.
2. Copy the layout from `tester-playground/` (`app.py`, `index.html`, `run.bat`, `run.sh`, `README.md`).
3. Use a **unique `PORT`** in `app.py` so multiple apps can run at once.
4. Add a row to the table in this README.
5. Link from [../README.md](../README.md) if the app is a primary entry point.

Suggested naming:

```text
One Click App/
├── README.md                 ← this index
├── tester-playground/        ← chat tester
├── prompt-studio/            ← prompt → HTML preview
└── <your-app-name>/          ← future apps
```

---

## Shared requirements (all apps)

- Python **3.8+**
- Valid **Qubrid API key** with access to `Qwen/Qwen3.7-Max`
- Internet to `https://platform.qubrid.com`
- Local machine only (not hosted on GitHub Pages)

---

**Model:** `Qwen/Qwen3.7-Max` · **Platform:** [Qubrid](https://platform.qubrid.com) · **Model README:** [../README.md](../README.md)
