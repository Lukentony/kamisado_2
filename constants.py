CELL_SIZE = 80
WINDOW_WIDTH = CELL_SIZE * 8 + 200
WINDOW_HEIGHT = CELL_SIZE * 8 + 40
BORDER_COLOR = (100, 100, 100)
CENTER_MARKER_SIZE = 15

COLORI = {
    "V": (0, 128, 0),        # Verde
    "G": (255, 255, 0),      # Giallo
    "R": (255, 0, 0),        # Rosso
    "Vi": (128, 0, 128),     # Viola
    "Bl": (0, 0, 255),       # Blu
    "Ar": (255, 165, 0),     # Arancione
    "Ma": (139, 69, 19),     # Marrone
    "N": (0, 0, 0)           # Nero
}

BOARD_COLORS = [
    ["V", "G", "R", "Vi", "Bl", "Ar", "Ma", "N"],
    ["G", "V", "Vi", "R", "Ar", "Bl", "N", "Ma"],
    ["R", "Vi", "V", "G", "Ma", "N", "Bl", "Ar"],
    ["Vi", "R", "G", "V", "N", "Ma", "Ar", "Bl"],
    ["Bl", "Ar", "Ma", "N", "V", "G", "R", "Vi"],
    ["Ar", "Bl", "N", "Ma", "G", "V", "Vi", "R"],
    ["Ma", "N", "Bl", "Ar", "R", "Vi", "V", "G"],
    ["N", "Ma", "Ar", "Bl", "Vi", "R", "G", "V"]
]