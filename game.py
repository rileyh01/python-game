import random

#Creates Game piece class
class GamePiece:
    pass

#Creates Player Class
class Player:
    pass

#game piece visual icons
red = "(R)"
blue = "(B)"
empty = "   "

board = []
def generate_board(x = 7, y = 6):
    board.clear()
    for index in range(0, x, 1):
        board.append([])
        for indexy in range(0, y, 1):
            board[index].append(empty)

generate_board(7, 6)
#print(board)

def print_board():
  print("""
     *****************************
     *{}*{}*{}*{}*{}*{}*{}*
     *****************************
     *{}*{}*{}*{}*{}*{}*{}*
     *****************************
     *{}*{}*{}*{}*{}*{}*{}*
     *****************************
     *{}*{}*{}*{}*{}*{}*{}*
     *****************************
     *{}*{}*{}*{}*{}*{}*{}*
     *****************************
     *{}*{}*{}*{}*{}*{}*{}*
     *****************************
     *                           *
    ***                         ***
  """.format(empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty, empty,))

print_board()
#print(empty_spot)