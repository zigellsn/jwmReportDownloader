# Installation

## Voraussetzungen
- [Python 3](https://www.python.org/)
- [Google Chrome](https://www.google.de/chrome/)
- [ChromeDriver](http://chromedriver.chromium.org/) muss vorhanden sein und in einem Verzeichnis liegen, das in der PATH-Umgebungsvariablen eingetragen ist.

## Installation
[Dieses Repository](https://github.com/zigellsn/jwmReportDownloader/archive/master.zip) herunterladen und entpacken. In das entpackte Verzeichnis mit dem Python-Skript wechseln. Dann:

*Windows*
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

*bash*
```bash
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```