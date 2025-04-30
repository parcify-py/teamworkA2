# 🎰 Slotový Automat – Popis Funkce `zobraz_vysledek`

Tato metoda slouží k vyhodnocení výsledku po každém "točení" (spinu) v našem výherním automatu. Pracuje s mřížkou symbolů (`self.mrizka`) a rozhoduje o výhře nebo prohře na základě shodných obrázků.

## 🏆 Možnosti výhry

Metoda kontroluje:

- **Jackpot (všechny symboly stejné):**
  - Výhra: 💎 100 000 bodů
  - Zobrazí se text "JACKPOT!!!", zvýrazní se všechna pole a spustí se výherní animace.
  - Hráč získá 3 hvězdičky.

- **Výherní linie:**
  - Za každý celý řádek, sloupec nebo diagonálu se stejnými symboly hráč získá:
    - 🎉 +100 bodů za každou shodu
    - Animaci a zvýraznění výherních polí
    - Až 3 hvězdy podle počtu výherních linií

- **Prohra:**
  - Pokud není žádná shoda, hráči se odečte 50 bodů.
  - Zobrazí se zpráva o neúspěchu.

## 🚨 Cheating detekce

Pokud skóre hráče přesáhne 1000 bodů, hra automaticky skončí s hláškou:
> „Myslím, že podvádíte. Vypadněte z mého kasina!“

## 🔁 Automatický režim (`autorun`)

Hra podporuje tzv. **autospin**:
- Pokud je zapnutý, další kolo se automaticky spustí po 2 sekundách.

## ✨ Bonusové funkce

- **Animace výhry:** Výherní pole se střídavě zbarvují žlutě a oranžově.
- **Zobrazení hvězdiček:** Podle výhry se zobrazí až 3 hvězdy.
- **Easter egg:** Po napsání slova `easteregg` na klávesnici se zobrazí okno s poděkováním autorům a animovaný GIF.

## 🧑‍💻 Autoři

Hru vytvořili:
-Mega skupina A2

---
