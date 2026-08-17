@echo off
title CYBERPUNK WI-FI DECRYPTOR (Python 3.12)
color 0a
cls

:: HUAWEI kullanicisi ve Python 3.12 hedefli kod
if exist "C:\Users\HUAWEI\Desktop\cypher_wifi.py" (
    cd /d "C:\Users\HUAWEI\Desktop"
    py -3.12 cypher_wifi.py
    goto END
)
if exist "C:\Users\HUAWEI\Desktop\cypher_wifi.py.txt" (
    cd /d "C:\Users\HUAWEI\Desktop"
    py -3.12 cypher_wifi.py.txt
    goto END
)
if exist "C:\Users\HUAWEI\Documents\cypher_wifi.py" (
    cd /d "C:\Users\HUAWEI\Documents"
    py -3.12 cypher_wifi.py
    goto END
)
if exist "C:\Users\HUAWEI\Documents\cypher_wifi.py.txt" (
    cd /d "C:\Users\HUAWEI\Documents"
    py -3.12 cypher_wifi.py.txt
    goto END
)

echo [!] HATA: 'cypher_wifi.py' dosyasi Masaustu veya Belgeler klasorunde bulunamadi!

:END
echo.
pause