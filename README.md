# Excel to VCF Converter

A Python desktop application that converts Excel contacts into VCF (vCard) files with a user-friendly GUI.

## Features

- **Excel File Support**: Reads both `.xlsx` and `.xls` files
- **Intuitive GUI**: Built with tkinter for easy use
- **Flexible Column Mapping**: Map Excel columns to contact fields:
  - Full Name
  - First Name
  - Last Name
  - Phone Number
  - Email
  - Organization
  - Address
- **Preview Function**: Preview customizable number of contacts (5, 10, 20, 50, or 100) before exporting
- **Error Handling**: User-friendly error messages and validation
- **VCF Export**: Generates standard vCard 3.0 format files
- **Automatic Country Code Fixing**: Intelligently detects and standardizes phone number formats with customizable default country codes
- **Excel Template Generator**: Create pre-formatted Excel templates with examples and instructions to avoid data entry mistakes

## Requirements

- Python 3.6 or higher
- pandas
- openpyxl (for .xlsx files)
- xlrd (for .xls files)

## Installation

1. Clone or download this repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python excel_to_vcf_converter.py
   ```

2. (Optional) Click "📄 Create Template" to generate a pre-formatted Excel template with examples and instructions

3. Click "Browse" to select your Excel file containing contacts

4. Configure options (optional):
   - Check "Auto-fix country codes" to enable automatic phone number formatting
   - Select your preferred default country code from the dropdown (e.g., +60 for Malaysia)
   - Choose preview count from dropdown (5, 10, 20, 50, or 100 contacts)

5. Map your Excel columns to contact fields using the dropdown menus:
   - Select the appropriate contact field for each Excel column
   - Choose "Ignore" for columns you don't want to include

6. (Optional) Click "Preview Contacts" to see how your contacts will be formatted with the selected preview count

7. Click "Convert to VCF" to generate the vCard file

8. Choose where to save your `.vcf` file

## Excel File Format

Your Excel file should have contact data organized in columns with headers in the first row. Example:

| Name      | Email            | Phone      | Company    | Address          |
|-----------|------------------|------------|------------|------------------|
| John Doe  | john@email.com   | 555-1234   | ABC Corp   | 123 Main St      |
| Jane Smith| jane@email.com   | 555-5678   | XYZ Inc    | 456 Oak Ave      |

## Excel Template Generator

The application includes a built-in template generator to help you avoid data entry mistakes:

### **Template Features:**
- **Pre-formatted columns** with proper headers
- **Mandatory field indicators** (*) showing required fields
- **3 example contacts** demonstrating different phone number formats:
  - Local format: `1173547602`
  - With leading zero: `01173547603`
  - International format: `+601173547604`
- **17 empty rows** ready for your data
- **Clear instructions** embedded in the template

### **How to Use:**
1. Click "📄 Create Template" button in the application
2. Save the template file to your desired location
3. Open the template in Excel
4. Fill in your contact details following the examples
5. Save the completed template
6. Use the file with the Excel to VCF Converter

### **Mandatory Fields:**
- **Full Name** OR **First Name + Last Name** (at least one name field required)
- **Phone Number** (required for contact functionality)

### **Optional Fields:**
- Email
- Organization
- Address

### **Phone Format Examples:**
| Format | Example | Result |
|---------|----------|---------|
| Local | `1173547602` | `+601173547602` |
| With leading zero | `01173547602` | `+601173547602` |
| International | `+601173547602` | `+601173547602` |
| With 00 prefix | `001173547602` | `+1173547602` |

## Generated VCF Format

The application generates standard vCard 3.0 format files that can be imported into:
- Mobile phones (Android, iOS)
- Email clients (Outlook, Thunderbird)
- Contact management applications
- CRM systems

## Country Code Fixing

The application can automatically detect and fix phone number formats:

**Supported Formats:**
- Local numbers (e.g., `1173547602` → `+601173547602`)
- Numbers with leading zero (e.g., `01173547602` → `+601173547602`)
- International format with 00 (e.g., `001173547602` → `+1173547602`)
- Already formatted numbers (e.g., `+601173547602` → unchanged)

**Logic:**
- Numbers starting with `+` are kept as-is
- Numbers starting with `00` are converted to `+`
- Numbers with leading zeros get the zero removed and default country code added
- Numbers 10+ digits get the default country code added
- Numbers less than 10 digits get the default country code added

**Available Country Codes:**
- `+60` (Malaysia) - default
- `+1` (USA/Canada)
- `+44` (UK)
- `+91` (India)
- `+86` (China)
- `+81` (Japan)
- `+82` (South Korea)
- `+66` (Thailand)
- `+65` (Singapore)
- `+62` (Indonesia)

## Error Handling

The application includes comprehensive error handling for:
- Invalid Excel files
- Missing or corrupted data
- File permission issues
- Invalid data formats

## Notes

- Empty cells are automatically skipped
- Phone numbers are cleaned and standardized with optional country code fixing
- Multiple phone numbers or emails per contact are not supported in this version
- The application preserves Unicode characters for international names and addresses
- Country code fixing can be disabled if you want to preserve original phone number formats

## Troubleshooting

**"Failed to load Excel file" error:**
- Ensure your Excel file is not password protected
- Check that the file is not open in another program
- Verify the file has the correct extension (.xlsx or .xls)

**"No data available" in preview:**
- Make sure you've mapped at least one column
- Check that your Excel file contains data rows
- Verify column names match exactly (case-sensitive)

## License

This project is open source and available under the MIT License.
