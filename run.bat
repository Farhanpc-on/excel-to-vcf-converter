@echo off
echo Starting Excel to VCF Converter...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.6 or higher and try again
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist ".venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo Error: Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install requirements
echo Installing required packages...
pip install -r requirements.txt

REM Run the application
echo.
echo Starting Excel to VCF Converter application...
python excel_to_vcf_converter.py

REM Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo Application closed with an error. Press any key to exit...
    pause >nul
)
