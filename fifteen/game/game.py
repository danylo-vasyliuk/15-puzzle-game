from .generator import GenerateBoardService


class Game:
    """Coordinates the board + input handler + renderer"""

    def __init__(self, generate_board_service: GenerateBoardService):
        self.generate_board_service = generate_board_service

        self.board = self.generate_board_service.generate()
        self.running = True

    def reset(self):
        self.board = self.generate_board_service.generate()

    def apply_move(self, cmd: str) -> bool:
        return self.board.move(cmd)
