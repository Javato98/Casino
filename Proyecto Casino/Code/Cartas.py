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



hit = "xyz"
sumador_c = 0
sumador_j = 0
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




# baraja = [("A", "♠"), ("A", "♥"), ("A", "♦"), ("A", "♠"), ("A", "♠"), ("A", "♠"), ('A', '♠')]

for palo in palos:
    for valor in valores:
        baraja.append((valor, palo))


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
    carta_aleatoria = random.choice(baraja)
    baraja.remove(carta_aleatoria)      #Borramos la carta de la baraja

    return carta_aleatoria



def suma_valores(valores_extraidos, sumador):

    sumador = 0

    for carta in valores_extraidos: #Primero comprobamos si en la mano hay un As para que valga 11 según las condiciones más favorables, y que vuelva a valer 1 en el caso de que sean dos ases
        if carta[0] == "A":
            if sumador < 12:
                valores_num[0] = 11
            elif sumador_c > 21:
                valores_num[0] = 1


    for carta in valores_extraidos:
        indice = valores.index(carta[0])
        sumador += valores_num[indice]
        if carta[0] == "A":
            valores_num[0] = 1

    return sumador




def croupier(): #Esta función es un generador de cartas


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






while finish == False:

    print("\n\n")

    #Cuando el contador este a 2, quiere decir que estamos en la primera mano, por lo que únicamente se reparten las manos de croupier y la del jugador
    if hit == "xyz": #Lo igualamanos a 'xyz' porque nos da igual la condición, solamente queremos que pase la primera vez por ahí vez por ahí

        mano_c.append(carta_rever)

        for i in range(4):
            carta_aleatoria = carta_rmdon()
            new_carta = croupier()
            


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
    

        hit = "s" 


    else:

        #Hacemos el hit (Pedir carta)
        hit = input("¿Quieres otra carta? (s/n): ").lower()
        sumador_j = suma_valores(valores_extraidos_j, sumador_j)

        if hit == "s":
            carta_aleatoria = carta_rmdon()
            new_carta = croupier()
            valores_extraidos_j.append(carta_aleatoria)
            mano_j.append(new_carta)
            sumador_j = suma_valores(valores_extraidos_j, sumador_j)

            #Imprimimos
            os.system("cls")
            manos_inic(mano_c, 1, 0)
            print(mesa)
            manos_hit(mano_j)
            print(sumador_j)


            if sumador_j > 21:
                input("Has perdido 1")
                hit = "n"
                finish = True
            


        else:
                

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
                        new_carta = croupier()
                        valores_extraidos_c.append(carta_aleatoria)
                        mano_c.append(new_carta)
                        
                        os.system("cls")
                        manos_hit(mano_c)
                        print(mesa)
                        manos_hit(mano_j)
                        time.sleep(1.5)
                            


                if (sumador_j > sumador_c and sumador_j <= 21) or (sumador_c > 21 and sumador_j <= 21) : #Corregir la primera condicion
                    input("Has ganado")

                elif sumador_j == sumador_c:
                    input("Empate")
                    input(sumador_j)
                    input(sumador_c)
                    
                else:
                    input("Has perdido")

                print(sumador_c)
                print(sumador_j)
                input()

                finish = True


input(len(baraja))

