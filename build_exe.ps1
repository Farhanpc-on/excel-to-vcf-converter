Write-Host "Building Excel to VCF Converter executable..." -ForegroundColor Green
Write-Host ""

# Check if required packages are installed
try {
    python -c "import PyInstaller, PIL" 2>$null
    Write-Host "Required packages found." -ForegroundColor Green
} catch {
    Write-Host "Installing required packages..." -ForegroundColor Yellow
    pip install pyinstaller pillow
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Failed to install packages. Please check the error messages." -ForegroundColor Red
        Read-Host "Press any key to exit..." -ForegroundColor Red
        exit 1
    }
}

# Create icon from JPEG
Write-Host "Creating application icon..." -ForegroundColor Yellow
try {
    python create_icon.py
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Icon created successfully." -ForegroundColor Green
    } else {
        Write-Host "Icon creation failed, building without icon..." -ForegroundColor Yellow
    }
} catch {
    Write-Host "Icon creation failed, building without icon..." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Creating executable file (this may take a few minutes)..." -ForegroundColor Yellow

# Build the executable
try {
    python build_exe.py
    if ($LASTEXITCODE -eq 0) {
        Write-Host "========================================" -ForegroundColor Green
        Write-Host "Build completed successfully!" -ForegroundColor Green
        Write-Host "========================================" -ForegroundColor Green
        Write-Host ""
        Write-Host "Executable location: dist\ExcelToVCFConverter.exe" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "You can now:" -ForegroundColor White
        Write-Host "- Double-click ExcelToVCFConverter.exe to run" -ForegroundColor White
        Write-Host "- Copy the .exe file to any computer" -ForegroundColor White
        Write-Host "- No Python installation required" -ForegroundColor White
        Write-Host "- Custom icon included" -ForegroundColor Green
        Write-Host "========================================" -ForegroundColor Green
    } else {
        Write-Host "Build failed! Check for error messages above." -ForegroundColor Red
        Write-Host ""
        Write-Host "Common solutions:" -ForegroundColor Yellow
        Write-Host "- Make sure you have enough disk space" -ForegroundColor White
        Write-Host "- Close other programs while building" -ForegroundColor White
        Write-Host "- Run as Administrator if needed" -ForegroundColor White
    }
} catch {
    Write-Host "An error occurred during build:" -ForegroundColor Red
    Write-Host $_ -ForegroundColor Red
}

Write-Host ""
Write-Host "Press any key to continue..." -ForegroundColor Cyan
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
