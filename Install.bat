@echo off
:: -------------------------------
:: RemotePC - Ajouter le serveur Python au démarrage automatique (dossier courant)
:: -------------------------------

:: Récupère le dossier courant (où le .bat est lancé)
set CURRENT_DIR=%~dp0

:: Chemin vers le server.py dans le dossier courant
set SERVER_PATH=%CURRENT_DIR%server.py

:: Vérifie si server.py existe
if not exist "%SERVER_PATH%" (
    echo ERREUR : Le fichier server.py n'a pas ete trouve dans %CURRENT_DIR%
    pause
    exit /b
)

:: Chemin du dossier démarrage automatique pour l'utilisateur courant
set STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

:: Nom du raccourci
set SHORTCUT_NAME=RemotePC.lnk

:: Crée le raccourci avec PowerShell
powershell -Command ^
"$WshShell = New-Object -ComObject WScript.Shell; ^
 $Shortcut = $WshShell.CreateShortcut('%STARTUP_FOLDER%\%SHORTCUT_NAME%'); ^
 $Shortcut.TargetPath = 'C:\Windows\System32\cmd.exe'; ^
 $Shortcut.Arguments = '/c python \"%SERVER_PATH%\"'; ^
 $Shortcut.WorkingDirectory = '%CURRENT_DIR%'; ^
 $Shortcut.Save()"

echo Raccourci cree dans le dossier de demarrage automatique.
echo Le serveur RemotePC se lancera automatiquement au demarrage de Windows.
pause
exit
