import random

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

board_x = 7
board_y = 6

board = []

space = """


"""

def generate_board(x = 7, y = 6):
    board.clear()
    for index in range(0, x, 1):
        board.append([])
        for indexy in range(0, y, 1):
            board[index].append(empty)

def print_board():
    lines = []
    for y in range(0, board_y * 2 + 1, 1):
        lines.append("")
        for x in range(0, board_x, 1):
            if y % 2 == 0:
                lines[y] += "*****"
            else:
                lines[y] += "*{}*".format(board[x][board_y - 1 - int((y-1)/2)].color)
        print(lines[y])

def check_y_value(column):
    for y in range(0, board_y, 1):
        if board[column][board_y - 1] != empty:
            return "Full"
        if board[column][y] == empty:
            return y

def play_token(player, column):
    if check_y_value(column) == "Full":
        return "Column Full Pick Again!"
    else:
        y = check_y_value(column)
    if player.color == "red":
        board[column][y] = red
    elif player.color == "blue":
        board[column][y] = blue
    else:
        return "Invalid Color"

def check_for_win():
    #Check Vertical Win
    for index_x in range(0, board_x, 1):
        for index_y in range(0, board_y - 3, 1):
            if board[index_x][index_y].color == board[index_x][index_y + 1].color == board[index_x][index_y + 2].color == board[index_x][index_y + 3].color and board[index_x][index_y].color != empty and board[index_x][index_y + 1] != empty and board[index_x][index_y + 2].color != empty and board[index_x][index_y + 3].color != empty:
                return board[index_x][index_y].color

    #Check Horizontal Win
    for index_y in range(0, board_y, 1):
        for index_x in range(0, board_x - 3, 1):
            if board[index_x][index_y].color == board[index_x+1][index_y].color == board[index_x +2][index_y].color == board[index_x + 3][index_y].color and board[index_x][index_y].color != empty and board[index_x + 1][index_y] != empty and board[index_x + 2][index_y].color != empty and board[index_x + 3][index_y].color != empty:
                return board[index_x][index_y].color

    #Check Diagnol Win Positive Slope
    for index_x in range(0, board_x - 3, 1):
        for index_y in range(0, board_y - 3, 1):
            if board[index_x][index_y].color == board[index_x + 1][index_y + 1].color == board[index_x + 2][index_y + 2].color == board[index_x + 3][index_y + 3].color and board[index_x][index_y].color != empty and board[index_x + 1][index_y + 1] != empty and board[index_x + 2][index_y + 2].color != empty and board[index_x + 3][index_y + 3].color != empty:
                return board[index_x][index_y].color

    #Check Diagnol Win Negative Slope
    for index_x in range(0, board_x - 3, 1):
        for index_y in range(board_y - 1, 2, -1):
            if board[index_x][index_y].color == board[index_x + 1][index_y - 1].color == board[index_x + 2][index_y - 2].color == board[index_x + 3][index_y - 3].color and board[index_x][index_y].color != empty and board[index_x + 1][index_y - 1] != empty and board[index_x + 2][index_y - 2].color != empty and board[index_x + 3][index_y - 3].color != empty:
                return board[index_x][index_y].color
    
    #No Win Detected
    return "No Win"



player_1 = Player("Riley")
player_1.assign_color("red")

player_2 = Player("Nolan")
player_2.assign_color("blue")

generate_board(board_x, board_y)
print_board()
print(check_for_win())
play_token(player_1, 0)
play_token(player_2, 1)
print(space)
print_board()
print(check_for_win())
play_token(player_1, 1)
play_token(player_2, 2)
print(space)
print_board()
print(check_for_win())
play_token(player_1, 2)
play_token(player_2, 3)
print(space)
print_board()
print(check_for_win())
play_token(player_1, 2)
play_token(player_2, 3)
print(space)
print_board()
print(check_for_win())
play_token(player_1, 1)
play_token(player_2, 3)
print(space)
print_board()
print(check_for_win())
play_token(player_1, 3)
play_token(player_2, 1)
print(space)
print_board()
print(check_for_win())