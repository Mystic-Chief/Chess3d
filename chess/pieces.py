import pygame

class Piece:
    def __init__(self, color):
        self.color = color

    def valid_moves(self, pos, board):
        """Override in subclasses."""
        raise NotImplementedError
    
    def capture_moves(self, pos, board):
        """Override in subclasses."""
        raise NotImplementedError

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.has_moved = False

    def valid_moves(self, pos, board):
        row, col = pos
        direction = -1 if self.color == "white" else 1
        moves = []
        
        # One square forward
        if 0 <= row + direction < 8 and board.board[row + direction][col] is None:
            moves.append((row + direction, col))
        
        # Two squares forward (only if not moved)
        if not self.has_moved and 0 <= row + 2 * direction < 8 and board.board[row + 2 * direction][col] is None:
            moves.append((row + 2 * direction, col))
        
        # Capturing diagonally
        for dcol in [-1, 1]:
            if 0 <= col + dcol < 8 and 0 <= row + direction < 8:
                target = board.board[row + direction][col + dcol]
                if target and target.color != self.color:
                    moves.append((row + direction, col + dcol))
        
        return moves
    
    def capture_moves(self, pos, board):
        return self.valid_moves(pos, board)

class Rook(Piece):
    def valid_moves(self, pos, board):
        return self._linear_moves(pos, board, [(1,0), (-1,0), (0,1), (0,-1)])

    def _linear_moves(self, pos, board, directions):
        row, col = pos
        moves = []
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if board.board[r][c] is None:
                    moves.append((r, c))
                elif board.board[r][c].color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
                r += dr
                c += dc
        return moves
    
class Bishop(Piece):
    def valid_moves(self, pos, board):
        return self._linear_moves(pos, board, [(1,1), (-1,-1), (1,-1), (-1,1)])
    
class Queen(Piece):
    def valid_moves(self, pos, board):
        return self._linear_moves(pos, board, [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)])
    
class Knight(Piece):
    def valid_moves(self, pos, board):
        row, col = pos
        moves = []
        offsets = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
        
        for dr, dc in offsets:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                target = board.board[r][c]
                if target is None or target.color != self.color:
                    moves.append((r, c))
        
        return moves
    
class King(Piece):
    def valid_moves(self, pos, board):
        row, col = pos
        moves = []
        offsets = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]
        
        for dr, dc in offsets:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                target = board.board[r][c]
                if target is None or target.color != self.color:
                    moves.append((r, c))
        
        return moves
