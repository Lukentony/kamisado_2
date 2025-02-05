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
        self.tower_font = pygame.font.Font(None, 36)

    def draw_board(self):
        self.screen.fill((200, 200, 200))
        pygame.draw.rect(self.screen, BORDER_COLOR, (0, 0, CELL_SIZE*8, CELL_SIZE*8), 3)

        for row in range(8):
            for col in range(8):
                cell_color = COLORI[BOARD_COLORS[row][col]]
                pygame.draw.rect(self.screen, cell_color, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))

                piece = self.game.board[row][col]
                if piece:
                    self.draw_tower(col, row, piece[0], cell_color)

    def draw_tower(self, col, row, player, cell_color):
        x = col * CELL_SIZE + CELL_SIZE//2
        y = row * CELL_SIZE + CELL_SIZE//2
        is_black_cell = BOARD_COLORS[row][col] == "N"
        
        # Colori dinamici
        main_color = (255, 255, 255) if player == 1 else (0, 0, 0)
        border_color = (0, 0, 0) if player == 1 else (255, 255, 255)
        text_color = border_color if is_black_cell else main_color

        if not is_black_cell:
            # Disegna torre completa
            pygame.draw.circle(self.screen, border_color, (x, y), CELL_SIZE//3 + 4)
            pygame.draw.circle(self.screen, main_color, (x, y), CELL_SIZE//3)
            pygame.draw.circle(self.screen, border_color, (x, y), CELL_SIZE//3 - 8, 4)

        # Disegna lettera
        letter = BOARD_COLORS[row][col][0]
        text = self.tower_font.render(letter, True, text_color)
        text_rect = text.get_rect(center=(x, y))
        self.screen.blit(text, text_rect)

    def draw_ui(self):
        pygame.draw.rect(self.screen, (240, 240, 240), (CELL_SIZE*8, 0, WINDOW_WIDTH - CELL_SIZE*8, WINDOW_HEIGHT))
        player_text = self.font.render(f"Turno: Giocatore {self.game.current_player}", True, (0, 0, 0))
        self.screen.blit(player_text, (CELL_SIZE*8 + 20, 20))
        
        if self.game.active_color:
            color_text = self.font.render("Colore attivo:", True, (0, 0, 0))
            self.screen.blit(color_text, (CELL_SIZE*8 + 20, 60))
            pygame.draw.rect(self.screen, COLORI[self.game.active_color], (CELL_SIZE*8 + 20, 90, 40, 40))

    def handle_click(self, pos):
        x, y = pos
        if x < CELL_SIZE*8:
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            
            if self.selected:
                if (row, col) in self.valid_moves:
                    success = self.game.make_move(*self.selected, row, col)
                    if success:
                        if self.game.winner:
                            print(f"Giocatore {self.game.winner} vince!")
                            pygame.quit()
                            exit()
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

            self.screen.fill((200, 200, 200))
            self.draw_board()
            self.draw_ui()
            
            if self.selected:
                for r, c in self.valid_moves:
                    x = c * CELL_SIZE + CELL_SIZE//2
                    y = r * CELL_SIZE + CELL_SIZE//2
                    pygame.draw.circle(self.screen, (255, 255, 0), (x, y), 5)

            pygame.display.flip()
            clock.tick(30)
        
        pygame.quit()