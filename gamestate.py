class Board:
    def __init__(self):
        self.loadnormal()

    def loadnormal(self):
        self.pieces = []
        PATTERN_A = ['R','N','B','Q','K','B','N','R']
        PATTERN_B = ['P','P','P','P','P','P','P','P']

        for i in range(8):
            self.pieces.append(Piece(PATTERN_A[i],1,i,7))
            self.pieces.append(Piece(PATTERN_B[i],1,i,6))
            self.pieces.append(Piece(PATTERN_B[i],0,i,1))
            self.pieces.append(Piece(PATTERN_A[i],0,i,0))

    def ispieceatpos(self,x,y):
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                print(piece.type)
                return True
        return False





class Piece:
    def __init__(self, type, color,x,y):
        self.type = type
        self.color = color
        self.x = x
        self.y = y

    def getcoord(self):
        LETTER = ['a','b','c','d','e','f','g','h']
        NUMBER = ['1','2','3','4','5','6','7','8']
        return LETTER[self.x]+NUMBER[self.y]

class Gamestate:
    def __init__(self):
        self.board = Board()
        self.eaten = []
        self.selsquare = (-1,-1)

    def issquaresel(self):
        return self.selsquare != (-1,-1)




