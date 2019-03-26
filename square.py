import pieces

class Square:
    def __init__(self, piece, color):
        self.piece = piece
        self.color = color
        self.block = {
            "white": '██',
            "black": '  '
        }
    
    def __str__(self):
        if (self.piece):
            return self.piece
        
        return self.block[self.color]
        
    __repr__ = __str__
        
