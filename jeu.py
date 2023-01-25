import os
import random
from termcolor import colored

class Board:

    def __init__(self, rows : int = 8, columns : int = 8, rate : float = 0.2):

        self.rows = rows
        self.columns = columns
        self.rate = rate

    def generate_board(self):

        self.board = []

        for row in range(0, (self.rows * 2) + 1):
            line = []

            for tile in range(0, (self.columns * 2 + 1)):  
                if row == 0:
                    if tile == 0:
                        line.append("╔")
                    elif tile == (self.columns * 2):
                        line.append("╗")
                    elif tile % 2 == 0:
                        line.append("╤")
                    else:
                        line.append("═══")

                elif row == (self.rows * 2):
                    if tile == 0:
                        line.append("╚")
                    elif tile == (self.columns * 2):
                        line.append("╝")
                    elif tile % 2 == 0:
                        line.append("╧")
                    else:
                        line.append("═══")

                elif row % 2 == 0:
                    if tile == 0:
                        line.append("╟")
                    elif tile == (self.columns * 2):
                        line.append("╢")
                    elif tile % 2 == 0:
                        line.append("┼")
                    else:
                        line.append("───")

                elif row % 2 != 0:
                    if (tile == 0) or (tile == (self.columns * 2)):
                        line.append("║")
                    elif tile % 2 == 0:
                        line.append("│")
                    else:
                        line.append("   ")

            self.board.append(line)

        # Board de départ

        # 2 cases pas générée aleatoirement (depart et arrivée)
        # si on est funky on pourrait faire bouger la case arrivée

        """
        2 - set random -> create pair
        3 - si on veut mettre random la case depart (position 1 a 6) SI ON A LE TEMPS
        trajet en serpentin: verif a faire avc la parité des lignes
    
        """

    def display_board(self):
        
        for row in self.board:
            printed_line = ""

            for position, tile in enumerate(row):
                if position < len(row):
                    printed_line += tile
                else:
                    printed_line += (tile + "\n")

            print(printed_line)

        ''' quoi faire quand les deux joueurs sont sur la même case ? '''

    def __str__():

        pass  
        # Disposition des tuiles
        # Disposition des portails    
        # Variété de tableau
        # déplacements: effets selon les cartes


class Tile:

    def __init__(self, pos_x, pos_y):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.representation = "   "

        # entré et sortie en premier

    def check_win():

        if player.pos_x == sortie.pos_x and player.pos_y == sortie.pos_y:
            print("GAGNÉ !")

        if ai.pos_x == sortie.pos_x and ai.pos_y == sortie.pos_y:
            print("PERDU !")

    def __str__():
        
        pass

class StartingPoint(Tile):

    def __init__(self):

        self.pos_x = rows
        self.pos_y = 0

        # sa representation
        pass
        # def what they do

class ExitPoint(Tile):

    def __init__(self):

        self.pos_x = 0
        self.pos_y = columns

        # sa representation
        pass
        # def what they do

class Portal(Tile):

    def __init__(self):
        # self.next : Portail
        # self.i = i: int
        # self.j = j: int

        # sa representation
        pass
        # def what they do
        
        # idée: quand le joueur passe dans un portail, 
        # afficher un petit texte de mise en situation comme quoi il a changé d'univers/ il se retrouve dans de contrées inconnus
        """"
        portail: si elle est juste un portail, il y a des verif a faire. (verifier que ce n'Est pas une case chance)
        on peut placer les portails en paire (decider combien on en veut ex. 5% des cases)
        placer les portails aleatoirement (liste de portails to_set  set_portail)

        to_set: ex. 5% pos_aleatoire. 
        index aleatoire(2 index(a,b): set portals next) (i,j) 0... len(to_set)-1, 

        [Portals(i,j),
         Portals(i,j)
         ...
         Portals(i,j)]

        to_set[a].next = to_set[b]
        to_set[b].next = to_set[a]
        set.append(to_set[a])
        set.append(to_set[b])
        delete de l'Ancienne liste
    
        
        penser a la proportion paire
        tester si bidirectionnel est fun ou pas (pt implanter certains portails unidirectionnels)

        set_portals: logique: (enlever de tp_set et la mettre dans la liste set_portals quand ils sont definis)

        
        """""
    
    
class Obstacle(Tile):

    def __init__(self):

        # visel/representation graphique
        # def what they do
        pass

class Chance(Tile):

    def __init__(self): # +/-
        self.lucky_tile = "♣"


        # sa representation
        pass
        # quan d on tombe sur case chance, on ferait self.bag apped item
        # méthode qui fait piger random une carte de la classe carte
        # def what they do 

class Player(Tile):

    def __init__(self):
        # self = ☺

        self.bag = [] # Card
        # part avec une sac vide et ex tombe sur case chance
        # on ajoute une carte X a notre main 
        pass

    def roll_dice(self):

        return random.randint(1,6)
        # valeur de deplacement associé selon le lancé de dé.

    def play_card():

        # prend la valeur de placement et tu +1 ou -1 selon self.bag if les cartes sont dispo dans self.bag
        # if +1 présent. input veux tu faire +1
        # if -1 présent. input veux tu faire -1
        # if +1 -1 présent. input veux tuf aire +1 ou -1

        # prend valeur deplacement et retourne valeur de dep. modifiée

        # quand t'as ta valeur de dep final
        pass

    def move_token(self, roll):

        self.player_position += roll
        # trover moyen de avancer de D/G quand ligne impair et l'autre G/D paire
        pass

    def __str__():

        pass
        # le player est représenté 

class Ai(Player):

    # même actions que player, sans input
    pass


class Card:

    def __init__(self):

        # ex self.valeur = 1 ou -1
        ''' est ce qu'on fait deux classes différentes (+1, -1) ??? '''
        pass   


class Startup:

    def __init__(self):

        self.board = Board()
        self.board.generate_board()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):

        self.clear()

        with open("premise.txt", "r", encoding="utf-8") as premise_game:
            description = premise_game.read()
            print(f"{description}") 

        enter_the_game = input("Are you ready to enter? Y/N: ")

        if enter_the_game.lower() == "y": 
            exit = False
            while not exit:
                self.clear()
                print(colored("Welcome to Portals and Portals :", "green"))
                print("1 - Play")
                print("2 - Read the Instructions")
                print("3 - Change the difficulty")
                print("4 - Exit the game\n")

                player_option = int(input("Please enter your option's number (1, 2, 3 or 4): "))
                self.clear()

                if player_option == 1:
                    self.board.display_board()
                    sortie = input("\nPress Enter to exit: ")

                elif player_option == 2:
                    self.instructions()

                elif player_option == 3:
                    pass

                elif player_option == 4:
                    print("\n\n\nSee you next time!\n\n\n")
                    exit = True

                else: 
                    print("Sorry, this is not one of the options")

        elif enter_the_game.lower() == "n":
            self.clear()
            print("\n\n\nIt is ok to be afraid.")
            print("Feel free to comeback when you find some courage.\n\n\n")

    @staticmethod
    def instructions():

        instructions_exit = False
        while not instructions_exit:
            with open("instructions.txt", "r", encoding="utf-8") as rules_game:
                rules = rules_game.read()
                print(rules)

            user_choice = input("Press Enter to go back to menu ")
            if user_choice == "":
                instructions_exit = True

    def play(self):

        self.play_game = Board()

    def change_level(self):
        exit = False
        while not exit:
            print("You can change the difficulty level")
            print("1 - Easy")
            print("2 - Moderate")
            print("3 - Hard")
            print("4 - Go back")

            level_choice = int(input("Please select your difficulty level (ex: 2): "))

            if level_choice == 1:
                pass
            elif level_choice == 2:
                pass
            elif level_choice == 3:
                pass
            elif level_choice == 4:
                exit = True

        # choix ==2 
        # self.rows sera changé pour 12

game = Startup()
game.menu()

# Demarrage

# Affichage du menu: 
# Niveaux ex: 8x8 avec 20% d'apparition de portail ( le passer a board) 
# Instructions