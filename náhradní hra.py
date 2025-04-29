import random
import time
import os
from colorama import init, Fore, Style

# color
init()

words = [
    "meloun", "banán", "třešeň", "hruška", "cuketa", "ostružina", "jasmín", "zebra",
    "jehla", "jogurt", "kanec", "citron", "malina", "nektarinka", "jelen", "panda",
    "kohout", "raketa", "ryba", "pes", "tygr", "udice", "kachna", "plameňák",
    "křeček", "cirkus", "racek", "čmelák", "štika", "větrník", "káča", "jablko",
    "žralok", "motýl", "vlk", "husa", "delfín", "mýval", "brouk", "zajíc",
    "krůta", "jóga", "oliheň", "liška", "mravenec", "nosorožec", "chobotnice",
    "tučňák", "včela", "robot", "sova", "tuleň", "hroznýš", "žehlička", "bažant",
    "dravý", "volavka", "žížala", "balónek", "štěně", "bagr", "právník",
    "bobule", "autobus", "jezevec", "kolo", "gorila", "dům", "stromek",
    "žirafa", "zebu", "iglú", "jóga", "kámen", "lampa", "auto", "nos",
    "okurka", "pila", "pepř", "rak", "pero", "slunce", "pantofel", "kachna",
    "lucerna", "chata", "květina", "hrnek", "skříň", "šťovík", "obrazovka", "sukně",
    "jestřáb", "automat", "býk", "vrabec", "gazela", "drak"
]

czech_alphabet = "aábcčdďeéěfghhiíjklmnňoópqrřsštťuúůvwxyýzž"

#console clear
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

#time stop
stop = lambda s=1: time.sleep(s)


def draw_hangman(mistakes):
    stages = [
        "",
        "   O",
        "   O\n   |",
        "   O\n  /|",
        "   O\n  /|\\",
        "   O\n  /|\\\n  /",
        "   O\n  /|\\\n  / \\"
    ]
    print(stages[min(mistakes, 6)])
    print()


def start_game():
    random_word = list(random.choice(words).lower())
    word = ['_' for _ in random_word]
    used_letters = []
    win_count = 0
    program = True

    # BASE LIVES
    base_lives = 6
    extra_lives = max(0, (len(random_word) - 5) // 2)
    max_lives = base_lives + extra_lives
    dead_count = 0

    clear()
    print(Fore.MAGENTA + "Vítej ve hře 'Šibenice'!" + Style.RESET_ALL)
    stop(1.5)
    print("Pravidla:")
    stop(1)
    print(f"1. Slovo má {len(random_word)} písmen, máš {max_lives} životů.")
    stop(1)
    print("2. Zadej jedno písmeno nebo zkus celé slovo.")
    stop(2)
    input("\nStiskni Enter pro začátek...")
    clear()

    while program:
        if win_count == len(random_word):
            print(Fore.GREEN + f"Gratuluji! Vyhrál jsi! Hledané slovo bylo: {''.join(random_word).upper()}" + Style.RESET_ALL)
            break

        if dead_count == max_lives:
            print(Fore.RED + f"Bohužel, prohrál jsi. Slovo bylo: {''.join(random_word).upper()}" + Style.RESET_ALL)
            draw_hangman(dead_count)
            break

        print(f"Zbývající životy: {max_lives - dead_count}")
        draw_hangman(dead_count)
        print(f"Slovo: {' '.join(word).upper()}")
        print(f"Použitá písmena: {' '.join(used_letters).upper()}")
        n = input("Zadej písmeno nebo zkus celé slovo: ").lower()
        clear()

        if n in used_letters:
            print("Toto písmeno jsi už použil!")
            stop(1)
            continue

        if n == ''.join(random_word):
            print(Fore.GREEN + f"Neuvěřitelné! Uhodl jsi celé slovo: {''.join(random_word).upper()}" + Style.RESET_ALL)
            break

        if len(n) == 1 and n in czech_alphabet:
            if n in random_word:
                for i in range(len(random_word)):
                    if random_word[i] == n:
                        word[i] = n
                        win_count += 1
                print(f"Správně! Písmeno '{n.upper()}' je ve slově.")
            else:
                print(f"Špatně. Písmeno '{n.upper()}' tam není.")
                dead_count += 1
            used_letters.append(n)
            stop(1)
        elif n == 'parcify':
            print("Tuto hru vytvořil Parcify -_-")
            stop(2)
        else:
            print("Zadej jedno písmeno české abecedy nebo celé slovo.")
            stop(2)

while True:
    start_game()
    again = input("\nChceš si zahrát znovu? (ano/ne): ").lower()
    if again != 'ano':
        print("Tak se měj hezky!")
        break
    clear()
