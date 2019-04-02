@ECHO OFF

REM Hier für WORKDIR das korrekte Verzeichnis angeben...
SET WORKDIR="C:\...\jwmReportDownloader"

CALL %WORKDIR%\venv\Scripts\activate.bat

REM Hier die gewünschten Parameter anfügen...
python %WORKDIR%\jwmReportDownloader.py

deactivate