from pathlib import Path
from cryptography.fernet import Fernet

KEY_FILE = Path("secret.key")


def ensure_key(key_path: Path = KEY_FILE) -> bytes:
    if not key_path.exists():
        key_path.write_bytes(Fernet.generate_key())
    return key_path.read_bytes()


def get_fernet(key_path: Path = KEY_FILE) -> Fernet:
    key = ensure_key(key_path)
    return Fernet(key)
