import pygame
from pygame.locals import *
from constants import *

class KamisadoGUI:
    def __init__(self, game):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Kamisado")
        self.game = game
        self.selected = None
        self.valid_moves = []
        self.font = pygame.font.Font(None, 24)
        self.tower_font = pygame.font.Font(None, 36)  # Font più grande per le lettere

    def draw_board(self):
        # Sfondo e bordo
        self.screen.fill((200, 200, 200))
        pygame.draw.rect(self.screen, BORDER_COLOR, (0, 0, CELL_SIZE*8, CELL_SIZE*8), 3)

        # Celle e torri
        for row in range(8):
            for col in range(8):
                # Cella
                cell_color = COLORI[BOARD_COLORS[row][col]]
                pygame.draw.rect(self.screen, cell_color, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))

                # Torre
                piece = self.game.board[row][col]
                if piece:
                    player, color = piece
                    self.draw_tower(col, row, player, cell_color)

    def draw_tower(self, col, row, player, cell_color):
        # Colori
        main_color = (255, 255, 255) if player == 1 else (0, 0, 0)
        border_color = (0, 0, 0) if player == 1 else (255, 255, 255)
        
        # Posizioni
        x = col * CELL_SIZE + CELL_SIZE//2
        y = row * CELL_SIZE + CELL_SIZE//2
        radius = CELL_SIZE//3
        
        # Disegno solo per caselle non nere
        if BOARD_COLORS[row][col] != "N":
            # Bordo esterno
            pygame.draw.circle(self.screen, border_color, (x, y), radius + 4)
            
            # Corpo principale
            pygame.draw.circle(self.screen, main_color, (x, y), radius)
            
            # Anello intermedio
            pygame.draw.circle(self.screen, border_color, (x, y), radius - 8, 4)
        
        # Lettera iniziale colore
        letter = BOARD_COLORS[row][col][0]
        text_color = border_color if BOARD_COLORS[row][col] == "N" else main_color
        text = self.tower_font.render(letter, True, text_color)
        text_rect = text.get_rect(center=(x, y))
        self.screen.blit(text, text_rect)

    def draw_ui(self):
        # Sidebar
        sidebar = pygame.Rect(CELL_SIZE*8, 0, WINDOW_WIDTH - CELL_SIZE*8, WINDOW_HEIGHT)
        pygame.draw.rect(self.screen, (240, 240, 240), sidebar)
        
        # Testo giocatore
        player_text = self.font.render(f"Turno: Giocatore {self.game.current_player}", True, (0, 0, 0))
        self.screen.blit(player_text, (CELL_SIZE*8 + 20, 20))
        
        # Colore attivo
        if self.game.active_color:
            color_text = self.font.render("Colore obbligatorio:", True, (0, 0, 0))
            self.screen.blit(color_text, (CELL_SIZE*8 + 20, 60))
            pygame.draw.rect(self.screen, COLORI[self.game.active_color], (CELL_SIZE*8 + 20, 90, 40, 40))

    def handle_click(self, pos):
        x, y = pos
        if x < CELL_SIZE*8:  # Click sulla scacchiera
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            
            if self.selected:
                if (row, col) in self.valid_moves:
                    if self.game.make_move(*self.selected, row, col):
                        print(f"Giocatore {self.game.current_player} vince!")
                        pygame.quit()
                        exit()
                    self.selected = None
                    self.valid_moves = []
                else:
                    self.selected = None
                    self.valid_moves = []
            else:
                piece = self.game.board[row][col]
                if piece and piece[0] == self.game.current_player:
                    if not self.game.active_color or piece[1] == self.game.active_color:
                        self.selected = (row, col)
                        self.valid_moves = self.game.get_valid_moves(row, col)

    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            # Disegno
            self.draw_board()
            self.draw_ui()
            
            # Evidenzia mosse valide
            if self.selected:
                for r, c in self.valid_moves:
                    x = c * CELL_SIZE + CELL_SIZE//2
                    y = r * CELL_SIZE + CELL_SIZE//2
                    pygame.draw.circle(self.screen, (255, 255, 0), (x, y), 5)

            pygame.display.flip()
            clock.tick(30)
        
        pygame.quit()