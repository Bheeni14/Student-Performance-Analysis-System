@echo off
REM Student Performance Analysis System - Launch Script
echo ========================================
echo Student Performance Analysis System
echo ========================================
echo.

echo Installing dependencies...
pip install -r requirements.txt
echo.

echo Launching Streamlit Web Application...
echo.
echo The application will open in your browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the server when done.
echo.

streamlit run app.py

pause
