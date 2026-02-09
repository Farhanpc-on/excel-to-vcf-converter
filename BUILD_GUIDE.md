# Excel to VCF Converter - Executable Build Guide

## 🎯 Quick Build Instructions

### Option 1: Automated Build (Recommended)
1. Run `build_exe.bat`
2. Wait for build to complete
3. Find `ExcelToVCFConverter.exe` in `dist` folder

### Option 2: Manual Build
1. Install PyInstaller: `pip install pyinstaller`
2. Run build script: `python build_exe.py`
3. Executable will be in `dist` folder

## 📦 What You Get

- **Single executable file**: `ExcelToVCFConverter.exe`
- **No Python required**: Runs on any Windows PC
- **Portable**: Copy and run anywhere
- **All features included**: Template generator, country code fixing, etc.

## 🔧 Build Requirements

- Python 3.7+ (for building only)
- PyInstaller (auto-installed by build script)
- All application dependencies (from requirements.txt)

## 📋 After Build

1. Test the executable: `dist\ExcelToVCFConverter.exe`
2. Distribute the single `.exe` file
3. Users can run without any installation

## 🚀 Distribution

The generated `.exe` file can be:
- Copied to USB drives
- Shared via email
- Downloaded from websites
- Run on any Windows PC

## ⚠️ Notes

- Antivirus may flag the exe (this is normal)
- First run may be slower (subsequent runs are fast)
- Build only works on Windows (exe is Windows-only)
