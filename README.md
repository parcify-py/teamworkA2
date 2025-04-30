# 🎰 Slotový Automat – Popis Funkce `zobraz_vysledek`

Tato metoda slouží k vyhodnocení výsledku po každém "točení" (spinu) v našem výherním automatu. Pracuje s mřížkou symbolů (`self.mrizka`) a rozhoduje o výhře nebo prohře na základě shodných obrázků.

---

## 🧩 Ukázka kódu

```python
def zobraz_vysledek(self):
    vyherni_pozice = set()
    vsechny = [self.mrizka[r][c].image for r in range(RADKY) for c in range(SLOUPCE)]

    # JACKPOT – všechny symboly jsou stejné
    if all(s == vsechny[0] for s in vsechny):
        vyherni_pozice = {(r, c) for r in range(RADKY) for c in range(SLOUPCE)}
        self.vysledek_label.config(text="💎 JACKPOT!!! +100 000 bodů 💎", fg="purple")
        self.animace_vitezstvi(vyherni_pozice)
        self.skore += 100000
        self.ukaz_hvezdy(3)
        self.prohry_za_sebou = 0
        self.skore_label.config(text=f"Skóre: {self.skore}")
        self.zkontroluj_cheating()
        self.otaci_se = False
        if self.autorun:
            self.root.after(2000, self.spustit)
        return

    # Výherní linie – řádky, sloupce, diagonály
    vyher_linie = 0

    for r in range(RADKY):
        radek = [self.mrizka[r][c].image for c in range(SLOUPCE)]
        if all(s == radek[0] for s in radek):
            vyher_linie += 1
            vyherni_pozice.update([(r, c) for c in range(SLOUPCE)])

    for c in range(SLOUPCE):
        sloupec = [self.mrizka[r][c].image for r in range(RADKY)]
        if all(s == sloupec[0] for s in sloupec):
            vyher_linie += 1
            vyherni_pozice.update([(r, c) for r in range(RADKY)])

    # Diagonály
    hlavni = [self.mrizka[i][i].image for i in range(RADKY)]
    if all(s == hlavni[0] for s in hlavni):
        vyher_linie += 1
        vyherni_pozice.update([(i, i) for i in range(RADKY)])

    vedlejsi = [self.mrizka[i][SLOUPCE - 1 - i].image for i in range(RADKY)]
    if all(s == vedlejsi[0] for s in vedlejsi):
        vyher_linie += 1
        vyherni_pozice.update([(i, SLOUPCE - 1 - i) for i in range(RADKY)])

    if vyher_linie > 0:
        body = 100 * vyher_linie
        self.vysledek_label.config(
            text=f"🎉 Výhra! {vyher_linie} shod! +{body} bodů!", fg="green"
        )
        self.animace_vitezstvi(vyherni_pozice)
        self.skore += body
        self.ukaz_hvezdy(min(3, vyher_linie))
        self.prohry_za_sebou = 0
    else:
        self.vysledek_label.config(text="Žádná shoda. -50 bodů", fg="red")
        self.skore -= 50
        self.prohry_za_sebou += 1

    self.skore_label.config(text=f"Skóre: {self.skore}")
    self.zkontroluj_cheating()
    self.otaci_se = False

    if self.autorun:
        self.root.after(2000, self.spustit)
