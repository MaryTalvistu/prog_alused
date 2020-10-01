from random import randint

valik = input("Kas soovite istekohta ise (´ise´) valida või loosida (´loos´)?")

if valik == "ise":
    print("Valisite ise")
    koht = input("Kas soovite istuda akna ääres(´aken´) või mitte (´muu´)?")
    if koht == "aken":
        print("Aknakoht")
    else:
        print("Vahekäigukoht")
else:
    loos = randint(1,3)
    if loos == 1:
        print("Istekoht loositi. Aknakoht.")
    else:
        print("Istekoht loositi. Vahekäigukoht.")