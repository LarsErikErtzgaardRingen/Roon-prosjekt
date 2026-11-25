# Gjør Roon-eksporten (Excel) om til albums.js, som nettsiden leser.
#
# Bruk:
#   pip install openpyxl
#   python tools/lag_albumliste.py Roon-database.xlsx

import json
import sys
from openpyxl import load_workbook

ark = load_workbook(sys.argv[1], read_only=True).active
rader = list(ark.iter_rows(values_only=True))
overskrifter = rader[0]

# Finn kolonnene vi trenger
artist_kol = overskrifter.index("Album Artist")
tittel_kol = overskrifter.index("Title")
dato_kol = overskrifter.index("Date")  # f.eks. "20211119"

album = []
for nummer, rad in enumerate(rader[1:], start=1):
    dato = rad[dato_kol]
    album.append({
        "id": f"a{nummer}",
        "artist": rad[artist_kol],
        "tittel": rad[tittel_kol],
        "aar": int(str(dato)[:4]) if dato else None,
    })

with open("albums.js", "w", encoding="utf-8") as fil:
    fil.write("// Albumlisten fra Roon-serveren (laget av tools/lag_albumliste.py)\n")
    linjer = [json.dumps(a, ensure_ascii=False) for a in album]  # ett album per linje
    fil.write("const ROON_ALBUMS = [\n" + ",\n".join(linjer) + "\n];\n")

print(f"Lagret {len(album)} album i albums.js")
