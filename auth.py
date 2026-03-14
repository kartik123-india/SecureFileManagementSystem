import hashlib
import sqlite3

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):

    conn = sqlite3.connect("vault/users.db")
    cursor = conn.cursor()

    hashed = hash_password(password)

    cursor.execute(
        "INSERT INTO users VALUES (?, ?)",
        (username, hashed)
    )

    conn.commit()
    conn.close()

    print("User Registered")

def login(username, password):

    conn = sqlite3.connect("vault/users.db")
    cursor = conn.cursor()

    hashed = hash_password(password)

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hashed)
    )

    result = cursor.fetchone()

    conn.close()

    return result