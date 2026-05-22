@echo off
cd /d "%~dp0"

python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo   Python is not installed or not on PATH.
    echo   Install Python 3.8+ from https://www.python.org/downloads/
    echo   During setup, check "Add python.exe to PATH".
    echo.
    pause
    exit /b 1
)

echo.
echo   Starting Qwen3.7-Max Tester / Playground...
echo   Press Ctrl+C in this window to stop the server.
echo.

python app.py
if errorlevel 1 pause
