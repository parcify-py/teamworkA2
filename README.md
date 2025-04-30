# teamworkA2
🏆 Vizuální efekty vítězství
Tento projekt obsahuje jednoduché vizuální animace a zpětnou vazbu pro zvýšení interaktivity.

🔁 animace_vitezstvi(pozice, krok=0)
Animace pro zvýraznění výherních políček například ve hře (např. piškvorky, tictactoe apod.).

Parametry:
pozice (list of tuples) – seznam souřadnic (řádek, sloupec) polí, která tvoří vítěznou kombinaci.

krok (int, volitelný) – vnitřní parametr pro sledování kroku animace. Není třeba nastavovat ručně.

Chování:
Barva pozadí daných polí střídá mezi yellow a orange.

Animace proběhne celkem 6x (0–5), s přechody každých 200 ms.

Využívá rekurzivní volání pomocí after.
self.animace_vitezstvi([(0, 0), (0, 1), (0, 2)])
Funkce ukaz_hvezdy(pocet)
Tato metoda slouží k dočasnému zobrazení hvězdiček jako vizuální zpětné vazby uživateli.

Popis:
Metoda zobrazí daný počet hvězdiček (⭐) v labelu hvezdy_label, a to po dobu 2 sekund. Poté se text automaticky vymaže.

Parametry:
pocet (int) – počet hvězdiček, které se mají zobrazit.

Chování:
Okamžitě se v labelu hvezdy_label zobrazí tolik hvězdiček, kolik udává parametr pocet.

Po 2000 milisekundách (2 sekundy) se obsah labelu smaže.
self.ukaz_hvezdy(3)  # zobrazí "⭐⭐⭐" na 2 sekundy
Požadavky:
self.hvezdy_label musí být Tkinter Label, který je již vytvořen.

self.root musí být hlavní Tkinter okno (Tk nebo Toplevel), protože se používá metoda after.
