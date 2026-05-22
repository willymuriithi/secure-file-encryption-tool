[Setup]
AppName=Secure File Encryption Tool
AppVersion=0.1.0
DefaultDirName={commonpf}\Secure File Encryption Tool
DefaultGroupName=Secure File Encryption Tool
DisableProgramGroupPage=yes
OutputBaseFilename=SecureFileEncryptionToolInstaller
Compression=lzma
SolidCompression=yes
WizardStyle=modern
DisableStartupPrompt=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "dist\SecureFileEncryptionTool.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Secure File Encryption Tool"; Filename: "{app}\SecureFileEncryptionTool.exe"
Name: "{commondesktop}\Secure File Encryption Tool"; Filename: "{app}\SecureFileEncryptionTool.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked

[Run]
Filename: "{app}\SecureFileEncryptionTool.exe"; Description: "Launch Secure File Encryption Tool"; Flags: nowait postinstall skipifsilent
