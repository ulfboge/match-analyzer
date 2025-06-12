@echo off
echo Aktiverar miljö...
call venv\Scripts\activate

echo Startar Streamlit-app...
streamlit run match_analysis_app.py

pause
