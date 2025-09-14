plansza = [[""], [""], [""],
           [""], [""], [""],
           [""], [""], [""]]

def wypisaniePlanszy(plansza):
    print("\n")
    for i in range(3):
        for j in range(3):
            if j < 2:
                print(f" a ", end="|")
            else:
                print(f" a ")
        if i < 2:
            print("─── ─── ───")
    print("\n")



wypisaniePlanszy(plansza)