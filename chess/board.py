from chess.pieces import Pawn, Rook, Knight, Bishop, Queen, King
class Board:
    def __init__(self):
        # Create an 8x8 board initialized with None
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def reset(self):
        """Reset the board and pieces to their initial state."""
        # Create a new board instance, ensuring all previous state is cleared
        self.board = [[None for _ in range(8)] for _ in range(8)]  # Clear the board
        self.setup()  # Call the setup method to place pieces in their starting positions

    def setup(self):
        """Set up the initial chess positions."""
        # Place pawns
        for col in range(8):
            self.board[1][col] = Pawn("black")
            self.board[6][col] = Pawn("white")

        # Place rooks
        self.board[0][0] = Rook("black")
        self.board[0][7] = Rook("black")
        self.board[7][0] = Rook("white")
        self.board[7][7] = Rook("white")

        # Place knights
        self.board[0][1] = Knight("black")
        self.board[0][6] = Knight("black")
        self.board[7][1] = Knight("white")
        self.board[7][6] = Knight("white")

        # Place bishops
        self.board[0][2] = Bishop("black")
        self.board[0][5] = Bishop("black")
        self.board[7][2] = Bishop("white")
        self.board[7][5] = Bishop("white")

        # Place queens
        self.board[0][3] = Queen("black")
        self.board[7][3] = Queen("white")

        # Place kings
        self.board[0][4] = King("black")
        self.board[7][4] = King("white")

    def display(self):
        for row in self.board:
            print(" ".join([f"{piece.__class__.__name__[0]}({piece.color[0]})" if piece else "." for piece in row]))

    def apply_move(self, move):
        # Example: 'e2 e4'
        start, end = move.split()
        start_row, start_col = self._convert_position(start)
        end_row, end_col = self._convert_position(end)

        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = None

    def _convert_position(self, pos):
        col = ord(pos[0].lower()) - ord('a')  # Convert 'a'-'h' to 0-7
        row = 8 - int(pos[1])  # Convert '1'-'8' to 7-0
        return row, col
