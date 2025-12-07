from fifteen.game.board import Board
from fifteen.game.generator import generate_solved


def test_solved_board_is_solved():
    board = Board(generate_solved())
    assert board.is_solved()


def test_invalid_move_does_not_change_board():
    board = Board(generate_solved())
    before = [row[:] for row in board.tiles]
    board.move("x")
    assert board.tiles == before
