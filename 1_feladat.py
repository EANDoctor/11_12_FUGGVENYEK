"""
1. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat) összeadja és az összegükkel tér vissza! A program tartalmazza a függvény hívását is!
"""

szamok_listaja = [1, 2, 3, 4, 5]

def osszegzo(szamok_listaja):
    osszegzo = 0 
    for szam in szamok_listaja:
        osszegzo += szam
    return osszegzo

print(osszegzo(szamok_listaja))
