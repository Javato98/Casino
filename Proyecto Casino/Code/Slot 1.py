import os
import time
from random import randint
from sty import fg

apuesta = 2
dinero = 500
enpartida = 100
finish = "s"
lose = False
win = False


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

            centrado(f"Deposito: {dinero}      En partida: {enpartida}      Apuesta: {fg(34) + str(apuesta) + fg.rs}")

            time.sleep(0.05)


    elif lose == True:

        apuesta = apuesta * -1

        while apuesta != 0:

            os.system("cls")

            apuesta = apuesta + 1
            enpartida = enpartida - 1

            centrado(f"Deposito: {dinero}      En partida: {enpartida}      Apuesta: {fg(160) +  str(apuesta) + fg.rs}")

            time.sleep(0.05)

    win = False
    lose = False
    






# Below are defined 6 lists of 6 strings which are displayed in game symbols
# Number in parenthesis for 'fg' method sets 8-bit color for string
strawberry = [fg(111) + '         ' + fg.rs,
               fg(34) + '    ##   ' + fg.rs,
              fg(196) + '   ####  ' + fg.rs,
              fg(196) + '   ####  ' + fg.rs,
              fg(196) + '    ##   ' + fg.rs,
              fg(111) + '         ' + fg.rs]

banana = [fg(226) + '         ' + fg.rs,
          fg(226) + '      #  ' + fg.rs,
          fg(226) + '     ##  ' + fg.rs,
          fg(220) + '    ##   ' + fg.rs,
          fg(220) + '  ##     ' + fg.rs,
          fg(226) + '         ' + fg.rs]

plum = [fg(22) + '         ' + fg.rs,
        fg(22) + '    ##   ' + fg.rs,
        fg(19) + '  ####   ' + fg.rs,
        fg(19) + ' #####   ' + fg.rs,
        fg(19) + '  ##     ' + fg.rs,
        fg(22) + '         ' + fg.rs]

raspberry = [fg(161) + '         ' + fg.rs,
              fg(34) + '    #    ' + fg.rs,
             fg(161) + '   ###   ' + fg.rs,
             fg(161) + '  #####  ' + fg.rs,
             fg(161) + '   ###   ' + fg.rs,
             fg(161) + '         ' + fg.rs]

orange = [fg(111) + '         ' + fg.rs,
           fg(40) + '     #   ' + fg.rs,
          fg(208) + '   ###   ' + fg.rs,
          fg(208) + '  #####  ' + fg.rs,
          fg(208) + '   ###   ' + fg.rs,
          fg(111) + '         ' + fg.rs]

seven = [fg(111) + '         ' + fg.rs,
          fg(88) + '   ####  ' + fg.rs,
         fg(124) + '      #  ' + fg.rs,
         fg(160) + '     #   ' + fg.rs,
         fg(196) + '    #    ' + fg.rs,
         fg(111) + '         ' + fg.rs]



class Slots:

    def __init__(self):
        """
        Defining 3 slots of machine as lists from already defined variables
        First slot is unique because except printable symbol it has also multiplier of bet
        """
        self.slot_one = [(strawberry, 2), (banana, 10), (plum, 3), (strawberry, 2), (raspberry, 5), (plum, 3), (orange, 8), (seven, 15)]
        self.slot_two = [banana, strawberry, plum, orange, strawberry, plum, raspberry, seven]
        self.slot_three = [plum, strawberry, raspberry, orange, plum, strawberry, seven, banana]

    def roll(self):
        """
        This method is responsible for showing machine's slots in motion
        """
        # First of all 3 random numbers are set
        # Since every symbol of slots has 6 lines, all 3 numbers must be divisible by 6 to make full rotates
        a, b, c = 1, 1, 1
        while a % 6 != 0:
            a = randint(70, 110)
        while b % 6 != 0:
            b = randint(60, 90)
        while c % 6 != 0:
            c = randint(70, 100)

        # This for loop composes 3 lists to pass them to function that will print current state of slots
        # Does this for random number of times using first random number set before
        # Variable 'i' will be used to access only some parts of displayed symbols
        i = 1
        for _ in range(a):
            os.system("cls")
            if i == 6:
                i = 0
                # After each 6 jumps of slots by single line first symbol of each slot list will be moved at the end
                self.slot_one.append(self.slot_one.pop(0))
                self.slot_two.append(self.slot_two.pop(0))
                self.slot_three.append(self.slot_three.pop(0))

            # Here are composed lists to be printed
            # First symbol may be partial and then will be taken part of forth symbol
            s1 = self.slot_one[0][0][i:] + self.slot_one[1][0] + self.slot_one[2][0] + self.slot_one[3][0][0:i]
            s2 = self.slot_two[0][i:] + self.slot_two[1] + self.slot_two[2] + self.slot_two[3][0:i]
            s3 = self.slot_three[0][i:] + self.slot_three[1] + self.slot_three[2] + self.slot_three[3][0:i]
            i += 1
            layout(s1, s2, s3)
            time.sleep(0.02)

        # Similar as before, but now first slot will not changed - no move
        i = 1
        for _ in range(b):
            os.system("cls")
            if i == 6:
                i = 0
                self.slot_two.append(self.slot_two.pop(0))
                self.slot_three.append(self.slot_three.pop(0))

            s1 = self.slot_one[0][0] + self.slot_one[1][0] + self.slot_one[2][0]
            s2 = self.slot_two[0][i:] + self.slot_two[1] + self.slot_two[2] + self.slot_two[3][0:i]
            s3 = self.slot_three[0][i:] + self.slot_three[1] + self.slot_three[2] + self.slot_three[3][0:i]
            i += 1
            layout(s1, s2, s3)
            time.sleep(0.02)

        # Last sequence, with only last slot changing
        i = 1
        for t in range(c):
            os.system("cls")
            if i == 6:
                i = 0
                self.slot_three.append(self.slot_three.pop(0))

            s1 = self.slot_one[0][0] + self.slot_one[1][0] + self.slot_one[2][0]
            s2 = self.slot_two[0] + self.slot_two[1] + self.slot_two[2]
            s3 = self.slot_three[0][i:] + self.slot_three[1] + self.slot_three[2] + self.slot_three[3][0:i]
            i += 1
            layout(s1, s2, s3)
            # Equation below gives last slot slowing-down effect, can be tweaked easily
            time.sleep(0.02 + t**2 / 90000)





def layout(s1, s2, s3):
    """
    Responsible for graphical representation of game
    :param s1, s2, s3: Three slots prepared by one of methods from Slots class
    """
    print('\n\t\t\tUP/DOWN LINE    x1')
    print('\t\t\tDIAGONAL LINE   x2')
    print('\t\t\tCENTER LINE     x3')
    print('\n\t   __________________________________________')
    print('\t  /                                         /|')
    print('\t /_________________________________________/ |')
    print('\t|                                         |  |')
    print('\t|                                         |  |')
    print('\t|                                         |  |')
    print('\t|   STRAWBERRY  x2       PLUM       x3    |  |')
    print('\t|                                         |  |')
    print('\t|   RASPBERRY   x5       ORANGE     x8    |  |')
    print('\t|                                         |  |')
    print('\t|   BANANA     x10       SEVENS    x15    |  |')
    print('\t|                                         |  |')
    print('\t|                                         |  |')
    print('\t|   -----------------------------------   |  |')
    for l, m, r in zip(s1, s2, s3):
        print('\t|  |', l, '|', m, '|',  r, '|  |  |')
    print('\t|   -----------------------------------   |  |')
    print('\t|                                         |  |')
    print(f'\t|    APUESTA : {apuesta}      ENPARTIDA : {enpartida}     |  |')
    print('\t|                                         | /')
    print('\t|_________________________________________|/')




def welcome():
    welcome = ['\n\n\t #######    #######    #######',
               '\t########   ########   ########',
               '\t     ##         ##         ##',
               '\t    ##         ##         ##',
               '\t   ##         ##         ##',
               '\t  ##         ##         ##',
               '\t  ##         ##         ##',
               '\n\n'
               '\t#### ###  #  #  # ##### ####',
               '\t#    #  # #  #  #   #   #  ',
               '\t###  ###  #  #  #   #   ####',
               '\t#    #  # #  #  #   #      #',
               '\t#    #  # ####  #   #   ####']
    for c in welcome:
        print(c)
        time.sleep(0.1)
    time.sleep(1)




def premios_slots():

    global apuesta
    global win

    if machine.slot_one[2][0] == machine.slot_two[1] and machine.slot_three[0] == machine.slot_two[1]:
        apuesta = (apuesta * 2) * machine.slot_one[2][1]
        win = True

    if machine.slot_one[0][0] == machine.slot_two[1] and machine.slot_three[2] == machine.slot_two[1]:
        apuesta = (apuesta * 2) * machine.slot_one[0][1]
        win = True

    if machine.slot_one[1][0] == machine.slot_two[1] and machine.slot_three[1] == machine.slot_two[1]:
        apuesta = (apuesta * 3) * machine.slot_one[1][1] 
        win = True

    if machine.slot_one[0][0] == machine.slot_two[0] and machine.slot_three[0] == machine.slot_two[0]:
        apuesta = apuesta  * machine.slot_one[0][1] 
        win = True

    if machine.slot_one[2][0] == machine.slot_two[2] and machine.slot_three[2] == machine.slot_two[2]:
        apuesta = apuesta  * machine.slot_one[2][1] 
        win = True

    if win == True:
        print("\n\n")
        print("Has ganado ", apuesta, " monedas.")
        input("Pulsa Enter para continuar")



machine = Slots()

welcome()
os.system("cls")
print("\n\n\n")
centrado("Introduce cuánto dinero quieres tener en partida:")
enpartida = int(input("\t\t\t\t\t\t\t\t--> "))
os.system("cls")
print("\n\n\n")
centrado("Introduce la apuesta con la quieres jugar: ")
print("\n")
centrado("Recuerda que en este modelo de juego la apuesta es invariable")
centrado("En el caso de que quieras modificar la apuesta tendrás que salir ")
centrado("al menú principal e introducirla de nuevo.")
print("\n")
apuesta = int(input("\t\t\t\t\t\t\t\t--> "))
memo_apuesta = apuesta



while finish == "s":

    apuesta = memo_apuesta
    enpartida = enpartida - apuesta

    
    machine.roll()
    premios_slots()

    imprime_resultado()

    print("\n")

    if enpartida <= 0:
        print("Lo siento te has quedado sin monedas.")
        input("Pulsa Enter para volver al menú principal")

    else:
        finish = input("¿Quieres jugar otra vez? (S/N): ").lower()
    
    


    





print(apuesta)
input()

