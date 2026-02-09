import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os
from pathlib import Path

class ExcelToVCFConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("📊 Excel to VCF Converter - Professional Contact Converter")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        self.root.resizable(True, True)
        
        # Variables
        self.excel_file_path = tk.StringVar()
        self.df = None
        self.column_mapping = {}
        self.mapping_widgets = {}
        
        # Country code fixing options
        self.fix_country_code = tk.BooleanVar(value=True)
        self.default_country_code = tk.StringVar(value="+60")  # Default to Malaysia
        self.preview_count = tk.StringVar(value="10")  # Default preview count
        
        # Contact fields that can be mapped
        self.contact_fields = [
            "Full Name", "First Name", "Last Name", "Phone Number", 
            "Email", "Organization", "Address", "Ignore"
        ]
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the main user interface"""
        # Configure root window
        self.root.configure(bg='#f0f0f0')
        
        # Main frame with padding and better styling
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
        
        # Configure grid weights for responsive design
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Excel to VCF Converter", 
                           font=("Segoe UI", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # File Selection Section with better styling
        file_section = ttk.LabelFrame(main_frame, text="📁 Select Excel File", padding="15")
        file_section.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        file_section.columnconfigure(0, weight=1)
        
        file_frame = ttk.Frame(file_section)
        file_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
        file_frame.columnconfigure(0, weight=1)
        
        self.file_entry = ttk.Entry(file_frame, textvariable=self.excel_file_path, width=60, font=("Segoe UI", 10))
        self.file_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        
        browse_btn = ttk.Button(file_frame, text="Browse", command=self.browse_excel_file, width=12)
        browse_btn.grid(row=0, column=1)
        
        # Column Mapping Section with better styling
        mapping_section = ttk.LabelFrame(main_frame, text="📋 Map Excel Columns to Contact Fields", padding="15")
        mapping_section.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 15))
        mapping_section.columnconfigure(0, weight=1)
        mapping_section.rowconfigure(1, weight=1)
        
        # Create scrollable frame for column mapping
        canvas = tk.Canvas(mapping_section, height=250, bg='white')
        scrollbar = ttk.Scrollbar(mapping_section, orient="vertical", command=canvas.yview)
        self.mapping_frame = ttk.Frame(canvas)
        
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas_frame = canvas.create_window((0, 0), window=self.mapping_frame, anchor="nw")
        
        canvas.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(5, 0))
        scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
        
        # Configure canvas and frame
        canvas.columnconfigure(0, weight=1)
        self.mapping_frame.columnconfigure(1, weight=1)
        
        # Update scroll region when frame changes
        def configure_scroll_region(event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))
        self.mapping_frame.bind("<Configure>", configure_scroll_region)
        
        # Options Section with better styling
        options_section = ttk.LabelFrame(main_frame, text="⚙️ Options", padding="15")
        options_section.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        
        # First row of options
        options_row1 = ttk.Frame(options_section)
        options_row1.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.country_code_check = ttk.Checkbutton(options_row1, text="Auto-fix country codes", 
                                           variable=self.fix_country_code)
        self.country_code_check.grid(row=0, column=0, sticky=tk.W)
        
        ttk.Label(options_row1, text="Default country code:").grid(row=0, column=1, padx=(30, 5))
        country_code_combo = ttk.Combobox(options_row1, textvariable=self.default_country_code, 
                                         values=["+60", "+1", "+44", "+91", "+86", "+81", "+82", "+66", "+65", "+62"], 
                                         state="readonly", width=10)
        country_code_combo.grid(row=0, column=2)
        
        # Second row of options
        options_row2 = ttk.Frame(options_section)
        options_row2.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        ttk.Label(options_row2, text="Preview count:").grid(row=0, column=0, sticky=tk.W)
        preview_combo = ttk.Combobox(options_row2, textvariable=self.preview_count, 
                                   values=["5", "10", "20", "50", "100"], 
                                   state="readonly", width=10)
        preview_combo.grid(row=0, column=1, padx=(10, 0), sticky=tk.W)
        
        # Action Buttons with better styling
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=3, pady=(0, 15))
        
        # Style buttons
        style = ttk.Style()
        style.configure("Preview.TButton", font=("Segoe UI", 10))
        style.configure("Convert.TButton", font=("Segoe UI", 10, "bold"))
        
        preview_btn = ttk.Button(button_frame, text="👁️ Preview Contacts", 
                             command=self.preview_contacts, style="Preview.TButton", width=18)
        preview_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        convert_btn = ttk.Button(button_frame, text="🔄 Convert to VCF", 
                            command=self.convert_to_vcf, style="Convert.TButton", width=18)
        convert_btn.pack(side=tk.LEFT)
        
        template_btn = ttk.Button(button_frame, text="📄 Create Template", 
                             command=self.create_template, style="Preview.TButton", width=18)
        template_btn.pack(side=tk.LEFT, padx=(15, 0))
        
        # Status Label with better styling
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        
        self.status_label = ttk.Label(status_frame, text="📋 Please select an Excel file to begin", 
                                     font=("Segoe UI", 10), foreground="#0066cc")
        self.status_label.pack(side=tk.LEFT)
        
        # Configure main frame grid weights
        main_frame.rowconfigure(2, weight=1)
    
    def browse_excel_file(self):
        """Open file dialog to select Excel file"""
        file_path = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[
                ("Excel Files", "*.xlsx *.xls"),
                ("Excel 2007+", "*.xlsx"),
                ("Excel 97-2003", "*.xls"),
                ("All Files", "*.*")
            ]
        )
        
        if file_path:
            self.excel_file_path.set(file_path)
            self.load_excel_file()
    
    def load_excel_file(self):
        """Load Excel file and display column headers for mapping"""
        try:
            # Read Excel file
            self.df = pd.read_excel(self.excel_file_path.get())
            
            # Clear existing mapping widgets
            for widget in self.mapping_frame.winfo_children():
                widget.destroy()
            self.mapping_widgets.clear()
            self.column_mapping.clear()
            
            # Get column names
            columns = self.df.columns.tolist()
            
            # Create mapping interface with better headers
            header_frame = ttk.Frame(self.mapping_frame)
            header_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
            
            ttk.Label(header_frame, text="📊 Excel Column", font=("Segoe UI", 10, "bold")).pack(
                side=tk.LEFT, padx=(0, 30)
            )
            ttk.Label(header_frame, text="👤 Map to Contact Field", font=("Segoe UI", 10, "bold")).pack(
                side=tk.LEFT
            )
            
            # Create dropdown for each column with better styling
            for i, column in enumerate(columns, 1):
                row_frame = ttk.Frame(self.mapping_frame)
                row_frame.grid(row=i, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=3)
                
                ttk.Label(row_frame, text=column, font=("Segoe UI", 9)).pack(
                    side=tk.LEFT, anchor=tk.W
                )
                
                # Create combobox for field mapping
                mapping_var = tk.StringVar(value="Ignore")
                combobox = ttk.Combobox(row_frame, textvariable=mapping_var, 
                                      values=self.contact_fields, state="readonly", width=20)
                combobox.pack(side=tk.RIGHT, anchor=tk.E)
                
                # Store mapping
                self.mapping_widgets[column] = mapping_var
            
            self.status_label.config(text=f"✅ Loaded {len(self.df)} rows from Excel file", 
                                   foreground="#008800")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load Excel file:\n{str(e)}")
            self.status_label.config(text="❌ Error loading Excel file", foreground="#cc0000")
    
    def get_column_mapping(self):
        """Get the current column mapping from UI"""
        mapping = {}
        for column, var in self.mapping_widgets.items():
            field = var.get()
            if field != "Ignore":
                mapping[field] = column
        return mapping
    
    def preview_contacts(self):
        """Preview first few contacts based on current mapping"""
        if self.df is None:
            messagebox.showwarning("Warning", "Please load an Excel file first")
            return
        
        mapping = self.get_column_mapping()
        if not mapping:
            messagebox.showwarning("Warning", "Please map at least one column")
            return
        
        try:
            # Create preview window
            preview_window = tk.Toplevel(self.root)
            preview_window.title("Contact Preview")
            preview_window.geometry("600x400")
            
            # Create text widget with scrollbar
            text_frame = ttk.Frame(preview_window)
            text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            text_widget = tk.Text(text_frame, wrap=tk.WORD)
            scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=text_widget.yview)
            text_widget.configure(yscrollcommand=scrollbar.set)
            
            text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            # Generate preview with selected count
            try:
                preview_limit = int(self.preview_count.get())
            except ValueError:
                preview_limit = 10  # Default fallback
            
            preview_text = f"Preview of first {preview_limit} contacts:\n" + "="*50 + "\n\n"
            
            for i in range(min(preview_limit, len(self.df))):
                row = self.df.iloc[i]
                contact_info = []
                
                for field, column in mapping.items():
                    value = ""
                    if pd.notna(row[column]) and str(row[column]).strip():
                        raw_value = row[column]
                        # Handle phone numbers that might be read as floats
                        if field == "Phone Number" and isinstance(raw_value, (float, int)):
                            # Convert to int to remove decimal point and scientific notation
                            value = str(int(raw_value))
                            # Apply country code fixing for preview
                            value = self.fix_phone_country_code(value)
                        else:
                            value = str(raw_value).strip()
                    
                    if value:
                        contact_info.append(f"{field}: {value}")
                
                preview_text += f"Contact {i+1}:\n"
                if contact_info:
                    preview_text += "\n".join(contact_info)
                else:
                    preview_text += "No data available"
                preview_text += "\n" + "-"*30 + "\n\n"
            
            text_widget.insert(tk.END, preview_text)
            text_widget.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate preview:\n{str(e)}")
    
    def convert_to_vcf(self):
        """Convert Excel data to VCF file"""
        if self.df is None:
            messagebox.showwarning("Warning", "Please load an Excel file first")
            return
        
        mapping = self.get_column_mapping()
        if not mapping:
            messagebox.showwarning("Warning", "Please map at least one column")
            return
        
        try:
            # Ask for save location
            save_path = filedialog.asksaveasfilename(
                title="Save VCF File",
                defaultextension=".vcf",
                filetypes=[("VCF Files", "*.vcf"), ("All Files", "*.*")]
            )
            
            if not save_path:
                return
            
            # Generate VCF content
            vcf_content = self.generate_vcf_content(mapping)
            
            # Write to file
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(vcf_content)
            
            messagebox.showinfo("✅ Success", f"Successfully converted {len(self.df)} contacts to VCF file:\n{save_path}")
            self.status_label.config(text=f"✅ Successfully saved {len(self.df)} contacts to VCF file", 
                                   foreground="#008800")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert to VCF:\n{str(e)}")
            self.status_label.config(text="❌ Error converting to VCF", foreground="#cc0000")
    
    def create_template(self):
        """Create Excel template file for users"""
        try:
            # Create template data with examples
            template_data = [
                {
                    'Full Name* (Required)': 'John Doe',
                    'First Name': 'John',
                    'Last Name': 'Doe', 
                    'Phone Number* (Required)': '1173547602',
                    'Email': 'john.doe@email.com',
                    'Organization': 'ABC Corporation',
                    'Address': '123 Main Street, City, State 12345'
                },
                {
                    'Full Name* (Required)': 'Jane Smith',
                    'First Name': 'Jane',
                    'Last Name': 'Smith',
                    'Phone Number* (Required)': '01173547603', 
                    'Email': 'jane.smith@company.com',
                    'Organization': 'XYZ Industries',
                    'Address': '456 Oak Avenue, Town, State 67890'
                },
                {
                    'Full Name* (Required)': 'Mohamed Ali',
                    'First Name': 'Mohamed',
                    'Last Name': 'Ali',
                    'Phone Number* (Required)': '+601173547604',
                    'Email': 'mohamed.ali@business.com',
                    'Organization': 'Tech Solutions Sdn Bhd',
                    'Address': '789 Palm Road, Kuala Lumpur, 50000'
                }
            ]
            
            # Add empty rows
            for i in range(4, 21):
                template_data.append({
                    'Full Name* (Required)': '',
                    'First Name': '',
                    'Last Name': '',
                    'Phone Number* (Required)': '',
                    'Email': '',
                    'Organization': '',
                    'Address': ''
                })
            
            # Create DataFrame
            df = pd.DataFrame(template_data)
            
            # Ask user where to save template
            template_path = filedialog.asksaveasfilename(
                title="Save Excel Template",
                defaultextension=".xlsx",
                filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")],
                initialname="Excel_Contact_Template.xlsx"
            )
            
            if not template_path:
                return
            
            # Save to Excel
            df.to_excel(template_path, index=False, sheet_name='Contacts')
            
            messagebox.showinfo("✅ Template Created", 
                            f"Excel template created successfully!\n\n"
                            f"📁 Saved to: {template_path}\n\n"
                            f"📋 Template includes:\n"
                            f"• 3 example contacts with different phone formats\n"
                            f"• 17 empty rows for your data\n"
                            f"• Clear column headers with mandatory field indicators (*)\n"
                            f"• Compatible with Excel to VCF Converter\n\n"
                            f"💡 Open the template file and fill in your contact details!")
            
            self.status_label.config(text="✅ Excel template created successfully", foreground="#008800")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create template:\n{str(e)}")
            self.status_label.config(text="❌ Error creating template", foreground="#cc0000")
    
    def fix_phone_country_code(self, phone_number):
        """Automatically fix and standardize phone number country codes"""
        if not self.fix_country_code.get():
            return phone_number
        
        # Remove any existing country code and clean the number
        clean_phone = ''.join(c for c in phone_number if c.isdigit())
        
        if not clean_phone:
            return phone_number
        
        # Default country code
        default_code = self.default_country_code.get()
        
        # Check if number already has country code
        if phone_number.startswith('+'):
            # Already has proper format, keep as is
            return phone_number
        elif clean_phone.startswith('00'):
            # Replace 00 with +
            return '+' + clean_phone[2:]
        elif len(clean_phone) >= 12 and not clean_phone.startswith('0'):
            # Likely already has country code (12+ digits, doesn't start with 0)
            return '+' + clean_phone
        elif len(clean_phone) >= 11 and clean_phone.startswith('0'):
            # Remove leading 0 and add country code (common format)
            return default_code + clean_phone[1:]
        elif len(clean_phone) >= 10:  # 10+ digits, likely needs country code
            # Add default country code for numbers 10+ digits
            return default_code + clean_phone
        else:  # Less than 10 digits, local number
            # Add default country code
            return default_code + clean_phone
    
    def generate_vcf_content(self, mapping):
        """Generate VCF content from Excel data"""
        vcf_lines = []
        
        for index, row in self.df.iterrows():
            # Start vCard
            vcf_lines.append("BEGIN:VCARD")
            vcf_lines.append("VERSION:3.0")
            
            # Get contact data
            full_name = ""
            first_name = ""
            last_name = ""
            phone = ""
            email = ""
            organization = ""
            address = ""
            
            for field, column in mapping.items():
                value = ""
                if pd.notna(row[column]) and str(row[column]).strip():
                    raw_value = row[column]
                    # Handle phone numbers that might be read as floats
                    if field == "Phone Number" and isinstance(raw_value, (float, int)):
                        # Convert to int to remove decimal point and scientific notation
                        value = str(int(raw_value))
                    else:
                        value = str(raw_value).strip()
                
                if field == "Full Name":
                    full_name = value
                elif field == "First Name":
                    first_name = value
                elif field == "Last Name":
                    last_name = value
                elif field == "Phone Number":
                    phone = value
                elif field == "Email":
                    email = value
                elif field == "Organization":
                    organization = value
                elif field == "Address":
                    address = value
            
            # Handle name fields
            if full_name:
                vcf_lines.append(f"FN:{full_name}")
                # Use full name for structured name if no first/last provided
                if not first_name and not last_name:
                    vcf_lines.append(f"N:{full_name};;;;")
            else:
                # Construct full name from first and last if available
                if first_name or last_name:
                    full_name = f"{first_name} {last_name}".strip()
                    vcf_lines.append(f"FN:{full_name}")
                    vcf_lines.append(f"N:{last_name};{first_name};;;")
            
            # Add phone number
            if phone:
                # Apply country code fixing
                fixed_phone = self.fix_phone_country_code(phone)
                vcf_lines.append(f"TEL;TYPE=CELL:{fixed_phone}")
            
            # Add email
            if email:
                vcf_lines.append(f"EMAIL:{email}")
            
            # Add organization
            if organization:
                vcf_lines.append(f"ORG:{organization}")
            
            # Add address
            if address:
                # Format address for VCF (replace newlines with commas)
                formatted_address = address.replace('\n', ', ').replace('\r', '')
                vcf_lines.append(f"ADR;TYPE=HOME:;;{formatted_address};;;;")
            
            # End vCard
            vcf_lines.append("END:VCARD")
            vcf_lines.append("")  # Empty line between cards
        
        return '\n'.join(vcf_lines)

def main():
    """Main function to run the application"""
    root = tk.Tk()
    app = ExcelToVCFConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
