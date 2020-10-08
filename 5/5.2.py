fail = open("konto.txt", encoding="UTF-8")
kontod = []
for rida in fail:
     kontod.append(float(rida))
fail.close()

for num in kontod:
     if num >= 0:
          print(num)