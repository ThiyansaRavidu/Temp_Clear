@echo off

echo Removing Temporary Files...
del /s /q %TEMP%\*.*
for /d %%p in ("%TEMP%\*.*") do rmdir "%%p" /s /q

echo Emptying Recycle Bin...
rd /s /q %systemdrive%\$Recycle.Bin

echo Removing System Files...
cleanmgr /sageset:1
cleanmgr /sagerun:1

echo Removing Windows Update Cleanup...
cleanmgr /sageset:50
cleanmgr /sagerun:50

echo Removing Thumbnails...
del /s /q %userprofile%\AppData\Local\Microsoft\Windows\Explorer\thumbcache_*.db

echo Removing Temporary Internet Files...
cd /d %userprofile%\AppData\Local\Microsoft\Windows\INetCache
del /s /q *.*

echo Removing Delivery Optimization Files...
del /s /q %systemdrive%\Windows\SoftwareDistribution\Download\*.*

echo Removing Downloaded Program Files...
del /s /q %userprofile%\Downloads\*.*

echo Removing Offline Web Pages...
rd /s /q %userprofile%\AppData\Local\Microsoft\Windows\INetCache\IE

echo Removing DirectX Shader Cache...
del /s /q %userprofile%\AppData\Local\Microsoft\Windows\DXCache\*.*

echo Removing Temporary Files in Downloads Folder...
cd /d %userprofile%\Downloads
del /s /q *.*

echo Removing Previous Windows Installations...
dism.exe /online /Cleanup-Image /StartComponentCleanup /ResetBase

echo Removing Temporary Files from Apps...
rd /s /q %userprofile%\AppData\Local\Temp

echo Removing System Restore Points...
vssadmin.exe Delete Shadows /All /Quiet

echo Removing C:\Windows\Temp folder...
rd /s /q C:\Windows\Temp

echo Removing Temporary Files from User's Temp Directory...
rd /s /q C:\Users\%userprofile%\AppData\Local\Temp

echo All specified files and folders removed successfully.
pause
