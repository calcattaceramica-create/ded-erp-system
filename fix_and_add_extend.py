# -*- coding: utf-8 -*-
import re

# قراءة الملف
with open('DED_Control_Panel.pyw', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. إضافة زر تمديد المدة
old_row2 = '''        create_action_btn(row2, "✏️ تعديل\\nEdit",
                         self.edit_license, self.colors['info'], self.colors['accent']).pack(
                         side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        create_action_btn(row2, "📄 عرض التفاصيل\\nView Details",
                         self.view_license_details, self.colors['purple_tab'], self.colors['accent']).pack(
                         side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        create_action_btn(row2, "🔄 تحديث\\nRefresh",
                         self.refresh_list, self.colors['success'], self.colors['success_hover']).pack(
                         side=tk.LEFT, padx=5, expand=True, fill=tk.X)'''

new_row2 = '''        create_action_btn(row2, "✏️ تعديل\\nEdit",
                         self.edit_license, self.colors['info'], self.colors['accent']).pack(
                         side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        create_action_btn(row2, "⏱️ تمديد المدة\\nExtend Duration",
                         self.extend_license, self.colors['warning'], self.colors['warning_hover']).pack(
                         side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        create_action_btn(row2, "📄 عرض التفاصيل\\nView Details",
                         self.view_license_details, self.colors['purple_tab'], self.colors['accent']).pack(
                         side=tk.LEFT, padx=5, expand=True, fill=tk.X)

        create_action_btn(row2, "🔄 تحديث\\nRefresh",
                         self.refresh_list, self.colors['success'], self.colors['success_hover']).pack(
                         side=tk.LEFT, padx=5, expand=True, fill=tk.X)'''

content = content.replace(old_row2, new_row2)

# 2. إضافة وظيفة extend_license
extend_func = '''
    def extend_license(self):
        """Extend License Duration"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a license!")
            return
        
        item = self.tree.item(selected[0])
        company = item['values'][0]
        
        license_key = None
        for key, data in self.licenses.items():
            if data.get('company') == company:
                license_key = key
                break
        
        if not license_key:
            messagebox.showerror("Error", "License not found!")
            return
        
        extend_window = tk.Toplevel(self.root)
        extend_window.title("Extend License Duration")
        extend_window.geometry("600x400")
        extend_window.configure(bg=self.colors['bg'])
        extend_window.transient(self.root)
        extend_window.grab_set()
        
        extend_window.update_idletasks()
        x = (extend_window.winfo_screenwidth() // 2) - (600 // 2)
        y = (extend_window.winfo_screenheight() // 2) - (400 // 2)
        extend_window.geometry(f'600x400+{x}+{y}')
        
        header = tk.Frame(extend_window, bg=self.colors['warning'], height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text="Extend License Duration",
            font=("Segoe UI", 16, "bold"),
            bg=self.colors['warning'],
            fg='white'
        ).pack(expand=True)
        
        content_frame = tk.Frame(extend_window, bg=self.colors['bg'])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        tk.Label(
            content_frame,
            text=f"Company: {company}",
            font=("Segoe UI", 14, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['text']
        ).pack(pady=10)
        
        current_expiry = self.licenses[license_key].get('expiry', 'N/A')
        tk.Label(
            content_frame,
            text=f"Current Expiry: {current_expiry}",
            font=("Segoe UI", 12),
            bg=self.colors['bg'],
            fg=self.colors['text']
        ).pack(pady=10)
        
        tk.Label(
            content_frame,
            text="Days to Extend:",
            font=("Segoe UI", 12, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['text']
        ).pack(pady=(20, 10))
        
        days_entry = tk.Entry(
            content_frame,
            font=("Segoe UI", 14),
            width=20,
            relief=tk.FLAT,
            bg=self.colors['card'],
            fg=self.colors['text'],
            insertbackground=self.colors['text']
        )
        days_entry.pack(pady=10, ipady=10)
        days_entry.insert(0, "30")
        days_entry.focus()
        
        btn_frame = tk.Frame(content_frame, bg=self.colors['bg'])
        btn_frame.pack(pady=30)
        
        def perform_extend():
            try:
                days = int(days_entry.get())
                if days <= 0:
                    messagebox.showerror("Error", "Please enter a valid number of days!")
                    return
                
                from datetime import datetime, timedelta
                current_date = datetime.strptime(current_expiry, "%Y-%m-%d")
                new_date = current_date + timedelta(days=days)
                new_expiry = new_date.strftime("%Y-%m-%d")
                
                self.licenses[license_key]['expiry'] = new_expiry
                self.licenses[license_key]['duration_days'] = self.licenses[license_key].get('duration_days', 365) + days
                
                self.save_licenses()
                self.sync_license_to_database(license_key, self.licenses[license_key])
                self.refresh_list()
                
                extend_window.destroy()
                messagebox.showinfo("Success", f"License extended successfully!\\n\\nNew Date: {new_expiry}")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to extend:\\n{str(e)}")
        
        tk.Button(
            btn_frame,
            text="Extend",
            font=("Segoe UI", 12, "bold"),
            bg=self.colors['success'],
            fg='white',
            relief=tk.FLAT,
            cursor="hand2",
            command=perform_extend,
            padx=30,
            pady=12
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            btn_frame,
            text="Cancel",
            font=("Segoe UI", 12, "bold"),
            bg=self.colors['danger'],
            fg='white',
            relief=tk.FLAT,
            cursor="hand2",
            command=extend_window.destroy,
            padx=30,
            pady=12
        ).pack(side=tk.LEFT, padx=10)

'''

# إضافة الوظيفة قبل view_license_details
pattern = r'(\s+def view_license_details\(self\):)'
content = re.sub(pattern, extend_func + r'\1', content)

# حفظ الملف
with open('DED_Control_Panel.pyw', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")

