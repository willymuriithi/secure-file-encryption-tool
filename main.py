from encrypt import encrypt_file
from decrypt import decrypt_file


def main():
    print("Secure File Encryption Tool")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a file? (E/D): ").strip().lower()
    file_path = input("Enter the file path: ").strip()

    if choice == 'e':
        encrypt_file(file_path)
    elif choice == 'd':
        decrypt_file(file_path)
    else:
        print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")


if __name__ == "__main__":
    main()