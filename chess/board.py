from chess.pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.current_turn = "white"
        self.setup()
    
    def setup(self):
        """Initializes the board with pieces in starting positions."""
        for col in range(8):
            self.board[1][col] = Pawn("black")
            self.board[6][col] = Pawn("white")
        
        self.board[0][0] = self.board[0][7] = Rook("black")
        self.board[7][0] = self.board[7][7] = Rook("white")
        self.board[0][1] = self.board[0][6] = Knight("black")
        self.board[7][1] = self.board[7][6] = Knight("white")
        self.board[0][2] = self.board[0][5] = Bishop("black")
        self.board[7][2] = self.board[7][5] = Bishop("white")
        self.board[0][3] = Queen("black")
        self.board[7][3] = Queen("white")
        self.board[0][4] = King("black")
        self.board[7][4] = King("white")
    
    def is_valid_move(self, start, end):
        """Checks if a move is valid, ensuring it doesn't put the king in check."""
        piece = self.board[start[0]][start[1]]
        if piece is None or piece.color != self.current_turn:
            return False
        
        if end in piece.valid_moves(start, self):
            # Simulate the move
            original_piece = self.board[end[0]][end[1]]
            self.board[end[0]][end[1]] = piece
            self.board[start[0]][start[1]] = None
            
            # Check if the move puts the king in check
            if self.is_in_check(self.current_turn):
                # Undo the move
                self.board[start[0]][start[1]] = piece
                self.board[end[0]][end[1]] = original_piece
                return False
            
            # Undo the move after validation
            self.board[start[0]][start[1]] = piece
            self.board[end[0]][end[1]] = original_piece
            return True
        
        return False
    
    def is_in_check(self, color):
        """Checks if the given color's king is under attack."""
        king_pos = None
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, King) and piece.color == color:
                    king_pos = (row, col)
                    break
        
        if king_pos is None:
            return False
        
        # Check if any opponent piece can attack the king
        opponent_color = "black" if color == "white" else "white"
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == opponent_color:
                    if king_pos in piece.valid_moves((row, col), self):
                        return True
        
        return False
    
    def is_checkmate(self, color):
        """Determines if the given color is in checkmate."""
        if not self.is_in_check(color):
            return False
        
        # Try every possible move for this color
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == color:
                    for move in piece.valid_moves((row, col), self):
                        original_piece = self.board[move[0]][move[1]]
                        self.board[move[0]][move[1]] = piece
                        self.board[row][col] = None
                        
                        if not self.is_in_check(color):
                            self.board[row][col] = piece
                            self.board[move[0]][move[1]] = original_piece
                            return False  # Found a way out of checkmate
                        
                        self.board[row][col] = piece
                        self.board[move[0]][move[1]] = original_piece
        
        return True  # No valid move found, checkmate
    
    def make_move(self, start, end):
        """Attempts to make a move if valid."""
        if self.is_valid_move(start, end):
            piece = self.board[start[0]][start[1]]
            self.board[end[0]][end[1]] = piece
            self.board[start[0]][start[1]] = None
            piece.has_moved = True  # Track first move for pawns and rooks
            
            # Switch turn
            self.current_turn = "black" if self.current_turn == "white" else "white"
            return True
        return False
