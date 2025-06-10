from cryptography.fernet import Fernet
import os
import base64
from dotenv import load_dotenv

load_dotenv()

# Get encryption key from environment
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")

# If no key in environment, generate one (for development only)
if not ENCRYPTION_KEY:
    print("⚠️  WARNING: No ENCRYPTION_KEY found in .env file!")
    print("🔑 Generating a temporary key for this session...")
    ENCRYPTION_KEY = Fernet.generate_key().decode()
    print(f"📝 Add this to your .env file: ENCRYPTION_KEY={ENCRYPTION_KEY}")
    print("🚨 This is for development only - use generate_keys.py for production!")

# Ensure key is bytes
if isinstance(ENCRYPTION_KEY, str):
    ENCRYPTION_KEY = ENCRYPTION_KEY.encode()

try:
    cipher_suite = Fernet(ENCRYPTION_KEY)
    print("✅ Encryption module initialized successfully")
except ValueError as e:
    print(f"❌ Invalid encryption key: {e}")
    print("🔧 Run 'python generate_keys.py' to generate a valid key")
    # Generate a temporary key to prevent crash
    ENCRYPTION_KEY = Fernet.generate_key()
    cipher_suite = Fernet(ENCRYPTION_KEY)
    print("🔑 Using temporary encryption key for this session")

def encrypt_sensitive_data(data: str) -> str:
    """Encrypt sensitive data like contact information"""
    if not data:
        return data
    try:
        encrypted_data = cipher_suite.encrypt(data.encode())
        return base64.b64encode(encrypted_data).decode()
    except Exception as e:
        print(f"Encryption error: {e}")
        return data  # Return original data if encryption fails

def decrypt_sensitive_data(encrypted_data: str) -> str:
    """Decrypt sensitive data"""
    if not encrypted_data:
        return encrypted_data
    try:
        decoded_data = base64.b64decode(encrypted_data.encode())
        decrypted_data = cipher_suite.decrypt(decoded_data)
        return decrypted_data.decode()
    except Exception as e:
        print(f"Decryption error: {e}")
        return encrypted_data  # Return as-is if decryption fails