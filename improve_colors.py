import re

# قراءة الملف الأصلي
with open('DED_Control_Panel.pyw', 'r', encoding='utf-8') as f:
    content = f.read()

# تحسين الألوان - استبدال الألوان القديمة بألوان جميلة
color_replacements = {
    "'bg': '#f8fafc'": "'bg': '#f0f4f8'",
    "'bg_light': '#ffffff'": "'bg_light': '#ffffff'",
    "'card': '#ffffff'": "'card': '#ffffff'",
    "'accent': '#3b82f6'": "'primary': '#8b5cf6'",
    "'accent_hover': '#2563eb'": "'primary_hover': '#7c3aed'",
    "'success': '#22c55e'": "'success': '#10b981'",
    "'success_hover': '#16a34a'": "'success_hover': '#059669'",
    "'purple_tab': '#a855f7'": "'purple_tab': '#8b5cf6'",
    "'gray_tab': '#6b7280'": "'gray_tab': '#6b7280'",
}

for old, new in color_replacements.items():
    content = content.replace(old, new)

# استبدال accent بـ primary في جميع الأماكن
content = content.replace("self.colors['accent']", "self.colors.get('primary', self.colors.get('accent', '#8b5cf6'))")
content = content.replace("self.colors['accent_hover']", "self.colors.get('primary_hover', self.colors.get('accent_hover', '#7c3aed'))")

# حفظ الملف المحسّن
with open('DED_Control_Panel.pyw', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ تم تحسين الألوان بنجاح!')
print('🎨 الألوان الجديدة:')
print('   - Primary: #8b5cf6 (بنفسجي جميل)')
print('   - Success: #10b981 (أخضر أنيق)')
print('   - Background: #f0f4f8 (رمادي فاتح)')
