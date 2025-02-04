from dataclasses import dataclass
from constants import KamisadoColor, BOARD_COLORS_ORDER
from typing import List, Tuple, Optional

@dataclass
class Tower:
    color: KamisadoColor
    player: int

class KamisadoGame:
    def __init__(self):
        self.board: List[List[Optional[Tower]]] = [[None for _ in range(8)] for _ in range(8)]
        self.current_player: int = 1
        self.active_color: Optional[KamisadoColor] = None
        self.winner: Optional[int] = None
        self._init_board()

    def _init_board(self):
        for row in range(8):
            for col in range(8):
                if row == 0:
                    self.board[row][col] = Tower(color=BOARD_COLORS_ORDER[row][col], player=1)
                elif row == 7:
                    self.board[row][col] = Tower(color=BOARD_COLORS_ORDER[row][col], player=2)

    def get_valid_moves(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        row, col = position
        moves = []
        
        if self.board[row][col] is None or self.board[row][col].player != self.current_player:
            return moves

        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                if self.board[r][c] is None:
                    moves.append((r, c))
                    r += dr
                    c += dc
                else:
                    break
        return moves

    def make_move(self, start_pos: Tuple[int, int], end_pos: Tuple[int, int]) -> bool:
        if self.winner is not None:
            return False

        if end_pos not in self.get_valid_moves(start_pos):
            return False

        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Muovi la torre
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = None

        # Aggiorna colore attivo
        self.active_color = BOARD_COLORS_ORDER[end_row][end_col]

        # Controlla vittoria
        if (self.current_player == 1 and end_row == 7) or (self.current_player == 2 and end_row == 0):
            self.winner = self.current_player
            return True

        # Cambia giocatore solo se non c'è un colore attivo obbligatorio
        self.current_player = 2 if self.current_player == 1 else 1
        return True