@echo off
@echo off
:menu
cls
echo.
echo.
echo.
echo.
echo     =============================
echo             Ryle's RVC TTS
echo     =============================
echo.
echo     Dont forget to setup `.env` with 'SOCKET_TOKEN' and "ALERTBOX"
echo.
echo     =====================================================================================
echo     This will launch the RVC window, the TTS Listener, and the Alertbox.
echo     Start #2 below, then click Start in the RVC window, and you're good to go.
echo     =====================================================================================
echo.
echo     1. Set Commands for Donos
echo     2. Launch RVC + TTS + AlertBox
echo     3. github
echo     4. Exit
echo.
set /p userinp=Enter your choice (1/2/3/4): 

if "%userinp%"=="1" goto launchA
if "%userinp%"=="2" goto launchB
if "%userinp%"=="3" goto launchC
if "%userinp%"=="4" goto exit

echo Invalid choice & pause & goto menu

:launchA
start "" RyleTTS.exe
echo Program A launched successfully!
pause
goto menu

:launchB

start "" sock.exe
start "" webviewer.exe
runtime\python.exe custom_realtime_gui.py
echo Program B launched successfully!
pause
goto menu

:launchC
start "" "C:\Path\To\ProgramC.exe"
echo Program C launched successfully!
pause
goto menu

:exit
echo Exiting...
exit

