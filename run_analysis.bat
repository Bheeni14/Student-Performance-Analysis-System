@echo off
REM Generate data and run complete analysis
echo ========================================
echo Running Complete Analysis Pipeline
echo ========================================
echo.

echo Installing dependencies...
pip install -r requirements.txt
echo.

echo Running analysis...
python main.py

echo.
echo ========================================
echo Analysis Complete!
echo ========================================
echo.
echo Check the following folders for results:
echo   - data/ (generated datasets)
echo   - visualizations/ (15+ charts)
echo   - reports/ (statistical reports)
echo.

pause
