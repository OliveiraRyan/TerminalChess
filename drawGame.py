import os
import sys
import platform
import math

from square import Square

# windows console clear command:
# os.system("CLS")


if platform.system() == "Windows":
    sys.stdout = open(sys.stdout.fileno(), mode='w',
                      encoding='utf8', buffering=1)


# init the board (inital chess board game state)
grid = []


def makeGrid():
    # global grid
    colorSwitcher = {
        "white": "black",
        "black": "white"
    }
    tileColor = "black"
    for col in range(0, 8):
        colTiles = []
        for row in range(0, 8):
            colTiles.append(Square(None, tileColor))
            tileColor = colorSwitcher[tileColor]
        grid.append(colTiles)
        tileColor = colorSwitcher[tileColor]


def drawNowPlaying():
    print(
        '  ----------------------\n'
        '  |   NOW PLAYING: W   |\n'
        '  ----------------------'
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

    for rowNum in range(1, 9):
        print(' {}  |'.format(abs(rowNum-9)), end='')
        for colTiles in range(8, 0, -1):
            print(grid[rowNum-1][colTiles-1], end='')
        print('|')

    print('     ', end='')
    for i in range(0, 8):
        print('¯¯', end='')
    print()


def drawRemainingPieces():
    pass


def drawGame():
    os.system('clear')
    makeGrid()

    drawNowPlaying()
    drawBoard()
    #TODO: Finish this function (after pieces are finished)
    drawRemainingPieces()


drawGame()
