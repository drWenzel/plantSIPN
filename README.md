# plantSIPN
Drawing of  "Steuerungstechnisch Interpretierte Petri-Netze" by use of a Domain Specific Language
===> SIPN Generator

## Vorbedingungen

- graphviz installiert (http://www.graphviz.org/)
- python installiert (am besten Anaconda-Distriubtion)
- python libary graphivz installiert
    $ pip install graphviz


## Programmierung
Erstellung einer SIPN-Berschreibung gem. Vorlage

    @sipnNetwork:start / <Name Ausgabe Datei>
    stelle: <name>
    startstelle: <name>
    eingang: <name>
    ausgang: <name>
    transition: <name>
    timertransition: <name> / <wert>
    loeschtransition: <name> / <wert>
    
    <quelle> -> <ziel> [Standardverbindung]
    <quelle> -O <ziel> [Negation am ziel (mit Oh)]
    <quelle> .. <ziel> [Ausgangsanschluss an einen Platz]
    
    @sipnNetwork:end


## Aufruf
    in "runMePlease.py" den Pfad zur Beschreibungsdatei angeben 
    ggf. noch ausgabeformat angpassen (# löschen / verschieben)
    createSipn ausführen

## Feedback / Anregungen / Anpassungen
Bitte Feedback via github
