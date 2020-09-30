vanus = int(input("Sisestage enda vanus: "))
sugu = input("Sisestage enda sugu: ")
treeningutyyp = input("Sisestage treeningu tüüp: ")

if sugu == "m" or sugu == "M":
    max_pulsisagedus = int(220 - vanus)
elif sugu == "n" or sugu == "N":
   max_pulsisagedus = int(206 - (vanus * 88 / 100))
else:
    print("Sisestus ebatäpne.")

if treeningutyyp == "1":
    vahim_pulsisagedus = int(max_pulsisagedus * 50 / 100)
    suurim_pulsisagedus = int(max_pulsisagedus * 70 / 100)
elif treeningutyyp == "2":
    vahim_pulsisagedus = int(max_pulsisagedus * 70 / 100)
    suurim_pulsisagedus = int(max_pulsisagedus * 80 / 100)
elif treeningutyyp == "3":
    vahim_pulsisagedus = int(max_pulsisagedus * 80 / 100)
    suurim_pulsisagedus = int(max_pulsisagedus * 87 / 100)
else:
    print("Sellist treeningutüüpi pole.")


print("Pulsi sagedus peaks olema vahemikus " + str(vahim_pulsisagedus) + " kuni " + str(suurim_pulsisagedus))