"""
3.1 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja,
hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!
"""

szamok_listaja = [3, 5, 9, 12, 14, 18, 20, 21, 27, 29, 31, 33]

def oszt_harommal(szamok_listaja):
    db = 0
    for szam in szamok_listaja:
        if szam % 3 == 0:
            db += 1
    return db

print(oszt_harommal(szamok_listaja))
