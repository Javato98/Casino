import random
import os
import sys
import time
from sty import fg, bg
from colorama import init, Fore, Back, Style


init()

os.system("cls")

casino_intr="""
                                                                                    /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$ /$$   /$$  /$$$$$$                   
                                                                                   /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/| $$$ | $$ /$$__  $$                  
                                                                                  | $$  \__/| $$  \ $$| $$  \__/  | $$  | $$$$| $$| $$  \ $$                  
                                                                                  | $$      | $$$$$$$$|  $$$$$$   | $$  | $$ $$ $$| $$  | $$                  
                                                                                  | $$      | $$__  $$ \____  $$  | $$  | $$  $$$$| $$  | $$                  
                                                                                  | $$    $$| $$  | $$ /$$  \ $$  | $$  | $$\  $$$| $$  | $$                  
                                                                                  |  $$$$$$/| $$  | $$|  $$$$$$/ /$$$$$$| $$ \  $$|  $$$$$$/                  
                                                                                   \______/ |__/  |__/ \______/ |______/|__/  \__/ \______/                   
                                                                                                                                                              
                                                                                                                                                              
                                                                                                                                                              
                                                                       /$$   /$$ /$$   /$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$ /$$   /$$ /$$$$$$$$ /$$$$$$$ 
                                                                      | $$  | $$| $$$ | $$ /$$__  $$| $$  | $$ /$$__  $$|_  $$_/| $$$ | $$| $$_____/| $$__  $$
                                                                      | $$  | $$| $$$$| $$| $$  \__/| $$  | $$| $$  \ $$  | $$  | $$$$| $$| $$      | $$  \ $$
                                                                      | $$  | $$| $$ $$ $$| $$      | $$$$$$$$| $$$$$$$$  | $$  | $$ $$ $$| $$$$$   | $$  | $$
                                                                      | $$  | $$| $$  $$$$| $$      | $$__  $$| $$__  $$  | $$  | $$  $$$$| $$__/   | $$  | $$
                                                                      | $$  | $$| $$\  $$$| $$    $$| $$  | $$| $$  | $$  | $$  | $$\  $$$| $$      | $$  | $$
                                                                      |  $$$$$$/| $$ \  $$|  $$$$$$/| $$  | $$| $$  | $$ /$$$$$$| $$ \  $$| $$$$$$$$| $$$$$$$/
                                                                       \______/ |__/  \__/ \______/ |__/  |__/|__/  |__/|______/|__/  \__/|________/|_______/ 

                                                                       

                                                                               ___       _____  ____   _____  _____  __ ___  ____  _____  _____  __ ___
                                                                              /   |     /  _  \/  _/  /  _  \/     \|  |  /  \_  \/  _  \/     \|  |  /
                                                                               |  |  _  |  _  <|  |---|  _  ||  |--||  _ < ---|  ||  _  ||  |--||  _ < 
                                                                              <____><_> \_____/\_____/\__|__/\_____/|__|__\\\_____/\__|__/\_____/|__|__\\
                                                                                                                                                       
                                                                               _____      _____  __ __  ____   _____  ____  _____                      
                                                                              <___  \    /  _  \/  |  \/  _/  /   __\/    \/  _  \                     
                                                                               /  __/ _  |  _  <|  |  ||  |---|   __|\-  -/|  _  |                     
                                                                              <_____|<_> \__|\_/\_____/\_____/\_____/ |__| \__|__/                     
                                                                                                                                                       
                                                                               _____      _____  ____   _____  ____  _____                             
                                                                              /  _  \    /  ___>/  _/  /  _  \/    \/  ___>                            
                                                                              >-<_  < _  |___  ||  |---|  |  |\-  -/|___  |                            
                                                                              \_____/<_> <_____/\_____/\_____/ |__| <_____/                            
                                                                                                                                                       
                                                                               __ __      _____  __  __  ___  ____                                     
                                                                              /  |  \    /   __\/  \/  \/___\/    \                                    
                                                                              \_    | _  |   __|>-    -<|   |\-  -/                                    
                                                                                \___/<_> \_____/\__/\__/\___/ |__|       
                                                 
"""




nr_num = (0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26)

nr = [fg(46) +  "0" + fg.rs, fg(160) +  "32" + fg.rs, fg(16) + "15" + fg.rs, fg(160) +  "19" + fg.rs, fg(16) +  "4" + fg.rs, fg(160) +  "21" + fg.rs, fg(16) +  "2" + fg.rs, fg(160) +  "25" + fg.rs, fg(16) +  "17" + fg.rs, fg(160) +  "34" + fg.rs, fg(16) +  "6" + fg.rs, fg(160) +  "27" + fg.rs, fg(16) +  "13" + fg.rs, fg(160) +  "36" + fg.rs, fg(16) +  "11" + fg.rs, fg(160) +  "30" + fg.rs, fg(16) +  "8" + fg.rs, fg(160) +  "23" + fg.rs, fg(16) +  "10" + fg.rs, fg(160) +  "5" + fg.rs, fg(16) +  "24" + fg.rs, fg(160) +  "16" + fg.rs, fg(16) +  "33" + fg.rs, fg(160) +  "1" + fg.rs, fg(16) +  "20" + fg.rs, fg(160) +  "14" + fg.rs, fg(16) +  "31" + fg.rs, fg(160) +  "9" + fg.rs, fg(16) +  "22" + fg.rs, fg(160) +  "18" + fg.rs, fg(16) +  "29" + fg.rs, fg(160) +  "7" + fg.rs, fg(16) +  "28" + fg.rs, fg(160) +  "12" + fg.rs, fg(16) +  "35" + fg.rs, fg(160) +  "3" + fg.rs, fg(16) +  "26" + fg.rs]


#Cambiar los colores, o poner un espacio a cada lado del número para ver si así no aparece la bola en el tablero.
nt = [fg(45) +  "0" + fg.rs, fg(160) +  " 1 " + fg.rs, fg(16) + " 2 " + fg.rs, fg(160) +  " 3 " + fg.rs, fg(16) +  " 4 " + fg.rs, fg(160) +  " 5 " + fg.rs, fg(16) +  " 6 " + fg.rs, fg(160) +  " 7 " + fg.rs, fg(16) +  " 8 " + fg.rs, fg(160) +  " 9 " + fg.rs, fg(16) +  " 10 " + fg.rs, fg(16) +  " 11 " + fg.rs, fg(160) +  " 12 " + fg.rs, fg(160) +  " 13 " + fg.rs, fg(16) +  " 14 " + fg.rs, fg(16) +  " 15 " + fg.rs, fg(160) +  " 16 " + fg.rs, fg(16) +  " 17 " + fg.rs, fg(160) +  " 18 " + fg.rs, fg(160) +  " 19 " + fg.rs, fg(16) +  " 20 " + fg.rs, fg(160) +  " 21 " + fg.rs, fg(16) +  " 22 " + fg.rs, fg(160) +  " 23 " + fg.rs, fg(16) +  " 24 " + fg.rs, fg(160) +  " 25 " + fg.rs, fg(16) +  " 26 " + fg.rs, fg(160) +  " 27 " + fg.rs, fg(16) +  " 28 " + fg.rs, fg(16) +  " 29 " + fg.rs, fg(160) +  " 30 " + fg.rs, fg(16) +  " 31 " + fg.rs, fg(160) +  " 32 " + fg.rs, fg(16) +  " 33 " + fg.rs, fg(160) +  " 34 " + fg.rs, fg(16) +  " 35 " + fg.rs, fg(160) +  " 36 " + fg.rs,]






ruleta = f"""





                                                                                                                                            *$%,'"++-(
                                                                                                                                      (,%,(#)&"("%#!'/%*.*)&
                                                                                                                                %%%&"&'$#'*#/,)$-,/,$/'..*+/*%--#)
                                                                                                                              &.#'''&.(,%)""$'-/.&.".(+)$##,)%.*))'$
                                                                                                                            )-.+,#*'*./&+)"$#,,$+')*%*.")"$(%-)&-$/(-&
                                                                                                                          $(%#/)'*-!%)."#'{bg(137)}               {bg.rs}*%..&**,*.!%.+/'
                                                                                                                        ('&!"%!-$/#,*/{bg(137)}     {nr[36]}   {nr[0]}   {nr[1]}       {bg.rs}!.-&.)+!#!."/!
                                                                                                                      *+#/!)&$'+-${bg(137)}     {nr[35]}                 {nr[2]}     {bg.rs}&$//)$*/.#(* 
                                                                                                                    .$-+&'+).'!%{bg(137)}   {nr[34]}     {bg.rs}.'/+,-&#&!%,,%{bg(137)}     {nr[3]}   {bg.rs}($$'),-,&*!'                                                               
                                                                                                                    '*"#!/(.&({bg(137)}   {nr[33]}   {bg.rs}/"$%!'%%'+$+$/&-/!(+/!{bg(137)}   {nr[4]}   {bg.rs}%".%).%&//                                                                
                                                                                                                   $+''.)/&.#{bg(137)}      {bg.rs}**""**              )&/(*.{bg(137)}   {nr[5]}  {bg.rs}/,-%-*(,'&                                                               
                                                                                                                  +&*//##+.&{bg(137)}  {nr[32]}  {bg.rs},'&*&$                 ,+$$)-{bg(137)}   {nr[6]}   {bg.rs}$)%$#))!..                                                             
                                                                                                                  /'"#!$%.'{bg(137)}  {nr[31]}   {bg.rs}+#/)  (&              -.   ".--{bg(137)}   {nr[7]}  {bg.rs}&(/+'#,)%*                                                            
  {bg(22)}                                                                                               {bg.rs}                 '$.#-,//{bg(137)}  {nr[30]}  {bg.rs}$&'!      &+          "#     !/,'{bg(137)}      {bg.rs},-+&/$#,       
  {bg(22)}       ____________________________________________________________________________________    {bg.rs}               %'%+)&,,$'{bg(137)}     {bg.rs}".$(        .!      (-        +$'"{bg(137)}   {nr[8]}  {bg.rs}/(&'.*,(&*
  {bg(22)}      /  |     |     |     |     |     |     |     |     |     |     |     |     |         |   {bg.rs}               !#/%"/.-+){bg(137)} {nr[29]}  {bg.rs}$+,.          "&  .-          +($#{bg(137)}   {nr[9]}  {bg.rs})'.#!&"(./
  {bg(22)}     /   | {nt[3]} | {nt[6]} | {nt[9]} |{nt[12]} |{nt[15]} |{nt[18]} |{nt[21]} |{nt[24]} |{nt[27]} |{nt[30]} |{nt[33]} |{nt[36]} |   2to1  |   {bg.rs}                %&$"%%/).${bg(137)}     {bg.rs}-%"#            &%            $%'${bg(137)}       {bg.rs},#"$,(-#$.
  {bg(22)}    /    |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|   {bg.rs}                !$"$#*(#*){bg(137)} {nr[28]}  {bg.rs}+*&#          &*  $#          ###&{bg(137)}   {nr[10]}   {bg.rs}*'$/#,.)(.
  {bg(22)}   /     |     |     |     |     |     |     |     |     |     |     |     |     |         |   {bg.rs}                "$(*-'.*!({bg(137)}  {nr[27]}   {bg.rs}$""/        ),      %,        $/&({bg(137)}  {nr[11]}  {bg.rs}%*&$$)'-,&
  {bg(22)}  |   0  | {nt[2]} | {nt[5]} | {nt[8]} |{nt[11]} |{nt[14]} |{nt[17]} |{nt[20]} |{nt[23]} |{nt[26]} |{nt[29]} |{nt[32]} |{nt[35]} |   2to1  |   {bg.rs}                  /,#-$-**{bg(137)}  {nr[26]}  {bg.rs}+**-      %$          $-      (.%,{bg(137)}      {bg.rs}%$(%*)+' 
  {bg(22)}   \     |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|   {bg.rs}                  #*,**,&(%*{bg(137)}  {nr[25]}  {bg.rs}/"*"  &/              #-  '&##{bg(137)}   {nr[12]} {bg.rs},./+'$&,&( 
  {bg(22)}    \    |     |     |     |     |     |     |     |     |     |     |     |     |         |   {bg.rs}                  &!!&*--*+%{bg(137)}       {bg.rs}#-.)&                  !"#/%-{bg(137)}  {nr[13]}  {bg.rs}',".&-#!+* 
  {bg(22)}     \   | {nt[1]} | {nt[4]} | {nt[7]} |{nt[10]} |{nt[13]} |{nt[16]} |{nt[19]} |{nt[22]} |{nt[25]} |{nt[28]} |{nt[31]} |{nt[34]} |   2to1  |   {bg.rs}                    '$'"!"*"$"{bg(137)}  {nr[24]}  {bg.rs}!.)(,"              .,&,.){bg(137)}  {nr[14]}  {bg.rs}-+)$//$/*+                                                              
  {bg(22)}      \__|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|   {bg.rs}                    '/#&"+%%-"{bg(137)}   {nr[23]}   {bg.rs}',+*,&&)/!**-$,$/(*!+'{bg(137)}   {nr[15]}   {bg.rs}.!#-$'..$(                                                               
  {bg(22)}         |                       |                       |                       |             {bg.rs}                    -#&%!-%),"--{bg(137)}   {nr[22]}     {bg.rs}--+#-,$!#-#$/+{bg(137)}    {nr[16]}    {bg.rs}+/'#*#*#*+./                                                               
  {bg(22)}         |        1st 12         |        2nd 12         |        3rd 12         |             {bg.rs}                      ()$"**!$//'/{bg(137)}    {nr[21]}                {nr[17]}      {bg.rs}+"+(+/,)%)*"                                                                
  {bg(22)}         |_______________________|_______________________|_______________________|             {bg.rs}                        "+#'.$'-!*&"&${bg(137)}     {nr[20]}   {nr[19]}   {nr[18]}      {bg.rs})/!..,(-&.*/#(  
  {bg(22)}         |           |           |           |           |           |           |             {bg.rs}                          )-#%/#!!!.$..#)*{bg(137)}              {bg.rs}$'/%-/+#+)%.-*'. 
  {bg(22)}         |   MANQUE  |   EVEN    |    RED    |   BLACK   |    ODD    |   PASSE   |             {bg.rs}                            /'#-+.%#$),)$/**%%&++%#,)"(+/,&((-($*'"+'*   
  {bg(22)}         |___________|___________|___________|___________|___________|___________|             {bg.rs}                              *!**!+,#&-&-%"&&..,*/(&'!/&##-/&*+%%," 
                                                                                                                                /."($&$'!!))/&$#%))"/*&&)!"'$%/,+- 
                                                                                                                                      (+$.-)%#*#!$.)*###/*&(
                                                                                                                                            #"*'"*#+(! 


           


           
"""


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





# VARIABLES GENERALES DEL CASINO

deposito = 500
enpartida = 200
apuesta = 0
win = False
lose = False
opc_casino = 0


# VARIABLES BLACKJACK

blackjack = False
hit = "s"
salir = False
seguir = "s"
dividir = "n"
sumador_c = 0
sumador_j = 0
finish = False

mano_j = []
mano_c = []
valores_extraidos_j = []
valores_extraidos_c = []
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

for palo in palos:
    for valor in valores:
        baraja.append((valor, palo))




# VARIABLES RULETA

bola = fg(15) + "●" + fg.rs

rojo = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
columna1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
columna2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
columna3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]





# FUNCIONES GENERALES DEL CASINO

def centrado(cadena):
    cadena_cent = cadena.center(260)
    print(cadena_cent)



def comprueba_moroso(tipo_apuesta, interfaz, mensaje): 
    if tipo_apuesta != int():
        tipo_apuesta = esdigito(tipo_apuesta, interfaz, mensaje)

    
    while (apuesta + tipo_apuesta) > enpartida:
        os.system("cls")
        print(ruleta)
        print("Lo siento pero tienes que introducir un número de monedas menor que el que tienes en partida.")
        print("\n", mensaje)
        tipo_apuesta = input("--> ")
        tipo_apuesta = esdigito(tipo_apuesta, interfaz, mensaje)
        
    return tipo_apuesta


def esdigito(comprobante, interfaz, mensaje):
    while not comprobante or not comprobante.isdigit():
        os.system("cls")
        print(interfaz)
        input("\nLo siento, esta opción solamente contempla números.\nVuelve a intentarlo, para ello pulsa Enter.")
        print("\n", mensaje)
        comprobante = input("--> ")

    return int(comprobante)


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
    

    
def vuelta_al_deposito():

    global enpartida
    global deposito

    while enpartida != 0:

        os.system("cls")
    
        enpartida = enpartida - 1
        deposito = deposito + 1

        centrado(f"Deposito: {deposito}      En partida: {enpartida}")

        time.sleep(0.01)






# FUNCIONES BLACKJACK


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
        centrado("YOU WIN")
        input()
        win = True


    elif sumador == sumador_c:
        centrado("Empate")
        input()

        
    else:
        centrado("YOU LOSE")
        input()
        lose = True



def black_jack(valores_extraidos, sumador):

    global blackjack

    if (valores_extraidos[0][0] == "A" and valores_extraidos[1][0] in valores[9:]) or (valores_extraidos[1][0] == "A" and valores_extraidos[0][0] in valores[9:]):

        blackjack = True
        sumador = 21
        
    
    return sumador










# FUNCIONES RULETA

def gira_rulet():

    if nr_num[contador] < 10:
      ruleta_anim = ruleta.replace(f"{nr[contador]}", f"{bola}")

    else:
       ruleta_anim = ruleta.replace(f"{nr[contador]}", f"{bola} ")

    print(ruleta_anim)  




# FUNCIONES SLOT


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
            a = random.randint(70, 110)
        while b % 6 != 0:
            b = random.randint(60, 90)
        while c % 6 != 0:
            c = random.randint(70, 100)

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
    os.system("cls")
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


















# ALGORITMO PRINCIPAL


while opc_casino != "4":
    os.system("cls")

    print(casino_intr)

    opc_casino = input("¿A qué juego quieres jugar?: ")
    if opc_casino == "4":
        sys.exit()

    os.system("cls")
    print(casino_intr)

    if opc_casino != "3":
        print("¿Con cuanto dinero quieres entrar a jugar?")
        print(f"Ahora mismo tienes {deposito}")
        enpartida = input("-->")
        enpartida = esdigito(enpartida, casino_intr, f"¿Con cuanto dinero quieres entrar a jugar?\nAhora mismo tienes {deposito}")


    while enpartida > deposito:
        os.system("cls")
        print(casino_intr)
        print("¿Con cuanto dinero quieres entrar a jugar?")
        print(f"Ahora mismo tienes {deposito}")
        enpartida = input("-->")
        enpartida = esdigito(enpartida, casino_intr, f"¿Con cuanto dinero quieres entrar a jugar?\nAhora mismo tienes {deposito}")

        if enpartida > deposito:
            print("Lo siento, pero las monedas con las que ingreses a la partida tiene que ser menor que el que tienes en el depósito.")
            input("Pulsa Enter para continuar")


    deposito = deposito - enpartida


# BALCKJACK

    if opc_casino == "1":

        salir = False
        finish = False
        seguir = "s"
       
            
        while salir == False:

            os.system("cls")


            if finish == True:

                print(mesa)
                seguir = input("¿Quieres jugar otra partida? (s/n): ").lower()        
                os.system("cls")


            if seguir == "s":

                #Si da tiempo poner la función comprobar 
                print(mesa)
                print("\n")
                apuesta = input("¿Cuánto quieres apostar?: ")
                apuesta = esdigito(apuesta, mesa, "¿Cuánto quieres apostar?: ")                
                while apuesta > enpartida:
                    print("\nLo siento pero la apuesta tiene que ser menor que las monedas que tengas en partida")
                    input("Pulsa Enter para continuar")
                    os.system("cls")
                    print(mesa)
                    print("\n")
                    apuesta = input("¿Cuánto quieres apostar?: ")
                    apuesta = esdigito(apuesta, mesa, "¿Cuánto quieres apostar?: ") 


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
                vuelta_al_deposito()


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




# RULETA

    if opc_casino == "2":

        finish = "s"

        while finish == "s":

            dict_apuesta_num = {}
            dict_apuesta_docena = {"Primera docena" : False, "Segunda docena" : False, "Tercera docena" : False}
            dict_apuesta_colum = {"Columna 1" : False, "Columna 2" : False, "Columna 3" : False,}
            dict_apuesta_color = {"Rojo" : False, "Negro" : False}
            dict_apuesta_par = {"Pares" : False, "Impares" : False}
            dict_apuesta_bajo = {"Alto" : False, "Bajo" : False}
            menu_rul = "0"
            apuesta = 0
            tiempo = 0.001
            rul_opt = int()
            tiempo_rulet = random.randint(300, 400)
            contador = 0


            # HAGAN SUS APUESTAS

            while menu_rul != "7":
                os.system("cls")

                print(ruleta)


                menu_ruleta = """¿A qué quieres jugar?\n
            1. Número
            2. Docenas 
            3. Columnas 
            4. Color
            5. Par o impar
            6. Bajo o alto 
            7. Comenzar partida
                """

                print(menu_ruleta)
                menu_rul = input("--> ")


                # Menú de cada tipo de apuesta

                match menu_rul:


                    case "1":
                        while rul_opt != 777:
                            os.system("cls")
                            print(ruleta)
                            print("Introduce un número: ")
                            print("Para salir introduce '777'")
                            rul_opt = input("--> ")
                            rul_opt = esdigito(rul_opt, ruleta, "Introduce un número: \nPara salir introduce '777'")

                            if rul_opt < 37:
                                dict_apuesta_num[rul_opt] = input(f"Introduce la apuesta para el número {rul_opt}: ")
                                dict_apuesta_num[rul_opt] = comprueba_moroso(dict_apuesta_num[rul_opt], ruleta, f"Introduce la apuesta para el número {rul_opt}: ")

                                apuesta += dict_apuesta_num[rul_opt]

                            else:
                                if rul_opt != 777:
                                    print("Esta opción no está contemplada.")
                                    input("Pulsa Enter para continuar")




                            

                    case "2":
                        os.system("cls")
                        print(ruleta)
                        print("""¿A qué docena quieres jugar?:\n
            1. Primera docena (1-12)
            2. Segunda docena (13-24)
            3. Tercera docena (25-36)\n""")
                        
                        rul_opt = input("--> ")
                        apuesta_docena = input("\nIntroduce la apuesta para la docena: ")
                        apuesta_docena = comprueba_moroso(apuesta_docena, ruleta, "\nIntroduce la apuesta para la docena: ")

                        match rul_opt:
                            case "1":
                                dict_apuesta_docena["Primera docena"] = apuesta_docena
                            case "2":
                                dict_apuesta_docena["Segunda docena"] = apuesta_docena
                            case "3":
                                dict_apuesta_docena["Tercera docena"] = apuesta_docena
                            
                        apuesta += apuesta_docena
                        


                    case "3":
                        os.system("cls")
                        print(ruleta)
                        print("""¿A qué columna quieres jugar?:\n
            1. Primer columna
            2. Segunda columna
            3. Tercera columna \n""")
                        
                        rul_opt = input("--> ")
                        apuesta_columna = input("\nIntroduce la apuesta para la columna: ")
                        apuesta_columna = comprueba_moroso(apuesta_columna, ruleta, "\nIntroduce la apuesta para la columna: ")

                        match rul_opt:
                            case "1":
                                dict_apuesta_colum["Columna 1"] = apuesta_columna
                            case "2":
                                dict_apuesta_colum["Columna 2"] = apuesta_columna
                            case "3":
                                dict_apuesta_colum["Columna 3"] = apuesta_columna

                        apuesta += apuesta_columna



                    case "4":
                        os.system("cls")
                        print(ruleta)

                        print("""¿A qué color quieres jugar?:\n
            1. Negro
            2. Rojo \n""")
                        
                        rul_opt = input(" --> ").lower()
                        apuesta_color = input("\nIntroduce la apuesta para el color: ")
                        apuesta_color = comprueba_moroso(apuesta_color, ruleta, "Introduce la apuesta para el color: ")

                        match rul_opt:
                            case "1":
                                dict_apuesta_color["Negro"] = apuesta_color
                            case "2":
                                dict_apuesta_color["Rojo"] = apuesta_color

                        apuesta += apuesta_color



                    case "5":
                        os.system("cls")
                        print(ruleta)
                        print("""¿A qué quieres jugar, pares o impares?:\n
            1. Pares
            2. Impares \n""")
                        
                        rul_opt = input(" --> ").lower()
                        apuesta_par = input("\nIntroduce la apuesta para pares / impares: ")
                        apuesta_par = comprueba_moroso(apuesta_par, ruleta, "Introduce la apuesta para pares / imprares: ")

                        match rul_opt:
                            case "1":
                                dict_apuesta_par["Pares"] = apuesta_par
                            case "2":
                                dict_apuesta_par["Impares"] = apuesta_par

                        apuesta += apuesta_par



                    case "6":
                        os.system("cls")
                        print(ruleta)
                        print("""¿A qué quieres jugar, alto o bajo?:\n
            1. Alto
            2. Bajo \n""")
                        
                        rul_opt = input(" --> ").lower()
                        apuesta_bajo = input("\nIntroduce la apuesta para alto / bajo: ")
                        apuesta_bajo = comprueba_moroso(apuesta_bajo, ruleta, "Introduce la apuesta para alto / bajo: ")

                        match rul_opt:
                            case "1":
                                dict_apuesta_bajo["Alto"] = apuesta_bajo
                            case "2":
                                dict_apuesta_bajo["Bajo"] = apuesta_bajo

                        apuesta += apuesta_bajo


            apuesta = apuesta * -1


            # Animación de la ruleta girando

            for i in range(tiempo_rulet):

                contador += 1
                
                if contador > 36:
                    contador = 0 

                time.sleep(tiempo)



                if i < tiempo_rulet / 1.5:
                    continue
                    

                elif i > tiempo_rulet / 1.5 and i < (tiempo_rulet * 94) / 100 :
                    tiempo = tiempo ** (99/100)


                else:
                    tiempo = tiempo ** (19/20)


                os.system("cls")
                gira_rulet()



            print(f"Ha salido el número ", Back.WHITE + nr[contador] + Back.RESET)   
                    


            num_aleatorio = nr_num[contador]


            # Se evalúan y de calcula el resultado de las apuestas realizadas

            for numero, dinero in dict_apuesta_num.items():
                if num_aleatorio == numero:
                    apuesta = apuesta + (dinero * 36)


            #comprobamos que el número que ha salido perteneve a la primera docena
            if num_aleatorio < 13:
                #Nos aseguramos que el usuario a apostado a la primera docena
                if dict_apuesta_docena["Primera docena"] != False:
                    #Añadimos los beneficios correspondientes a la apuesta
                    apuesta = apuesta + (apuesta_docena * 3)
            elif num_aleatorio < 25:
                if dict_apuesta_docena["Segunda docena"] != False:
                    apuesta = apuesta + (apuesta_docena * 3)
            elif num_aleatorio < 37:
                if dict_apuesta_docena["Tercera docena"] != False:
                    apuesta = apuesta + (apuesta_docena * 3)

            #Hay que implementar las apuestas de las diferentes tipos de apuesta

            if num_aleatorio in columna1 and dict_apuesta_colum["Columna 1"] != False:
                apuesta = apuesta + (apuesta_columna * 3)
            if num_aleatorio in columna2 and dict_apuesta_colum["Columna 2"] != False:
                apuesta = apuesta + (apuesta_columna * 3)
            if num_aleatorio in columna3 and dict_apuesta_colum["Columna 3"] != False:
                apuesta = apuesta + (apuesta_columna * 3)


            if num_aleatorio in rojo:
                if dict_apuesta_color["Rojo"] != False:
                    apuesta = apuesta + (apuesta_color * 2)
            else:
                if dict_apuesta_color["Negro"] != False:
                    apuesta = apuesta + (apuesta_color * 2)


            if num_aleatorio % 2 == 0:
                if dict_apuesta_par["Pares"] != False:
                    apuesta = apuesta + (apuesta_par * 2)
            else:
                if dict_apuesta_par["Impares"] != False:
                    apuesta = apuesta + (apuesta_par * 2)
            
            if num_aleatorio < 19:
                if dict_apuesta_bajo["Bajo"] != False:
                    apuesta = apuesta + (apuesta_bajo * 2)

            else:
                if dict_apuesta_bajo["Alto"] == True:
                    apuesta = apuesta + (apuesta_bajo * 2)

            


            if apuesta > 0:
                print("Tus beneficios son ", Fore.GREEN + str(apuesta) + Fore.RESET)
                input()
                win = True
            else:
                print("Tus beneficios son ", Fore.RED + str(apuesta) + Fore.RESET)
                input()                
                lose = True
                if apuesta < 0:
                    apuesta = apuesta * -1

            imprime_resultado()
                

            finish = input("¿Quieres jugar otra partida? (S/N): ").lower()

            if finish != "s":
                vuelta_al_deposito()

            





# SLOT

    if opc_casino == "3":

        machine = Slots()

        welcome()
        os.system("cls")
        print("\n\n\n")
        centrado("Introduce cuánto dinero quieres tener en partida:")
        enpartida = input("\t\t\t\t\t\t\t\t--> ")
        enpartida = esdigito(enpartida, "", "Introduce cuánto dinero quieres tener en partida:")
        os.system("cls")
        print("\n\n\n")
        centrado("Introduce la apuesta con la quieres jugar: ")
        print("\n")
        centrado("Recuerda que en este modelo de juego la apuesta es invariable")
        centrado("En el caso de que quieras modificar la apuesta tendrás que salir ")
        centrado("al menú principal e introducirla de nuevo.")
        print("\n")
        apuesta = input("\t\t\t\t\t\t\t\t--> ")
        apuesta = esdigito(apuesta, "Introduce la apuesta con la quieres jugar: \nRecuerda que en este modelo de juego la apuesta es invariable\nEn el caso de que quieras modificar la apuesta tendrás que salir", "")
        deposito = deposito - enpartida
        memo_apuesta = apuesta
        finish = "s"



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

                if finish != "s":
                    vuelta_al_deposito()

        



