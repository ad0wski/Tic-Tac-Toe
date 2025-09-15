plansza = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

zasady = """
Zasady gry: Kółko i krzyżyk 🎮

1. Gra odbywa się na planszy 3x3.
2. Gracze na zmianę stawiają swoje symbole: X lub 0.
3. Aby wykonać ruch, podaj numer pola od 1 do 9:
   1 | 2 | 3
   4 | 5 | 6
   7 | 8 | 9
4. Wygrywa gracz, który jako pierwszy ułoży 3 swoje symbole w rzędzie,
   kolumnie lub na ukos.
5. Jeśli wszystkie pola zostaną zajęte i nikt nie wygrał — jest remis."""
print(zasady)

aktualnyGracz = "X"

def wypisaniePlanszy(plansza):
        print("\n")
        for i in range(3):
            for j in range(3):
                if j < 2:
                    print(f" {plansza[i][j]} ", end=" |")
                else:
                    print(f" {plansza[i][j]} ")
            if i < 2:
                print("───  ───  ───")
        print("\n")

def ruch(aktualnyGracz, plansza, wybranePole):
    if plansza[(wybranePole - 1) // 3][(wybranePole - 1) % 3] != " ":
        print("To pole jest zajęte! ")
    else:
        plansza[(wybranePole - 1) // 3][(wybranePole - 1) % 3] = aktualnyGracz

def zmianaGracza(aktualnyGracz):
    if aktualnyGracz == "X":
        aktualnyGracz = "0"
    else:
        aktualnyGracz = "X"
    return aktualnyGracz

def czyWygrana(plansza, aktualnyGracz):
    for i in range(3):
        if plansza[0][i] == plansza[1][i] == plansza[2][i] == aktualnyGracz:
            return True
        elif plansza[i][0] == plansza[i][1] == plansza[i][2] == aktualnyGracz:
            return True
    if plansza[0][0] == plansza[1][1] == plansza[2][2] == aktualnyGracz:
        return True
    if plansza[0][2] == plansza[1][1] == plansza[2][0] == aktualnyGracz:
        return True
    return False

ruchy = 0

while True:
    ruchy += 1
    wypisaniePlanszy(plansza)

    wybranePole = int(input("Podaj numerek pola, które chcesz zająć: "))

    ruch(aktualnyGracz, plansza, wybranePole)
    
    if czyWygrana(plansza, aktualnyGracz) == True:
        wypisaniePlanszy(plansza)
        print(f"WYGRYWA {aktualnyGracz}")
        break

    if ruchy == 9:
        wypisaniePlanszy(plansza)
        print("REMIS! ")
        break

    aktualnyGracz = zmianaGracza(aktualnyGracz)