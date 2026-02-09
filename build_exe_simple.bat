@echo off
echo Building Excel to VCF Converter executable...
echo.

REM Check if PyInstaller is installed
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
    if errorlevel 1 (
        echo Failed to install PyInstaller. Please run: pip install pyinstaller
        pause
        exit /b 1
    )
)

echo.
echo Creating executable file (this may take a few minutes)...
python build_exe.py

if errorlevel 1 (
    echo Build failed! Check for error messages above.
    echo.
    echo Common solutions:
    echo - Make sure you have enough disk space
    echo - Close other programs while building
    echo - Run as Administrator if needed
    pause
    exit /b 1
)

echo.
echo ========================================
echo Build completed successfully!
echo.
echo Executable location: dist\ExcelToVCFConverter.exe
echo.
echo You can now:
echo - Double-click ExcelToVCFConverter.exe to run
echo - Copy the .exe file to any computer
echo - No Python installation required
echo ========================================
pause
