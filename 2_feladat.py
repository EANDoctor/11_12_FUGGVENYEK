"""
2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett listaelemek (egész számok) között van páros,
ellenkező esetben a visszatérési érték False! A program tartalmazza a függvény hívását is!
"""

szamok_listaja = [1, 3, 5, 7, 8]

def paros_e(szamok_listaja):
    for szam in szamok_listaja:
        if szam % 2 == 0:
            return True
    return False

print(paros_e(szamok_listaja))
