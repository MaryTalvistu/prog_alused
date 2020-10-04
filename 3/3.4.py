from random import randint

isik = int(input("Mitu pöialpoissi tahab õunu [0-7]? "))
poialpoisse = 1
ounte_arv = 0
while (poialpoisse <= isik):
    ounu = randint(1, 2)
    print(ounu)
    ounte_arv += ounu
    poialpoisse += 1
jaak = 14 - ounte_arv
print("Lumivalgekesele jäi " + str(jaak) + " õuna.")


