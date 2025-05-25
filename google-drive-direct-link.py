import tkinter as tk
from tkinter import ttk
import re
import pyperclip

def convert_link(event=None):
    input_url = entry_input.get()
    
    # استخراج آیدی فایل با regex پیشرفته
    match = re.search(r'(/d/|id=)([a-zA-Z0-9_-]+)', input_url)
    if not match:
        show_status("لینک معتبر نیست! فرمت صحیح: https://drive.google.com/...", "error")
        return
    
    file_id = match.group(2)
    converted_url = f"https://lh3.googleusercontent.com/d/{file_id}"
    
    # به روزرسانی فیلد خروجی
    entry_output.config(state='normal')
    entry_output.delete(0, tk.END)
    entry_output.insert(0, converted_url)
    entry_output.config(state='readonly')
    
    # کپی اتوماتیک و نمایش پیام
    pyperclip.copy(converted_url)
    show_status("لینک تبدیل و کپی شد!", "success")

def show_status(message, type):
    status_label.config(text=message, foreground=("red" if type == "error" else "green"))
    root.after(3000, lambda: status_label.config(text=""))

def paste_text(event=None):
    try:
        text = root.clipboard_get()
        entry_input.delete(0, tk.END)
        entry_input.insert(0, text)
    except tk.TclError:
        show_status("کلیپ‌بورد خالی یا حاوی متن نامعتبر است", "error")

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("Google Drive Link Converter")
root.geometry("650x250")
root.resizable(False, False)

# تنظیمات استایل پیشرفته
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", font=("B Nazanin", 12))
style.configure("TButton", font=("B Nazanin", 12), padding=6)
style.configure("TEntry", padding=5)

# ایجاد منوی راست کلیک
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Paste", command=paste_text)

def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

# بخش ورودی
frame_input = ttk.Frame(root)
frame_input.pack(pady=10, padx=10, fill=tk.X)

ttk.Label(frame_input, text="لینک را وارد کنید (Ctrl+V یا کلیک راست):").pack(side=tk.TOP, anchor=tk.W)
entry_input = ttk.Entry(frame_input, width=70)
entry_input.pack(side=tk.LEFT, fill=tk.X, expand=True)

# اتصال رویدادها
root.bind_all("<Control-v>", paste_text)  # برای ویندوز/لینوکس
root.bind_all("<Command-v>", paste_text)  # برای مک
entry_input.bind("<Button-3>", show_context_menu)  # کلیک راست

# دکمه تبدیل
btn_convert = ttk.Button(root, text="تبدیل کن", command=convert_link)
btn_convert.pack(pady=8)

# بخش خروجی
frame_output = ttk.Frame(root)
frame_output.pack(pady=10, padx=10, fill=tk.X)

ttk.Label(frame_output, text="لینک تبدیل شده:").pack(side=tk.TOP, anchor=tk.W)
entry_output = ttk.Entry(frame_output, width=70, state='readonly')
entry_output.pack(side=tk.LEFT, fill=tk.X, expand=True)

# نوار وضعیت
status_label = ttk.Label(root, text="", font=("B Nazanin", 10))
status_label.pack(pady=5)

root.mainloop()