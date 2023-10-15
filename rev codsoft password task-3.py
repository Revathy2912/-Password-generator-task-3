#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_scale.get()
    complexity = complexity_scale.get()

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
    length_scale.set(8)
    complexity_scale.set(1)
    password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("PASSWORD GENERATOR")

# Heading
heading_label = tk.Label(root, text="PASSWORD GENERATOR", font=("bold", 20))
heading_label.pack(pady=10)

user_label = tk.Label(root, text="User Name:")
user_label.pack()
user_entry = tk.Entry(root)
user_entry.pack(pady=5)

length_label = tk.Label(root, text="Password Length:",font=("bold", 16))
length_label.pack()
length_scale = tk.Scale(root, from_=1, to=50, orient=tk.HORIZONTAL, length=200,bg="skyblue")
length_scale.set(8)
length_scale.pack(pady=5)
complexity_label = tk.Label(root, text="Password Complexity:",font=("bold", 16))
complexity_label.pack()
complexity_scale = tk.Scale(root, from_=1, to=3, orient=tk.HORIZONTAL, length=200,bg="skyblue")
complexity_scale.set(1)
complexity_scale.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password",bg="pink", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Password:",font=("bold", 25))
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack(pady=5)

reset_button = tk.Button(root, text="Reset Password", command=reset_password,bg="pink")
reset_button.pack(pady=5)

root.mainloop()


# In[ ]:




