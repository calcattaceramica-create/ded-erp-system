import re

# قراءة الملف
with open('DED_Control_Panel.pyw', 'r', encoding='utf-8') as f:
    content = f.read()

# تحسين حقول الإدخال - إضافة padding وتحسين الخطوط
improvements = [
    # تحسين حجم الخط في حقول الإدخال
    ('font=("Segoe UI", 10)', 'font=("Segoe UI", 11)'),
    ('font=("Segoe UI", 9)', 'font=("Segoe UI", 10)'),
    
    # تحسين padding في الأزرار
    ('padx=20, pady=10', 'padx=24, pady=12'),
    ('padx=15, pady=8', 'padx=20, pady=10'),
    
    # تحسين العناوين
    ('font=("Segoe UI", 16, "bold")', 'font=("Segoe UI", 18, "bold")'),
    ('font=("Segoe UI", 14, "bold")', 'font=("Segoe UI", 16, "bold")'),
]

for old, new in improvements:
    content = content.replace(old, new)

# حفظ الملف
with open('DED_Control_Panel.pyw', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ تم تحسين حقول الإدخال والأزرار!')
print('📝 التحسينات:')
print('   - خطوط أكبر وأوضح')
print('   - padding محسّن للأزرار')
print('   - عناوين أكبر وأكثر وضوحاً')
