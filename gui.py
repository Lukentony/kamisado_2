import pygame
from pygame.locals import *
from constants import *
from game_logic import KamisadoGame

class KamisadoGUI:
    def __init__(self, game: KamisadoGame):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Kamisado")
        self.game = game
        self.selected_piece: Optional[Tuple[int, int]] = None
        self.valid_moves: List[Tuple[int, int]] = []

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = BOARD_COLORS_ORDER[row][col].value
                rect = pygame.Rect(col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, color, rect)

                if (row, col) == self.selected_piece:
                    pygame.draw.rect(self.screen, HIGHLIGHT_COLOR, rect, 3)

    def draw_pieces(self):
        for row in range(8):
            for col in range(8):
                tower = self.game.board[row][col]
                if tower:
                    x = col * CELL_SIZE + CELL_SIZE//2
                    y = row * CELL_SIZE + CELL_SIZE//2
                    pygame.draw.circle(self.screen, 
                                     PLAYER_COLORS[tower.player], 
                                     (x, y), 
                                     CELL_SIZE//3)
                    
                    # Disegna numero giocatore
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(tower.player), True, (0, 0, 0))
                    text_rect = text.get_rect(center=(x, y))
                    self.screen.blit(text, text_rect)

    def handle_click(self, pos):
        col = pos[0] // CELL_SIZE
        row = pos[1] // CELL_SIZE

        if not (0 <= row < 8 and 0 <= col < 8):
            return

        if self.selected_piece:
            if (row, col) in self.valid_moves:
                if self.game.make_move(self.selected_piece, (row, col)):
                    self.selected_piece = None
                    self.valid_moves = []
            else:
                self.selected_piece = None
                self.valid_moves = []
        else:
            tower = self.game.board[row][col]
            if tower and tower.player == self.game.current_player:
                self.selected_piece = (row, col)
                self.valid_moves = self.game.get_valid_moves((row, col))

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    self.handle_click(pygame.mouse.get_pos())

            self.screen.fill((0, 0, 0))
            self.draw_board()
            self.draw_pieces()
            
            # Disegna mosse valide
            for (row, col) in self.valid_moves:
                pygame.draw.circle(self.screen, HIGHLIGHT_COLOR, 
                                 (col*CELL_SIZE + CELL_SIZE//2, row*CELL_SIZE + CELL_SIZE//2), 
                                 10)

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()