import os
import sys
import platform

from square import Square

# windows console clear command:     
# os.system("CLS")


if platform.system() == "Windows":
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

def drawNowPlaying():
    pass


def drawBoard():
    pass
    # print(a_block)
    # print(u'♣')
    # os.system('echo ██')
    # print('██')
    # print('五行')
    # print(block.encode('UTF-8'))
    # print(block2.decode('cp437'))

    
def drawRemainingPieces():
    pass

def drawGame():
    os.system('clear')
    whiteSquare = Square(None, "white")
    blackSquare = Square(None, "black")
    print(whiteSquare)
    print(blackSquare)
    print(whiteSquare)
    print(blackSquare)


# init the board (inital chess board game state)
    


drawGame()