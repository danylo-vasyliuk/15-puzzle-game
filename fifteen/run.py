from game.game import Game
from ui.renderer import Renderer
from ui.input_handler import InputHandler


def run():
    game = Game()

    while game.running:
        Renderer.clear()
        Renderer.draw_header()
        Renderer.draw_board(game.board.tiles)

        if game.board.is_solved():
            Renderer.draw_win_message()
            if input("Play again? [y/n]: ").lower().startswith("y"):
                game.reset()
                continue
            break

        cmd = InputHandler.get_command()

        if cmd in {"w", "a", "s", "d"}:
            game.apply_move(cmd)

        elif cmd == "r":
            game.reset()

        elif cmd == "q":
            break


if __name__ == "__main__":
    run()
