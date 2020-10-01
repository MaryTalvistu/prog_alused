ringide_arv = int(input("Sisestage ringide arv: "))
ringi_number = 1
porgandite_arv = 0
while(ringi_number <= ringide_arv):
    # print(ringi_number)
    if(ringi_number % 2 == 0):
        porgandite_arv = porgandite_arv + ringi_number
      #  print("Said " + str(ringi_number) + " porgandit")
        # print("Kokku on hetkel " + str(porgandite_arv) + " porgandeid")
    ringi_number += 1
print("Porgandite koguarv " + str(porgandite_arv))