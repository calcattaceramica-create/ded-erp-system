# -*- coding: utf-8 -*-

with open('DED_Control_Panel.pyw', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# إضافة زر تمديد المدة بعد زر Edit (بعد السطر 771)
new_button = '''
        create_action_btn(row2, "⏱️ تمديد المدة\\nExtend Duration",
                         self.extend_license, self.colors['warning'], self.colors['warning_hover']).pack(
                         side=tk.LEFT, padx=5, expand=True, fill=tk.X)
'''

# إدراج الزر بعد السطر 771
lines.insert(772, new_button)

# حفظ الملف
with open('DED_Control_Panel.pyw', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Button added!")
