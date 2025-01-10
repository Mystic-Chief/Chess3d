from chess.board import Board
from chess.rules import Rules

def test_validate_move():
    board = Board()
    board.setup()
    assert Rules.validate_move(board, "e2 e4") == True
    assert Rules.validate_move(board, "e3 e4") == False
