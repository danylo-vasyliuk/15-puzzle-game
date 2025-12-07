from .generator import generate_random_board_walk


class Game:
    """Coordinates the board + input handler + renderer"""

    def __init__(self):
        self.board = generate_random_board_walk()
        self.running = True

    def reset(self):
        self.board = generate_random_board_walk()

    def apply_move(self, cmd: str) -> bool:
        return self.board.move(cmd)
