import os
import random
from termcolor import colored
import time

class Board:

    def __init__(self, rows : int = 6, columns : int = 6, num_portals : int = 6, num_lucky : int = 12):
        self.rows = rows
        self.columns = columns
        self.num_portals = num_portals
        self.num_lucky = num_lucky
        self.new_board = []

    def __str__(self):    
        printed_line = ""
        for row in self.new_board:
            
            for position, tile in enumerate(row):
                if position < (len(row)-1):
                    printed_line += str(tile)
                else:
                    printed_line += (str(tile) + "\n")

        return printed_line

    def generate_board(self):
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
                        self.exit_point = ExitPoint(row, tile)
                        line.append(self.exit_point)
                    elif (row == (self.rows * 2)- 1) and tile == 1:
                        self.start_point = StartingPoint(row, tile)
                        line.append(self.start_point) 
                        self.player = Player(row, tile)
                        self.ai = Ai(row, tile)                  
                    else:
                        line.append(Tile(row, tile))
                        self.empty_tiles.append([row, tile])

            self.new_board.append(line)

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
            
            next_to = 0
            for pos in range(len(dans_cadre)): 
                if dans_cadre[pos] == True and self.new_board[pos_x + directions[pos][0]][pos_y + directions[pos][1]].is_portal != True :
                    next_to += 1
                elif dans_cadre[pos] == False:
                    next_to += 1
                
            if next_to == 4:        
                self.new_board[pos_x][pos_y] = Portal(pos_x, pos_y)
                self.portals_to_set.append(self.new_board[pos_x][pos_y])
                self.empty_tiles.remove(self.empty_tiles[new_portal])
                i += 1

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
            
            next_to = 0
            for pos in range(len(dans_cadre)):
                if dans_cadre[pos] == True and self.new_board[pos_x + directions[pos][0]][pos_y + directions[pos][1]].is_chance != True :
                    next_to += 1
                elif dans_cadre[pos] == False:
                    next_to += 1

            if next_to == 4:
                self.new_board[pos_x][pos_y] = Chance(pos_x, pos_y)
                self.empty_tiles.remove(self.empty_tiles[new_lucky])
                i += 1

    def gameloop(self):

        self.player = Player((self.columns * 2)- 1, 1)
        self.ai = Ai((self.columns * 2)- 1, 1)
        players = [self.player, self.ai]
        print(self)
        
        exit = False
        while not exit:  
            for p in players:
                print(f"Current player: {p}")
                n_line, n_tile = p.game_round()
                self.move_tiles(p, n_line, n_tile)
                game.clear()
                print(self)
                exit = self.check_win(p)
                if exit == True:
                    print("Congratulations, you arrived at the end of the realm of portals!")
                    input("Press Enter to go back to the menu and try the next level")
                    break
                    
    def move_tiles(self, p : "Player" , n_line, n_tile):
        
        time.sleep(1)
        self.new_board[p.pos_x][p.pos_y] = p.under    # la tuile actuelle reprend la valeur de tile_under
        p.under = self.new_board[n_line][n_tile]      # on donne à tile_under la valeur de la prochaine case
        if p.under.is_chance:
            p.deck.add_card(Card())
        if p.under.is_portal != True:                 # on verifie si la case sauvée dessous est un portail
            self.new_board[n_line][n_tile] = p        # on remplace la prochaine case par la tuile player
        else:
            n_line = p.under.next.pos_x               # on remplace la nouvelle ligne par celle a next_x
            n_tile = p.under.next.pos_y               # on remplace la nouvelle tuile par celle a next_y
            self.new_board[n_line][n_tile] = p        # on remplace la valeur de next tile par le portail suivant
        p.pos_x = n_line                                # pas sur pourquoi les joueurs ne restent pas sur le portail de sortie
        p.pos_y = n_tile

    def check_win(self, p):
        if (p.pos_x == self.exit_point.pos_x) and (p.pos_y == self.exit_point.pos_y):
            return True
        else:
            return False


class Tile:

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.is_exit = False
        self.is_portal = False
        self.is_chance = False
        self.is_player = False
        self.is_ai = False

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


class Deck:

    def __init__(self) -> None:
        self.cards: list[Card]
        self.cards = []

    def play(self) -> "Card":
        
        if self.cards:
            print(self)
            card_choice = int(input("Which card do you want to play (1, 2, 3): "))
            if card_choice == 1:
                carte = self.cards[card_choice-1]
            elif card_choice == 2:
                carte = self.cards[card_choice-1]
            elif card_choice == 3:
                carte = self.cards[card_choice-1]

            self.cards.remove(carte)

            return carte
        else:
            print("Sac vide")

    def add_card(self, card : "Card"):
        if len(self.cards) < 3:
            self.cards.append(card)
        else:
            print("The deck is already full")    

    def __str__(self) -> str:
        str_deck = ""
        if self.cards:
            for pos, card in enumerate(self.cards):
                str_deck += f"{pos+1}. {card}"
        return str_deck

class Player(Tile):

    def __init__(self, pos_x : int, pos_y : int):
        super().__init__(pos_x, pos_y)
        self.is_player = True
        self.deck : Deck
        self.deck = Deck()
        self.under = game.board.new_board[len(game.board.new_board)-2][1]

    def __str__(self):
        self.under : Ai

        if self.under.is_ai != True:
            return " ☺ "
        else:
            return "☺ ☻"

    def game_round(self):
        input("Press Enter to roll your dice\n")
        nb_steps = random.randint(1,6)
        print(f"The dice gives you this number of steps: {nb_steps}")

        card = self.deck.play()

        if card is not None:
            if card.card_value:
                nb_steps += 1
            else:
                nb_steps -= 1
        
        
        next_pos_x, next_pos_y = self.pos_x, self.pos_y    
        current_row = int((next_pos_x + 1) / 2)
        current_tile = int((next_pos_y + 1) / 2)

        while nb_steps > 0:
            if current_row == 1:
                if current_tile != 1:
                    current_tile -= 1
                else:
                    current_row = int((next_pos_x + 1) / 2)
                    current_tile = int((next_pos_y + 1) / 2)
                    nb_steps = 0
            elif current_row % 2 == 1:        
                if current_tile == 1:
                    current_row -= 1
                else:
                    current_tile -= 1
            elif current_row % 2 == 0:
                if current_tile == game.board.columns:
                    current_row -= 1
                else:
                    current_tile += 1
            
            nb_steps -= 1

        next_pos_x = int((current_row * 2) -1)
        next_pos_y = int((current_tile * 2) -1)

        return next_pos_x, next_pos_y

class Ai(Player):
    def __init__(self, pos_x : int, pos_y : int):
        super().__init__(pos_x, pos_y)        
        self.is_player = False
        self.is_ai = True

    def __str__(self):
        self.under : Player

        if self.under.is_player != True:
            return " ☻ "
        else:
            return "☺ ☻"

class Card:

    def __init__(self):

        self.card_value = random.random()

    def __str__(self):
        if self.card_value:
            return "+1"
        else:
            return "-1"


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

        self.board = Board()

        enter_the_game = input("Are you ready to enter? Y/N: ")
        if enter_the_game.lower() == "y": 
            exit = False
            while not exit:

                self.clear()
                print("Welcome to Portals and Portals :")
                print(f"1 - Play - {self.level}")
                print("2 - Read the Instructions")
                print("3 - Change the difficulty")
                print("4 - Exit the game\n")

                player_option = int(input("Please enter your option's number (1, 2, 3 or 4): "))
                self.clear()

                if player_option == 1:
                    self.board.new_board = []
                    self.board.generate_board()
                    self.board.gameloop()

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

    def change_level(self):   
        print("You can change the difficulty level")
        print("1 - Easy")
        print("2 - Moderate")
        print("3 - Hard")
        
        level_choice = int(input("Please select your difficulty level (ex: 2): "))

        if level_choice == 1:
            self.board = Board(6, 6, 6, 12)
            self.level = "Easy"
            
        elif level_choice == 2:
            self.board = Board(8, 8, 8, 16)
            self.level = "Moderate"
            
        elif level_choice == 3:
            self.board = Board(12, 12, 12, 24)
            self.level = "Hard"

        
game = Startup()
game.menu()