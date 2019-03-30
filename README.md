# jvmReportDownloader
Downloader für Berichte von [JW Management](https://www.jwmanagement.org/)

## Voraussetzungen
- [Python 3](https://www.python.org/)
- [Google Chrome](https://www.google.de/chrome/)
- [ChromeDriver](http://chromedriver.chromium.org/) muss vorhanden sein und in einem Verzeichnis liegen, das in der PATH-Umgebungsvariablen eingetragen ist.

## Installation
Dieses Repository herunterladen und evtl. entpacken. Dann:
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
| `--user` oder `-h`       | muss | User                                                                                           |
| `--password` oder `-p`   | muss | Passwort des Users                                                                             |
| `--project` oder `-r`    | muss | Projekt-ID                                                                                     |
| `--start-date` oder `-s` | kann | Startdatum (siehe *Datumsangaben*)                                                             |
| `--end-date` oder `-e`   | kann | Enddatum (siehe *Datumsangaben*)                                                               |
| `--directory` oder `-d`  | kann | Downloadverzeichnis (ohne abschließenden Schrägstrich) - Standard ist das aktuelle Verzeichnis |

### Datumsangaben
Alle Datumsangaben sind in der Form `<Jahr>M<Monat>` einzugeben.
Z.B `2019M03` für März 2019 und `2020M04` für April 2020.

| start-date      | end-date        | Verhalten                                     |
| --------------- | --------------- | --------------------------------------------- |
| nicht angegeben | nicht angegeben | Läd Bericht des aktuellen Monats              |
| nicht angegeben | angegeben       | Läd Bericht vom aktuellen Monat bis end-date  |
| angegeben       | nicht angegeben | Läd Bericht des Monats start-date             |
| angegeben       | angegeben       | Läd alle Berichte von start-date bis end-date |


### Beispiel
Der Aufruf
```bash
python jmvReportDownloader.py --user=myuser --password=mypassword --project=abcABC123 --directory=/my/download/dir --start-date=2019M03 --end-date=2020M04
```
läd mit dem User myuser mit dem Password mypassword von dem Projekt abcABC123 alle Berichte zwischen einschließlich 
März 2019 und April 2020 herunter.