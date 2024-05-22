import random
import os
from sty import fg, bg
from colorama import init, Fore, Back, Style

os.system("cls")

palos = ["♠", "♥", "♦", "♣"]
valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",]
baraja = []

for palo in palos:
    for valor in valores:
        baraja.append([valor, palo])

def croupier():

    mano = []
    
    for i in range(2):

        carta_aleatoria = random.choice(baraja)

        if carta_aleatoria[1] == "♥" or carta_aleatoria[1] == "♦":
            carta_aleatoria[0] = fg(160) + carta_aleatoria[0] + fg.rs 
            carta_aleatoria[1] = fg(160) + carta_aleatoria[1] + fg.rs


        if carta_aleatoria[0] == "10":

            carta = ["┌─────────┐",
            f"│{carta_aleatoria[0]}       │",
            "│         │",
            "│         │",
            f"│    {carta_aleatoria[1]}    │",
            "│         │",
            "│         │",
            f"│       {carta_aleatoria[0]}│",
            "└─────────┘"]
                        
        else:

            carta = ["┌─────────┐",
            f"│{carta_aleatoria[0]}        │",
            "│         │",
            "│         │",
            f"│    {carta_aleatoria[1]}    │",
            "│         │",
            "│         │",
            f"│        {carta_aleatoria[0]}│",
            "└─────────┘"]




        mano.append(carta)

    for linea in range(len(carta)):
        print(f"{mano[0][linea]}  {mano[1][linea]}")
    
    input()


croupier() 

    
