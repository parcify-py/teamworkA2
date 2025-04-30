# teamworkA2
# 🖼️ Prohlížeč obrázků v Tkinteru

Tento jednoduchý Pythonový projekt umožňuje načítat a zobrazovat obrázky z určené složky pomocí grafického rozhraní vytvořeného s knihovnou **Tkinter**.

## 🔧 Funkce
- Automatické načtení všech obrázků ze zvolené složky
- Podpora formátů: `.png`, `.jpg`, `.jpeg`, `.gif`
- Úprava velikosti obrázků dle přednastavené hodnoty
- Příprava obrázků pro zobrazení ve widgetech jako je `Label` nebo `Canvas`

## 📁 Předpoklady
- Python 3.x
- Knihovny:
  - `Pillow` (`pip install pillow`)
  - `tkinter` (součástí standardní knihovny v Pythonu)

## ⚙️ Nastavení
Upravte hodnoty těchto konstant podle potřeby:

```python
SLOZKA_OBRAZKU = "cesta/k/vaší/složce"
VELIKOST_OBRAZKU = (150, 150)  # šířka, výška v pixelech
