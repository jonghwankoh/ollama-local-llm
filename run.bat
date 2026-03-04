@echo off
setlocal

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH.
    pause
    exit /b %errorlevel%
)

:: Install requirements if needed (optional, uncomment to enable auto-install)
:: pip install -r requirements.txt

if "%1"=="" (
    echo Usage: run.bat [profile_name]
    echo Example: run.bat qwen2.5
    echo.
    echo Available profiles:
    dir /b profiles\*.yaml
    pause
    exit /b 1
)

python local_llm.py run --profile %1

pause
