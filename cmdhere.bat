path %~dp0;c:\windows;c:\windows\system32;c:\windows\system32\wbem;%PATH%

set TIP=@shell32.dll,-22022
reg add "HKEY_CURRENT_USER\Console\%%SystemRoot%%_system32_cmd.exe" /v "ScreenBufferSize" /t REG_DWORD /d 65536100 /f
reg add "HKEY_CURRENT_USER\Console\%%SystemRoot%%_system32_cmd.exe" /v "WindowSize" /t REG_DWORD /d 2293860 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor" /v "DisableUNCCheck" /t REG_DWORD /d 1 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor" /v "PathCompletionChar" /t REG_DWORD /d 64 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Command Processor" /v "CompletionChar" /t REG_DWORD /d 9 /f
reg add "HKEY_CURRENT_USER\Software\Microsoft\Command Processor" /v "DisableUNCCheck" /t REG_DWORD /d 1 /f
ver | findstr /r "5\.[01]\." && (
    reg add "HKEY_CLASSES_ROOT\Folder\shell\DOS" /v "" /t REG_SZ /d "%TIP%" /f
    reg add "HKEY_CLASSES_ROOT\Folder\shell\DOS\command" /v "" /t REG_SZ /d "%ComSpec% /d" /f
)
ver | findstr /r "6\.[01]\." && (
    reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\DOS" /v "" /t REG_SZ /d "%TIP%" /f
    reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\DOS\command" /v "" /t REG_SZ /d "%ComSpec% /d" /f
)
