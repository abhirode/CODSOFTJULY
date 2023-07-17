import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    complexity = int(complexity_entry.get())

    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than zero.")
        return

    if complexity <= 0:
        messagebox.showerror("Error", "Password complexity must be greater than zero.")
        return

    characters = ""
    if complexity >= 1:
        characters += string.ascii_letters
    if complexity >= 2:
        characters += string.digits
    if complexity >= 3:
        characters += string.punctuation

    password = ''.join(random.choices(characters, k=length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

def reset_password():
    length_entry.delete(0, tk.END)
    length_entry.insert(tk.END, "8")
    complexity_entry.delete(0, tk.END)
    complexity_entry.insert(tk.END, "1")
    password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Password Generator")

# Heading
heading_label = tk.Label(root, text="Password Generator", font=("bold", 16))
heading_label.pack(pady=10)

# User Name Entry
user_frame = tk.Frame(root)
user_frame.pack(pady=5)

user_label = tk.Label(user_frame, text="User Name:")
user_label.pack(side=tk.LEFT)
user_entry = tk.Entry(user_frame)
user_entry.pack(side=tk.LEFT, padx=5)

# Password Length Entry
length_frame = tk.Frame(root)
length_frame.pack(pady=5)

length_label = tk.Label(length_frame, text="Password Length:")
length_label.pack(side=tk.LEFT)
length_entry = tk.Entry(length_frame)
length_entry.pack(side=tk.LEFT, padx=5)
length_entry.insert(tk.END, "8")

# Password Complexity Entry
complexity_frame = tk.Frame(root)
complexity_frame.pack(pady=5)

complexity_label = tk.Label(complexity_frame, text="Password Complexity:")
complexity_label.pack(side=tk.LEFT)
complexity_entry = tk.Entry(complexity_frame)
complexity_entry.pack(side=tk.LEFT, padx=5)
complexity_entry.insert(tk.END, "1")

# Generate Password Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Password Display
password_frame = tk.Frame(root)
password_frame.pack(pady=5)

password_label = tk.Label(password_frame, text="Password:")
password_label.pack(side=tk.LEFT)
password_entry = tk.Entry(password_frame)
password_entry.pack(side=tk.LEFT, padx=5)

# Reset Password Button
reset_button = tk.Button(root, text="Reset Password", command=reset_password)
reset_button.pack(pady=10)

root.mainloop()
