import secrets
from cryptography.fernet import Fernet

def generate_secret_key(length=64):
    return secrets.token_urlsafe(length)

def generate_encryption_key():
    return Fernet.generate_key().decode()

if __name__ == "__main__":
    secret_key = generate_secret_key()
    encryption_key = generate_encryption_key()
    print(f"SECRET_KEY={secret_key}")
    print(f"ENCRYPTION_KEY={encryption_key}")