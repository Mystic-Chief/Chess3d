class Rules:
    @staticmethod
    def is_checkmate(board, king_position, color):
        """Check if the king of the given color is in checkmate."""
        # Check if the king is in check
        if not Rules.is_check(board, king_position, color):
            return False
        
        # Check if the king can escape the check
        row, col = king_position
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                piece = board.board[r][c]
                if piece is None or piece.color != color:
                    # Check if the king can move to the square and not be in check
                    if not Rules.is_check(board, (r, c), color):
                        return False

        # Check if any other piece can block the check or capture the attacking piece
        for row in range(8):
            for col in range(8):
                piece = board.board[row][col]
                if piece and piece.color == color:
                    valid_moves = piece.valid_moves((row, col), board)
                    for move in valid_moves:
                        if not Rules.is_check(board, move, color):
                            return False
        return True

    @staticmethod
    def is_stalemate(board, color):
        """Check if the given color is in stalemate (not in check, but no valid moves)."""
        for row in range(8):
            for col in range(8):
                piece = board.board[row][col]
                if piece and piece.color == color:
                    valid_moves = piece.valid_moves((row, col), board)
                    if valid_moves:
                        return False
        return True

    @staticmethod
    def is_check(board, king_position, color):
        """Check if the king of the given color is in check."""
        row, col = king_position
        # Check all directions for pieces that could attack the king
        for r in range(8):
            for c in range(8):
                piece = board.board[r][c]
                if piece and piece.color != color:
                    if (row, col) in piece.valid_moves((r, c), board):
                        return True
        return False

    @staticmethod
    def is_valid_move(start, end, board):
        """Validate if the move from start to end is legal for the piece at start."""
        start_row, start_col = start
        end_row, end_col = end
        piece = board.board[start_row][start_col]
        
        if piece is None:
            return False  # No piece to move
        
        valid_moves = piece.valid_moves((start_row, start_col), board)
        if (end_row, end_col) in valid_moves:
            target_piece = board.board[end_row][end_col]
            if target_piece is None or target_piece.color != piece.color:
                return True  # Move is valid
        return False
