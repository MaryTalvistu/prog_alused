fail = open("rebased.txt", encoding="UTF-8")
vastuvoetud = []
for rida in fail:
     vastuvoetud.append(int(rida))
fail.close()

print(vastuvoetud)
aasta = input("Sisestage aasta: ")

if aasta == "2011":
    arv = vastuvoetud[0]
elif aasta == "2012":
    arv = vastuvoetud[1]
elif aasta == "2013":
    arv = vastuvoetud[2]
elif aasta == "2014":
    arv = vastuvoetud[3]
elif aasta == "2015":
    arv = vastuvoetud[4]
elif aasta == "2016":
    arv = vastuvoetud[5]
elif aasta == "2017":
    arv = vastuvoetud[6]
elif aasta == "2018":
    arv = vastuvoetud[7]
else:
    arv = vastuvoetud[8]

print(aasta + ". aastal võeti vastu " + str(arv) + " inimest.")