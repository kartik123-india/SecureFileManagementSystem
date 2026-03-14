import tkinter as tk
from tkinter import filedialog
from auth import register, login
from encryption import encrypt_file, decrypt_file

def register_user():
    register(username.get(), password.get())
    status.config(text="User Registered")

def login_user():
    result = login(username.get(), password.get())

    if result:
        status.config(text="Login Successful")
    else:
        status.config(text="Login Failed")

def encrypt():
    file_path = filedialog.askopenfilename()
    encrypt_file(file_path, password.get())
    status.config(text="File Encrypted")

def decrypt():
    decrypt_file(password.get())
    status.config(text="File Decrypted")

root = tk.Tk()
root.title("Secure File Management System")

tk.Label(root, text="Username").pack()
username = tk.Entry(root)
username.pack()

tk.Label(root, text="Password").pack()
password = tk.Entry(root, show="*")
password.pack()

tk.Button(root, text="Register", command=register_user).pack()
tk.Button(root, text="Login", command=login_user).pack()

tk.Button(root, text="Encrypt File", command=encrypt).pack()
tk.Button(root, text="Decrypt File", command=decrypt).pack()

status = tk.Label(root, text="")
status.pack()

root.mainloop()