import random
import os
import time
from sty import fg, bg
from colorama import init, Fore, Back, Style

init()

os.system("cls")

mesa = bg(22) + fg(124) + """
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                oooooooooo.  oooo                      oooo                oooo                     oooo                                                                                     
                                                                `888'   `Y8b `888                      `888                `888                     `888                                                                                     
                                                                 888     888  888   .oooo.    .ooooo.   888  oooo           888  .oooo.    .ooooo.   888  oooo                                                                               
                                                                 888oooo888'  888  `P  )88b  d88' `"Y8  888 .8P'            888 `P  )88b  d88' `"Y8  888 .8P'                                                                                
                                                                 888    `88b  888   .oP"888  888        888888.             888  .oP"888  888        888888.                                                                                 
                                                                 888    .88P  888  d8(  888  888   .o8  888 `88b.           888 d8(  888  888   .o8  888 `88b.                                                                               
                                                                o888bood8P'  o888o `Y888""8o `Y8bod8P' o888o o888o      .o. 88P `Y888""8o `Y8bod8P' o888o o888o                                                                              
                                                                                                                        `Y888P                                                                                                               
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
"""  + Back.RESET + fg.rs 



# VARIABLES GENERALES DEL CASINO

deposito = 500
enpartida = 200
apuesta = 0
win = False
lose = False





# VARIABLES BLACKJACK

blackjack = False
hit = "s"
salir = False
seguir = "s"
dividir = "n"
sumador_c = 0
sumador_j = 0
finish = False

mano_j_1 = []
mano_j_2 = []
sumador_j_1 = 0
sumador_j_2 = 0
valores_extraidos_j_1 = []
valores_extraidos_j_2 = []

palos = ["♠", "♥", "♦", "♣"]
valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",]
valores_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
baraja = []
carta_rever =[
Back.LIGHTWHITE_EX + fg(197) + "    __     " + Back.RESET + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + "   /\ \    " + Back.RESET + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + "  /::\ \   " + Back.RESET + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + " /::::\_\  " + Back.RESET + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + " \::::/ /  " + Back.RESET + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + "  \::/ /   " + Back.RESET + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + "   \/_/    " + Back.RESET + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + "           " + Back.RESET + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + "           " + Back.RESET + fg.rs]

mano_j = []
mano_c = []
valores_extraidos_j = []
valores_extraidos_c = []



# baraja = [("A", "♠"), ("A", "♥"), ("A", "♦"), ("A", "♠"), ("A", "♠"), ("A", "♠"), ("A", "♠"), ("A", "♥"), ("A", "♦"), ("A", "♠"), ("A", "♠"), ("A", "♠"), ("A", "♠"), ("A", "♥"), ("A", "♦"),  ("J", "♥"), ("J", "♥"), ("J", "♠"), ('J', '♥'), ("J", "♥"), ("J", "♥"), ("J", "♠"), ('J', '♥'), ("J", "♥"), ("J", "♥"), ("J", "♠"), ('J', '♥'), ("J", "♥"), ("J", "♥"), ("J", "♠"), ('J', '♥')]

for palo in palos:
    for valor in valores:
        baraja.append((valor, palo))



#FUNCIONES GENERALES DEL CASINO


#Creamos un print que centre las cadenas que imprimimos
def centrado(cadena):
    cadena_cent = cadena.center(260)
    print(cadena_cent)



def imprime_resultado():

    global apuesta 
    global enpartida
    global win
    global lose


    if win == True:

        while apuesta != 0:

            os.system("cls")
        
            apuesta = apuesta - 1
            enpartida = enpartida + 1

            centrado(f"Deposito: {deposito}      En partida: {enpartida}      Apuesta: {fg(34) + str(apuesta) + fg.rs}")

            time.sleep(0.05)


    elif lose == True:

        apuesta = apuesta * -1

        while apuesta != 0:

            os.system("cls")

            apuesta = apuesta + 1
            enpartida = enpartida - 1

            centrado(f"Deposito: {deposito}      En partida: {enpartida}      Apuesta: {fg(160) +  str(apuesta) + fg.rs}")

            time.sleep(0.05)

    win = False
    lose = False
    






#FUNCIONES BLACK JACK



def manos_inic(mano, carta1, carta2):

    print("\n")

    for linea in range(len(carta_rever)):       #Ponemos la longitud de la carta rever porque es la única que esta fuera de una función no por otra cosa
        centrado(f"{mano[carta1][linea]}   {mano[carta2][linea]}")


def manos_hit(mano):
    for linea in range(len(carta_rever)):
        print("")
        for carta in range(len(mano)):
            print(f"{mano[carta][linea]}  ", end = " ")
    print("")


def carta_rmdon():
    carta_aleatoria = random.choice(baraja_use)
    baraja_use.remove(carta_aleatoria)      #Borramos la carta de la baraja

    return carta_aleatoria

    


def suma_valores(valores_extraidos, sumador):

    sumador = 0
    prim_vez_as = False

    for carta in valores_extraidos:
        indice = valores.index(carta[0])
        sumador += valores_num[indice]
        if carta[0] =="A":
            if sumador < 11:
                prim_vez_as = True
                sumador += 10
                

    for carta in valores_extraidos:
        if carta[0] == "A":
            if sumador > 21 and prim_vez_as == True:
                prim_vez_as = False
                sumador -= 10

    return sumador


def imprime_manos_hit(valores_extraidos, sumador, mano):

    carta_aleatoria = carta_rmdon()
    new_carta = crea_cartas(carta_aleatoria)
    valores_extraidos.append(carta_aleatoria)
    mano.append(new_carta)
    sumador = suma_valores(valores_extraidos, sumador)

    #Imprimimos
    os.system("cls")
    manos_inic(mano_c, 1, 0)
    print(mesa)
    
    if mano == mano_j_1:
        print("1º Mano")
    
    elif mano == mano_j_2:
        print("2º Mano")

    manos_hit(mano)


    return sumador





def crea_cartas(carta_aleatoria): #Esta función es un generador de cartas

     #En el caso de que sea 10, lo adaptamos para que la carta no se sobresalga por los lados
    if carta_aleatoria[0] == "10":

        carta = ["           ",
        f" {carta_aleatoria[0]}        ",
        "           ",
        "           ",
        f"     {carta_aleatoria[1]}     ",
        "           ",
        "           ",
        f"        {carta_aleatoria[0]} ",
        "           "]
                    
    else:

        carta = ["           ",
        f" {carta_aleatoria[0]}         ",
        "           ",
        "           ",
        f"     {carta_aleatoria[1]}     ",
        "           ",
        "           ",
        f"         {carta_aleatoria[0]} ",
        "           "]
    
    #Le metemos los colores  las cartas
    if carta_aleatoria[1] == "♥" or carta_aleatoria[1] == "♦":
        for indice, linea in enumerate(carta):
            linea2 = Back.LIGHTWHITE_EX + fg(160) + linea + Back.RESET + fg.rs 
            carta[indice] = linea2

    else:
        for indice, linea in enumerate(carta):
            linea2 = Back.LIGHTWHITE_EX + fg(16) + linea + Back.RESET + fg.rs 
            carta[indice] = linea2


    return carta


def croupier_hit(sumador, mano):

    sumador_c = 0

    sumador_c = suma_valores(valores_extraidos_c, sumador_c)



    while sumador_c < 17 and sumador_c <= sumador:


        sumador_c = suma_valores(valores_extraidos_c, sumador_c)


        if sumador_c < 17 and sumador_c <= sumador:

            print("\n")
            carta_aleatoria = carta_rmdon()
            new_carta = crea_cartas(carta_aleatoria)
            valores_extraidos_c.append(carta_aleatoria)
            mano_c.append(new_carta)
            
            os.system("cls")
            manos_hit(mano_c)
            print(mesa)
            manos_hit(mano)
            time.sleep(1.5)



    return sumador_c


def ganador_bj(sumador):

    global win
    global lose

    if (sumador > sumador_c and sumador <= 21) or (sumador_c > 21 and sumador <= 21) :
        centrado(Fore.GREEN + "YOU WIN" + Fore.RESET)
        input()
        win = True


    elif sumador == sumador_c:
        centrado("Empate")
        input()

        
    else:
        centrado(Fore.RED + "YOU LOSE" + Fore.RESET)
        input()
        lose = True



def black_jack(valores_extraidos, sumador):

    global blackjack

    if (valores_extraidos[0][0] == "A" and valores_extraidos[1][0] in valores[9:]) or (valores_extraidos[1][0] == "A" and valores_extraidos[0][0] in valores[9:]):

        blackjack = True
        sumador = 21
        
    
    return sumador


























# ALGORITMO PRINCIPAL 

while salir == False:




    if finish == True:

        seguir = input("¿Quieres jugar otra partida? (s/n): ").lower()        
        os.system("cls")


    if seguir == "s":

        #Si da tiempo poner la función comprobar 
        print(mesa)
        print("\n")
        apuesta = int(input("¿Cuánto quieres apostar?: "))
        os.system("cls")

        hit = "s"
        blackjack = False
        finish = False
        mano_j = []
        mano_c = []
        sumador_c = 0
        valores_extraidos_c = []
        valores_extraidos_j = []
        baraja_use = list(baraja)

    else:
        salir = True


#Empieza la partida

    while finish == False:

#Se reparten las manos

        mano_c.append(carta_rever)

        for i in range(4):
            carta_aleatoria = carta_rmdon()
            new_carta = crea_cartas(carta_aleatoria)
            

            if i % 2 == 0:
                mano_j.append(new_carta)
                valores_extraidos_j.append(carta_aleatoria)
            
            else:
                mano_c.append(new_carta)
                valores_extraidos_c.append(carta_aleatoria)

        manos_inic(mano_c, 1, 0)
        print(mesa)
        manos_inic(mano_j, 0, 1)

        sumador_j = suma_valores(valores_extraidos_j, sumador_j)

        pairs = valores_extraidos_j[0][0] == valores_extraidos_j[1][0]



    #Si es blackjack se termina la partida

        sumador_j = black_jack(valores_extraidos_j, sumador_j)

        if blackjack == True:
            win = True
            apuesta = apuesta * 3/2
            input("BLACKJACK")
            imprime_resultado()
            finish = True


    
#En el caso de sea pairs y quiera dividir la mano
        

        elif pairs:
            
            dividir = input("¿Quieres dividir la mano? (s/n): ").lower()

        if dividir == "s" and pairs:

            mano_j_1 = [mano_j[0]]
            mano_j_2 = [mano_j[1]]
            sumador_j_1 = 0
            sumador_j_2 = 0
            valores_extraidos_j_1 = [valores_extraidos_j[0]]
            valores_extraidos_j_2 = [valores_extraidos_j[1]]


#Primera mano 

            sumador_j_1 = imprime_manos_hit(valores_extraidos_j_1,sumador_j_1, mano_j_1)

            sumador_j_1 = black_jack(valores_extraidos_j_1, sumador_j_1)
            if blackjack == True:
                input("BLACKJACK")
                blackjack = False


            while hit == "s" and sumador_j_1 < 21:

                hit = input("¿Quieres otra carta? (s/n): ").lower()

                if hit == "s":

    #Hit de la primera mano

                    sumador_j_1 = imprime_manos_hit(valores_extraidos_j_1, sumador_j_1, mano_j_1)



    #Segunda mano  

            input("Pasamos a la segunda mano")
            hit = "s"
            sumador_j_2 = imprime_manos_hit(valores_extraidos_j_2, sumador_j_2, mano_j_2)

            sumador_j_2 = black_jack(valores_extraidos_j_2, sumador_j_2)
            if blackjack == True:
                input("BLACKJACK")


            while hit == "s" and sumador_j_2 < 21:

                hit = input("¿Quieres otra carta? (s/n): ").lower()

    #Hit segunda mano

                if hit == "s":
                    sumador_j_2 = imprime_manos_hit(valores_extraidos_j_2, sumador_j_2, mano_j_2)

        blackjack = False


        if dividir != "s" and sumador_j != 21:


            while hit == "s":

                hit = input("¿Quieres otra carta? (s/n): ").lower()

                if hit == "s":

                    sumador_j = imprime_manos_hit(valores_extraidos_j, sumador_j, mano_j)

                    if sumador_j > 21:
                        #Poner has perdido
                        hit = "n"
                        finish = True
                        lose = True
                        centrado(Fore.RED + "YOU LOSE" + Fore.RESET)
                        input()
                        imprime_resultado()
        

            

        
#Parte del croupier

        if finish == False:


            croupier_play = not (sumador_j_1 >= 21 and sumador_j_2 >= 21)
                
            if croupier_play:
                

                #Parte en la que juega el crea_cartas
                os.system("cls")
                manos_inic(mano_c, 1, 0)
                print(mesa)
                if pairs and dividir == "s":
                    manos_hit(mano_j_1)
                    manos_hit(mano_j_2)
                else:
                    manos_hit(mano_j)
                time.sleep(2)

                #Borramos la carta reverse
                mano_c.pop(0)

                #El crea_cartas muestra sus cartas
                os.system("cls")
                manos_inic(mano_c, 0, 1)
                print(mesa)
                if pairs and dividir == "s":
                    manos_hit(mano_j_1)
                    manos_hit(mano_j_2)
                else:
                    manos_hit(mano_j)
                time.sleep(2)

                sumador_c = black_jack(valores_extraidos_c, sumador_c)
                blackjack = False

                if pairs and dividir == "s":
                    
                    if sumador_c != 21:

                        sumador_c = croupier_hit(sumador_j_1, mano_j_1)

                else:

                    if sumador_c != 21:

                        sumador_c = croupier_hit(sumador_j, mano_j)
                

                


            
            else:
                mano_c.pop(2)


                

                


            if pairs and dividir == "s":
                

                os.system("cls")
                manos_hit(mano_c)
                print(mesa)
                print("1º Mano")
                manos_hit(mano_j_1)
                time.sleep(1.5)
                black_jack(valores_extraidos_j_1, sumador_j_1)
                memo_apuesta = apuesta
                if blackjack == True:
                    apuesta = apuesta * 3/2
                    win = True
                    blackjack = False
                    input("BLACKJACK")
                else:
                    ganador_bj(sumador_j_1)
                print("Sumador croupier:", sumador_c)
                print("Sumador jugador: ", sumador_j)
                imprime_resultado()



                os.system("cls")
                manos_hit(mano_c)
                print(mesa)
                print("2º Mano")
                manos_hit(mano_j_2)
                time.sleep(1.5)
                black_jack(valores_extraidos_j_2, sumador_j_2)
                apuesta = memo_apuesta
                if blackjack == True:
                    win = True
                    apuesta = apuesta * 3/2
                    input("BLACKJACK")
                else:
                    ganador_bj(sumador_j_2)

                imprime_resultado()



            else:

                ganador_bj(sumador_j)
                imprime_resultado()




            finish = True



