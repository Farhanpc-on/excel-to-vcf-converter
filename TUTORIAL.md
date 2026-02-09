# 📋 Excel to VCF Converter - Step-by-Step Tutorial

## 🎯 Tutorial 1: Your First Conversion (5 Minutes)

### Step 1: Launch Application
1. **Double-click** `excel_to_vcf_converter.py` or `run.bat`
2. **Wait for** main window to appear
3. **You should see**: Title, file selection, column mapping, options, buttons

### Step 2: Create Your First Template
1. **Click** "📄 Create Template" button
2. **Save as** "My_Contacts.xlsx" on Desktop
3. **Open the file** in Excel
4. **Fill in 3-5 test contacts**:
   - Row 2: John Doe, 1173547602, john@email.com
   - Row 3: Jane Smith, 01173547603, jane@email.com
   - Row 4: Ali Ahmad, +60123456789, ali@company.com
5. **Save and close** Excel

### Step 3: Load Your Excel File
1. **Click** "📁 Browse" button
2. **Select** "My_Contacts.xlsx" from Desktop
3. **Click Open**
4. **You should see** your column names in the mapping area

### Step 4: Map Your Columns
1. **Look at** the dropdown menus next to your column names
2. **Set each mapping**:
   - "Full Name* (Required)" → "Full Name"
   - "Phone Number* (Required)" → "Phone Number"
   - "Email" → "Email"
   - Leave others as "Ignore" for now
3. **Double-check** your mappings

### Step 5: Configure Options
1. **Check** "✅ Auto-fix country codes" box
2. **Select** "+60" for Malaysia (or your country)
3. **Set** preview count to "5" (for testing)
4. **Leave other settings** as default

### Step 6: Preview Your Contacts
1. **Click** "👁️ Preview Contacts" button
2. **Review the preview window**:
   - Check names are correct
   - Verify phone numbers have +60 prefix
   - Ensure emails look right
3. **Close preview** if everything looks good

### Step 7: Convert to VCF
1. **Click** "🔄 Convert to VCF" button
2. **Choose save location** (Desktop is good)
3. **Name the file** "My_Contacts.vcf"
4. **Click Save**
5. **Wait for** success message

### Step 8: Test Your VCF File
1. **Open** the folder where you saved the file
2. **Double-click** "My_Contacts.vcf"
3. **It should open** in your default contacts app
4. **Check that** all 3-5 contacts appear correctly

---

## 🎯 Tutorial 2: Converting Real Data (10 Minutes)

### Step 1: Prepare Your Excel File
1. **Open your existing** Excel file with contacts
2. **Check the format**:
   - Row 1: Column headers
   - Row 2+: Contact data
   - At least 2 columns: Name and Phone
3. **Fix any issues**:
   - Remove special characters from phone numbers
   - Ensure emails have @ symbol
   - Check for empty rows

### Step 2: Load and Map
1. **Launch** the converter application
2. **Browse to** your Excel file
3. **Map columns** based on your headers:
   - "Name" → "Full Name"
   - "Telephone" → "Phone Number"
   - "Email Address" → "Email"
   - "Company" → "Organization"
4. **Set unused columns** to "Ignore"

### Step 3: Optimize Settings
1. **Country Code**: Enable auto-fix for your country
2. **Preview Count**: Set to 20 for larger files
3. **Test first**: Use preview to check a sample
4. **Adjust if needed**: Change mappings or settings

### Step 4: Convert and Verify
1. **Convert** the file to VCF
2. **Save with** descriptive name (e.g., "Company_Contacts_2024.vcf")
3. **Test import** on your phone:
   - Email the file to yourself
   - Open on phone and import
   - Verify first few contacts

---

## 🎯 Tutorial 3: Advanced Features (15 Minutes)

### Step 1: Using Different Name Formats
**Option A: Full Name Only**
- Excel column: "Contact Name"
- Map to: "Full Name"
- Result: "John Doe" in VCF

**Option B: First + Last Name**
- Excel columns: "First Name", "Last Name"
- Map to: "First Name", "Last Name"
- Result: "Doe;John;;;" in VCF (proper format)

**Option C: Mixed**
- Excel: "Full Name", "First Name", "Last Name"
- Map: "Full Name" only (ignore others)
- Result: Uses full name, ignores first/last

### Step 2: Handling Multiple Phone Formats
**Your Excel might have:**
- `012-3456789` → becomes `+60123456789`
- `+60 12 3456789` → becomes `+60123456789`
- `(012) 345-6789` → becomes `+60123456789`
- `00123456789` → becomes `+123456789`

### Step 3: Large File Management
**For files over 1000 contacts:**
1. **Split into smaller files** (500 contacts each)
2. **Use preview count 50** to check samples
3. **Convert each file separately**
4. **Import in batches** on your phone
5. **Merge duplicates** if they occur

### Step 4: Quality Assurance
**Before final conversion:**
1. **Preview multiple samples** (first, middle, last)
2. **Check special characters** in names
3. **Verify email formats** (name@domain.com)
4. **Test phone formatting** with country codes
5. **Save backup** of original Excel

---

## 🔧 Common Tutorial Tasks

### Task 1: Fix Wrong Phone Numbers
**Problem**: Numbers showing as `+6011735476020` (extra zero)
**Solution**:
1. Check original Excel data
2. Remove trailing zeros
3. Ensure "Auto-fix country codes" is enabled
4. Convert again

### Task 2: Handle Missing Names
**Problem**: Some contacts have no names
**Solution**:
1. Use "First Name" + "Last Name" mapping
2. Fill missing data in Excel
3. Use "Ignore" for completely empty rows
4. Preview to verify

### Task 3: International Contacts
**Problem**: Mixed country phone numbers
**Solution**:
1. Disable "Auto-fix country codes"
2. Format all numbers manually in Excel
3. Use consistent format (+countrycode)
4. Convert with auto-fix disabled

---

## 💡 Tutorial Tips

### 🎯 Before You Start:
- **Always use template** for new files
- **Clean data in Excel first**
- **Make backup of original file**
- **Test with small sample first**

### 🔧 During Conversion:
- **Use preview extensively** - it's your best friend
- **Check column mappings carefully** - most errors here
- **Verify country code setting** - matches your location
- **Save with descriptive names** - easy to find later

### 📱 After Conversion:
- **Test VCF file immediately**
- **Import small batch first**
- **Check for duplicates**
- **Keep original Excel file**

---

## 📞 Tutorial Support

### If You Get Stuck:
1. **Re-read the relevant tutorial section**
2. **Try the exact steps shown**
3. **Check FAQ.md** for your specific problem
4. **Use template feature** as fallback

### Practice Exercises:
1. **Create 5 test contacts** in template
2. **Convert with different settings**
3. **Import to phone** and verify
4. **Try advanced features** once comfortable

---

**🎓 Tutorial Completion**: After these tutorials, you'll be able to:
- Convert any Excel file to VCF format
- Handle various phone number formats
- Troubleshoot common issues
- Use advanced features effectively
- Manage large contact files efficiently
