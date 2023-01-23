class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        
    def board_generator(self):
        self.board = [[]] # matrice

        # Board de départ
        # logique avec random de generateur de tuile, if l'un est tombe du le 20% de chance, l'autre ne peut pas
        # for line in lines:
        #   for tile in tiles:
        #       self.tile = Tuile ou Chance ou Obstacle . random
        #       self.board[row.append(self.tile)]

        # 2 cases pas générée aleatoirement ( depart et arrivée)
        # si on est funky on pourrait faire bouger la case arrivée

        # quoi faire quand les deux joueurs sont sur la même case

    def __str__():
        pass
        
    # Disposition des tuiles
    # Disposition des portails    
    # Variété de tableau
    # déplacements: effets selon les cartes

class Tile:
    # Obstacles

    def __init__():
        pass

    def win_tile():
        pass
    
    def __str__():
        pass
    
class Portal(Tile):
    def __init__():
        # sa representation
        pass
    # def what they do
    

    
class Obstacle(Tile):
    def __init__():
        # visel/representation graphique
        # def what they do
        pass
    
    

class Chance(Tile):
    def __init__(): # +/-
        # sa representation
        pass
    # quan d on tombe sur case chance, on ferait self.bag apped item
    # méthode qui fait piger random une carte de la classe carte
    # def what they do


class Card:
    def __init__(self):
        # ex self.valeur = 1 ou -1
        ### est ce qu'on fait deux classes différentes (+1, -1) ???
        pass    
 
class Player(Tile):
    def __init__(self,):
        self.bag = [] # Card

        # part avec une sac vide et ex tombe sur case chance
        # on ajoute une carte X a notre main 

        # scoreboard
        pass
    def roll_dice():
        # valeur de deplacement associé selon le lancé de dé.
        pass
    def play_card():
        # prend la valeur de placement et tu +1 ou -1 selon self.bag if les cartes sont dispo dans self.bag
        # if +1 présent. input veux tu faire +1
        #if -1 présent. input veux tu faire -1
        #if +1 -1 présent. input veux tuf aire +1 ou -1

        #prend valeur deplacement et retourne valeur de dep. modifiée

        # quand t'as ta valeur de dep final
        pass

    def move_token():
        # trover moyen de avancer de D/G quand ligne impair et l'autre G/D paire
        pass


    def __str__():
        pass
    # le player est reprenté 
        

class Ai(Player):
    # même actions que player, sans input

        pass
    

class Startup:
    def __init__(self):
        self.board = Board()
        pass

    def menu(self):

        with open("premise.txt", "r", encoding="utf-8") as premise_game:
            description = premise_game.read()
            print(description)

        enter_the_game = ("Are you ready to enter? Y/N: ")

        if enter_the_game == "Y":
            exit = False
            while not exit:
                print("Welcome to Portals and Portals")
                print("1 - Read the Instructions")
                print("2 - Play")
                print("3 - Change the difficulty")
                print("4 - Exit the game")
                

                player_option = int(input(" Please enter your option's number. 1,2 3 or 4: "))

                if player_option == 1:
                    self.instruction()
                    
                elif player_option == 2:
                    pass
                elif player_option == 3:
                    pass
                elif player_option == 4:
                    print("See you next time!")
                    exit = True
                else: 
                    print("Sorry, this is not one of the options")
        elif enter_the_game == "N":
            print("It is ok to be afraid. Feel free to comeback when you find some courage")


    
    def instruction():
        with open("instroctions.txt", "r", encoding="utf-8") as rules_game:
            rules = rules_game.read()
            print(rules)
        
        

    def play():
        #appeler class board (rows = 8, columns = 8, % = 20)

        pass
        
    def change_level():
        # menu description difficultée
        # 
        # choix ==2 
        # self.rows sera changé pour 12

        pass
Startup()

# Demarrage

# Affichage du menu: 
# Niveaux ex: 8x8 avec 20% d'apparition de portail ( le passer a board) 
# Instructions 
# 