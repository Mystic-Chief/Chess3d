import pygame

class Piece:
    def __init__(self, color):
        self.color = color

    def valid_moves(self, pos, board):
        """This method should be overridden by each piece subclass"""
        raise NotImplementedError

    def capture_moves(self, pos, board):
        """This method should return capture moves"""
        raise NotImplementedError

class Pawn(Piece):
    def valid_moves(self, pos, board):
        row, col = pos
        direction = -1 if self.color == "white" else 1
        moves = []
        
        # Move one square forward
        if board.board[row + direction][col] is None:
            moves.append((row + direction, col))
        
        # Capture diagonally
        for dc in [-1, 1]:
            if 0 <= col + dc < 8 and 0 <= row + direction < 8:
                target = board.board[row + direction][col + dc]
                if target and target.color != self.color:
                    moves.append((row + direction, col + dc))
        
        return moves

class Rook(Piece):
    def valid_moves(self, pos, board):
        row, col = pos
        moves = []
        # Horizontal and vertical moves
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = row, col
            while 0 <= r + dr < 8 and 0 <= c + dc < 8:
                r, c = r + dr, c + dc
                if board.board[r][c] is None:
                    moves.append((r, c))
                elif board.board[r][c].color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
        return moves

class Knight(Piece):
    def valid_moves(self, pos, board):
        row, col = pos
        moves = []
        for dr, dc in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                target = board.board[r][c]
                if target is None or target.color != self.color:
                    moves.append((r, c))
        return moves

class Bishop(Piece):
    def valid_moves(self, pos, board):
        row, col = pos
        moves = []
        # Diagonal moves
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            r, c = row, col
            while 0 <= r + dr < 8 and 0 <= c + dc < 8:
                r, c = r + dr, c + dc
                if board.board[r][c] is None:
                    moves.append((r, c))
                elif board.board[r][c].color != self.color:
                    moves.append((r, c))
                    break
                else:
                    break
        return moves

class Queen(Piece):
    def valid_moves(self, pos, board):
        # Queen is a combination of rook and bishop
        row, col = pos
        moves = []
        for piece in [Rook(self.color), Bishop(self.color)]:
            moves.extend(piece.valid_moves(pos, board))
        return moves

class King(Piece):
    def valid_moves(self, pos, board):
        row, col = pos
        moves = []
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                target = board.board[r][c]
                if target is None or target.color != self.color:
                    moves.append((r, c))
        return moves
