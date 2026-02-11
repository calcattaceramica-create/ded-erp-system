# -*- coding: utf-8 -*-

with open('DED_Control_Panel.pyw', 'r', encoding='utf-8') as f:
    content = f.read()

# إصلاح السطر 1552
old_text = '''                extend_window.destroy()
                messagebox.showinfo("Success", f"License extended successfully!

New Date: {new_expiry}")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to extend:
{str(e)}")'''

new_text = '''                extend_window.destroy()
                success_msg = f"License extended successfully!\n\nNew Date: {new_expiry}"
                messagebox.showinfo("Success", success_msg)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number!")
            except Exception as e:
                error_msg = f"Failed to extend:\n{str(e)}"
                messagebox.showerror("Error", error_msg)'''

content = content.replace(old_text, new_text)

with open('DED_Control_Panel.pyw', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed!")
