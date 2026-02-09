# 📊 Excel to VCF Converter - Quick Start Guide

## 🚀 Getting Started in 3 Easy Steps

### Step 1: Create Template (Recommended for New Users)
1. Open the application
2. Click **"📄 Create Template"** button
3. Save the template file
4. Open in Excel and fill in your contacts

### Step 2: Convert Your Excel File
1. Click **"📁 Browse"** and select your Excel file
2. Map your columns to contact fields:
   - **Full Name** OR **First Name + Last Name** (required)
   - **Phone Number** (required)
   - **Email, Organization, Address** (optional)
3. Configure options:
   - ✅ **Auto-fix country codes** (recommended)
   - 🌍 **Default country code** (+60 for Malaysia)
   - 👁️ **Preview count** (10 contacts default)
4. Click **"👁️ Preview Contacts"** to verify
5. Click **"🔄 Convert to VCF"** to generate file

### Step 3: Use Your VCF File
1. Save the generated `.vcf` file
2. Import into your phone/contacts app
3. All contacts are now available!

## 📋 Column Mapping Guide

| Excel Column | Should Map To | Notes |
|-------------|---------------|---------|
| Name | Full Name | Best option |
| First Name | First Name | Use with Last Name |
| Last Name | Last Name | Use with First Name |
| Phone | Phone Number | Required field |
| Email | Email | Optional |
| Company | Organization | Optional |
| Address | Address | Optional |

## 🌍 Country Code Examples

| Input Format | Example | Output |
|--------------|---------|---------|
| Local | `1173547602` | `+601173547602` |
| With Zero | `01173547602` | `+601173547602` |
| International | `+601173547602` | `+601173547602` |
| With 00 | `001173547602` | `+1173547602` |

## ⚡ Pro Tips

- **Use the template** - avoids formatting errors
- **Check preview** - verify before converting
- **Clean phone numbers** - remove ( ) - characters
- **Use valid emails** - format: name@domain.com
- **Keep addresses short** - better VCF compatibility

## 🔧 Troubleshooting

**"No data available" in preview?**
- Map at least one column
- Check Excel file has data rows

**"Failed to load Excel file"?**
- File not password protected
- File not open in another program
- Correct file extension (.xlsx or .xls)

**Phone numbers wrong?**
- Enable "Auto-fix country codes"
- Check default country code setting
- Remove special characters from Excel

## 📞 Need Help?

1. Check this guide first
2. Try the template feature
3. Use preview to test settings
4. Contact support if issues persist

---

**🎯 Success Tip**: Start with the template, use preview, and your contacts will convert perfectly every time!
