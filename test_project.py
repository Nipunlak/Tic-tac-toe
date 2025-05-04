import pytest

from project import check_draw, check_winner, valid_move, mark


def test_draw():
    board = [["X", "O", "X"], ["O", "X", "O"], ["X", "X", "O"]]
    another_board = [["O", "X", "O"], ["X", "O", "X"], ["O", "O", "X"]]

    assert check_draw(board) == True
    assert check_draw(another_board) == True


def test_winner():
    # player one winning
    board = [["X", "O", "X"], ["O", "X", "O"], ["O", "X", "X"]]
    assert check_winner(board, "X") == "X"

    # player two winning
    board_new = [["O", "X", 3], [4, "O", 6], ["X", "X", "O"]]
    assert check_winner(board_new, "O") == "O"


def test_vald_move():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert valid_move(1, board) == True

    assert valid_move(10, board) == False
    assert valid_move(0, board) == False

    board_new = [["X", 2, 3], [4, 5, 6], [7, 8, 9]]
    assert valid_move(1, board_new) == False


def test_mark():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with pytest.raises(ValueError):
        mark(0, board, "X")