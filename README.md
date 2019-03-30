# jvmReportDownloader
Downloader für Berichte von [JW Management](https://www.jwmanagement.org/)

## Voraussetzungen
- [Python 3](https://www.python.org/)
- [Google Chrome](https://www.google.de/chrome/)
- [ChromeDriver](http://chromedriver.chromium.org/) muss vorhanden sein und in einem Verzeichnis liegen, das in der PATH-Umgebungsvariablen eingetragen ist.

## Installation
[Dieses Repository](https://github.com/zigellsn/jwmReportDownloader/archive/master.zip) herunterladen und entpacken. Dann:
```bash
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
```

## Verwendung
Falls noch nicht geschehen
```bash
./venv/Scripts/activate
```
Dann:
```bash
python jmvReportDownloader.py --parameter...
```

## Parameter
| Parameter                |      | Bedeutung                                                                                      |
| ------------------------ | ---- | ---------------------------------------------------------------------------------------------- |
| `--help` oder `-h`       | kann | Hilfetext anzeigen                                                                             |
| `--user` oder `-u`       | muss | User                                                                                           |
| `--password` oder `-p`   | muss | Passwort des Users                                                                             |
| `--project` oder `-r`    | muss | Projekt-ID                                                                                     |
| `--start-date` oder `-s` | kann | Startdatum (siehe *Datumsangaben*)                                                             |
| `--end-date` oder `-e`   | kann | Enddatum (siehe *Datumsangaben*)                                                               |
| `--directory` oder `-d`  | kann | Downloadverzeichnis (ohne abschließenden Schrägstrich) - Standard ist das aktuelle Verzeichnis |

### Datumsangaben
Alle Datumsangaben sind in der Form `<Jahr>M<Monat>` einzugeben - z.B 
`2019M03` für März 2019 und `2020M04` für April 2020.

| start-date      | end-date        | Verhalten                                                  |
| --------------- | --------------- | ---------------------------------------------------------- |
| nicht angegeben | nicht angegeben | Downloaden der Berichte des aktuellen Monats               |
| nicht angegeben | angegeben       | Downloaden der Berichte vom aktuellen Monat bis *end-date* |
| angegeben       | nicht angegeben | Downloaden der Berichte des Monats *start-date*            |
| angegeben       | angegeben       | Downloaden aller Berichte von *start-date* bis *end-date*  |


### Beispiel
Der Aufruf
```bash
python jmvReportDownloader.py --user=myuser --password=mypassword --project=abcABC123 --directory=/my/download/dir --start-date=2019M03 --end-date=2020M04
```
lädt von [https://www.jwmanagement.org/](https://www.jwmanagement.org/) mit dem User *myuser* mit dem Password 
*mypassword* vom Projekt *abcABC123* alle Berichte zwischen einschließlich 
März 2019 und April 2020 herunter.