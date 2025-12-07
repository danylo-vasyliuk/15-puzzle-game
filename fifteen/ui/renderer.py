import os
from typing import List


class Renderer:
    @staticmethod
    def clear():
        os.system("clear")

    @staticmethod
    def draw_board(tiles: List[List[int]]):
        line = "+----" * 4 + "+"
        print(line)
        for row in tiles:
            row_str = "|"
            for n in row:
                cell = "   " if n == 0 else f"{n:3d}"
                row_str += f"{cell} |"
            print(row_str)
            print(line)

    @staticmethod
    def draw_header():
        print("=== 15 Puzzle Game ===")
        print("Goal: arrange tiles 1–15. Empty is represented as 0.")
        print("Controls: w/a/s/d move, r restart, q quit\n")

    @staticmethod
    def draw_win_message():
        print("\nYou solved the puzzle!")
