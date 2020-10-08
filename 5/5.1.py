fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
     vastuvõetud.append(int(rida))
fail.close()

print(vastuvõetud)
aasta = input("Sisestage aasta: ")

if aasta == "2011":
    arv = vastuvõetud[0]
elif aasta == "2012":
    arv = vastuvõetud[1]
elif aasta == "2013":
    arv = vastuvõetud[2]
elif aasta == "2014":
    arv = vastuvõetud[3]
elif aasta == "2015":
    arv = vastuvõetud[4]
elif aasta == "2016":
    arv = vastuvõetud[5]
elif aasta == "2017":
    arv = vastuvõetud[6]
elif aasta == "2018":
    arv = vastuvõetud[7]
else:
    arv = vastuvõetud[8]

print(aasta + ". aastal võeti vastu " + str(arv) + " inimest.")