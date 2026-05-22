#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if command -v python3 &>/dev/null; then
  PYTHON=python3
elif command -v python &>/dev/null; then
  PYTHON=python
else
  echo "  Python is not installed."
  exit 1
fi

echo ""
echo "  Starting Qwen3.7-Max Prompt Studio..."
echo "  Press Ctrl+C to stop the server."
echo ""

exec "$PYTHON" app.py
