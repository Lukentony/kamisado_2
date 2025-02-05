from constants import BOARD_COLORS  # Aggiungi questa linea

class KamisadoGame:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.current_player = 1
        self.active_color = None
        self.winner = None
        self._init_board()

    def _init_board(self):
        for col in range(8):
            # Giocatore 1 (riga 0)
            self.board[0][col] = (1, BOARD_COLORS[0][col])
            # Giocatore 2 (riga 7)
            self.board[7][col] = (2, BOARD_COLORS[7][col])

    def get_valid_moves(self, row, col):
        if self.board[row][col] is None or self.board[row][col][0] != self.current_player:
            return []
        
        if self.active_color and self.board[row][col][1] != self.active_color:
            return []

        moves = []
        directions = [(-1,-1), (-1,1), (1,-1), (1,1)]
        
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

    def make_move(self, start_row, start_col, end_row, end_col):
        if self.winner:
            return False

        valid_moves = self.get_valid_moves(start_row, start_col)
        if (end_row, end_col) not in valid_moves:
            return False

        # Salva il colore prima della mossa
        target_color = BOARD_COLORS[end_row][end_col]
        
        # Esegui la mossa
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = None
        
        # Aggiorna stato
        self.active_color = target_color
        
        # Controlla vittoria
        if (self.current_player == 1 and end_row == 7) or (self.current_player == 2 and end_row == 0):
            self.winner = self.current_player
            return True

        # Cambia giocatore
        self.current_player = 2 if self.current_player == 1 else 1
        return True