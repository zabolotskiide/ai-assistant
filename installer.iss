[Setup]
AppName=JARVIS
AppVersion=1.0
DefaultDirName={autopf}\JARVIS
OutputBaseFilename=JARVIS_SETUP

[Files]
Source: "..\dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\JARVIS"; Filename: "{app}\main.exe"

[Run]
Filename: "{app}\main.exe"; Flags: nowait postinstall
