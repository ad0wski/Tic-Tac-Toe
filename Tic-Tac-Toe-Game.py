plansza = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

aktualnyGracz = "X"

while True:
    wypisaniePlanszy(plansza)

    if aktualnyGracz == "X":
        aktualnyGracz = "0"
    else:
        aktualnyGracz = "X"

    wybranePole = int(input("Podaj numerek pola, które chcesz zająć: "))

    ruch(aktualnyGracz, plansza, wybranePole)

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

    def czyWygrana(plansza, gracz):
        pass