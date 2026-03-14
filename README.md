# Secure File Management System

A Python-based secure file storage application that protects files using strong cryptographic techniques.

## Features
- User Authentication using SHA-256 password hashing
- AES-256 File Encryption
- File Decryption
- Secure File Vault
- Graphical User Interface using Tkinter
- SQLite database for user management

## Technologies Used
- Python
- AES-256 (PyCryptodome)
- SHA-256
- SQLite
- Tkinter GUI

## How to Run the Project

1. Install Python
2. Install dependencies

pip install pycryptodome

3. Run the application

python main.py

## Project Structure

SecureFileManagementSystem
│
├── main.py
├── auth.py
├── encryption.py
├── database.py
├── vault/
└── users.db
