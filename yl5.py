ainepunktide_arv = input("Sisestage ainepunktide arv: ")
n2dalate_arv = input("Sisestage nädalate arv: ")
eeldatav_ajakulu = int(ainepunktide_arv) * 26 / int(n2dalate_arv) 
print(round(eeldatav_ajakulu))