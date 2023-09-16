import pygame
import data

class Paddles():
    def __init__(self) -> None:
        self.data = data.Data()

        self.y = 110
        self.paddle_1_posy = self.y
        self.paddle_2_posy = self.y
        self.paddle_height = 180
        self.paddles_speed = 2

        self.paddle = pygame.Surface((20, self.paddle_height))
        self.paddle.fill((255, 255, 255))
        self.paddle_1_rect = self.paddle.get_rect(midtop = (40, self.paddle_1_posy))

        self.paddle_2_rect = self.paddle.get_rect(midtop = (760, self.paddle_2_posy))

    def paddles_movement(self, data: data.Data) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.paddle_1_rect.y >= 0:
            self.paddle_1_rect.y -= self.paddles_speed
        if keys[pygame.K_s] and self.paddle_1_rect.y + self.paddle_height <= data.game_height:
            self.paddle_1_rect.y += self.paddles_speed

        if keys[pygame.K_UP] and self.paddle_2_rect.y >= 0:
            self.paddle_2_rect.y -= self.paddles_speed
        if keys[pygame.K_DOWN] and self.paddle_2_rect.y + self.paddle_height <= data.game_height:
            self.paddle_2_rect.y += self.paddles_speed

    def paddles_reset(self) -> None:
        self.paddle_1_rect.y = self.y
        self.paddle_2_rect.y = self.y
