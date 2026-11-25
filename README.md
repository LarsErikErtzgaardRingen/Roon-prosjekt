Lars Eriks ROON-musikksamling

En oversikt over alle albumene på musikkserveren min. Musikken ligger på en NAS-disk som er koblet til en Roon-server. Albumlisten er eksportert fra Roon, og alt jeg registrerer i appen, lagres i nettleserens localStorage.

Live-versjon: https://github.com/LarsErikErtzgaardRingen/Roon-prosjekt.git

FUNKSJONALITET

Albumlisten: 
Viser alle albumene på serveren med tittel, artist og utgivelsesår. 
Viser 50 album pr side. "Vis flere" henter nye 50 album.

Hørt-counter:
Trykk "Hørt" hver gang du har hørt et album. Telleren viser hvor mange ganger det er hørt totalt. Det er også lagt til en angreknapp, sånn for sikkerhets skyld. 

Stjerner: 
Gi albumet karakter fra 1 til 6 stjerner ved å trykke på stjernene. 
Stjernene kan justeres, og om brukeren trykker på samme stjerne to ganger fjernes vurderingen. 

Kommentar: 
Hvert album har fått sitt eget kommentarfelt. Kommentaren lagres automatisk når brukeren går ut. 

Legge til album: 
Skjemaet øverst på siden gir mulighet for å legge til nytt album, med artist, albumnavn, og utgivelsesår. 

Slette: 
"Slett" fjerner ett album etter at du har bekreftet. "Slett alle album" sletter alle data som er lagt inn. 

Søk, filter og sortering:
Søk på artist etter albumtittel. Søket finner også ord inni andre ord. 
Filter: Alle album, bare hørte, eller ikke hørte. 
Sortering: Albumartist A til Å, albumtittel, A til Å, nyeste først, mest hørt, eller flest stjerner. 

Statistikk: 
Øverst på siden vises hvor mange album som finnes på serveren totalt, hvor mange som er hørt, totalt antall avspillingen, og snittkarakter på stjerner. 

script.js er delt i tre deler:

1. Data og lagring: henter albumene fra localStorage. Første gang lages lista fra Roon-dataene.

2. Visning: funksjonene som filtrerer, sorterer og viser albumene og statistikken.

3. Event listeners: reagerer på det brukeren gjør. De endrer dataene, lagrer og tegner lista på nytt.

Dataene fra Roon: (NB!! Her fikk brukte jeg KI for å hjelpe meg!)

Jeg eksporterte albumlisten fra Roon til et Excel-regneark (Library → Albums → Select all → Export to Excel).
Et Python-skript (tools/lag_albumliste.py) konverterte regnearket til JSON-data i fila albums.js. Det tok med artist, tittel og år for hvert album.
albums.js lastes inn før script.js i index.html. Første gang siden åpnes, kopieres albumene til localStorage. Etter det jobber appen bare mot localStorage.


