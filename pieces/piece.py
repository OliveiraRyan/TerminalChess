class Piece:
    
    def __init__(self, color, row, col, name):
        self.color = color
        self.row = row
        self.col = col

        if color == "W":
            self.label = "{}'".format(name.upper())
        else:
            self.label = "{}.".format(name.lower())

    ''' By the piece's move rules, scan the board and return a
    set of tiles that the piece can move to '''
    def scan(self):
        moveList = []
        return moveList
            
    def __str__(self):
        return self.label

    __repr__ = __str__     