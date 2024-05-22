import random
import os
import time
from sty import fg, bg
from colorama import init, Fore, Back, Style

init()

os.system("cls")

# DINERO
dinero = 500
enpartida = 550
beneficios = 20
win = True
lose = False

def centrado(cadena):
    cadena_cent = cadena.center(260)
    print(cadena_cent)



def imprime_resultado():

    global beneficios 
    global enpartida 

    if win == True:

        while beneficios != 0:

            os.system("cls")
        
            beneficios = beneficios - 1
            enpartida = enpartida + 1

            centrado(f"Deposito: {dinero}      En partida: {enpartida}      Apuesta: {fg(34) + str(beneficios) + fg.rs}")

            time.sleep(0.05)


    elif lose == True:

        while beneficios != 0:

            os.system("cls")

            beneficios = beneficios + 1
            enpartida = enpartida - 1

            centrado(f"Deposito: {dinero}      En partida: {enpartida}      Apuesta: {fg(160) + str(beneficios) + fg.rs}")

            time.sleep(0.05)


imprime_resultado()


