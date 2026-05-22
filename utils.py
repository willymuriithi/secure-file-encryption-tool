from pathlib import Path
from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

KEY_FILE = Path("secret.key")


def ensure_key(key_path: Path = KEY_FILE) -> bytes:
    if not key_path.exists():
        key_path.write_bytes(Fernet.generate_key())
    return key_path.read_bytes()


def get_fernet(key_path: Path = KEY_FILE) -> Fernet:
    key = ensure_key(key_path)
    return Fernet(key)


def generate_salt(length: int = 16) -> bytes:
    """Generate a random salt for password-based key derivation."""
    return os.urandom(length)


def derive_key_from_password(password: str, salt: bytes, iterations: int = 390000) -> bytes:
    """Derive a 32-byte key from a password and salt using PBKDF2-HMAC-SHA256.

    Returns a URL-safe base64-encoded key suitable for Fernet.
    """
    password_bytes = password.encode("utf-8")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )
    key = kdf.derive(password_bytes)
    return base64.urlsafe_b64encode(key)


def get_fernet_from_password(password: str, salt: bytes) -> Fernet:
    key = derive_key_from_password(password, salt)
    return Fernet(key)
