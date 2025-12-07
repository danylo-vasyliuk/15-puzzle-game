from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    row: int
    col: int


class Board:
    SIZE = 4
    EMPTY = 0

    def __init__(self, tiles: list[list[int]]):
        self._tiles = tiles

    @property
    def tiles(self) -> list[list[int]]:
        return self._tiles

    def find_empty(self) -> Position:
        for r in range(self.SIZE):
            for c in range(self.SIZE):
                if self._tiles[r][c] == self.EMPTY:
                    return Position(r, c)
        raise RuntimeError("Empty tile not found.")

    def move(self, direction: str) -> bool:
        """Move empty tile; returns True if move succeeds."""
        direction = direction.lower()
        empty = self.find_empty()

        delta = {
            "w": Position(-1, 0),
            "s": Position(1, 0),
            "a": Position(0, -1),
            "d": Position(0, 1),
        }

        if direction not in delta:
            return False

        target = Position(
            empty.row + delta[direction].row, empty.col + delta[direction].col
        )

        if not (0 <= target.row < self.SIZE and 0 <= target.col < self.SIZE):
            return False

        # Swap
        self._tiles[empty.row][empty.col], self._tiles[target.row][target.col] = (
            self._tiles[target.row][target.col],
            self._tiles[empty.row][empty.col],
        )
        return True

    def is_solved(self) -> bool:
        """Check if puzzle is in solved state."""
        expected = list(range(1, self.SIZE * self.SIZE)) + [self.EMPTY]
        flat = [cell for row in self._tiles for cell in row]
        return flat == expected
