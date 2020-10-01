suurus = float(input("Sisestage kirja suurus megabaitides: "))
teema = input("Sisestage kirja teema pealkiri: ")
fail = input("Kas kirjaga on kaasas fail: ")

if fail == "jah" and suurus > 1 or teema == '':
    print("Kiri on spämm")
else:
    print("Kiri ei ole spämm")