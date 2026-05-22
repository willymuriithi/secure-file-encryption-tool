from pathlib import Path
from utils import get_fernet, get_fernet_from_password, generate_salt


def encrypt_file(file_path: str, key_path: str = "secret.key", password: str = None):
    source_path = Path(file_path)
    if not source_path.exists():
        print(f"File not found: {source_path}")
        return

    data = source_path.read_bytes()

    if password:
        # Password-based encryption: prefix file with salt
        salt = generate_salt()
        fernet = get_fernet_from_password(password, salt)
        encrypted_data = fernet.encrypt(data)
        encrypted_file_path = source_path.with_name(source_path.name + ".encrypted")
        # store salt + token
        encrypted_file_path.write_bytes(salt + encrypted_data)
    else:
        fernet = get_fernet(Path(key_path))
        encrypted_data = fernet.encrypt(data)
        encrypted_file_path = source_path.with_name(source_path.name + ".encrypted")
        encrypted_file_path.write_bytes(encrypted_data)

    print(f"File encrypted successfully: {encrypted_file_path}")
            