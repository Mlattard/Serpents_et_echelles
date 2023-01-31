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
                    elif row == 1 and tile == 1:
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

    def gameloop(self):
        exit = False
        self.player = Player((self.columns * 2)- 1, 1)
        self.ia = Ai((self.columns * 2)- 1, 1)
        players = [self.player, self.ia]
        
        while not exit:
            print(self)
            for p in players:
                i,j = p.game_round()
                self.move(p,i,j)
                # print(self) voir si on veut voir le deplacement de l'ia
                exit = self.check_win()
                
    def check_win():
        if (pos_x == self.exit.pos_x) and (pos_y == self.exit.pos_y):
            return True
        else:
            return False


class Tile:

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __str__(self):
        return "   "

class StartingPoint(Tile):

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)

    def __str__(self):
        return " S "

class ExitPoint(Tile):

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.is_exit = True

    def __str__(self):
        return " E "

class Portal(Tile):

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.is_portal = True
        self.next : Portal 
        self.color = None

    def __str__(self):
        return colored(" ☼ ", self.color)
        
class Chance(Tile):

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.is_chance = True
        
    def __str__(self):
        return " ♣ "

    def get_card(self):
        return Card()     

class Player(Tile):

    def __init__(self, pos_x : int, pos_y : int):
        super().__init__(pos_x, pos_y)
        self.is_player = True
        self.bag = []
        self.tile_under = board[len(self.new_board)-2][1]

    def __str__(self):
        self.tile_under : Ai

        if self.tile_under.is_ai != True:
            return " ☺ "
        else:
            return "☺ ☻"

    """On lance le dé et on trouve la tuile suivante"""

    def game_round(self):
        nb_steps = random.randint(1,6)
        print(f"The dice gives you this number of steps: {nb_steps}")

        if self.bag != []:
            if ("+1" in self.bag) and ("-1" not in self.bag):
                play_card = input("Would you like to advance one tile more? Y/N :")
                if play_card.lower() == "y":
                    nb_steps += 1
            if ("+1" not in self.bag) and ("-1" in self.bag):
                play_card = input("Would you like to advance one tile less? Y/N :")
                if play_card.lower() == "y":
                    nb_steps -= 1
            if ("+1" in self.bag) and ("-1" in self.bag):
                play_card = input("Would you like to advance one tile less? Y/N :")
                if play_card.lower() == "y":
                    nb_steps -= 1
                else:
                    play_card = input("Would you like to advance one tile less? Y/N :")
                    if play_card.lower() == "y":
                        nb_steps -= 1

        """"rendu la on a determiné le nombre de deplacement à faire"""
        
        next_pos_x, next_pos_y = self.pos_x, self.pos_y    
        current_row = (next_pos_x + 1) / 2
        current_tile = (next_pos_y + 1) / 2

        for i in range (1, nb_steps + 1):
            if current_row % 2 == 0:
                if current_tile < game.board.columns:
                    current_tile += 1
                    nb_steps -= 1
                else:
                    current_row -= 1
            elif current_row % 2 == 1:        
                if current_row > 1:
                    current_tile -= 1
                    nb_steps -= 1
                else:
                    current_row -= 1

        next_pos_x = (current_row * 2) -1
        next_pos_y = (current_tile * 2) -1

        self.board.new_board[self.pos_x][self.pos_y] = self.tile_under         # la tuile actuelle reprend la valeur de tile_under
        self.tile_under = self.next_tile                                 # on donne a tile_under la valeur de la prochaine case
        self.next_tile = game.board.new_board[next_pos_x][next_pos_y]    # on remplace la prochaine case par la tuile player

        if self.tile_under == Portal:                                    # on verifie si la case sauvée dessous est un portail
            self.next_tile = self.next_tile.next                         # on remplace la valeur de next tile par le portail suivant

class Ai(Player):
    def __init__(self):
        super().__init__()
        self.is_ai = True

    def __str__(self):
        return " ☻ "


class Card:

    def __init__(self):
        self.card_value = random.choice(-1,1)
        return self.card_value


class Startup:

    def __init__(self):
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
                    board = Board()
                    board.generate_board()
                    board.gameloop()

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



"""
    print(self)
    i,j = self.player.play()
    self.move(player,i,j)
    # pt print(self) sleep (0.5) -> cls()



    OU PLUTÔT :self.players = [player, AI]
    
    dans la classe Board
    def gameloop():
        while not exit
            print(self)  
            for p in players:
                i,j = p.play()
                self.move(p,i,j)
                # print(self) voir si necessaire
                exit = self.check_win
                if pos_x == self.exit.pos_X and pos_y == self.exit.pos_y
                return True 
                else: return False


def move(p,i,f):

    pos_x = 
    pos_y = 
    i =
    j =
    if self.board[i][j] is not portail
    self.board[pos_x][pos_y] = p.under
    p.under = self.board[i][j]
    self.board[i][j] = p


    i = self.board[i][j].next.x
    j = self.board[i][j].next.y



"""