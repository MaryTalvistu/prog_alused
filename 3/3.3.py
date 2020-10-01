
from random import randint

arv = int(input("Sisestage täringu visete arv: "))
kord = 1
while(kord <= arv):
    # teeme viske
    vise = randint(1, 6)
    # kontrollime, palju tuli
    print(vise)
    # teeme uue viske
    kord +=1
