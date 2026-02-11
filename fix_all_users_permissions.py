"""
Fix all users permissions on Render
إصلاح صلاحيات جميع المستخدمين على Render
"""
import os
os.environ['FLASK_ENV'] = 'production'

from run import app, db
from app.models import User, Role, Permission

print("=" * 80)
print("🔧 إصلاح صلاحيات جميع المستخدمين")
print("🔧 Fix all users permissions")
print("=" * 80)

with app.app_context():
    # Get all users
    users = User.query.all()
    
    print(f"\n📊 عدد المستخدمين: {len(users)}")
    print(f"📊 Total users: {len(users)}\n")
    
    # Get admin role
    admin_role = Role.query.filter_by(name='admin').first()
    
    if not admin_role:
        print("❌ دور admin غير موجود!")
        print("❌ Admin role not found!")
        exit(1)
    
    # Check if admin role has all permissions
    all_permissions = Permission.query.all()
    print(f"📊 عدد الصلاحيات الكلية: {len(all_permissions)}")
    print(f"📊 Total permissions: {len(all_permissions)}")
    print(f"📊 صلاحيات دور admin: {len(admin_role.permissions)}")
    print(f"📊 Admin role permissions: {len(admin_role.permissions)}\n")
    
    # Make sure admin role has all permissions
    if len(admin_role.permissions) < len(all_permissions):
        print("⚠️ دور admin لا يملك جميع الصلاحيات!")
        print("⚠️ Admin role doesn't have all permissions!")
        print("🔧 إضافة جميع الصلاحيات لدور admin...")
        
        admin_role.permissions = all_permissions
        db.session.commit()
        print("✅ تم إضافة جميع الصلاحيات لدور admin\n")
    
    # Fix each user
    for user in users:
        print(f"\n👤 المستخدم: {user.username}")
        print(f"   - ID: {user.id}")
        print(f"   - الاسم: {user.full_name}")
        print(f"   - is_admin: {user.is_admin}")
        print(f"   - is_active: {user.is_active}")
        print(f"   - role_id: {user.role_id}")
        print(f"   - role: {user.role.name if user.role else 'None'}")
        
        changes_made = False
        
        # Make sure user is active
        if not user.is_active:
            print("   ⚠️ المستخدم غير نشط - سيتم تفعيله")
            user.is_active = True
            changes_made = True
        
        # If user is admin username, make sure is_admin=True
        if user.username == 'admin' and not user.is_admin:
            print("   ⚠️ مستخدم admin ليس is_admin=True - سيتم تفعيله")
            user.is_admin = True
            changes_made = True
        
        # Make sure user has admin role
        if user.role_id != admin_role.id:
            print(f"   ⚠️ المستخدم ليس في دور admin - سيتم تغييره من {user.role.name if user.role else 'None'} إلى admin")
            user.role_id = admin_role.id
            changes_made = True
        
        if changes_made:
            db.session.commit()
            print("   ✅ تم تحديث المستخدم")
        else:
            print("   ✅ المستخدم صحيح")
        
        # Test permissions
        print(f"   🔍 اختبار الصلاحيات:")
        print(f"      - has_permission('dashboard.view'): {user.has_permission('dashboard.view')}")
        print(f"      - has_permission('sales.create'): {user.has_permission('sales.create')}")
        print(f"      - has_permission('settings.view'): {user.has_permission('settings.view')}")

print("\n" + "=" * 80)
print("✅ تم الانتهاء!")
print("✅ Done!")
print("\n📝 الآن:")
print("   1. جميع المستخدمين نشطون (is_active=True)")
print("   2. جميع المستخدمين في دور admin")
print("   3. دور admin يملك جميع الصلاحيات")
print("   4. مستخدم admin لديه is_admin=True")
print("\n📝 Now:")
print("   1. All users are active (is_active=True)")
print("   2. All users have admin role")
print("   3. Admin role has all permissions")
print("   4. Admin user has is_admin=True")
print("\n🔄 يرجى تسجيل الخروج ثم الدخول مرة أخرى")
print("🔄 Please logout and login again")
print("=" * 80)

