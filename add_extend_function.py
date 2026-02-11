# -*- coding: utf-8 -*-

with open('DED_Control_Panel.pyw', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# الوظيفة الجديدة
extend_function = '''    def extend_license(self):
        """Extend License Duration"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("تحذير - Warning", "الرجاء اختيار ترخيص!\\nPlease select a license!")
            return
        
        item = self.tree.item(selected[0])
        company = item['values'][0]
        
        license_key = None
        for key, data in self.licenses.items():
            if data.get('company') == company:
                license_key = key
                break
        
        if not license_key:
            messagebox.showerror("خطأ - Error", "الترخيص غير موجود!\\nLicense not found!")
            return
        
        extend_window = tk.Toplevel(self.root)
        extend_window.title("تمديد مدة الترخيص - Extend License Duration")
        extend_window.geometry("600x400")
        extend_window.configure(bg=self.colors['bg'])
        extend_window.transient(self.root)
        extend_window.grab_set()
        
        extend_window.update_idletasks()
        x = (extend_window.winfo_screenwidth() // 2) - (600 // 2)
        y = (extend_window.winfo_screenheight() // 2) - (400 // 2)
        extend_window.geometry('600x400+{}+{}'.format(x, y))
        
        header = tk.Frame(extend_window, bg=self.colors['warning'], height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        tk.Label(
            header,
            text="⏱️ تمديد مدة الترخيص\\nExtend License Duration",
            font=("Segoe UI", 16, "bold"),
            bg=self.colors['warning'],
            fg='white'
        ).pack(expand=True)
        
        content_frame = tk.Frame(extend_window, bg=self.colors['bg'])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        tk.Label(
            content_frame,
            text="الشركة - Company: {}".format(company),
            font=("Segoe UI", 14, "bold"),
            bg=self.colors['bg'],
            fg=self.colors['text']
        ).pack(pady=10)
        
        current_expiry = self.licenses[license_key].get('expiry', 'N/A')
        tk.Label(
            content_frame,
            text="تاريخ الانتهاء الحالي - Current Expiry: {}".format(current_expiry),
            font=("Segoe UI", 12),
            bg=self.colors['bg'],
            fg=self.colors['text']
        ).pack(pady=10)
        
        tk.Label(
            content_frame,
            text="عدد الأيام للتمديد - Days to Extend:",
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
                    messagebox.showerror("خطأ - Error", "الرجاء إدخال عدد صحيح من الأيام!\\nPlease enter a valid number of days!")
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
                success_msg = "تم تمديد الترخيص بنجاح!\\n\\nLicense extended successfully!\\n\\nالتاريخ الجديد - New Date: {}".format(new_expiry)
                messagebox.showinfo("نجح - Success", success_msg)
            except ValueError:
                messagebox.showerror("خطأ - Error", "الرجاء إدخال رقم صحيح!\\nPlease enter a valid number!")
            except Exception as e:
                error_msg = "فشل التمديد - Failed to extend:\\n{}".format(str(e))
                messagebox.showerror("خطأ - Error", error_msg)
        
        tk.Button(
            btn_frame,
            text="✅ تمديد - Extend",
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
            text="❌ إلغاء - Cancel",
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

# إدراج الوظيفة قبل view_license_details (قبل السطر 1457)
lines.insert(1456, extend_function)

# حفظ الملف
with open('DED_Control_Panel.pyw', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Function added successfully!")

