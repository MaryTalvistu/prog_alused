# jususliku numbri genereerimiseks impordin randint funktsiooni
from random import randint

# funktsiooni inimeste_arv loomine
def inimeste_arv(naiskondade_arv, tugiisikute_arv):
    return naiskondade_arv * (22 + tugiisikute_arv)

print (inimeste_arv(12,10))


# küsin toimumiskohta
toimumiskoht = input("Kus toimusid maailmameistrivõistlused: ");
print("Turniirid toimusid " + toimumiskoht)

# küsin toimunud turniiride arvu ja muudan sõne arvuks
turniiride_koguarv = int(input("Kui palju turniire toimus: "));

# loon kõigepealt tühja turniiride nimekirja ja siis lisan sinna juhusega valitud naiskondade arvud
# nimekirjas on niipalju elemente kui sisestatud turniiride koguarv
turniiride_nimekiri = []
i = 0
while i <= turniiride_koguarv-1:
    turniiride_nimekiri.append(randint(10,30))
    i += 1
# print(turniiride_nimekiri)

# võtan ühekaupa nimekirjast naiskondade arvud
# kui naiskondi rohkem kui 15, siis tugiisikuid 10, muidu 8
for naiskondade_arv in turniiride_nimekiri:
    if naiskondade_arv > 15:
        tugiisikute_arv = 10
    else:
        tugiisikute_arv = 8

# turniiril osalejate arvu arvutamine
    inimeste_arv = naiskondade_arv * (22 + tugiisikute_arv)
    print("Turniiril oli " + str(naiskondade_arv) + " naiskonda ja vastavalt inimesi " + str(inimeste_arv))


