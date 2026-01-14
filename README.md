# Statischer Website-Generator

Dies ist ein einfacher statischer Website-Generator, der in Python geschrieben wurde. Er wandelt Markdown-Dateien in eine vollständige HTML-Website um.

## Funktionen

- **Markdown-Konvertierung**: Wandelt Markdown-Dateien aus dem Verzeichnis `content/` in HTML-Dateien um.
- **Rekursive Generierung**: Unterstützt verschachtelte Verzeichnisstrukturen im Content-Ordner.
- **Template-Unterstützung**: Verwendet eine `template.html`, um das Layout der Seiten zu definieren.
- **Konfigurierbarer Basepath**: Ermöglicht das Setzen eines Basis-Pfads für Links und Bilder, was besonders nützlich für das Hosting auf GitHub Pages (Subfolder) ist.
- **Statische Dateien**: Kopiert automatisch alle Dateien aus dem Verzeichnis `static/` (wie CSS oder Bilder) in das Zielverzeichnis.

## Voraussetzungen

- Python 3.x

## Projektstruktur

- `src/`: Enthält den Python-Quellcode für den Generator.
- `content/`: Enthält die Markdown-Quelldateien für die Website.
- `static/`: Enthält statische Assets wie CSS-Dateien und Bilder.
- `template.html`: Die HTML-Vorlage für alle generierten Seiten.
- `docs/`: Das Zielverzeichnis für die generierte Website (wird bei der Generierung erstellt).
- `build.sh`: Ein Skript für den Produktions-Build.

## Nutzung

### Lokale Entwicklung

Um die Seite lokal mit dem Standard-Basis-Pfad `/` zu generieren, führen Sie folgenden Befehl im Hauptverzeichnis aus:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python3 src/main.py
```

Die generierte Website befindet sich anschließend im Ordner `docs/`.

### Produktions-Build (für GitHub Pages)

Für die Veröffentlichung auf GitHub Pages (z.B. unter `https://<user>.github.io/<repo>/`) wird ein spezifischer `basepath` benötigt. Dafür gibt es das `build.sh` Skript:

```bash
./build.sh
```

Dieses Skript setzt den `basepath` standardmäßig auf `/staticsite/` (entsprechend dem Repository-Namen).

## Tests

Das Projekt enthält eine Testsuite. Um die Tests auszuführen, nutzen Sie:

```bash
./test.sh
```
