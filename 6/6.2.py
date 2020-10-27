kylaliste_arv = int(input("Sisestage kutsutud külaliste arv: "));
teatanud = int(input("Sisestage teatanud külaliste arv: "));

def eelarve(x):
    return x * 10 + 55;

print("Maksimaalne eelarve: " + str(eelarve(kylaliste_arv)) + " eurot.");
print("Minimaalne eelarve: " + str(eelarve(teatanud)) + " eurot.");