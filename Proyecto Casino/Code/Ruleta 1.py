import random
import os
import time
from sty import fg, bg
from colorama import init, Fore, Back, Style


init()

os.system("cls")


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







def centrado(cadena):
    cadena_cent = cadena.center(260)
    print(cadena_cent)


def gira_rulet():

    if nr_num[contador] < 10:
      ruleta_anim = ruleta.replace(f"{nr[contador]}", f"{bola}")

    else:
       ruleta_anim = ruleta.replace(f"{nr[contador]}", f"{bola} ")

    print(ruleta_anim)  




finish = "s"
bola = fg(15) + "●" + fg.rs



rojo = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
columna1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
columna2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
columna3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]




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
                    rul_opt = int(input("--> "))

                    if rul_opt < 37:
                        dict_apuesta_num[rul_opt] = int(input(f"Introduce la apuesta para el número {rul_opt}: "))
                        apuesta -= dict_apuesta_num[rul_opt]

                    else:
                        if rul_opt != 777:
                            print("Esta opción no está contemplada.")
                            input("Pulsa Enter para continuar")

                print(dict_apuesta_num)


                    

            case "2":
                os.system("cls")
                print(ruleta)
                print("""¿A qué docena quieres jugar?:\n
    1. Primera docena (1-12)
    2. Segunda docena (13-24)
    3. Tercera docena (25-36)\n""")
                
                rul_opt = input("--> ")
                apuesta_docena = int(input("\nIntroduce la apuesta para la docena: "))

                match rul_opt:
                    case "1":
                        dict_apuesta_docena["Primera docena"] = apuesta_docena
                    case "2":
                        dict_apuesta_docena["Segunda docena"] = apuesta_docena
                    case "3":
                        dict_apuesta_docena["Tercera docena"] = apuesta_docena
                    
                apuesta -= apuesta_docena
                


            case "3":
                os.system("cls")
                print(ruleta)
                print("""¿A qué columna quieres jugar?:\n
    1. Primer columna
    2. Segunda columna
    3. Tercera columna \n""")
                
                rul_opt = input("--> ")
                apuesta_columna = int(input("\nIntroduce la apuesta para la columna: "))

                match rul_opt:
                    case "1":
                        dict_apuesta_colum["Columna 1"] = apuesta_columna
                    case "2":
                        dict_apuesta_colum["Columna 2"] = apuesta_columna
                    case "3":
                        dict_apuesta_colum["Columna 3"] = apuesta_columna

                apuesta -= apuesta_columna



            case "4":
                os.system("cls")
                print(ruleta)

                print("""¿A qué color quieres jugar?:\n
    1. Negro
    2. Rojo \n""")
                
                rul_opt = input(" --> ").lower()
                apuesta_color = int(input("\nIntroduce la apuesta para el color: "))

                match rul_opt:
                    case "1":
                        dict_apuesta_color["Negro"] = apuesta_color
                    case "2":
                        dict_apuesta_color["Rojo"] = apuesta_color

                apuesta -= apuesta_color



            case "5":
                os.system("cls")
                print(ruleta)
                print("""¿A qué quieres jugar, pares o impares?:\n
    1. Pares
    2. Impares \n""")
                
                rul_opt = input(" --> ").lower()
                apuesta_par = int(input("\nIntroduce la apuesta para pares / impares: "))

                match rul_opt:
                    case "1":
                        dict_apuesta_par["Pares"] = apuesta_par
                    case "2":
                        dict_apuesta_par["Impares"] = apuesta_par

                apuesta -= apuesta_par



            case "6":
                os.system("cls")
                print(ruleta)
                print("""¿A qué quieres jugar, alto o bajo?:\n
    1. Alto
    2. Bajo \n""")
                
                rul_opt = input(" --> ").lower()
                apuesta_bajo = int(input("\nIntroduce la apuesta para alto / bajo: "))

                match rul_opt:
                    case "1":
                        dict_apuesta_bajo["Alto"] = apuesta_bajo
                    case "2":
                        dict_apuesta_bajo["Bajo"] = apuesta_bajo

                apuesta -= apuesta_bajo


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
            print(apuesta)

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
        

    finish = input("¿Quieres jugar otra partida? (S/N): ").lower()

    




#Comprobar que lo de los diccionarios, quizas con meterlo en variables basta
