import pytest

from fifteen.game.generator import (
    generate_solved,
    GenerateRandomBoardWalk,
    GenerateRandomBoardPermutation,
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


def test_invalid_board_unsolvable():
    # A known unsolvable configuration
    tiles = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 12, 11],  # swapped last two → unsolvable
        [13, 14, 15, 0],
    ]
    assert is_solvable(tiles) is False


class TestGenerateRandomBoardPermutation:
    @pytest.fixture
    def service(self):
        return GenerateRandomBoardPermutation()

    def test_permutation_generator_produces_solvable(self, service):
        board = service.generate()
        assert is_solvable(board.tiles)

    def test_permutation_generator_produces_valid_tiles(self, service):
        board = service.generate()
        flat = flatten(board.tiles)
        assert sorted(flat) == list(range(16))

    def test_multiple_random_permutations_solvable(self, service):
        boards = [service.generate() for _ in range(50)]
        assert all(is_solvable(b.tiles) for b in boards)

    def test_permutation_generator_never_produces_solved_in_practice(self, service):
        boards = [service.generate() for _ in range(20)]
        assert any(not b.is_solved() for b in boards)


class TestGenerateRandomBoardWalk:
    @pytest.fixture
    def service(self):
        return GenerateRandomBoardWalk()

    def test_random_walk_produces_solvable(self, service):
        board = service.generate()
        assert is_solvable(board.tiles)

    def test_random_walk_produces_valid_tiles(self, service):
        board = service.generate()
        flat = flatten(board.tiles)
        assert sorted(flat) == list(range(16))

    def test_random_walk_with_zero_steps_produces_solved(self, service):
        service._steps = 0
        board = service.generate()
        assert board.is_solved()

    def test_random_walk_changes_board_for_large_steps(self, service):
        board = service.generate()
        assert not board.is_solved()  # almost impossible to stay solved

    @pytest.mark.parametrize("steps", [1, 5, 10, 50, 100, 200, 500])
    def test_random_walk_various_steps(self, service, steps):
        service._steps = steps
        board = service.generate()
        assert is_solvable(board.tiles)

    def test_multiple_random_walks_valid(self, service):
        boards = [service.generate() for _ in range(50)]
        for b in boards:
            flat = flatten(b.tiles)
            assert sorted(flat) == list(range(16))
            assert is_solvable(b.tiles)
