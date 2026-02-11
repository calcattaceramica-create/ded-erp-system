import os

# قراءة الملف الأصلي
with open('DED_Control_Panel.pyw', 'r', encoding='utf-8') as f:
    original_content = f.read()

# البحث عن قسم create_license_manager_tab
start_marker = "def create_license_manager_tab(self):"
end_marker = "def add_license(self):"

if start_marker in original_content and end_marker in original_content:
    start_idx = original_content.find(start_marker)
    end_idx = original_content.find(end_marker)
    
    # الكود الجديد المحسّن
    new_license_tab_code = '''def create_license_manager_tab(self):
        """إنشاء تاب مدير التراخيص بتصميم جميل ومتجاوب"""
        container = tk.Frame(self.license_tab_frame, bg=self.colors["card"])
        container.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)

        # العنوان الرئيسي
        title_frame = tk.Frame(container, bg=self.colors["card"])
        title_frame.pack(fill=tk.X, pady=(0, 25))
        
        tk.Label(title_frame, text="➕ إضافة ترخيص جديد - Add New License", 
                font=("Segoe UI", 18, "bold"),
                fg=self.colors["text"], bg=self.colors["card"]).pack()

        # حاوية النموذج مع Scrollbar
        form_container = tk.Frame(container, bg=self.colors["card"])
        form_container.pack(fill=tk.BOTH, expand=True)

        # Canvas للتمرير
        canvas = tk.Canvas(form_container, bg=self.colors["card"], highlightthickness=0)
        scrollbar = ttk.Scrollbar(form_container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=self.colors["card"])

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # النموذج
        form_frame = tk.Frame(scrollable_frame, bg=self.colors["card"])
        form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # حقول الإدخال بتصميم جميل
        self.create_modern_entry(form_frame, "🏢 اسم الشركة - Company:", "company")
        self.create_modern_entry(form_frame, "⏱️ المدة (أيام) - Duration:", "duration", default="365")
        self.create_modern_entry(form_frame, "👤 اسم المستخدم - Username:", "username")
        self.create_modern_entry(form_frame, "🔒 كلمة المرور - Password:", "password", is_password=True)
        self.create_modern_entry(form_frame, "📧 البريد الإلكتروني - Email:", "email")
        self.create_modern_entry(form_frame, "📱 رقم الهاتف - Phone:", "phone")
        self.create_modern_entry(form_frame, "👥 عدد المستخدمين - Max Users:", "max_users", default="10")

        # الأزرار
        buttons_frame = tk.Frame(form_frame, bg=self.colors["card"])
        buttons_frame.pack(fill=tk.X, pady=20)

        self.create_modern_button(buttons_frame, "✅ إنشاء الترخيص - Create License", 
                                 self.add_license, self.colors["primary"], self.colors["primary_hover"])
        
        self.create_modern_button(buttons_frame, "📋 عرض جميع التراخيص - View All Licenses", 
                                 self.view_licenses, self.colors["info"], "#2563eb")

    def create_modern_entry(self, parent, label_text, field_name, default="", is_password=False):
        """إنشاء حقل إدخال حديث"""
        entry_frame = tk.Frame(parent, bg=self.colors["card"])
        entry_frame.pack(fill=tk.X, pady=8)
        
        # Label
        label_container = tk.Frame(entry_frame, bg=self.colors["card"])
        label_container.pack(fill=tk.X, pady=(0, 8))
        
        tk.Label(label_container, text=label_text, font=("Segoe UI", 10, "bold"),
                fg="#374151", bg=self.colors["card"]).pack(side=tk.RIGHT)
        
        # Entry container with border
        entry_container = tk.Frame(entry_frame, bg="#e5e7eb", bd=0)
        entry_container.pack(fill=tk.X)
        
        # Inner frame for padding
        inner_frame = tk.Frame(entry_container, bg="#ffffff", bd=0)
        inner_frame.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Entry field
        if is_password:
            entry = tk.Entry(inner_frame, font=("Segoe UI", 11), bg="#ffffff",
                           fg="#1f2937", bd=0, relief=tk.FLAT, show="●")
        else:
            entry = tk.Entry(inner_frame, font=("Segoe UI", 11), bg="#ffffff",
                           fg="#1f2937", bd=0, relief=tk.FLAT)
        
        entry.pack(fill=tk.BOTH, expand=True, padx=12, pady=10)
        
        if default:
            entry.insert(0, default)
        
        # Focus effects
        entry.bind("<FocusIn>", lambda e: entry_container.configure(bg="#8b5cf6"))
        entry.bind("<FocusOut>", lambda e: entry_container.configure(bg="#e5e7eb"))
        
        # حفظ المرجع
        setattr(self, f"{field_name}_entry", entry)

    def create_modern_button(self, parent, text, command, bg_color, hover_color):
        """إنشاء زر حديث مع تأثيرات hover"""
        btn_frame = tk.Frame(parent, bg=bg_color, cursor="hand2")
        btn_frame.pack(fill=tk.X, pady=5)
        
        label = tk.Label(btn_frame, text=text, font=("Segoe UI", 11, "bold"),
                        fg="#ffffff", bg=bg_color, cursor="hand2")
        label.pack(padx=24, pady=12)
        
        # Hover effects
        def on_enter(e):
            btn_frame.configure(bg=hover_color)
            label.configure(bg=hover_color)
        
        def on_leave(e):
            btn_frame.configure(bg=bg_color)
            label.configure(bg=bg_color)
        
        btn_frame.bind("<Enter>", on_enter)
        btn_frame.bind("<Leave>", on_leave)
        btn_frame.bind("<Button-1>", lambda e: command())
        label.bind("<Enter>", on_enter)
        label.bind("<Leave>", on_leave)
        label.bind("<Button-1>", lambda e: command())

    '''
    
    # استبدال الكود القديم بالجديد
    new_content = original_content[:start_idx] + new_license_tab_code + original_content[end_idx:]
    
    # حفظ الملف الجديد
    with open('DED_Control_Panel_Beautiful.pyw', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ تم إنشاء الواجهة الجميلة بنجاح!")
    print(f"📁 الملف: DED_Control_Panel_Beautiful.pyw")
else:
    print("❌ لم يتم العثور على الأقسام المطلوبة")
