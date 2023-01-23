def menu():

        with open("premise.txt", "r", encoding="utf-8") as premise_game:
            description = premise_game.read()
            print(description)
menu()