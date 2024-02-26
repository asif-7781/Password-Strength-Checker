import tkinter as tk
from tkinter import ttk, messagebox
import string

def check_password_strength():
    password = entry_password.get()
    counts = {
        'lowercase': sum(1 for char in password if char in string.ascii_lowercase),
        'uppercase': sum(1 for char in password if char in string.ascii_uppercase),
        'digits': sum(1 for char in password if char in string.digits),
        'whitespaces': sum(1 for char in password if char == ' '),
        'special characters': len(password) - sum(counts.values())
    }

    strength = sum(1 for count in counts.values() if count > 0)

    if strength == 1:
        remarks = "Very Weak"
    elif strength == 2:
        remarks = "Weak"
    elif strength == 3:
        remarks = "Moderate"
    elif strength == 4:
        remarks = "Strong"
    elif strength == 5:
        remarks = "Very Strong"

    messagebox.showinfo("Password Strength Analysis", 
                        f"Password Strength: {remarks}\n"
                        f"Lowercase letters: {counts['lowercase']}\n"
                        f"Uppercase letters: {counts['uppercase']}\n"
                        f"Digits: {counts['digits']}\n"
                        f"Whitespaces: {counts['whitespaces']}\n"
                        f"Special characters: {counts['special characters']}")

def toggle_visibility():
    if entry_password.cget("show") == "":
        entry_password.config(show="*")
        button_visibility.config(text="Show Password")
    else:
        entry_password.config(show="")
        button_visibility.config(text="Hide Password")

root = tk.Tk()
root.title("Password Strength Checker")

style = ttk.Style()
style.theme_use('clam')

style.configure('TButton', font=('Arial', 12), background='#4CAF50', foreground='white')
style.configure('TLabel', font=('Arial', 12), background='#f0f0f0')
style.configure('TEntry', font=('Arial', 12))

label_password = ttk.Label(root, text="Enter Password:")
label_password.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_password = ttk.Entry(root, show="*")
entry_password.grid(row=0, column=1, padx=10, pady=10)

button_visibility = ttk.Button(root, text="Show Password", command=toggle_visibility)
button_visibility.grid(row=0, column=2, padx=10, pady=10)

button_check = ttk.Button(root, text="Check Strength", command=check_password_strength)
button_check.grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()
