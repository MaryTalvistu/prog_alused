number = int(input("Kuu number: "));

def kuu_nimi(number):
    number = number - 1
    kuu = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return(kuu[number])


print(kuu_nimi(number))

#number = int(input("Sisesta kuupäev kujul DD.MM.YYYY: ").split(".")[1]);

kuupäev = input("Sisesta kuupäev kujul DD.MM.YYYY: ");

def kuupäev_sõnena():
    jada = kuupäev.split(".");
    return(jada)


päev = jada[0];
kuu = jada[1];
aasta = jada[2];


def kuu_nimi(kuu):
    kuu = kuu - 1
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return(kuud[kuu])

print(päev + kuu_nimi(kuu) + aasta)
