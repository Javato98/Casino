import random
import os
import time
from sty import fg, bg
from colorama import init, Fore, Back, Style

init()

os.system("cls")



ruleta = f"""
  ______________________________________________________________________________________________
 /           _________________________________________________________________________________  \ 
/           |     |     |     |     |     |     |     |     |     |     |     |     |         |  \\
|  1st 12   |  3  |  6  |  9  | 12  | 15  | 18  | 21  | 24  | 27  | 30  | 33  | 36  |   2to1  |  |
|           |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|  |
|           |     |     |     |     |     |     |     |     |     |     |     |     |         |  |
|  2nd 12   |  2  |  5  |  8  | 11  | 14  | 17  | 20  | 23  | 26  | 29  | 32  | 35  |   2to1  |  |
|           |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|  |
|           |     |     |     |     |     |     |     |     |     |     |     |     |         |  |
|  3rd 12   |  1  |  4  |  7  | 10  | 13  | 16  | 19  | 22  | 25  | 28  | 31  | 34  |   2to1  |  |
\           |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|  /
 \\_____________________________________________________________________________________________/

"""

ruleta2 = f"""





                                                                                                                                            *$%,'"++-(
                                                                                                                                      (,%,(#)&"("%#!'/%*.*)&
                                                                                                                                %%%&"&'$#'*#/,)$-,/,$/'..*+/*%--#)
                                                                                                                              &.#'''&.(,%)""$'-/.&.".(+)$##,)%.*))'$
                                                                                                                            )-.+,#*'*./&+)"$#,,$+')*%*.")"$(%-)&-$/(-&
                                                                                                                          $(%#/)'*-!%)."#'              *%..&**,*.!%.+/'
                                                                                                                        ('&!"%!-$/#,*/                      !.-&.)+!#!."/!
                                                                                                                      *+#/!)&$'+-$                              &$//)$*/.#(* 
                                                                                                                    .$-+&'+).'!%          .'/+,-&#&!%,,%          ($$'),-,&*!'
                                                                                                                    '*"#!/(.&(        /"$%!'%%'+$+$/&-/!(+/!        %".%).%&//
                                                                                                                    $+''.)/&.#      **""**              )&/(*.      /,-%-*(,'&
                                                                                                                  +&*//##+.&      ,'&*&$                  ,+$$)-      $)%$#))!..
                                                                                                                  /'"#!$%.'&      +#/)  (&              -.  ".--      &(/+'#,)%*
                                                                                                                  '$.#-,//      $&'!      &+          "#      !/,'      ,-+&/$#,        
         ____________________________________________________________________________________                   %'%+)&,,$'      ".$(        .!      (-        +$'"      /(&'.*,(&*
        /  |     |     |     |     |     |     |     |     |     |     |     |     |         |                  !#/%"/.-+)      $+,.          "&  .-          +($#      )'.#!&"(./
       /   |  3  |  6  |  9  | 12  | 15  | 18  | 21  | 24  | 27  | 30  | 33  | 36  |   2to1  |                  %&$"%%/).$      -%"#            &%            $%'$      ,#"$,(-#$.
      /    |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|                  !$"$#*(#*)      +*&#          &*  $#          ###&      *'$/#,.)(.
     /     |     |     |     |     |     |     |     |     |     |     |     |     |         |                  "$(*-'.*!(      $""/        ),      %,        $/&(      %*&$$)'-,&
    |   0  |  2  |  5  |  8  | 11  | 14  | 17  | 20  | 23  | 26  | 29  | 32  | 35  |   2to1  |                    /,#-$-**      +**-      %$          $-      (.%,      %$(%*)+' 
     \     |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|                    #*,**,&(%*      /"*"  &/              #-  '&##      ,./+'$&,&( 
      \    |     |     |     |     |     |     |     |     |     |     |     |     |         |                    &!!&*--*+%      /#-.)&                  !"#/%-      ',".&-#!+* 
       \   |  1  |  4  |  7  | 10  | 13  | 16  | 19  | 22  | 25  | 28  | 31  | 34  |   2to1  |                      '$'"!"*"$"      !.)(,"              .,&,.)      -+)$//$/*+ 
        \__|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|                      '/#&"+%%-"        ',+*,&&)/!**-$,$/(*!+'        .!#-$'..$( 
           |                       |                       |                       |                                -#&%!-%),"--          --+#-,$!#-#$/+          +/'#*#*#*+./ 
           |        1st 12         |        2nd 12         |        3rd 12         |                                  ()$"**!$//'/                              +"+(+/,)%)*" 
           |_______________________|_______________________|_______________________|                                    "+#'.$'-!*&"&$                      )/!..,(-&.*/#(  
           |           |           |           |           |           |           |                                      )-#%/#!!!.$..#)*              $'/%-/+#+)%.-*'. 
           |   MANQUE  |   EVEN    |    RED    |   BLACK   |    ODD    |   PASSE   |                                        /'#-+.%#$),)$/**%%&++%#,)"(+/,&((-($*'"+'*   
           |___________|___________|___________|___________|___________|___________|                                          *!**!+,#&-&-%"&&..,*/(&'!/&##-/&*+%%," 
                                                                                                                                /."($&$'!!))/&$#%))"/*&&)!"'$%/,+- 
                                                                                                                                      (+$.-)%#*#!$.)*###/*&(
                                                                                                                                            #"*'"*#+(! 


           


           







"""
nr = [fg(46) +  "0" + fg.rs, fg(160) +  "1" + fg.rs, fg(16) + "2" + fg.rs, fg(160) +  "3" + fg.rs, fg(16) +  "4" + fg.rs, fg(160) +  "5" + fg.rs, fg(16) +  "6" + fg.rs, fg(160) +  "7" + fg.rs, fg(16) +  "8" + fg.rs, fg(160) +  "9" + fg.rs, fg(16) +  "10" + fg.rs, fg(16) +  "11" + fg.rs, fg(160) +  "12" + fg.rs, fg(160) +  "13" + fg.rs, fg(160) +  "14" + fg.rs, fg(16) +  "15" + fg.rs, fg(160) +  "16" + fg.rs, fg(16) +  "17" + fg.rs, fg(160) +  "18" + fg.rs, fg(160) +  "19" + fg.rs, fg(16) +  "20" + fg.rs, fg(160) +  "21" + fg.rs, fg(16) +  "22" + fg.rs, fg(160) +  "23" + fg.rs, fg(16) +  "24" + fg.rs, fg(160) +  "25" + fg.rs, fg(16) +  "26" + fg.rs, fg(160) +  "27" + fg.rs, fg(16) +  "28" + fg.rs, fg(16) +  "29" + fg.rs, fg(160) +  "30" + fg.rs, fg(16) +  "31" + fg.rs, fg(160) +  "32" + fg.rs, fg(16) +  "33" + fg.rs, fg(160) +  "34" + fg.rs, fg(16) +  "35" + fg.rs, fg(160) +  "36" + fg.rs]

nt = list(nr)    

bola = fg(15) + "●" + fg.rs
print(bola)



ruleta3 = f"""





                                                                                                                                            *$%,'"++-(
                                                                                                                                      (,%,(#)&"("%#!'/%*.*)&
                                                                                                                                %%%&"&'$#'*#/,)$-,/,$/'..*+/*%--#)
                                                                                                                              &.#'''&.(,%)""$'-/.&.".(+)$##,)%.*))'$
                                                                                                                            )-.+,#*'*./&+)"$#,,$+')*%*.")"$(%-)&-$/(-&
                                                                                                                          $(%#/)'*-!%)."#'{bg(137)}               {bg.rs}*%..&**,*.!%.+/'
                                                                                                                        ('&!"%!-$/#,*/{bg(137)}     {nr[36]}   {nr[0]}   {nr[32]}       {bg.rs}!.-&.)+!#!."/!
                                                                                                                      *+#/!)&$'+-${bg(137)}     {nr[3]}                 {nr[15]}     {bg.rs}&$//)$*/.#(* 
                                                                                                                    .$-+&'+).'!%{bg(137)}   {nr[35]}     {bg.rs}.'/+,-&#&!%,,%{bg(137)}     {nr[19]}   {bg.rs}($$'),-,&*!'                                                                
                                                                                                                    '*"#!/(.&({bg(137)}   {nr[12]}   {bg.rs}/"$%!'%%'+$+$/&-/!(+/!{bg(137)}   {nr[4]}   {bg.rs}%".%).%&//                                                                
                                                                                                                   $+''.)/&.#{bg(137)}      {bg.rs}**""**              )&/(*.{bg(137)}   {nr[21]}  {bg.rs}/,-%-*(,'&                                                                
                                                                                                                  +&*//##+.&{bg(137)}  {nr[28]} {bg.rs},'&*&$                  ,+$$)-{bg(137)}  {nr[2]}   {bg.rs}$)%$#))!..                                                                
                                                                                                                  /'"#!$%.'{bg(137)}  {nr[7]}   {bg.rs}+#/)  (&              -.   ".--{bg(137)}   {nr[25]}  {bg.rs}&(/+'#,)%*                                                            
                                                                                                                  '$.#-,//{bg(137)}  {nr[29]}  {bg.rs}$&'!      &+          "#     !/,'{bg(137)}      {bg.rs},-+&/$#,       
         ____________________________________________________________________________________                   %'%+)&,,$'{bg(137)}     {bg.rs}".$(        .!      (-        +$'"{bg(137)}   {nr[17]}  {bg.rs}/(&'.*,(&*
        {bg(22)}/  |     |     |     |     |     |     |     |     |     |     |     |     |         |{bg.rs}                  !#/%"/.-+){bg(137)} {nr[18]}  {bg.rs}$+,.          "&  .-          +($#{bg(137)}   {nr[34]}  {bg.rs})'.#!&"(./
       {bg(22)}/   |  {nt[3]}  |  {nt[6]}  |  {nt[9]}  | {nt[12]}  | {nt[15]}  | {nt[18]}  | {nt[21]}  | {nt[24]}  | {nt[27]}  | {nt[30]}  | {nt[33]}  | {nt[36]}  |   2to1  |{bg.rs}                   %&$"%%/).${bg(137)}     {bg.rs}-%"#            &%            $%'${bg(137)}       {bg.rs},#"$,(-#$.
      {bg(22)}/    |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|{bg.rs}                   !$"$#*(#*){bg(137)} {nr[22]}  {bg.rs}+*&#          &*  $#          ###&{bg(137)}   {nr[6]}   {bg.rs}*'$/#,.)(.
     {bg(22)}/     |     |     |     |     |     |     |     |     |     |     |     |     |         |{bg.rs}                   "$(*-'.*!({bg(137)}  {nr[9]}   {bg.rs}$""/        ),      %,        $/&({bg(137)}  {nr[27]}  {bg.rs}%*&$$)'-,&
    {bg(22)}|   0  |  {nt[2]}  |  {nt[5]}  |  {nt[8]}  | {nt[11]}  | {nt[14]}  | {nt[17]}  | {nt[20]}  | {nt[23]}  | {nt[26]}  | {nt[29]}  | {nt[32]}  | {nt[35]}  |   2to1  |{bg.rs}                     /,#-$-**{bg(137)}  {nr[31]}  {bg.rs}+**-      %$          $-      (.%,{bg(137)}      {bg.rs}%$(%*)+' 
     {bg(22)}\     |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|{bg.rs}                     #*,**,&(%*{bg(137)}  {nr[14]}  {bg.rs}/"*"  &/              #-  '&##{bg(137)}   {nr[13]} {bg.rs},./+'$&,&( 
      {bg(22)}\    |     |     |     |     |     |     |     |     |     |     |     |     |         |{bg.rs}                     &!!&*--*+%{bg(137)}       {bg.rs}#-.)&                  !"#/%-{bg(137)}  {nr[36]}  {bg.rs}',".&-#!+* 
       {bg(22)}\   |  {nt[1]}  |  {nt[4]}  |  {nt[7]}  | {nt[10]}  | {nt[13]}  | {nt[16]}  | {nt[19]}  | {nt[22]}  | {nt[25]}  | {nt[28]}  | {nt[31]}  | {nt[34]}  |   2to1  |{bg.rs}                       '$'"!"*"$"{bg(137)}  {nr[20]}  {bg.rs}!.)(,"              .,&,.){bg(137)}  {nr[11]}  {bg.rs}-+)$//$/*+                                                              
        {bg(22)}\__|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|{bg.rs}                       '/#&"+%%-"{bg(137)}   {nr[1]}   {bg.rs}',+*,&&)/!**-$,$/(*!+'{bg(137)}   {nr[30]}   {bg.rs}.!#-$'..$(                                                               
           {bg(22)}|                       |                       |                       |{bg.rs}                                 -#&%!-%),"--{bg(137)}   {nr[33]}     {bg.rs}--+#-,$!#-#$/+{bg(137)}    {nr[8]}    {bg.rs}+/'#*#*#*+./                                                               
           {bg(22)}|        1st 12         |        2nd 12         |        3rd 12         |{bg.rs}                                   ()$"**!$//'/{bg(137)}    {nr[16]}                {nr[23]}      {bg.rs}+"+(+/,)%)*"                                                                
           {bg(22)}|_______________________|_______________________|_______________________|{bg.rs}                                     "+#'.$'-!*&"&${bg(137)}     {nr[24]}   {nr[5]}   {nr[10]}      {bg.rs})/!..,(-&.*/#(  
           {bg(22)}|           |           |           |           |           |           |{bg.rs}                                       )-#%/#!!!.$..#)*{bg(137)}              {bg.rs}$'/%-/+#+)%.-*'. 
           {bg(22)}|   MANQUE  |   EVEN    |    RED    |   BLACK   |    ODD    |   PASSE   |{bg.rs}                                         /'#-+.%#$),)$/**%%&++%#,)"(+/,&((-($*'"+'*   
           {bg(22)}|___________|___________|___________|___________|___________|___________|{bg.rs}                                           *!**!+,#&-&-%"&&..,*/(&'!/&##-/&*+%%," 
                                                                                                                                /."($&$'!!))/&$#%))"/*&&)!"'$%/,+- 
                                                                                                                                      (+$.-)%#*#!$.)*###/*&(
                                                                                                                                            #"*'"*#+(! 


           


           
"""



ruleta4 = f"""
  
         ____________________________________________________________________________________  
        /  |     |     |     |     |     |     |     |     |     |     |     |     |         |  
       /   |  {fg(160)}3{fg.rs}  |  {fg(16)}6{fg.rs}  |  {fg(160)}9{fg.rs}  | {fg(16)}12{fg.rs}  | {fg(160)}15{fg.rs}  | {fg(16)}18{fg.rs}  | {fg(160)}21{fg.rs}  | {fg(16)}24{fg.rs}  | {fg(160)}27{fg.rs}  | {fg(16)}30{fg.rs}  | {fg(160)}33{fg.rs}  | {fg(16)}36{fg.rs}  |   2to1  |  
      /    |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|  
     /     |     |     |     |     |     |     |     |     |     |     |     |     |         |  
    |   0  |  {fg(16)}2{fg.rs}  |  {fg(160)}5{fg.rs}  |  {fg(16)}8{fg.rs}  | {fg(160)}11{fg.rs}  | {fg(16)}14{fg.rs}  | {fg(160)}17{fg.rs}  | {fg(16)}20{fg.rs}  | {fg(160)}23{fg.rs}  | {fg(16)}26{fg.rs}  | {fg(160)}29{fg.rs}  | {fg(16)}32{fg.rs}  | {fg(160)}35{fg.rs}  |   2to1  |  
     \     |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|__f__|_________|  
      \    |     |     |     |     |     |     |     |     |     |     |     |     |         |  
       \   |  {fg(160)}1{fg.rs}  |  {fg(16)}4{fg.rs}  |  {fg(160)}7{fg.rs}  | {fg(16)}10{fg.rs}  | {fg(160)}13{fg.rs}  | {fg(16)}16{fg.rs}  | {fg(160)}19{fg.rs}  | {fg(16)}22{fg.rs}  | {fg(160)}25{fg.rs}  | {fg(16)}28{fg.rs}  | {fg(160)}31{fg.rs}  | {fg(16)}34{fg.rs}  |   2to1  |  
        \__|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|  
           |                       |                       |                       |
           |        1st 12         |        2nd 12         |        3rd 12         |
           |_______________________|_______________________|_______________________|
           |           |           |           |           |           |           |
           |   MANQUE  |   EVEN    |    {fg(160)}RED{fg.rs}    |   {fg(16)}BLACK{fg.rs}   |    ODD    |   PASSE   |
           |___________|___________|___________|___________|___________|___________|                   
"""





print(ruleta3)



    


input()



ruleta4 = f"""
  
         ____________________________________________________________________________________  
        /  |     |     |     |     |     |     |     |     |     |     |     |     |         |  
       /   |  {fg(160)}3{fg.rs}  |  {fg(16)}6{fg.rs}  |  {fg(160)}9{fg.rs}  | {fg(16)}12{fg.rs}  | {fg(160)}15{fg.rs}  | {fg(16)}18{fg.rs}  | {fg(160)}21{fg.rs}  | {fg(16)}24{fg.rs}  | {fg(160)}27{fg.rs}  | {fg(16)}30{fg.rs}  | {fg(160)}33{fg.rs}  | {fg(16)}36{fg.rs}  |   2to1  |  
      /    |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|  
     /     |     |     |     |     |     |     |     |     |     |     |     |     |         |  
    |   0  |  {fg(16)}2{fg.rs}  |  {fg(160)}5{fg.rs}  |  {fg(16)}8{fg.rs}  | {fg(160)}11{fg.rs}  | {fg(16)}14{fg.rs}  | {fg(160)}17{fg.rs}  | {fg(16)}20{fg.rs}  | {fg(160)}23{fg.rs}  | {fg(16)}26{fg.rs}  | {fg(160)}29{fg.rs}  | {fg(16)}32{fg.rs}  | {fg(160)}35{fg.rs}  |   2to1  |  
     \     |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|__f__|_________|  
      \    |     |     |     |     |     |     |     |     |     |     |     |     |         |  
       \   |  {fg(160)}1{fg.rs}  |  {fg(16)}4{fg.rs}  |  {fg(160)}7{fg.rs}  | {fg(16)}10{fg.rs}  | {fg(160)}13{fg.rs}  | {fg(16)}16{fg.rs}  | {fg(160)}19{fg.rs}  | {fg(16)}22{fg.rs}  | {fg(160)}25{fg.rs}  | {fg(16)}28{fg.rs}  | {fg(160)}31{fg.rs}  | {fg(16)}34{fg.rs}  |   2to1  |  
        \__|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|  
           |                       |                       |                       |
           |        1st 12         |        2nd 12         |        3rd 12         |
           |_______________________|_______________________|_______________________|
           |           |           |           |           |           |           |
           |   MANQUE  |   EVEN    |    {fg(160)}RED{fg.rs}    |   {fg(16)}BLACK{fg.rs}   |    ODD    |   PASSE   |
           |___________|___________|___________|___________|___________|___________|                   
"""


ruleta1 = f"""
  ______________________________________________________________________________________________
 /           _________________________________________________________________________________  \ 
/           |     |     |     |     |     |     |     |     |     |     |     |     |         |  \\
|  1st 12   |  3  |  6  |  9  | 12  | 15  | 18  | 21  | 24  | 27  | 30  | 33  | 36  |   2to1  |  |
|           |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|  |
|           |     |     |     |     |     |     |     |     |     |     |     |     |         |  |
|  2nd 12   |  2  |  5  |  8  | 11  | 14  | 17  | 20  | 23  | 26  | 29  | 32  | 35  |   2to1  |  |
|           |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|  |
|           |     |     |     |     |     |     |     |     |     |     |     |     |         |  |
|  3rd 12   |  1  |  4  |  7  | 10  | 13  | 16  | 19  | 22  | 25  | 28  | 31  | 34  |   2to1  |  |
\           |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|  /
 \\_____________________________________________________________________________________________/

"""

ruleta2 = f"""





                                                                                                                                            *$%,'"++-(
                                                                                                                                      (,%,(#)&"("%#!'/%*.*)&
                                                                                                                                %%%&"&'$#'*#/,)$-,/,$/'..*+/*%--#)
                                                                                                                              &.#'''&.(,%)""$'-/.&.".(+)$##,)%.*))'$
                                                                                                                            )-.+,#*'*./&+)"$#,,$+')*%*.")"$(%-)&-$/(-&
                                                                                                                          $(%#/)'*-!%)."#'              *%..&**,*.!%.+/'
                                                                                                                        ('&!"%!-$/#,*/                      !.-&.)+!#!."/!
                                                                                                                      *+#/!)&$'+-$                              &$//)$*/.#(* 
                                                                                                                    .$-+&'+).'!%          .'/+,-&#&!%,,%          ($$'),-,&*!'
                                                                                                                    '*"#!/(.&(        /"$%!'%%'+$+$/&-/!(+/!        %".%).%&//
                                                                                                                    $+''.)/&.#      **""**              )&/(*.      /,-%-*(,'&
                                                                                                                  +&*//##+.&      ,'&*&$                  ,+$$)-      $)%$#))!..
                                                                                                                  /'"#!$%.'&      +#/)  (&              -.  ".--      &(/+'#,)%*
                                                                                                                  '$.#-,//      $&'!      &+          "#      !/,'      ,-+&/$#,        
         ____________________________________________________________________________________                   %'%+)&,,$'      ".$(        .!      (-        +$'"      /(&'.*,(&*
        /  |     |     |     |     |     |     |     |     |     |     |     |     |         |                  !#/%"/.-+)      $+,.          "&  .-          +($#      )'.#!&"(./
       /   |  3  |  6  |  9  | 12  | 15  | 18  | 21  | 24  | 27  | 30  | 33  | 36  |   2to1  |                  %&$"%%/).$      -%"#            &%            $%'$      ,#"$,(-#$.
      /    |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|                  !$"$#*(#*)      +*&#          &*  $#          ###&      *'$/#,.)(.
     /     |     |     |     |     |     |     |     |     |     |     |     |     |         |                  "$(*-'.*!(      $""/        ),      %,        $/&(      %*&$$)'-,&
    |   0  |  2  |  5  |  8  | 11  | 14  | 17  | 20  | 23  | 26  | 29  | 32  | 35  |   2to1  |                    /,#-$-**      +**-      %$          $-      (.%,      %$(%*)+' 
     \     |_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|                    #*,**,&(%*      /"*"  &/              #-  '&##      ,./+'$&,&( 
      \    |     |     |     |     |     |     |     |     |     |     |     |     |         |                    &!!&*--*+%      /#-.)&                  !"#/%-      ',".&-#!+* 
       \   |  1  |  4  |  7  | 10  | 13  | 16  | 19  | 22  | 25  | 28  | 31  | 34  |   2to1  |                      '$'"!"*"$"      !.)(,"              .,&,.)      -+)$//$/*+ 
        \__|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_________|                      '/#&"+%%-"        ',+*,&&)/!**-$,$/(*!+'        .!#-$'..$( 
           |                       |                       |                       |                                -#&%!-%),"--          --+#-,$!#-#$/+          +/'#*#*#*+./ 
           |        1st 12         |        2nd 12         |        3rd 12         |                                  ()$"**!$//'/                              +"+(+/,)%)*" 
           |_______________________|_______________________|_______________________|                                    "+#'.$'-!*&"&$                      )/!..,(-&.*/#(  
           |           |           |           |           |           |           |                                      )-#%/#!!!.$..#)*              $'/%-/+#+)%.-*'. 
           |   MANQUE  |   EVEN    |    RED    |   BLACK   |    ODD    |   PASSE   |                                        /'#-+.%#$),)$/**%%&++%#,)"(+/,&((-($*'"+'*   
           |___________|___________|___________|___________|___________|___________|                                          *!**!+,#&-&-%"&&..,*/(&'!/&##-/&*+%%," 
                                                                                                                                /."($&$'!!))/&$#%))"/*&&)!"'$%/,+- 
                                                                                                                                      (+$.-)%#*#!$.)*###/*&(
                                                                                                                                            #"*'"*#+(! 


           


           







"""

print(ruleta3)
input()