from pathlib import Path
from cryptography.fernet import InvalidToken
from utils import get_fernet, get_fernet_from_password, unpack_file_payload


def decrypt_file(file_path: str, key_path: str = "secret.key", password: str = None):
    encrypted_path = Path(file_path)
    if not encrypted_path.exists():
        print(f"File not found: {encrypted_path}")
        return

    encrypted_data = encrypted_path.read_bytes()

    try:
        if password:
            # first 16 bytes are salt
            salt = encrypted_data[:16]
            token = encrypted_data[16:]
            fernet = get_fernet_from_password(password, salt)
            decrypted_data = fernet.decrypt(token)
        else:
            fernet = get_fernet(Path(key_path))
            decrypted_data = fernet.decrypt(encrypted_data)
    except InvalidToken:
        print("Decryption failed: invalid key/password or corrupted file.")
        return

    original_name, file_data = unpack_file_payload(decrypted_data)
    if original_name:
        decrypted_file_path = encrypted_path.with_name(original_name)
    elif encrypted_path.suffix == ".encrypted":
        decrypted_file_path = encrypted_path.with_suffix(".decrypted")
    else:
        decrypted_file_path = encrypted_path.with_name(encrypted_path.name + ".decrypted")

    decrypted_file_path.write_bytes(file_data)
    print(f"File decrypted successfully: {decrypted_file_path}")
    return decrypted_file_path

