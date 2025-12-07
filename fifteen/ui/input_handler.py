class InputHandler:
    VALID_MOVES = {"w", "a", "s", "d", "r", "q"}

    @staticmethod
    def get_command() -> str:
        cmd = input("Your move: ").strip().lower()
        return cmd if cmd in InputHandler.VALID_MOVES else ""
