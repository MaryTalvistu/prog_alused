# muutujate andmed
nimi = input("Sisestage oma nimi: ")
lubatud_kiirus = input("Sisestage lubatud kiirus km/h: ")
reaalne_kiirus = input("Sisestage reaalne kiirus km/h: ")
# arvutused
trahv = (int(reaalne_kiirus) - int(lubatud_kiirus)) * 3
# arvestame, et trahv üle 190 ei oleks
trahv = min(trahv, 190)
# väljastus
print(nimi + ", kiiruse ületamise eest on Teie trahv " + str(trahv) + " eurot.")