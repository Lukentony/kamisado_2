import pygame
from pygame.locals import *
from constants import COLORS, CELL_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT

class Lesson:
    def __init__(self, title, description, example_board, interactive_step=None):
        self.title = title
        self.description = description
        self.example_board = example_board
        self.interactive_step = interactive_step
        self.is_completed = False

class TutorialManager:
    def __init__(self):
        self.lessons = self.load_lessons()
        self.current_lesson_index = 0
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        self.is_running = False

    def load_lessons(self):
        return [
            Lesson(
                title="Introduzione a Kamisado",
                description="Muovi le torri in base al colore attivo.",
                example_board=[
                    ['R', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', 'B']
                ],
                interactive_step=lambda: self.simulate_move((0, 0), (3, 3))
            ),
            Lesson(
                title="Mosse obbligatorie",
                description="Devi muovere la torre del colore attivo.",
                example_board=[
                    ['R', 'G', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', 'B']
                ]
            )
        ]

    def simulate_move(self, start, end):
        # Simula una mossa per l'interazione
        print(f"Simulazione: da {start} a {end}")
        return True

    def run_tutorial(self, screen):
        self.is_running = True
        while self.is_running:
            self.handle_input()
            self.show_lesson(screen)
            pygame.display.flip()

    def show_lesson(self, screen):
        screen.fill(COLORS['white'])
        lesson = self.lessons[self.current_lesson_index]

        # Titolo
        title_surface = self.font.render(lesson.title, True, COLORS['black'])
        screen.blit(title_surface, (50, 50))

        # Descrizione
        desc_surface = self.small_font.render(lesson.description, True, COLORS['black'])
        screen.blit(desc_surface, (50, 100))

        # Esempio di scacchiera
        self.draw_example_board(screen, lesson.example_board, (50, 150))

        # Progresso
        self.draw_progress(screen)

    def draw_example_board(self, screen, board, position):
        x, y = position
        for row in range(len(board)):
            for col in range(len(board[row])):
                rect = pygame.Rect(x + col*CELL_SIZE, y + row*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, COLORS['gray'], rect, 1)
                if board[row][col] != ' ':
                    piece_surface = self.font.render(board[row][col], True, COLORS['black'])
                    screen.blit(piece_surface, (x + col*CELL_SIZE + 20, y + row*CELL_SIZE + 20))

    def draw_progress(self, screen):
        progress_text = f"Lezione {self.current_lesson_index + 1} di {len(self.lessons)}"
        progress_surface = self.small_font.render(progress_text, True, COLORS['black'])
        screen.blit(progress_surface, (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 50))

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.is_running = False
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.current_lesson_index = min(self.current_lesson_index + 1, len(self.lessons) - 1)
                elif event.key == K_LEFT:
                    self.current_lesson_index = max(self.current_lesson_index - 1, 0)
                elif event.key == K_RETURN and self.lessons[self.current_lesson_index].interactive_step:
                    self.lessons[self.current_lesson_index].interactive_step()
                    self.lessons[self.current_lesson_index].is_completed = True