from gui import KamisadoGUI
from game_logic import KamisadoGame

if __name__ == "__main__":
    game = KamisadoGame()
    gui = KamisadoGUI(game)
    gui.run()