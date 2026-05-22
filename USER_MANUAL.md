# Secure File Encryption Tool — User Manual

## Overview

Secure File Encryption Tool is a desktop application for Windows that lets you encrypt and decrypt files using either:
- a generated key file, or
- a password-derived key.

The app can be run directly from Python or installed as a package. A Windows installer is also available for easy deployment.

---

## Installation

### Option 1: Install from source as a Python package

1. Open PowerShell in the project directory.
2. Create and activate a virtual environment:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install the package:
   ```powershell
   py -m pip install --upgrade pip
   py -m pip install .
   ```
4. Launch the app:
   ```powershell
   secure-file-encryption-tool
   ```

### Option 2: Run the app directly from source

If you prefer not to install the package, run the GUI directly:

```powershell
py gui.py
```

### Option 3: Use the standalone Windows executable

1. Install PyInstaller:
   ```powershell
   py -m pip install pyinstaller
   ```
2. Build the executable:
   ```powershell
   pyinstaller --onefile --windowed --name SecureFileEncryptionTool gui.py
   ```
3. Open `dist\SecureFileEncryptionTool.exe`.

### Option 4: Install using the Windows installer

1. Install Inno Setup 6 or later from https://jrsoftware.org/isinfo.php.
2. Build the installer:
   ```powershell
   .\build_installer.bat
   ```
3. Run the generated installer at `Output\SecureFileEncryptionToolInstaller.exe`.
4. After installation, launch the app from the Start Menu under `Secure File Encryption Tool`.

---

## How to use the app

### Main screen

The app window has these controls:
- `Selected file`: choose the file to encrypt or decrypt.
- `Key file`: the key file used in Key mode.
- `Password`: the password used in Password mode.
- `Mode`: switch between `Key file` and `Password` encryption.
- `Encrypt` / `Decrypt`: perform the selected action.
- `Status`: shows current progress and result messages.

### Step-by-step: Encrypt a file

1. Click `Browse...` and choose the file you want to protect.
2. Choose `Key file` or `Password` mode.

#### Key file mode

- If a key file already exists, click `Browse Key...` and select it.
- If you do not choose a key file, the app will use or create `secret.key` in the current folder.
- Click `Encrypt`.

#### Password mode

- Select the `Password` radio button.
- Enter a strong password.
- Click `Encrypt`.

3. After successful encryption, the app creates a file named `yourfile.encrypted`.
4. The status message and popup will confirm the encrypted file path.

### Step-by-step: Decrypt a file

1. Click `Browse...` and select the `.encrypted` file.
2. Choose the same mode used for encryption.

#### Key file mode

- Choose the same key file that encrypted the file.
- Click `Decrypt`.

#### Password mode

- Select `Password` mode.
- Enter the same password used during encryption.
- Click `Decrypt`.

3. The app restores the original filename and extension when possible. If the encrypted file was created by this app, you should see the original filename like `yourfile.png`, `song.mp3`, or `video.mp4`.
4. Confirm success from the message box and status label.

---

## Important details

### Key mode behavior

- The app uses a Fernet key stored in a `.key` file.
- If `secret.key` does not exist, the app creates it automatically.
- Keep the key file safe and do not share it publicly.
- Losing the key file means encrypted data cannot be decrypted.

### Password mode behavior

- The app derives the encryption key from the provided password.
- A random salt is stored inside the encrypted file.
- Use the same password to decrypt the file.
- If the password is lost, the encrypted data cannot be recovered.

### Output files

- Encrypted output: `filename.encrypted`
- Decrypted output: the original filename and extension are restored when possible.

### Security reminders

- Do not store passwords or key files in insecure locations.
- Avoid encrypting files to the same folder as the input file if you want to keep the original.
- Do not delete the original file until you verify the encrypted/decrypted output.

---

## Troubleshooting

### The app says the file was not found

- Confirm the selected file path is correct.
- Make sure the file is not locked by another application.

### Decryption failed with invalid key/password

- Verify you selected the same mode used for encryption.
- Check that the key file or password is exact.
- If the encrypted file was modified, decryption will fail.

### App does not launch after installation

- Reinstall the app using the generated installer.
- Launch from the Start Menu or run `secure-file-encryption-tool` in PowerShell.

---

## Best practices

- Use a strong password of at least 12 characters for password mode.
- Keep a backup copy of the key file if you use key mode.
- Test encryption and decryption on a non-critical file first.
