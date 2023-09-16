import pygame
import random

class Ball():
    def __init__(self) -> None:
        self.ball_size = 20
        self.x = 400
        self.y = self.random_y()
        self.ball_speed = 2

        self.ball_surface = pygame.image.load('src/graph/ball.png').convert_alpha()
        self.ball_rect = self.ball_surface.get_rect(center = (self.x, self.y))

        self.ball_rect.x = self.x
        self.ball_rect.y = self.y
        self.move_x = self.random_move()
        self.move_y = self.random_move()

    def ball_movement(self) -> None:
        if self.move_x == 1:
            self.ball_rect.x += self.ball_speed
        elif self.move_x == -1:
            self.ball_rect.x -= self.ball_speed
        if self.move_y == 1:
            self.ball_rect.y += self.ball_speed
        elif self.move_y == -1:
            self.ball_rect.y -= self.ball_speed

    def random_move(self) -> None:
        number = random.randint(-1,1)
        if number == 0:
            return self.random_move()
        else:
            return number

    def random_y(self) -> int:
        number = random.randint(100,300)
        if number % 2 == 1: #only even
            return self.random_y()
        else:
            return number

    def ball_reset(self) -> None:
        self.ball_rect.x = self.x
        self.ball_rect.y = self.random_y()
        self.move_x = self.random_move()
        self.move_y = self.random_move()
