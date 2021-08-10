# Hintergrund
Anscheinend ist es möglich, [Tiger mit Löwen zu kreuzen](https://de.wikipedia.org/wiki/Liger "Warum
auch immer"). Dabei entstehen entweder *Liger* (Löwe x Tigerin) oder *Töwen* (Tiger x Löwin). 

Da dieser Graus wohl nicht genug war, wurden auch z.B. Tiger mit Ligerinnen gekreuzt, wobei ein
Ti-Liger herauskommt. Leider (oder zum Glück) sind männliche Töwen und Liger unfruchtbar, weswegen
die entsprechende
[Kreuzungstabelle](https://de.wikipedia.org/wiki/Gro%C3%9Fkatzenhybride#%C3%9Cberblick) enttäuschend
klein ausfällt. Mit diesem Programm sehen wir über diese kleine biologische Einschränkung hinweg.

### Anmerkung
Eine Kreuzung aus Löwe und Liger heißt offiziell und unsinnigerweise "Li-Liger" statt "Lö-Liger".
Dieser Gehirnfurz wird in diesem Programm gekonnt ignoriert bzw. ausgemerzt. 

# MOAR LIGER
Verwendung: `python liger.py n resultat.csv`

Damit landet die Kreuzungstabelle für n generationen in der Datei resultat.csv.

## Achtung
Die Anzahl der verschiedenen Kombinationen quadriert sich mit jeder Generation (zwar nicht ganz,
da es Duplikate gibt, aber es steigt trotzdem ziemlich schnell). n=4 bringt Google Docs allmählich
in's Schwitzen, und für n=5 hatte ich auf meinem Laptop keine Gedult mehr (etwa 25.000^2 neue
Kreuzungen). 

Kurzum: n > 4 wird nicht empfohlen. 