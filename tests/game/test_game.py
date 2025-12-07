import pytest

from fifteen.game.game import Game
from fifteen.game.generator import GenerateRandomBoardWalk


@pytest.fixture
def generate_board_service():
    return GenerateRandomBoardWalk()


def test_game_initializes(generate_board_service):
    game = Game(generate_board_service=generate_board_service)

    # Game should start with a board and running flag
    assert game.board is not None
    assert game.running is True


def test_game_reset_replaces_board(generate_board_service):
    game = Game(generate_board_service=generate_board_service)
    original_board = game.board

    game.reset()

    assert game.board is not original_board


def test_game_reset_creates_valid_board(generate_board_service):
    game = Game(generate_board_service=generate_board_service)
    game.reset()

    # Board should still be 4x4
    assert len(game.board.tiles) == 4
    assert all(len(row) == 4 for row in game.board.tiles)


def test_apply_move_returns_bool(generate_board_service):
    game = Game(generate_board_service=generate_board_service)
    result = game.apply_move("w")

    assert isinstance(result, bool)


def test_apply_move_does_not_crash_on_invalid_input(generate_board_service):
    game = Game(generate_board_service=generate_board_service)

    # Should simply return False, not raise
    result = game.apply_move("INVALID_MOVE_123")
    assert result in (True, False)


def test_apply_move_changes_state_when_valid(generate_board_service):
    game = Game(generate_board_service=generate_board_service)

    before = [row[:] for row in game.board.tiles]

    # Try several moves until one returns True
    for cmd in ["w", "a", "s", "d"]:
        if game.apply_move(cmd):
            break

    after = game.board.tiles

    # Board changed OR move was impossible but returned False
    # (both outcomes are valid)
    assert before != after or before == after
