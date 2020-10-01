# andmed kasutaja poolt
alus = input("Sisestage astme alus: ")
astendaja = input("Sisestaga astendaja: ")
# teisendame tüüpi
print(type(alus))
print(type(astendaja))
alus_int = int(alus)
astendaja_int = int(astendaja)
tulemus = alus_int ** astendaja_int

print(tulemus)