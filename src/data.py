import pygame

class Data():
    def __init__(self) -> None:
        self.game_width = 800
        self.game_height = 400
        self.game_mode = 0 #game mode (0-load objects, 1-start/restart, 2-before run, 3-running )
        self.clock_speed = 100
        self.speed_up = 0

        self.screen = pygame.display.set_mode((self.game_height, self.game_width))
        self.clock = pygame.time.Clock()

    def fonts(self) -> None:
        self.font_logo = pygame.font.Font('src/font/CONSOLA.TTF', 50)
        self.font_normal = pygame.font.Font(None, 35)
        self.font_clock = pygame.font.Font(None, 27)

    def data_menu(self) -> None:
        self.fonts()

        self.main_menu = pygame.Surface((self.game_height - 100, self.game_width))
        self.main_menu.fill((26, 26, 26))
        self.logo_surface = self.font_logo.render("Ping pong", True, "White")
        self.play_button = pygame.Surface((100, 50))
        self.play_button.fill((166, 166, 166))
        self.play_text = self.font_normal.render("Play", True, "White")
        self.exit_button = self.font_normal.render("Exit", True, "White")

    def data_game(self) -> None:
        self.fonts()

        self.bottom_panel_surface = pygame.Surface((self.game_width, 100))
        self.bottom_panel_surface.fill((26, 26, 26))
        self.restart_button = self.font_normal.render("Restart", True, "White")
        self.menu_button = self.font_normal.render("Menu", True, "White")

    def data_reset(self) -> None:
        self.clock_speed = 100
        self.speed_up = 0
