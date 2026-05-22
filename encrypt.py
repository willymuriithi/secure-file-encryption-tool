from pathlib import Path
from utils import get_fernet, get_fernet_from_password, generate_salt, pack_file_payload


def encrypt_file(file_path: str, key_path: str = "secret.key", password: str = None):
    source_path = Path(file_path)
    if not source_path.exists():
        print(f"File not found: {source_path}")
        return

    data = source_path.read_bytes()
    payload = pack_file_payload(source_path.name, data)
    encrypted_file_path = source_path.with_name(source_path.name + ".encrypted")

    if password:
        salt = generate_salt()
        fernet = get_fernet_from_password(password, salt)
        encrypted_data = fernet.encrypt(payload)
        encrypted_file_path.write_bytes(salt + encrypted_data)
    else:
        fernet = get_fernet(Path(key_path))
        encrypted_data = fernet.encrypt(payload)
        encrypted_file_path.write_bytes(encrypted_data)

    print(f"File encrypted successfully: {encrypted_file_path}")
    return encrypted_file_path
            