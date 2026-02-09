# PyInstaller build script for Excel to VCF Converter
import PyInstaller.__main__

# Build options - now with custom icon
PyInstaller.__main__.run([
    'excel_to_vcf_converter.py',
    '--onefile',
    '--windowed',
    '--name=ExcelToVCFConverter',
    '--icon=logo_excel2vcf.ico',
    '--clean',
    '--noconfirm'
])
