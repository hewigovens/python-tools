
reg add "HKEY_CURRENT_USER\Console" /v "ScreenBufferSize" /t REG_DWORD /d 65536100 /f
reg add "HKEY_CURRENT_USER\Console" /v "WindowSize" /t REG_DWORD /d 2293860 /f
reg add "HKEY_CURRENT_USER\Console" /v "QuickEdit" /t REG_DWORD /d 1 /f

reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor" /v "DisableUNCCheck" /t REG_DWORD /d 1 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor" /v "PathCompletionChar" /t REG_DWORD /d 64 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor" /v "CompletionChar" /t REG_DWORD /d 9 /f

ver | findstr /r "5\." && (
    reg add "HKEY_CLASSES_ROOT\Folder\shell\DOS" /v "" /t REG_SZ /d "@shell32.dll,-22022" /f
    reg add "HKEY_CLASSES_ROOT\Folder\shell\DOS\command" /v "" /t REG_SZ /d "cmd.exe /d /s /k ver" /f
)
ver | findstr /r "6\." && (
    reg add "HKEY_CLASSES_ROOT\Folder\shell\runas" /v "" /t REG_SZ /d "@shell32.dll,-22022" /f
    reg add "HKEY_CLASSES_ROOT\Folder\shell\runas" /v "Icon" /t REG_SZ /d "%windir%\System32\imageres.dll,-78" /f
    reg add "HKEY_CLASSES_ROOT\Folder\shell\runas\command" /v "" /t REG_SZ /d "cmd.exe /d /s /k ver" /f
)

pause