from pathlib import Path
from cryptography.fernet import InvalidToken
from utils import get_fernet


def decrypt_file(file_path: str, key_path: str = "secret.key"):
    encrypted_path = Path(file_path)
    if not encrypted_path.exists():
        print(f"File not found: {encrypted_path}")
        return

    fernet = get_fernet(Path(key_path))
    encrypted_data = encrypted_path.read_bytes()

    try:
        decrypted_data = fernet.decrypt(encrypted_data)
    except InvalidToken:
        print("Decryption failed: invalid key or corrupted file.")
        return

    if encrypted_path.suffix == ".encrypted":
        decrypted_file_path = encrypted_path.with_suffix(".decrypted")
    else:
        decrypted_file_path = encrypted_path.with_name(encrypted_path.name + ".decrypted")

    decrypted_file_path.write_bytes(decrypted_data)
    print(f"File decrypted successfully: {decrypted_file_path}")