
class Square:

    ALPHACOLS = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
    
    def __init__(self,row ,col, piece = None):
        self.row = row
        self.col = col
        self.piece = piece
        self.alphacol = self.ALPHACOLS[col]

    def __eq__(self,other):
        return self.row == other.row and self.col == other.col

    def has_piece(self):
        return self.piece != None
    
    def isempty(self):
        return not self.has_piece()          # no piece present
    
    def has_team_piece(self,color):
        return self.has_piece() and self.piece.color == color            #checking if piece is there and also colour is same
        
    def has_enemy_piece(self, color):
        return self.has_piece() and self.piece.color != color            #checking if piece is there and also colour is different   
    
    def isempty_or_enemy(self, color):
        return self.isempty() or self.has_enemy_piece(color)
    
    @staticmethod              #no need to create objects to call function
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:          #chess piece won't go out of the chessboard
                return False
            
        return True
    

    @staticmethod
    def get_alphacol(col):
        ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        return ALPHACOLS[col]