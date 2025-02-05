from game_logic import KamisadoGame
from gui import KamisadoGUI

if __name__ == "__main__":
    game = KamisadoGame()
    gui = KamisadoGUI(game)
    gui.run()