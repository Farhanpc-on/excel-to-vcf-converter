# 📊 Excel to VCF Converter

A professional Python desktop application that converts Excel contacts into VCF (vCard) files with advanced features like automatic country code fixing and template generation.

## 🎯 Features

- **📁 Excel File Support**: Read .xlsx and .xls files with pandas
- **🗺️ Column Mapping**: Flexible mapping of Excel columns to contact fields
- **🌍 Country Code Fixing**: Automatic phone number standardization with customizable default country codes
- **📄 Template Generator**: Create pre-formatted Excel templates with examples and instructions
- **👁️ Preview Function**: Preview customizable number of contacts before exporting
- **🎨 Professional UI**: Modern, user-friendly interface with custom branding
- **⚡ Error Handling**: Robust error handling with user-friendly messages
- **📱 VCF Export**: Generate standard vCard 3.0 format files compatible with mobile devices

## 🚀 Quick Start

### Option 1: Using Python
```bash
# Clone the repository
git clone https://github.com/yourusername/excel-to-vcf-converter.git
cd excel-to-vcf-converter

# Install dependencies
pip install -r requirements.txt

# Run the application
python excel_to_vcf_converter.py
```

### Option 2: Using Executable
1. Download `ExcelToVCFConverter.exe` from [Releases](https://github.com/yourusername/excel-to-vcf-converter/releases)
2. Double-click to run (no installation required)

## 📋 Requirements

- Python 3.6 or higher
- pandas
- openpyxl (for .xlsx files)
- xlrd (for .xls files)

## 🎯 Usage

1. **Create Template** (recommended): Click "📄 Create Template" to generate a pre-formatted Excel file
2. **Load Excel File**: Click "📁 Browse" and select your Excel file
3. **Map Columns**: Map Excel columns to contact fields (Full Name, Phone Number, Email, etc.)
4. **Configure Options**: Enable country code fixing and set default country code
5. **Preview**: Click "👁️ Preview Contacts" to verify formatting
6. **Convert**: Click "🔄 Convert to VCF" to generate the vCard file

## 🌍 Country Code Examples

| Input Format | Example | Output |
|--------------|---------|---------|
| Local | `1173547602` | `+601173547602` |
| With leading zero | `01173547602` | `+601173547602` |
| International | `+601173547602` | `+601173547602` |
| With 00 prefix | `001173547602` | `+1173547602` |

## 📄 Documentation

- **[QUICK_START.md](QUICK_START.md)** - 5-minute getting started guide
- **[TUTORIAL.md](TUTORIAL.md)** - Comprehensive step-by-step tutorial
- **[FAQ.md](FAQ.md)** - Common issues and solutions
- **[INSTALLATION.md](INSTALLATION.md)** - Complete installation guide
- **[BUILD_GUIDE.md](BUILD_GUIDE.md)** - Build executable instructions

## 🔧 Building from Source

### Build Executable
```bash
# Install build dependencies
pip install -r requirements_exe.txt

# Build with PowerShell
powershell -ExecutionPolicy Bypass -File build_exe.ps1

# Or use Python directly
python build_exe.py
```

### Build Requirements
- PyInstaller 5.0.0+
- Pillow 8.0.0+ (for icon processing)

## 📱 VCF Compatibility

Generated VCF files are compatible with:
- **Android**: Contacts app
- **iOS**: Contacts app
- **Windows**: Outlook, People app
- **macOS**: Contacts app
- **Email clients**: Thunderbird, Apple Mail

## 🎨 Screenshots

*(Add screenshots of your application here)*

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **Documentation**: Check the [Documentation Index](DOCUMENTATION_INDEX.md)
- **Issues**: [GitHub Issues](https://github.com/yourusername/excel-to-vcf-converter/issues)
- **FAQ**: See [FAQ.md](FAQ.md) for common problems

## 🎯 Roadmap

- [ ] Add support for multiple phone numbers per contact
- [ ] Add support for multiple email addresses per contact
- [ ] Add contact photo support
- [ ] Add batch processing for multiple Excel files
- [ ] Add cloud storage integration (Google Drive, OneDrive)

## 📊 Statistics

- **Lines of Code**: ~400
- **Dependencies**: 4 main packages
- **Supported Formats**: .xlsx, .xls, .vcf
- **Platform**: Windows (with cross-platform compatibility)

---

**🎯 Made with ❤️ for easy contact management**

*If this project helped you, please give it a ⭐ on GitHub!*
