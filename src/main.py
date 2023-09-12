import pygame
import random
import time
from sys import exit

class Main():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Ping pong")

        #screen etc
        self.screen = pygame.display.set_mode((400, 800))
        self.current_state = "menu" #stan gry
        self.clock = pygame.time.Clock()
        
        #fonty
        self.font_logo = pygame.font.Font('src/font/CONSOLA.TTF',50)
        self.play_font = pygame.font.Font(None,35)
        self.exit_font = pygame.font.Font(None,35)
        self.clock_font = pygame.font.Font(None,27)
        
        #obiekty menu
        self.main_menu = pygame.Surface((300, 800))
        self.main_menu.fill((26, 26, 26))
        self.logo_surface = self.font_logo.render("Ping pong", True, "White")
        self.play_button = pygame.Surface((100, 50))
        self.play_button.fill((166, 166, 166))
        self.play_text = self.play_font.render("Play", True, "White")
        self.exit_button = self.exit_font.render("Exit", True, "White")
        
        #obiekty i zmienne gry
        self.player_1 = "0"
        self.player_2 = "0"
        self.start_guard = 0
        self.clock_speed = 100
        self.speed_up = 0
        
        self.bottom_panel_surface = pygame.Surface((800,100))
        self.bottom_panel_surface.fill((26, 26, 26))
        self.ball_surface = pygame.image.load('src/graph/ball.png').convert_alpha()
        
        self.move_x = self.random_number()
        self.move_y = self.random_number()
        self.ball_rect = self.ball_surface.get_rect(center = (400, 200))
        
        self.paddle_1_posy = 110
        self.paddle_1_height = 180
        self.paddle_1 = pygame.Surface((20, self.paddle_1_height))
        self.paddle_1.fill((255, 255, 255))
        self.paddle_1_rect = self.paddle_1.get_rect(midtop = (40, self.paddle_1_posy))
        self.paddle_2_posy = 110
        self.paddle_2_height = 180
        self.paddle_2 = pygame.Surface((20, self.paddle_2_height))
        self.paddle_2.fill((255, 255, 255))
        self.paddle_2_rect = self.paddle_2.get_rect(midtop = (760, self.paddle_2_posy))
        
        self.restart_button = self.exit_font.render("Restart", True, "White")
        self.menu_button = self.exit_font.render("Menu", True, "White")
        
        self.build_program() #start programu menu+gra
        
    def random_number(self): #losowosc pilki przy starcie gry
            number = random.randint(-1,1)
            if number == 0:
                return self.random_number()
            else:
                return number
    
    def game_start(self): #do restartu gry
        self.start_guard = 0
        self.clock_speed = 100
        self.speed_up = 0
        self.ball_rect.x = 400
        self.ball_rect.y = 200
        self.paddle_1_rect.y = 110
        self.paddle_2_rect.y = 110
        
        self.move_x = self.random_number()
        self.move_y = self.random_number()
            
    def build_program(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                #funkcje dla menu
                elif event.type == pygame.MOUSEBUTTONDOWN and self.current_state == "menu":
                    if 150 <= event.pos[0] <= 250 and 200 <= event.pos[1] <= 250:
                        self.current_state = "game"
                        self.screen = pygame.display.set_mode((800, 500))#800x400 - game, 800x100 - bottom panel
                    if 150 <= event.pos[0] <= 250 and 300 <= event.pos[1] <= 350:
                        pygame.quit()
                        exit()
                #funkcje dla gry
                elif event.type == pygame.MOUSEBUTTONDOWN and self.current_state == "game":
                    if 475 <= event.pos[0] <= 575 and 425 <= event.pos[1] <= 475: #menu
                        self.current_state = "menu"
                        self.screen = pygame.display.set_mode((400, 800))
                        self.game_start()
                        self.player_1 = "0"
                        self.player_2 = "0"
                    if 350 <= event.pos[0] <= 450 and 425 <= event.pos[1] <= 475: #exit
                        pygame.quit()
                        exit()
                    if 225 <= event.pos[0] <= 325 and 425 <= event.pos[1] <= 475: #restart
                        self.game_start()
                        self.player_1 = "0"
                        self.player_2 = "0"
                        
            self.screen.fill((0,0,0))
            #menu
            if self.current_state == "menu":
                self.screen.fill((89,89,89))
                self.screen.blit(self.main_menu, (50, 0))
                self.screen.blit(self.logo_surface, (80, 100))
                self.screen.blit(self.play_button, (150, 200))
                self.screen.blit(self.play_text, (175, 212))
                self.screen.blit(self.play_button, (150, 300))
                self.screen.blit(self.exit_button, (175, 312))
            #gra
            elif self.current_state == "game":
                self.screen.fill((0, 0, 0))
                self.screen.blit(self.bottom_panel_surface, (0, 400))
                
                #pilka + paddles
                self.screen.blit(self.ball_surface, self.ball_rect)
                self.player_1_surface = self.font_logo.render(self.player_1, True, "White")
                self.player_2_surface = self.font_logo.render(self.player_2, True, "White")
                self.screen.blit(self.player_1_surface, (40, 430))
                self.screen.blit(self.player_2_surface, (730, 430))
                self.screen.blit(self.paddle_1, self.paddle_1_rect)
                self.screen.blit(self.paddle_2, self.paddle_2_rect)
                
                #przyciski gry
                self.screen.blit(self.play_button, (350, 425))
                self.screen.blit(self.exit_button, (375, 437))
                self.screen.blit(self.play_button, (225, 425))
                self.screen.blit(self.restart_button, (234, 437))
                self.screen.blit(self.play_button, (475, 425))
                self.screen.blit(self.menu_button, (493, 437))
                
                #licznik
                self.speed_text = self.clock_font.render("Speed: "+str(self.clock_speed), True, "White")
                self.screen.blit(self.speed_text, (350, 405))
                
                #poczekaj przy poczatku gry
                if self.start_guard == 1:
                    self.start_guard = 2
                    time.sleep(1)
                
                #przyspiesz z uplywem rozgrywki
                self.speed_up += 1
                if self.speed_up == 20 and self.clock_speed < 400:
                    self.clock_speed += 1
                    self.speed_up = 0
                
                #logika pilki
                if self.move_x == 1:
                    self.ball_rect.x += 2
                    if self.start_guard == 0:self.start_guard = 1 #tylko do spowalniania na poczatku gry
                elif self.move_x == -1:
                    self.ball_rect.x -= 2  
                    if self.start_guard == 0:self.start_guard = 1 #tylko do spowalniania na poczatku gry
                if self.move_y == 1:
                    self.ball_rect.y += 2
                    if self.start_guard == 0:self.start_guard = 1 #tylko do spowalniania na poczatku gry
                elif self.move_y == -1:
                    self.ball_rect.y -= 2
                    if self.start_guard == 0:self.start_guard = 1 #tylko do spowalniania na poczatku gry
                
                if self.ball_rect.y == 400 - 20:
                    self.move_y = -1
                if self.ball_rect.x == 800 - 20:
                    time.sleep(2)
                    self.player_1 = str(int(self.player_1) + 1)
                    self.game_start()
                if self.ball_rect.y == 0:
                    self.move_y = 1
                if self.ball_rect.x == 0:
                    time.sleep(2)
                    self.player_2 = str(int(self.player_2) + 1)
                    self.game_start()
                
                if self.ball_rect.x == 50 and self.ball_rect.y <= self.paddle_1_rect.y + self.paddle_1_height and self.ball_rect.y >= self.paddle_1_rect.y - 20:
                    self.move_x = 1
                
                if self.ball_rect.x == 730 and self.ball_rect.y <= self.paddle_2_rect.y + self.paddle_2_height and self.ball_rect.y >= self.paddle_2_rect.y - 20:
                    self.move_x = -1
                
                #logika paddles
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w] and self.paddle_1_rect.y >= 0:
                    self.paddle_1_rect.y -= 2
                if keys[pygame.K_s] and self.paddle_1_rect.y + self.paddle_1_height <= 400:
                    self.paddle_1_rect.y += 2
                
                if keys[pygame.K_UP] and self.paddle_2_rect.y >= 0:
                    self.paddle_2_rect.y -= 2
                if keys[pygame.K_DOWN] and self.paddle_2_rect.y + self.paddle_2_height <= 400:
                    self.paddle_2_rect.y += 2
                
                
                
            pygame.display.flip()
            self.clock.tick(self.clock_speed) #100 tps to wartosc poczatkowa predkosci gry
   
if __name__ == '__main__':
    Main()