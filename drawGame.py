import os
import sys
import platform
import math
import pieces

from square import Square

# windows console clear command:
# os.system("CLS")


if platform.system() == "Windows":
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)


# init the board (inital chess board game state)
grid = []

# init the remaining pieces on the board
piecesRemaining = {
    "WhitePawn": 8,
    "WhiteRook": 2,
    "WhiteKnight": 2,
    "WhiteBishop": 2,
    "WhiteQueen": 1,
    "WhiteKing": 1,

    "BlackPawn": 8,
    "BlackRook": 2,
    "BlackKnight": 2,
    "BlackBishop": 2,
    "BlackQueen": 1,
    "BlackKing": 1
}

# Current player's turn
playerTurn = 'W'


def makeGrid():
    # global grid
    colorSwitcher = {
        "white": "black",
        "black": "white"
    }
    # If playerColor = White, tileColor = black, and vice versa
    tileColor = "black"
    for row in range(0, 8):
        rowTiles = []
        for col in range(0, 8):
            rowTiles.append(Square(None, tileColor))
            tileColor = colorSwitcher[tileColor]

        grid.append(rowTiles)
        tileColor = colorSwitcher[tileColor]




    # init pawns
    for col in range(0, 8):
        grid[1][col].piece = pieces.Pawn("W", 1, col)
        grid[6][col].piece = pieces.Pawn("B", 6, col)

    # init rest of pieces
    grid[0][0].piece = pieces.Rook("W", 0, 0)
    grid[0][1].piece = pieces.Knight("W", 0, 1)
    grid[0][2].piece = pieces.Bishop("W", 0, 2)
    grid[0][3].piece = pieces.Queen("W", 0, 3)
    grid[0][4].piece = pieces.King("W", 0, 4)
    grid[0][5].piece = pieces.Bishop("W", 0, 5)
    grid[0][6].piece = pieces.Knight("W", 0, 6)
    grid[0][7].piece = pieces.Rook("W", 0, 7)

    grid[7][0].piece = pieces.Rook("B", 6, 0)
    grid[7][1].piece = pieces.Knight("B", 6, 1)
    grid[7][2].piece = pieces.Bishop("B", 6, 2)
    grid[7][3].piece = pieces.Queen("B", 6, 3)
    grid[7][4].piece = pieces.King("B", 6, 4)
    grid[7][5].piece = pieces.Bishop("B", 6, 5)
    grid[7][6].piece = pieces.Knight("B", 6, 6)
    grid[7][7].piece = pieces.Rook("B", 6, 7)
    

def drawNowPlaying():
    print(
'''  ----------------------
  |   NOW PLAYING: {}   |
  ----------------------'''.format(playerTurn)
    )


def drawBoard():
    # global grid
    print('     ', end='')
    for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        print(i+' ', end='')
    print()

    print('     ', end='')
    for i in range(0,8):
        print('__', end='')
    print()

    #if playerColor = Black,  for rowNum in range(0, 8):
    #    print(' {}  |'.format(abs(rowNum-1), end='')
    for rowNum in range(7, -1, -1):
        print(' {}  |'.format(rowNum+1), end='')
        for colTiles in range(0, 8):
            print(grid[rowNum][colTiles], end='')
        print('|')

    print('     ', end='')
    for i in range(0, 8):
        print('¯¯', end='')
    print()


def drawRemainingPieces():
    # global piecesRemaining
    print(
''' REMAINING:
 _______________________ 
   White:   |   Black:
  {WhitePawn}P'  {WhiteRook}R'  |  {BlackPawn}p.  {BlackRook}r.
  {WhiteKnight}N'  {WhiteBishop}B'  |  {BlackKnight}n.  {BlackBishop}b.
  {WhiteQueen}Q'  {WhiteKing}K'  |  {BlackQueen}q.  {BlackKing}k.'''.format(
      WhitePawn=piecesRemaining["WhitePawn"],
      WhiteRook=piecesRemaining["WhiteRook"],
      WhiteKnight=piecesRemaining["WhiteKnight"],
      WhiteBishop=piecesRemaining["WhiteBishop"],
      WhiteQueen=piecesRemaining["WhiteQueen"],
      WhiteKing=piecesRemaining["WhiteKing"],

      BlackPawn=piecesRemaining["BlackPawn"],
      BlackRook=piecesRemaining["BlackRook"],
      BlackKnight=piecesRemaining["BlackKnight"],
      BlackBishop=piecesRemaining["BlackBishop"],
      BlackQueen=piecesRemaining["BlackQueen"],
      BlackKing=piecesRemaining["BlackKing"]
      ))


def drawGame():
    os.system('clear')

    drawNowPlaying()
    drawBoard()
    drawRemainingPieces()


makeGrid()
drawGame()
