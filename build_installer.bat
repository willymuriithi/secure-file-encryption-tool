@echo off
setlocal

REM Build the standalone executable first
python -m pip install --upgrade pyinstaller
if %ERRORLEVEL% neq 0 (
    echo Failed to install PyInstaller.
    exit /b %ERRORLEVEL%
)

REM Ensure tkinterdnd2 is available for drag-and-drop support in the GUI
python -m pip install --upgrade tkinterdnd2
if %ERRORLEVEL% neq 0 (
    echo Failed to install tkinterdnd2.
    exit /b %ERRORLEVEL%
)

python -m PyInstaller --onefile --windowed --name SecureFileEncryptionTool gui.py
if %ERRORLEVEL% neq 0 (
    echo PyInstaller build failed.
    exit /b %ERRORLEVEL%
)

if not exist "dist\SecureFileEncryptionTool.exe" (
    echo Build output not found: dist\SecureFileEncryptionTool.exe
    exit /b 1
)

REM Build the Windows installer using Inno Setup
if exist "%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe" (
    "%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe" installer.iss
) else if exist "%ProgramFiles%\Inno Setup 6\ISCC.exe" (
    "%ProgramFiles%\Inno Setup 6\ISCC.exe" installer.iss
) else (
    echo Inno Setup compiler not found.
    echo Install Inno Setup and ensure ISCC.exe is in PATH or located under Program Files.
    exit /b 1
)

if %ERRORLEVEL% neq 0 (
    echo Installer build failed.
    exit /b %ERRORLEVEL%
)

echo Installer build complete.
pause
