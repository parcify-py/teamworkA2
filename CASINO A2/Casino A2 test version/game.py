import tkinter as tk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk, ImageSequence
import random
import os

# Nastavení
RADKY = 3
SLOUPCE = 3
VELIKOST_OBRAZKU = (100, 100)
SLOZKA_OBRAZKU = "images"
POCET_OTACEK = 10


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

        self.mrizka = [[None for _ in range(SLOUPCE)] for _ in range(RADKY)]
        self.skore = 0
        self.autorun = False
        self.autospin_aktivni = False
        self.prohry_za_sebou = 0
        self.sekvence = ""
        self.otaci_se = False  # blokace vícenásobného spinu

        self.vytvor_gui()
        self.root.bind("<Key>", self.zpracuj_klavesu)

    def vytvor_gui(self):
        self.ramecek = tk.Frame(self.root, bg="green")
        self.ramecek.pack(padx=20, pady=20)

        for r in range(RADKY):
            for c in range(SLOUPCE):
                nahodny = random.choice(self.symboly)
                stitek = tk.Label(self.ramecek, image=nahodny, bg="black")
                stitek.image = nahodny
                stitek.grid(row=r, column=c, padx=5, pady=5)
                self.mrizka[r][c] = stitek

        self.tlacitko = tk.Button(self.root, text="ROZTOČIT 🎲", command=self.spustit,
                                  font=("Arial", 16), bg="gold")
        self.tlacitko.pack(pady=10)

        self.auto_button = tk.Button(self.root, text="Autospin 🔁", command=self.toggle_autorun,
                                     font=("Arial", 12), bg="lightblue")
        self.auto_button.pack(pady=5)

        self.vysledek_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.vysledek_label.pack(pady=5)

        self.skore_label = tk.Label(self.root, text=f"Skóre: {self.skore}", font=("Arial", 12))
        self.skore_label.pack(pady=5)

        self.hvezdy_label = tk.Label(self.root, text="", font=("Arial", 24), fg="yellow")
        self.hvezdy_label.pack()

    def spustit(self):
        if self.otaci_se:  # blokace dalšího spinu
            return

        if self.autospin_aktivni and not self.autorun:
            return

        self.otaci_se = True
        self.vysledek_label.config(text="")
        self.zvyrazni_vsechny(bg="black")
        self.otacet(POCET_OTACEK)

    def otacet(self, zbyva):
        if zbyva == 0:
            self.zobraz_vysledek()
            return

        for r in range(RADKY):
            for c in range(SLOUPCE):
                if self.prohry_za_sebou > 2 and random.random() < 0.2 * self.prohry_za_sebou:
                    symbol = self.symboly[0]
                else:
                    symbol = random.choice(self.symboly)
                self.mrizka[r][c].config(image=symbol)
                self.mrizka[r][c].image = symbol

        self.root.after(100, lambda: self.otacet(zbyva - 1))

    def zobraz_vysledek(self):
        vyherni_pozice = set()
        vsechny = [self.mrizka[r][c].image for r in range(RADKY) for c in range(SLOUPCE)]

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

    def zkontroluj_cheating(self):
        if self.skore > 1000:
            messagebox.showwarning("Konec hry", "Myslím, že podvádíte. Vypadněte z mého kasina!")
            self.root.destroy()

    def zvyrazni_vsechny(self, bg="black"):
        for r in range(RADKY):
            for c in range(SLOUPCE):
                self.mrizka[r][c].config(bg=bg)

    def animace_vitezstvi(self, pozice, krok=0):
        barva = "yellow" if krok % 2 == 0 else "orange"
        for r, c in pozice:
            self.mrizka[r][c].config(bg=barva)
        if krok < 5:
            self.root.after(200, lambda: self.animace_vitezstvi(pozice, krok + 1))

    def ukaz_hvezdy(self, pocet):
        self.hvezdy_label.config(text="⭐" * pocet)
        self.root.after(2000, lambda: self.hvezdy_label.config(text=""))

    def toggle_autorun(self):
        self.autorun = not self.autorun
        self.autospin_aktivni = self.autorun
        if self.autorun:
            self.auto_button.config(text="Stop ✋")
            self.tlacitko.config(state="disabled")
            self.spustit()
        else:
            self.auto_button.config(text="Autospin 🔁")
            self.tlacitko.config(state="normal")

    def zpracuj_klavesu(self, event):
        self.sekvence += event.char.lower()
        self.sekvence = self.sekvence[-9:]
        if "easteregg" in self.sekvence:
            self.images_load()

    def images_load(self):
        okno = Toplevel(self.root)
        okno.title("About")
        okno.geometry("400x300")
        label = tk.Label(okno, text="This game was made by \n Milan Kruml and parcify 🎮", font=("Arial", 14))
        label.pack(pady=10)

        canvas = tk.Canvas(okno, width=300, height=200)
        canvas.pack()

        try:
            gif = Image.open('load.gif')
            frames = [ImageTk.PhotoImage(f.copy().resize((300, 200))) for f in ImageSequence.Iterator(gif)]

            def animace(index=0):
                canvas.create_image(150, 100, image=frames[index])
                okno.after(100, animace, (index + 1) % len(frames))

            animace()
        except:
            canvas.create_text(150, 100, text="", font=("Arial", 12), fill="red")

# --- Spuštění ---
if __name__ == "__main__":
    root = tk.Tk()
    app = SlotovyAutomat(root)
    root.mainloop()
