from pieces import Piece
# import drawGame


class Knight(Piece):

    def __init__(self, color, row, col):
        Piece.__init__(self, color, row, col, "n")

    ''' By the piece's move rules, scan the board and return a
    set of tiles that the piece can move to '''
    def scan(self):
        moveList = []
        return moveList