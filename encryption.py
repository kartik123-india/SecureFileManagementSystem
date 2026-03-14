from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

def generate_key(password):
    return hashlib.sha256(password.encode()).digest()

def encrypt_file(file_path, password):
    key = generate_key(password)

    cipher = AES.new(key, AES.MODE_CBC)

    with open(file_path, "rb") as f:
        data = f.read()

    padding = 16 - len(data) % 16
    data += bytes([padding]) * padding

    ciphertext = cipher.encrypt(data)

    with open("vault/encrypted_file.bin", "wb") as f:
        f.write(cipher.iv)
        f.write(ciphertext)

    print("File Encrypted Successfully")


def decrypt_file(password):
    key = generate_key(password)

    with open("vault/encrypted_file.bin", "rb") as f:
        iv = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)

    data = cipher.decrypt(ciphertext)

    padding = data[-1]
    data = data[:-padding]

    with open("vault/decrypted_file", "wb") as f:
        f.write(data)

    print("File Decrypted Successfully")