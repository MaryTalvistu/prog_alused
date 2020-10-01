'''
# üldtsükkel
for kord in range(1, 6, 1):
    print(str(kord) + ". tere")
print("=============")

# vastupidi
for kord in range(5, 0, -1):
    print(str(kord) + ". tere")
print("=============")

# eelkontrolliga tsükkel
kord = 1
while(kord <= 5):
    print(str(kord) + ". tere")
    kord = kord + 1 # kord += 1
print("=============")


kord = 5
while(kord > 0):
    print(str(kord) + ". tere")
    kord = kord - 1 # kord -= 1
print("=============")
'''

kord = 1
while(kord <= 5):
    if(kord == 3):
        kord += 1
        continue
    else:
        print(str(kord) + ".tere")
        kord += 1

kord = 1
while(kord <= 5):
    if(kord == 3):
        kord += 1
        break
    else:
        print(str(kord) + ".tere")
        kord += 1