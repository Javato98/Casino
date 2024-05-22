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
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                             
"""  + fg.rs 



hit = "s"
salir = False
seguir = "s"
aduana1 = 1
sumador_c = 0
sumador_j = 0
condi_blackjack = False
finish = False
palos = ["♠", "♥", "♦", "♣"]
valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",]
valores_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
baraja = []
carta_rever =[
Back.LIGHTWHITE_EX + fg(197) + "    __     " + bg(22) + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + "   /\ \    " + bg(22) + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + "  /::\ \   " + bg(22) + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + " /::::\_\  " + bg(22) + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + " \::::/ /  " + bg(22) + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + "  \::/ /   " + bg(22) + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + "   \/_/    " + bg(22) + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + "           " + bg(22) + fg.rs,
Back.LIGHTWHITE_EX + fg(197) + "           " + bg(22) + fg.rs]

mano_j = []
mano_c = []
valores_extraidos_j = []
valores_extraidos_c = []



baraja = [("A", "♠"), ("A", "♥"), ("A", "♦"), ("A", "♠"), ("A", "♠"), ("A", "♠"), ('A', '♠')]

# for palo in palos:
#     for valor in valores:
#         baraja.append((valor, palo))


#Creamos un print que centre las cadenas que imprimimos
def centrado(cadena):
    cadena_cent = cadena.center(260)
    print(cadena_cent)


def manos_inic(mano, carta1, carta2):
    print(bg(22) + "")
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
    new_carta = croupier(carta_aleatoria)
    valores_extraidos.append(carta_aleatoria)
    mano.append(new_carta)
    sumador = suma_valores(valores_extraidos, sumador)

    #Imprimimos
    os.system("cls")
    manos_inic(mano_c, 1, 0)
    print(mesa)
    manos_hit(mano)
    print(sumador)


    return sumador




def croupier(carta_aleatoria): #Esta función es un generador de cartas

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
            linea2 = Back.LIGHTWHITE_EX + fg(160) + linea + bg(22) + fg.rs 
            carta[indice] = linea2

    else:
        for indice, linea in enumerate(carta):
            linea2 = Back.LIGHTWHITE_EX + fg(16) + linea + bg(22) + fg.rs 
            carta[indice] = linea2


    return carta










# ALGORITMO PRINCIPAL 

while salir == False:


    if aduana1 == 0:
        print(bg(22))
        seguir = input("¿Quieres jugar otra partida? (s/n): ").lower()
        os.system("cls")


    if seguir == "s":
        hit = "s"
        finish = False
        mano_j = []
        mano_c = []
        sumador_c = 0
        valores_extraidos_c = []
        valores_extraidos_j = []
        baraja_use = list(baraja)
        aduana1 = 1

    else:
        salir = True



    while finish == False:

        print("\n\n")

        #Cuando el contador este a 2, quiere decir que estamos en la primera mano, por lo que únicamente se reparten las manos de croupier y la del jugador
        if aduana1 == 1: #Lo igualamanos a 'xyz' porque nos da igual la condición, solamente queremos que pase la primera vez por ahí vez por ahí

            mano_c.append(carta_rever)

            for i in range(4):
                carta_aleatoria = carta_rmdon()
                new_carta = croupier(carta_aleatoria)
                

                if i % 2 == 0:
                    mano_j.append(new_carta)
                    valores_extraidos_j.append(carta_aleatoria)
                
                else:
                    mano_c.append(new_carta)
                    valores_extraidos_c.append(carta_aleatoria)

            manos_inic(mano_c, 1, 0)
            print(mesa)
            manos_inic(mano_j, 0, 1)

            if (valores_extraidos_j[0][0] == "A" and valores_extraidos_j[1][0] in valores[9:]) or (valores_extraidos_j[1][0] == "A" and valores_extraidos_j[0][0] in valores[9:]):
                print("BLACK JACK")
                sumador_j = 21
                input("Has ganado")
                finish = True
        

            aduana1 = 2


        else:

            if valores_extraidos_j[0][0] == valores_extraidos_j[1][0]:

                if aduana1 != 3:
                
                    dividir = input("¿Quieres dividir las mano? (s/n): ")

                    if dividir == "s":

                        mano_j_1 = [mano_j[0]]
                        mano_j_2 = [mano_j[1]]
                        sumador_j_1 = 0
                        sumador_j_2 = 0
                        valores_extraidos_j_1 = [valores_extraidos_j[0]]
                        valores_extraidos_j_2 = [valores_extraidos_j[1]]
                        aduana1 = 3

                        manos_inic(mano_c, 1, 0)
                        print(mesa)
                        manos_hit(mano_j_1)
                        manos_hit(mano_j_2)
                        
                
                else:

                    while hit == "s":

                        hit = input("¿Quieres otra carta? (s/n): ").lower()

                        if hit == "s":

                            print("Primera mano")
                            imprime_manos_hit(valores_extraidos_j_1, sumador_j_1, mano_j_1)
                            manos_hit(mano_j_2)

                        elif sumador_j_1 > 21 or hit != "s":
                        	#Imprimelo aqui para que solo lo haga una vez
                            hit = "s"
                            while hit == "s":

                                #Aquí nos quedamos

                                hit = input("¿Quieres otra carta? (s/n): ").lower()

                                if hit == "s":
                                    print("Segunda mano")
                                    sumador_j_2 = imprime_manos_hit(valores_extraidos_j_2, sumador_j_2, mano_j_2)
                                    manos_hit(mano_j_1)
                                
                                elif sumador_j_2 > 21 or hit != "s":
                                    hit = "n"
                                    aduana1 = 0
                                    finish = True

                
            else:

                while hit == "s":

                    hit = input("¿Quieres otra carta? (s/n): ").lower()

                    if hit == "s":
                
                        sumador_j = imprime_manos_hit(valores_extraidos_j, sumador_j, mano_j)

                    elif sumador_j > 21:
                        hit = "n"
                        aduana1 = 0
                        finish = True
                

#A ver como cojones ponemos la condicion del croupier para cuando se divida la baraja 

#Puedes plantearte hacer una funcion guardando todo esto y pojer tres condiciones, dependiendo de la mano_j que sea, cambiando los parametros en funcion de cual sea 
            if hit != "s":
                    

                    #Parte en la que juega el croupier
                    os.system("cls")
                    manos_inic(mano_c, 1, 0)
                    print(mesa)
                    manos_hit(mano_j)
                    time.sleep(2)

                    #Borramos la carta reverse
                    mano_c.pop(0)

                    #El croupier muestra sus cartas
                    os.system("cls")
                    manos_inic(mano_c, 0, 1)
                    print(mesa)
                    manos_hit(mano_j)
                    time.sleep(2)


                    while sumador_c < 17 and sumador_c <= sumador_j:


                        sumador_c = suma_valores(valores_extraidos_c, sumador_c)

                        

                        if sumador_c < 17 and sumador_c <= sumador_j:

                            print("\n")
                            carta_aleatoria = carta_rmdon()
                            new_carta = croupier(carta_aleatoria)
                            valores_extraidos_c.append(carta_aleatoria)
                            mano_c.append(new_carta)
                            
                            os.system("cls")
                            manos_hit(mano_c)
                            print(mesa)
                            manos_hit(mano_j)
                            time.sleep(1.5)
                                


                    if (sumador_j > sumador_c and sumador_j <= 21) or (sumador_c > 21 and sumador_j <= 21) :
                        input("Has ganado")


                    elif sumador_j == sumador_c:
                        input("Empate")

                        
                    else:
                        input("Has perdido")

                    print("Croupier: ", sumador_c)
                    print("Jugador: ", sumador_j)
                    print("Valores Jugador", valores_extraidos_j)
                    print("Valores Crou",valores_extraidos_c)

                    print("Baraja: ", len(baraja))
                    print("Baraja use: ", len(baraja_use))
                    input()

                    finish = True
                    aduana1 = 0



