from enum import Enum
import pygame

class KamisadoColor(Enum):
    RED = (242, 0, 60)
    ORANGE = (255, 148, 0)
    YELLOW = (255, 228, 0)
    GREEN = (0, 158, 73)
    BLUE = (0, 174, 239)
    PURPLE = (142, 37, 141)
    BROWN = (247, 147, 30)
    PINK = (234, 119, 179)

# Layout ufficiale Kamisado
BOARD_COLORS_ORDER = [
    [KamisadoColor.RED, KamisadoColor.GREEN, KamisadoColor.BLUE, KamisadoColor.PINK,
     KamisadoColor.YELLOW, KamisadoColor.ORANGE, KamisadoColor.BROWN, KamisadoColor.PURPLE],
    [KamisadoColor.GREEN, KamisadoColor.YELLOW, KamisadoColor.PINK, KamisadoColor.BROWN,
     KamisadoColor.RED, KamisadoColor.PURPLE, KamisadoColor.ORANGE, KamisadoColor.BLUE],
    [KamisadoColor.BLUE, KamisadoColor.PINK, KamisadoColor.RED, KamisadoColor.ORANGE,
     KamisadoColor.GREEN, KamisadoColor.BROWN, KamisadoColor.PURPLE, KamisadoColor.YELLOW],
    [KamisadoColor.PINK, KamisadoColor.BROWN, KamisadoColor.ORANGE, KamisadoColor.PURPLE,
     KamisadoColor.BLUE, KamisadoColor.YELLOW, KamisadoColor.RED, KamisadoColor.GREEN],
    [KamisadoColor.YELLOW, KamisadoColor.RED, KamisadoColor.GREEN, KamisadoColor.BLUE,
     KamisadoColor.PURPLE, KamisadoColor.PINK, KamisadoColor.BROWN, KamisadoColor.ORANGE],
    [KamisadoColor.ORANGE, KamisadoColor.PURPLE, KamisadoColor.BROWN, KamisadoColor.YELLOW,
     KamisadoColor.PINK, KamisadoColor.GREEN, KamisadoColor.BLUE, KamisadoColor.RED],
    [KamisadoColor.BROWN, KamisadoColor.ORANGE, KamisadoColor.PURPLE, KamisadoColor.RED,
     KamisadoColor.BLUE, KamisadoColor.BLUE, KamisadoColor.GREEN, KamisadoColor.PINK],
    [KamisadoColor.PURPLE, KamisadoColor.BLUE, KamisadoColor.YELLOW, KamisadoColor.GREEN,
     KamisadoColor.BROWN, KamisadoColor.RED, KamisadoColor.PINK, KamisadoColor.ORANGE]
]

CELL_SIZE = 80
WINDOW_SIZE = (CELL_SIZE * 8, CELL_SIZE * 8)
PLAYER_COLORS = {1: (255, 255, 255), 2: (0, 0, 0)}
HIGHLIGHT_COLOR = (255, 255, 0)