from pathlib import Path
from utils import get_fernet


def encrypt_file(file_path: str, key_path: str = "secret.key"):
    source_path = Path(file_path)
    if not source_path.exists():
        print(f"File not found: {source_path}")
        return

    fernet = get_fernet(Path(key_path))
    encrypted_data = fernet.encrypt(source_path.read_bytes())
    encrypted_file_path = source_path.with_name(source_path.name + ".encrypted")
    encrypted_file_path.write_bytes(encrypted_data)

    print(f"File encrypted successfully: {encrypted_file_path}")
            