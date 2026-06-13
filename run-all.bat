@echo off
echo ===============================================
echo Starting Gesture Control Matrix...
echo Backend on http://localhost:2000
echo Frontend on http://localhost:2001
echo ===============================================
echo.

:: Start Backend in new terminal
start "Gesture Control Backend" cmd /k "cd /d %~dp0backend && call venv\Scripts\activate && python server.py"

:: Wait a bit for backend to start
timeout /t 5 /nobreak > nul

:: Start Frontend in new terminal
start "Gesture Control Frontend" cmd /k "cd /d %~dp0frontend && call npm install && call npm run dev"

echo All services starting!
echo Press any key to close this window...
pause > nul
