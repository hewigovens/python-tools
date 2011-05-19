netsh interface ipv6 install
netsh interface ipv6 6to4 set state default default
netsh interface ipv6 6to4 set state state=enabled undoonstop=disabled
netsh interface ipv6 set teredo enterpriseclient
rem netsh interface ipv6 set teredo enterpriseclient teredo.remlab.net
netsh interface ipv6 set teredo enterpriseclient teredo.ipv6.microsoft.com
netsh interface ipv6 set prefix ::1/128 50 0
netsh interface ipv6 set prefix ::/0 40 1
netsh interface ipv6 set prefix 2002::/16 30 1
netsh interface ipv6 set prefix ::/96 20 3
netsh interface ipv6 set prefix ::ffff:0:0/96 10 4
netsh interface ipv6 set prefix 2001::/32 5 1
ping 1.0.0.0 -n 1 -w 10000
netsh interface ipv6 show teredo
pause