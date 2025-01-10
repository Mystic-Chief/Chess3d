import pytest
from chess.board import Board

def test_setup():
    board = Board()
    board.setup()
    assert board.board[1][0] == ('P', 'black')  # Pawn
    assert board.board[7][4] == ('K', 'white')  # King
