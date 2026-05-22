@echo off
python -m pip install --upgrade pyinstaller
pyinstaller --onefile --windowed --name SecureFileEncryptionTool gui.py
if %ERRORLEVEL% neq 0 (
    echo Build failed.
    exit /b %ERRORLEVEL%
)

echo Build complete. Executable available at dist\SecureFileEncryptionTool.exe
pause
