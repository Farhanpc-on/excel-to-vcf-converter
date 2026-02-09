# ❓ Excel to VCF Converter - FAQ & Troubleshooting

## 🔥 Most Common Issues

### Q: My phone numbers are wrong in the VCF file!
**A**: Enable "Auto-fix country codes" in options:
1. Check the ✅ box next to "Auto-fix country codes"
2. Select your country code (+60 for Malaysia)
3. Convert again

**Q**: I see extra zeros in phone numbers!
**A**: This is the country code fixing working:
- `1173547602` becomes `+601173547602` (correct)
- The "+60" is Malaysia's country code

**Q**: Some contacts are missing from VCF file!
**A**: Check your Excel file:
- Make sure rows have data (not empty)
- Ensure at least Name + Phone are filled
- Check for hidden characters in cells

---

## 📋 File & Data Issues

### Q: "Failed to load Excel file" error
**A**: Try these solutions:
1. **Close Excel file** if it's open
2. **Check file extension** - must be .xlsx or .xls
3. **Remove password protection** from file
4. **Check file permissions** - not read-only

### Q: Excel columns don't appear in mapping
**A**: Verify your file structure:
1. **Headers in first row** (row 1)
2. **Data starts in row 2** or later
3. **No blank rows** at top
4. **Use the template** to avoid this

### Q: Preview shows "No data available"
**A**: Check column mapping:
1. **Map at least one column** to a contact field
2. **Don't set all to "Ignore"**
3. **Ensure Excel has data rows**
4. **Refresh file** - load it again

---

## 🌍 Country Code Issues

### Q: Wrong country code is being added
**A**: Change the default setting:
1. Look in "⚙️ Options" section
2. Select your country from dropdown:
   - +60 Malaysia
   - +1 USA/Canada
   - +44 UK
   - +91 India
   - +86 China
   - +81 Japan
   - +82 South Korea
   - +66 Thailand
   - +65 Singapore
   - +62 Indonesia

### Q: My country code isn't listed
**A**: Use the closest option or disable auto-fix:
1. **Disable auto-fix** if you want original format
2. **Use +1** for North America
3. **Use +44** for European countries

### Q: Phone numbers already have country codes
**A**: The app handles this automatically:
- `+60123456789` stays unchanged
- `00160123456789` becomes `+60123456789`
- Existing + codes are preserved

---

## 📱 VCF Import Issues

### Q: VCF file won't import on my phone
**A**: Try these steps:
1. **Check file size** - some phones have limits
2. **Use smaller batches** - convert 50 contacts at a time
3. **Check VCF format** - should be standard vCard 3.0
4. **Restart phone** after import

### Q: Contacts are duplicated after import
**A**: This is normal behavior:
1. **Delete old contacts** before importing new ones
2. **Use "merge duplicates"** feature if available
3. **Import in small batches** to identify issues

### Q: Special characters in contacts are wrong
**A**: Encoding issues:
1. **Save Excel as UTF-8** if possible
2. **Use simple characters** - avoid emojis in Excel
3. **Check phone language settings**

---

## 🔧 Technical Issues

### Q: Application is slow or freezes
**A**: Performance tips:
1. **Reduce preview count** - use 5 instead of 100
2. **Close other programs** while converting
3. **Use smaller Excel files** - under 1000 contacts
4. **Restart application** if it's been running long

### Q: "Out of memory" error
**A**: Memory solutions:
1. **Break into smaller files** - 500 contacts each
2. **Close other applications**
3. **Restart computer** to free memory
4. **Use 64-bit Python** if available

### Q: Application won't start
**A**: Startup troubleshooting:
1. **Run as Administrator**
2. **Check Windows version** (needs Windows 7+)
3. **Disable antivirus** temporarily
4. **Install Microsoft .NET Framework** (Windows feature)

---

## 📄 Template & Excel Issues

### Q: Template won't open in Excel
**A**: Excel compatibility:
1. **Update Excel** to latest version
2. **Try different Excel** (Excel 2010+)
3. **Open with Google Sheets** as alternative
4. **Save as CSV** and convert manually

### Q: Template has wrong format
**A**: Template customization:
1. **Don't change column headers** - they're mapped automatically
2. **Keep required fields** - Full Name and Phone Number
3. **Use examples** as format guide
4. **Delete extra columns** - only use the 7 standard ones

---

## 🆘️ Error Messages Explained

### "Failed to load Excel file"
- **Cause**: File corrupted, wrong format, or permissions
- **Fix**: Use template, check file extension, ensure file is closed

### "No data available"
- **Cause**: No columns mapped or empty Excel file
- **Fix**: Map at least one column, check Excel has data

### "Failed to convert to VCF"
- **Cause**: Invalid data, permissions, or disk space
- **Fix**: Check data format, save to different location

### "Error creating template"
- **Cause**: Write permissions or disk space
- **Fix**: Save to Desktop, run as Administrator

---

## 📞 Getting Help

### Before Contacting Support:
1. **Note exact error message**
2. **What you were doing** step-by-step
3. **Your Windows version**
4. **Sample of your data** (remove sensitive info)

### Self-Service Resources:
1. **QUICK_START.md** - Step-by-step guide
2. **README.md** - Full documentation
3. **Template feature** - Eliminates most errors
4. **Preview function** - Test before converting

---

**💡 Golden Rule**: 90% of problems are solved by using the template feature and checking column mapping!
