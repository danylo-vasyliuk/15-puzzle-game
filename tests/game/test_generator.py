import pytest

from fifteen.game.generator import (
    generate_solved,
    generate_random_board_permutation,
    generate_random_board_walk,
    is_solvable,
    count_inversions,
    flatten,
)


def test_solved_board_valid():
    board = generate_solved()
    flat = flatten(board)
    assert sorted(flat) == list(range(16))
    assert is_solvable(board)


def test_solved_board_inversions_zero():
    board = generate_solved()
    assert count_inversions(flatten(board)) == 0


def test_permutation_generator_produces_solvable():
    board = generate_random_board_permutation()
    assert is_solvable(board.tiles)


def test_permutation_generator_produces_valid_tiles():
    board = generate_random_board_permutation()
    flat = flatten(board.tiles)
    assert sorted(flat) == list(range(16))


def test_permutation_generator_never_produces_solved_in_practice():
    boards = [generate_random_board_permutation() for _ in range(20)]
    assert any(not b.is_solved() for b in boards)


def test_random_walk_produces_solvable():
    board = generate_random_board_walk(steps=200)
    assert is_solvable(board.tiles)


def test_random_walk_produces_valid_tiles():
    board = generate_random_board_walk()
    flat = flatten(board.tiles)
    assert sorted(flat) == list(range(16))


def test_random_walk_with_zero_steps_produces_solved():
    board = generate_random_board_walk(steps=0)
    assert board.is_solved()


def test_random_walk_changes_board_for_large_steps():
    board = generate_random_board_walk(steps=200)
    assert not board.is_solved()  # almost impossible to stay solved


def test_invalid_board_unsolvable():
    # A known unsolvable configuration
    tiles = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 12, 11],  # swapped last two → unsolvable
        [13, 14, 15, 0],
    ]
    assert is_solvable(tiles) is False


@pytest.mark.parametrize("steps", [1, 5, 10, 50, 100, 200, 500])
def test_random_walk_various_steps(steps):
    board = generate_random_board_walk(steps)
    assert is_solvable(board.tiles)


def test_multiple_random_permutations_solvable():
    boards = [generate_random_board_permutation() for _ in range(50)]
    assert all(is_solvable(b.tiles) for b in boards)


def test_multiple_random_walks_valid():
    boards = [generate_random_board_walk() for _ in range(50)]
    for b in boards:
        flat = flatten(b.tiles)
        assert sorted(flat) == list(range(16))
        assert is_solvable(b.tiles)
