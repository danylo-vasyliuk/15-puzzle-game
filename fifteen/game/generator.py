import random

from .board import Board


def flatten(matrix: list[list[int]]) -> list[int]:
    return [n for row in matrix for n in row]


def generate_solved() -> list[list[int]]:
    nums = list(range(1, 16)) + [0]
    return [nums[i * 4 : (i + 1) * 4] for i in range(4)]


def count_inversions(flat: list[int]) -> int:
    vals = [n for n in flat if n != 0]
    return sum(
        1
        for i in range(len(vals))
        for j in range(i + 1, len(vals))
        if vals[i] > vals[j]
    )


def is_solvable(tiles: list[list[int]]) -> bool:
    flat = flatten(tiles)
    inv = count_inversions(flat)
    empty_row = 3 - next(r for r, row in enumerate(tiles) if 0 in row)

    # Solvability rule for 4×4 board
    return (inv + empty_row) % 2 == 0


def generate_random_board_permutation() -> Board:
    nums = list(range(16))
    while True:
        random.shuffle(nums)
        tiles = [nums[i * 4 : (i + 1) * 4] for i in range(4)]
        if is_solvable(tiles):
            return Board(tiles)


def generate_random_board_walk(steps: int = 200) -> Board:
    board = Board(generate_solved())

    for _ in range(steps):
        empty = board.find_empty()

        moves = []
        if empty.row > 0:
            moves.append("w")
        if empty.row < 3:
            moves.append("s")
        if empty.col > 0:
            moves.append("a")
        if empty.col < 3:
            moves.append("d")

        board.move(random.choice(moves))

    return board
