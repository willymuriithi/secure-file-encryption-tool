# Secure File Encryption Tool

A simple desktop application to encrypt and decrypt files using either a key file or a password. It uses Python's `cryptography` library and a Tkinter GUI for easy use.

## Install as a Python package

1. Open a terminal in the project folder.
2. Create a virtual environment (recommended):
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install the app:
   ```powershell
   py -m pip install --upgrade pip
   py -m pip install .
   ```
4. Run the GUI app:
   ```powershell
   secure-file-encryption-tool
   ```

## Run directly from source

```powershell
py gui.py
```

## Build a standalone Windows executable

1. Install PyInstaller:
   ```powershell
   py -m pip install pyinstaller
   ```
2. Build the executable:
   ```powershell
   pyinstaller --onefile --windowed --name SecureFileEncryptionTool gui.py
   ```
3. Find the app in `dist\SecureFileEncryptionTool.exe`.

## Build a Windows installer

This project includes an Inno Setup script and helper batch file to create a Windows installer.

1. Install Inno Setup 6 or later from https://jrsoftware.org/isinfo.php
2. Build the installer:
   ```powershell
   .\build_installer.bat
   ```
3. The installer will be created in the `Output` folder as `SecureFileEncryptionToolInstaller.exe`.

> If Inno Setup is not installed or `ISCC.exe` is not on your PATH, the batch file will prompt you to install it.

## Build a wheel distribution

```powershell
py -m pip install build
py -m build
```

Then install the wheel:
```powershell
py -m pip install dist\secure_file_encryption_tool-0.1.0-py3-none-any.whl
```

## Usage

- Select a file to encrypt or decrypt.
- Choose either `Key file` mode or `Password` mode.
- Click `Encrypt` or `Decrypt`.

## Notes

- In key mode, the app uses `secret.key` by default and creates one automatically if missing.
- In password mode, the app stores a salt prefix inside the encrypted file and derives the key from the password.
