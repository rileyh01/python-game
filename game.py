import random
import sys, os

#Creates Game piece class
class GamePiece:
    def __init__(self, color):
        self.color = color

#Creates Player Class
class Player:
    def __init__(self, name = "Boring", victory = "I am victorious"):
        self.name = name
        self.victory = victory
    def declare_victory():
        print(self.name + "won!")
        print("They say: " + self.victory)
    def assign_color(self, color):
        self.color = color


#game piece visual icons
red = GamePiece("(R)")
blue = GamePiece("(B)")
empty = GamePiece("   ")

board = []
available_colors = ["Red", "Blue"]

space = """\n \n"""

def generate_board(x = 7, y = 6):
    board.clear()
    for index in range(0, x, 1):
        board.append([])
        for indexy in range(0, y, 1):
            board[index].append(empty)

def print_board(board_x, board_y):
    lines = []
    for y in range(0, board_y * 2 + 1, 1):
        lines.append("")
        for x in range(0, board_x, 1):
            if y % 2 == 0:
                lines[y] += "*****"
            else:
                lines[y] += "*{}*".format(board[x][board_y - 1 - int((y-1)/2)].color)
        print(lines[y])

def check_y_value(column, board_y):
    for y in range(0, board_y, 1):
        if board[column][board_y - 1] != empty:
            return "Full"
        if board[column][y] == empty:
            return y

def play_token(player, column, board_y):
    if check_y_value(column, board_y) == "Full":
        return "Column Full Pick Again!"
    else:
        y = check_y_value(column, board_y)
    if player.color == "red":
        board[column][y] = red
    elif player.color == "blue":
        board[column][y] = blue
    else:
        return "Invalid Color"

def check_for_win(board_x, board_y):
    #Check Vertical Win
    #print("testing1")
    for index_x in range(0, board_x, 1):
        for index_y in range(0, board_y - 3, 1):
            if board[index_x][index_y].color == board[index_x][index_y + 1].color == board[index_x][index_y + 2].color == board[index_x][index_y + 3].color and board[index_x][index_y].color != empty and board[index_x][index_y + 1] != empty and board[index_x][index_y + 2].color != empty and board[index_x][index_y + 3].color != empty:
                return "win"
    #print("testing2")
    #Check Horizontal Win
    for index_y in range(0, board_y, 1):
        for index_x in range(0, board_x - 3, 1):
            if board[index_x][index_y].color == board[index_x+1][index_y].color == board[index_x +2][index_y].color == board[index_x + 3][index_y].color and board[index_x][index_y].color != empty and board[index_x + 1][index_y] != empty and board[index_x + 2][index_y].color != empty and board[index_x + 3][index_y].color != empty:
                return "win"
    #print("testing3")
    #Check Diagnol Win Positive Slope
    for index_x in range(0, board_x - 3, 1):
        for index_y in range(0, board_y - 3, 1):
            if board[index_x][index_y].color == board[index_x + 1][index_y + 1].color == board[index_x + 2][index_y + 2].color == board[index_x + 3][index_y + 3].color and board[index_x][index_y].color != empty and board[index_x + 1][index_y + 1] != empty and board[index_x + 2][index_y + 2].color != empty and board[index_x + 3][index_y + 3].color != empty:
                return "win"
    #print("testing4")
    #Check Diagnol Win Negative Slope
    for index_x in range(0, board_x - 3, 1):
        for index_y in range(board_y - 1, 2, -1):
            if board[index_x][index_y].color == board[index_x + 1][index_y - 1].color == board[index_x + 2][index_y - 2].color == board[index_x + 3][index_y - 3].color and board[index_x][index_y].color != empty and board[index_x + 1][index_y - 1] != empty and board[index_x + 2][index_y - 2].color != empty and board[index_x + 3][index_y - 3].color != empty:
                return "win"
    #print("testing5")
    #No Win Detected
    return "No Win"

def player_setup():
    colors = ""
    for x in range(0, len(available_colors), 1):
        colors += available_colors[x]
        if x < len(available_colors) - 1:
            colors += ", " 
        else:
            colors += "! "

    name = input("Player 1 what is your name? ")
    color = input(name + " what would you like your color to be? Your options are: " + colors)
    available_colors.remove(color.title())
    player_1 = Player(name)
    player_1.assign_color(color.lower())

    colors = ""
    for x in range(0, len(available_colors), 1):
        colors += available_colors[x]
        if x < len(available_colors) - 1:
            colors += ", " 
        else:
            colors += "! "

    name = input("Player 2 what is your name? ")
    color = input(name + " what would you like your color to be? Your options are: " + colors)
    available_colors.remove(color.title())
    player_2 = Player(name)
    player_2.assign_color(color.lower())

    return player_1, player_2

def randomize_first_player():
    num = random.randint(0, 1)
    if num == 0:
        return 1
    else:
        return 2

def play_game():
    win = False
    os.system('cls')
    print("Welcome to connect 4!")
    wants_to_play = input("Would you like to play a game? (Y/N): ")
    if wants_to_play.upper() == "Y":
        print("Get Ready to Have Some Fun!!!")
        temp = input("Press Enter To Continue!")
        os.system('cls')
        print("Now its time to determine the size of the board!")
        default = input("Would you like the default size of 7 columns x 6 rows? (Y/N): ")
        if default == "Y":
            board_x = 7
            board_y = 6
            generate_board()
        else:
            board_x = int(input("How many columns would you like? "))
            board_y = int(input("How many rows would you like? "))
            generate_board(board_x, board_y)
        
        temp = input("The board has been generated! Press Enter to Coninue!")
        os.system('cls')

        #Sets up players
        player1, player2 = player_setup()

        temp = input("Now that your players are set up press Enter to Continue!")
        os.system('cls')
        rand = input("Would you like to randomize who goes first? (Y/N): ")
        if rand.lower() == "y":
            first = randomize_first_player()
            if first == 1:
                print(player1.name + " will be going first!")
                temp = imput("Press enter when you are ready to begin!")
            elif first == 2:
                print(player2.name + " will be going first!")
                temp = imput("Press enter when you are ready to begin!") 
            else:
                return "error"
        else:
            print(player1.name + " will be going first!")
            temp = input("Press Enter when you are ready to begin!")
            os.system('cls')
            while win == False:
                print_board(board_x, board_y)
                column = input(player1.name + " what column would you like to place your token in? (1-" + str(board_x) + "): ")
                play_token(player1, int(column) - 1, board_y)
                os.system('cls')
                print_board(board_x, board_y)
                #print(check_for_win(board_x, board_y))
                if check_for_win(board_x, board_y) == "win":
                    win == True
                    print(player1.name + " has won the game!")
                    return
                temp = input("enter")
                column = input(player2.name + " what column would you like to place your token in? (1-" + str(board_x) + "): ")
                play_token(player2, int(column) - 1, board_y)
                os.system('cls')
                print_board(board_x, board_y)
                if check_for_win(board_x, board_y) == "win":
                    win == True
                    print(player1.name + " has won the game!")
                    return
                temp = input("enter")
                os.system('cls')            

    else:
        print("Thats Okay. Play some other time.")
        return "N"
    
play_game()       
print("Test Done")
