import pygame
import time
from sys import exit
from abc import ABC, abstractmethod

import data
import paddles
import ball
import players

#strategy_pattern
class Game_strategy(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def build_game(self, data: data.Data, paddles: paddles.Paddles, ball: ball.Ball) -> None:
        pass

class Menu(Game_strategy):
    def __str__(self) -> str:
        return "Menu"

    def build_game(self, data: data.Data, paddles: paddles.Paddles, ball: ball.Ball) -> None:
        def menu_objects() -> None:
            data.data_menu() #wywolanie def. funkcji z obiektami menu.

            data.screen.fill((89,89,89))
            data.screen.blit(data.main_menu, (50, 0))
            data.screen.blit(data.logo_surface, (80, 100))
            data.screen.blit(data.play_button, (150, 200))
            data.screen.blit(data.play_text, (175, 212))
            data.screen.blit(data.play_button, (150, 300))
            data.screen.blit(data.exit_button, (175, 312))

            data.screen.blit(paddles.paddle, (130, 450))
            data.screen.blit(paddles.paddle, (250, 450))
            data.screen.blit(ball.ball_surface, (190, 530))

        menu_objects()

class Game(Game_strategy):
    def __init__(self) -> None:
        self.players = players.Players()

    def __str__(self) -> str:
        return "Game"

    def build_game(self, data: data.Data, paddles: paddles.Paddles, ball: ball.Ball) -> None:
        def game_modes() -> None:
            #game mode = 3 (running)
            if data.game_mode == 3:
                ball.ball_movement()
                paddles.paddles_movement(data)
                game_logic()
            #game mode = 2 (before run)
            elif data.game_mode == 2:
                time.sleep(1)
                data.game_mode = 3
            #game mode = 1 (start / restart)
            elif data.game_mode == 1:
                paddles.paddles_reset()
                ball.ball_reset()
                data.data_reset()
                data.game_mode = 2
            #game mode = 0 (load objects)
            elif data.game_mode == 0:
                self.players.players_reset()
                data.data_game() #load game objects
                data.game_mode = 1

        def game_objects() -> None:
            data.screen.blit(data.bottom_panel_surface, (0, data.game_height))
            #ball + paddles + players
            data.screen.blit(ball.ball_surface, ball.ball_rect)
            data.screen.blit(paddles.paddle, paddles.paddle_1_rect)
            data.screen.blit(paddles.paddle, paddles.paddle_2_rect)
            data.screen.blit(self.players.player_1_surface, (40, 430))
            data.screen.blit(self.players.player_2_surface, (730, 430))
            #game_buttons
            data.screen.blit(data.play_button, (350, 425))
            data.screen.blit(data.exit_button, (375, 437))
            data.screen.blit(data.play_button, (225, 425))
            data.screen.blit(data.restart_button, (234, 437))
            data.screen.blit(data.play_button, (475, 425))
            data.screen.blit(data.menu_button, (493, 437))
            #speed_clock
            speed_text = data.font_clock.render("Speed: "+str(data.clock_speed), True, "White")
            data.screen.blit(speed_text, (350, 405))

        def game_logic() -> None:
            if ball.ball_rect.y == data.game_height - ball.ball_size:
                ball.move_y = -1
            if ball.ball_rect.x == data.game_width - ball.ball_size: #right side
                self.players.player_1_point()
                time.sleep(2)
                data.game_mode = 1
            if ball.ball_rect.y == 0:
                ball.move_y = 1
            if ball.ball_rect.x == 0: #left side
                self.players.player_2_point()
                time.sleep(2)
                data.game_mode = 1

            if ball.ball_rect.x == 50 and (ball.ball_rect.y <= (paddles.paddle_1_rect.y + paddles.paddle_height)) \
            and ball.ball_rect.y >= (paddles.paddle_1_rect.y - ball.ball_size):
                ball.move_x = 1

            if ball.ball_rect.x == 730 and (ball.ball_rect.y <= (paddles.paddle_2_rect.y + paddles.paddle_height)) \
            and (ball.ball_rect.y >= (paddles.paddle_2_rect.y - ball.ball_size)):
                ball.move_x = -1

        def game_speed() -> None:
            if data.speed_up == 20 and data.clock_speed < 450:
                data.clock_speed += 1
                data.speed_up = 0
            data.speed_up += 1

        game_modes()
        game_objects()
        game_speed()

class Main():
    def __init__(self, data: data.Data, paddles: paddles.Paddles, ball: ball.Ball, game_strategy) -> None:
        pygame.init()
        pygame.display.set_caption("Ping pong")

        self.game_strategy = game_strategy
        self.data = data
        self.paddles = paddles
        self.ball = ball

    def build_program(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and str(self.game_strategy) == "Menu":
                    if 150 <= event.pos[0] <= 250 and 200 <= event.pos[1] <= 250:
                        self.game_strategy = Game()
                        self.data.screen = pygame.display.set_mode((self.data.game_width, self.data.game_height + 100))#800x400 - game, 800x100 - bottom panel
                    if 150 <= event.pos[0] <= 250 and 300 <= event.pos[1] <= 350:
                        pygame.quit()
                        exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and str(self.game_strategy) == "Game":
                    if 475 <= event.pos[0] <= 575 and 425 <= event.pos[1] <= 475: #menu_button
                        self.game_strategy = Menu()
                        self.data.screen = pygame.display.set_mode((self.data.game_height, self.data.game_width))
                        self.data.game_mode = 0
                    if 350 <= event.pos[0] <= 450 and 425 <= event.pos[1] <= 475: #exit_button
                        pygame.quit()
                        exit()
                    if 225 <= event.pos[0] <= 325 and 425 <= event.pos[1] <= 475: #restart_button
                        self.data.game_mode = 0

            self.data.screen.fill((0,0,0))

            self.game_strategy.build_game(self.data, self.paddles, self.ball) #game_strategy

            pygame.display.flip()
            self.data.clock.tick(self.data.clock_speed)

def main() -> None:
    main = Main(data.Data(), paddles.Paddles(), ball.Ball(), Menu())
    main.build_program()

if __name__ == '__main__':
    main()
