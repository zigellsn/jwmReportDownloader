@ECHO OFF

REM Hier für WORKPATH das korrekte Verzeichnis angeben...
SET WORKPATH="C:\...\jwmReportDownloader"

CALL %WORKPATH%\venv\Scripts\activate.bat

REM Hier die gewünschten Parameter anfügen...
python %WORKPATH%\jwmReportDownloader.py

deactivate