import re

# قراءة الملف
with open('DED_Control_Panel.pyw', 'r', encoding='utf-8') as f:
    content = f.read()

# البحث عن زر التعديل وإضافة زر التمديد بجانبه
# البحث عن السطر الذي يحتوي على زر "تعديل"
edit_button_pattern = r"(create_action_btn\(row2, \"✏️ تعديل\\nEdit\",\s+self\.edit_license,.*?\)\.pack\(.*?\))"

# استبدال لإضافة زر التمديد
replacement = r'''\1

        create_action_btn(row2, "⏱️ تمديد المدة\\nExtend Duration",
                         self.extend_license, '#f59e0b', '#d97706').pack(
                         side=tk.LEFT, padx=5, expand=True, fill=tk.X)'''

content = re.sub(edit_button_pattern, replacement, content, count=1)

# حفظ الملف
with open('DED_Control_Panel.pyw', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ تم إضافة زر تمديد المدة في الواجهة!')
print('🎨 الزر الجديد: ⏱️ تمديد المدة - Extend Duration')
