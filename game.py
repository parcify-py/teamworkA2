import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
Ы
# --- Konfigurace ---
POCET_VALCU = 3               # Počet válců (slotů)
VELIKOST_OBRAZKU = (100, 100) # Rozměr obrázků
SLOZKA_OBRAZKU = "images"     # Složka s obrázky

# Načtení obrázků ze složky
def nacti_obrazky():
    seznam = []
    for soubor in os.listdir(SLOZKA_OBRAZKU):
        if soubor.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            cesta = os.path.join(SLOZKA_OBRAZKU, soubor)
            obrazek = Image.open(cesta).resize(VELIKOST_OBRAZKU)
            foto = ImageTk.PhotoImage(obrazek)
            seznam.append(foto)
    return seznam

class SlotovyAutomat:
    def __init__(self, root):
        self.root = root
        self.root.title("Hrací automat 🎰")

        self.symboly = nacti_obrazky()
        if len(self.symboly) < 3:
            messagebox.showerror("Chyba", "Vlož alespoň 3 obrázky do složky 'images'")
            root.destroy()
            return

        self.valce = []
        self.vytvor_gui()

    def vytvor_gui(self):
        ramecek = tk.Frame(self.root, bg="green")
        ramecek.pack(padx=20, pady=20)

        # Vytvoření válců
        for _ in range(POCET_VALCU):
            nahodny = random.choice(self.symboly)
            stitek = tk.Label(ramecek, image=nahodny, bg="black")
            stitek.image = nahodny  # uložíme referenci
            stitek.pack(side=tk.LEFT, padx=10)
            self.valce.append(stitek)

        # Tlačítko SPIN
        tlacitko = tk.Button(self.root, text="ROZTOČIT 🎲", command=self.spustit,
                             font=("Arial", 16), bg="gold")
        tlacitko.pack(pady=20)

    def spustit(self):
        vysledky = []

        for i in range(POCET_VALCU):
            symbol = random.choice(self.symboly)
            self.valce[i].config(image=symbol)
            self.valce[i].image = symbol
            vysledky.append(symbol)

        # Kontrola výhry
        if all(v == vysledky[0] for v in vysledky):
            messagebox.showinfo("Jackpot!", "🎉 Máš 3 stejné obrázky! Výhra!")
        else:
            print("Výsledek: žádná výhra.")

# --- Spuštění aplikace ---
if __name__ == "__main__":
    root = tk.Tk()
    app = SlotovyAutomat(root)
    root.mainloop()
