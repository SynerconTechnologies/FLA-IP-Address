; -- SSS2 GUI.iss --

[Setup]
AppName=EnterFLAip
AppVersion=1.0
DefaultDirName={pf}\Synercon
DefaultGroupName=Synercon
Compression=lzma2
SolidCompression=yes
OutputDir=userdocs:Synercon
OutputBaseFilename=SetupFLA-IP-Utility
UninstallDisplayIcon={app}\FLA-IP-Utility

[Files]
Source: "build\exe.win32-3.4\*"; DestDir: "{app}"; Flags: recursesubdirs
Source: "*.ico"; DestDir: "{app}"

[Icons]
Name: "{group}\FLA-IP-Utility"; Filename: "{app}\EnterFLAip.exe" ; WorkingDir: "{app}"
Name: "{group}\Uninstall EnterFLAip"; Filename: "{uninstallexe}"

[Tasks]
Name: desktopicon; Description: "Create a &desktop icon"; 
Name: quicklaunchicon; Description: "Create a &Quick Launch icon";

[Run]
Filename: "{app}\EnterFLAip.exe"; Description: "Launch application"; Flags: postinstall nowait skipifsilent 