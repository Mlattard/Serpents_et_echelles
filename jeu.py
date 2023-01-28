import os
import random
from termcolor import colored

class Board:

    def __init__(self, rows : int = 6, columns : int = 6, num_portals : int = 6, num_lucky : int = 6):

        self.rows = rows
        self.columns = columns
        self.num_portals = num_portals
        self.num_lucky = num_lucky
        self.new_board = []

    def generate_board(self):
       
        """Génération du plateau vide et des cases Départ et Arrivée"""
        self.empty_tiles = []

        for row in range(0, (self.rows * 2)+ 1):
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
                    elif row == 1 and (tile == (self.columns * 2)- 1):
                        line.append(ExitPoint(row, tile))
                    elif (row == (self.rows * 2)- 1) and tile == 1:
                        line.append(StartingPoint(row, tile))                      
                    else:
                        line.append(Tile(row, tile))
                        self.empty_tiles.append([row, tile])

            self.new_board.append(line)

        """Génération des portails"""
        i = 0
        self.portals_to_set = []
        while i in range(self.num_portals):
            new_portal = random.randint(0, len(self.empty_tiles)- 1)
            pos_x = self.empty_tiles[new_portal][0]
            pos_y = self.empty_tiles[new_portal][1]
            directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
            dans_cadre = []

            for x, y in directions:
                if (pos_x + x >= 0 and pos_x + x < len(self.new_board)) and (pos_y + y >= 0 and pos_y + y < len(self.new_board[0])):
                    dans_cadre.append(True)
                else:
                    dans_cadre.append(False)
            
            touche = 0
            for pos in range(len(dans_cadre)): 
                if dans_cadre[pos] == True and (str(self.new_board[pos_x + directions[pos][0]][pos_y + directions[pos][1]]) != " ☼ "):
                    touche += 1
                elif dans_cadre[pos] == False:
                    touche += 1
                
            if touche == 4:        
                self.new_board[pos_x][pos_y] = Portal(pos_x, pos_y)
                self.portals_to_set.append(self.new_board[pos_x][pos_y])
                self.empty_tiles.remove(self.empty_tiles[new_portal])
                i += 1

        """Association des portails"""
        self.set_done = []
        pos = 0
        while self.portals_to_set != []:
            new_set = random.sample(self.portals_to_set, 2)
            new_set[0].color = game.COLORS[pos]
            new_set[1].color = game.COLORS[pos]
            self.set_done.append(new_set)
            pos += 1
            new_set[0].next = new_set[1]
            new_set[1].next = new_set[0]
            self.portals_to_set.remove(new_set[0])
            self.portals_to_set.remove(new_set[1])
            

        """Génération des cases chanceuses"""
        i = 0
        while i in range(self.num_lucky):
            new_lucky = random.randint(0, len(self.empty_tiles)- 1)
            pos_x = self.empty_tiles[new_lucky][0]
            pos_y = self.empty_tiles[new_lucky][1]
            directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
            dans_cadre = []
            
            for x, y in directions:
                if (pos_x + x >= 0 and pos_x + x < len(self.new_board)) and (pos_y + y >= 0 and pos_y + y < len(self.new_board[0])):
                    dans_cadre.append(True)
                else:
                    dans_cadre.append(False)
            
            touche = 0
            for pos in range(len(dans_cadre)):
                if dans_cadre[pos] == True and (str(self.new_board[pos_x + directions[pos][0]][pos_y + directions[pos][1]]) != " ♣ "):
                    touche += 1
                elif dans_cadre[pos] == False:
                    touche += 1

            if touche == 4:
                self.new_board[pos_x][pos_y] = Chance(pos_x, pos_y)
                self.empty_tiles.remove(self.empty_tiles[new_lucky])
                i += 1

    def display_board(self):
        
        for row in self.new_board:
            printed_line = ""

            for position, tile in enumerate(row):
                if position < len(row):
                    printed_line += str(tile)
                else:
                    printed_line += (str(tile) + "\n")

            print(printed_line)



class Tile:

    def __init__(self, pos_x, pos_y):

        self.pos_x = pos_x
        self.pos_y = pos_y

    def __str__(self):
        return "   "

    def check_win():

        if player.pos_x == sortie.pos_x and player.pos_y == sortie.pos_y:
            print("GAGNÉ !")

        if ai.pos_x == sortie.pos_x and ai.pos_y == sortie.pos_y:
            print("PERDU !")

class StartingPoint(Tile):

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)

    def __str__(self):
        return " S "

class ExitPoint(Tile):

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)

    def __str__(self):
        return " E "

class Portal(Tile):

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.next : Portal 
        self.color = None

    def __str__(self):
        return colored(" ☼ ", self.color)
        
        
# class Obstacle(Tile):

#     def __init__(self):

#         # visel/representation graphique
#         # def what they do
#         pass

class Chance(Tile):

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        
    def __str__(self):
        return " ♣ "

    def get_card(self):
        return Card()     

class Player(Tile):

    def __init__(self):
        self.bag = []
        # part avec une sac vide et ex tombe sur case chance
        # on ajoute une carte X a notre main 
    
    def __str__(self):
        return " ☺ "

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
    def both_player(self):
        return "☺ ☻"

class Ai(Player):
    def __init__(self):
        super().__init__()
        pass

    def __str__(self):
        return " ☻ "



class Card:

    def __init__(self):
        self.valeur = random.choice(-1,1)
        return self.valeur

     
class Startup:

    def __init__(self):
        self.board = Board()
        self.level = "Easy"
        self.COLORS = ("red", "green", "yellow", "blue", "magenta", "cyan")

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
                print(f"1 - Play - {self.level}")
                print("2 - Read the Instructions")
                print("3 - Change the difficulty")
                print("4 - Exit the game\n")

                player_option = int(input("Please enter your option's number (1, 2, 3 or 4): "))
                self.clear()
                
                if player_option == 1:
                    game.board.new_board = []
                    self.board.generate_board()
                    self.board.display_board()
                    exit = input("\nPress Enter to exit: ")

                elif player_option == 2:
                    self.instructions()

                elif player_option == 3:
                    self.change_level()

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
        print("You can change the difficulty level")
        print("1 - Easy")
        print("2 - Moderate")
        print("3 - Hard")
        
        level_choice = int(input("Please select your difficulty level (ex: 2): "))

        if level_choice == 1:
            self.board = Board(6, 6, 6, 6)
            self.level = "Easy"
            
        elif level_choice == 2:
            self.board = Board(8, 8, 8, 8)
            self.level = "Moderate"
            
        elif level_choice == 3:
            self.board = Board(12, 12, 12, 12)
            self.level = "Hard"

        self.board.generate_board()

        
game = Startup()
game.menu()

# ajouter un menu pour cjhanger la langue d'affichage