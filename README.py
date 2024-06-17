import tkinter as tk
from tkinter import messagebox
import math

# تابع ارزیابی عبارت
def evaluate_expression(expression):
    try:
        # تبدیل توابع به فرمت قابل اجرا در پایتون
        expression = expression.replace('^', '**').replace('π', str(math.pi)).replace('e', str(math.e))
        result = str(eval(expression))
        return result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        return ""

# تابع پردازش کلیک دکمه
def on_button_click(button_text):
    current_text = display_var.get()
    if button_text == "=":
        result = evaluate_expression(current_text)
        display_var.set(result)
    elif button_text == "C":
        display_var.set("")
    elif button_text == "√":
        result = str(math.sqrt(float(current_text)))
        display_var.set(result)
    else:
        display_var.set(current_text + button_text)

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("ماشین حساب مهندسی")

# تنظیم رنگ پس‌زمینه ملایم
root.configure(bg='#f0f0f0')

# متغیر برای نمایش مقدار در نمایشگر
display_var = tk.StringVar()

# ایجاد و تنظیم نمایشگر
display = tk.Entry(root, textvariable=display_var, font=('Arial', 20), bd=10, insertwidth=2, width=20, borderwidth=4, bg='#ffffff')
display.grid(row=0, column=0, columnspan=5)

# لیست دکمه‌ها
buttons = [
    '7', '8', '9', '/', 'sin',
    '4', '5', '6', '*', 'cos',
    '1', '2', '3', '-', 'tan',
    '0', '.', '=', '+', 'log',
    '(', ')', '^', '√', 'π',
    'C', 'exp', 'e', 'mod', 'ln'
]

# رنگ دکمه‌ها
button_bg = '#dcdcdc'
button_fg = '#000000'
active_bg = '#a9a9a9'

# تابع برای تغییر رنگ دکمه هنگام فشردن
def on_press(event):
    event.widget.config(bg=active_bg)

# تابع برای بازگرداندن رنگ دکمه به حالت اولیه
def on_release(event):
    event.widget.config(bg=button_bg)

# ایجاد و تنظیم دکمه‌ها
row_val = 1
col_val = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, font=('Arial', 14),
                       bg=button_bg, fg=button_fg, bd=0,
                       command=lambda text=button_text: on_button_click(text))
    button.grid(row=row_val, column=col_val, padx=5, pady=5, ipadx=20, ipady=20)
    button.bind("<ButtonPress-1>", on_press)
    button.bind("<ButtonRelease-1>", on_release)
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

# شروع حلقه اصلی برنامه
root.mainloop()
