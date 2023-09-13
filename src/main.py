import pygame
import random
import time
from sys import exit
from abc import ABC, abstractmethod

#klasa data zawierajaca zmienne i obiekty
class Data():
    #podstawowe zmienne
    def __init__(self) -> None:
        #screen etc
        self.screen = pygame.display.set_mode((400, 800))
        self.current_state = "menu" #stan gry
        self.clock = pygame.time.Clock() 
        #obiekty i zmienne gry
        self.player_1 = "0"
        self.player_2 = "0"
        self.start_guard = 0 #zmienna oznaczajaca aktualne stadium gry
        
    #czcionki
    def fonts(self) -> None: 
        #fonty
        self.font_logo = pygame.font.Font('src/font/CONSOLA.TTF',50)
        self.play_font = pygame.font.Font(None,35)
        self.exit_font = pygame.font.Font(None,35)
        self.clock_font = pygame.font.Font(None,27)
    
    #losowosc pilki przy starcie gry
    def random_number(self) -> None: 
        number = random.randint(-1,1)
        if number == 0:
            return self.random_number()
        else:
            return number

    #do restartu gry
    def game_start(self) -> None: 
        self.start_guard = 0
        self.clock_speed = 100
        self.speed_up = 0
        self.ball_rect.x = 400
        self.ball_rect.y = 200
        self.paddle_1_rect.y = 110
        self.paddle_2_rect.y = 110
        
        self.move_x = self.random_number()
        self.move_y = self.random_number()

    #obiekty menu
    def data_menu(self) -> None: 
        self.fonts()
        
        self.main_menu = pygame.Surface((300, 800))
        self.main_menu.fill((26, 26, 26))
        self.logo_surface = self.font_logo.render("Ping pong", True, "White")
        self.play_button = pygame.Surface((100, 50))
        self.play_button.fill((166, 166, 166))
        self.play_text = self.play_font.render("Play", True, "White")
        self.exit_button = self.exit_font.render("Exit", True, "White")
    
    #obiekty i zmienne gry
    def data_game(self) -> None: 
        self.fonts()
        
        self.clock_speed = 100
        self.speed_up = 0
        self.move_x = self.random_number()
        self.move_y = self.random_number()
        
        self.bottom_panel_surface = pygame.Surface((800,100))
        self.bottom_panel_surface.fill((26, 26, 26))
        
        self.ball_surface = pygame.image.load('src/graph/ball.png').convert_alpha()
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

#strategia gry
class Game_strategy(ABC):
    @abstractmethod
    def build_game(self, data: Data) -> None:
        pass

# Klasy konktetne(Menu i Game) implementujaca strategie
class Menu(Game_strategy):
    def __str__(self) -> str:
        return "Menu"
    def build_game(self, data: Data) -> None:
        data.data_menu() #wywolanie def. funkcji z obiektami menu. 
            
        data.screen.fill((89,89,89))
        data.screen.blit(data.main_menu, (50, 0))
        data.screen.blit(data.logo_surface, (80, 100))
        data.screen.blit(data.play_button, (150, 200))
        data.screen.blit(data.play_text, (175, 212))
        data.screen.blit(data.play_button, (150, 300))
        data.screen.blit(data.exit_button, (175, 312))

class Game(Game_strategy):
    def __str__(self) -> str:
        return "Game"
    
    def build_game(self, data: Data) -> None:
        if data.start_guard == 0: #tryb 0 poczatek gry
            data.data_game() #data.data_game() #wywolanie def. funkcji z obiektami gry
            data.start_guard = 1 #tryb 1 start gry
        
        data.screen.blit(data.bottom_panel_surface, (0, 400))  
        #pilka + paddles
        data.screen.blit(data.ball_surface, data.ball_rect)
        data.player_1_surface = data.font_logo.render(data.player_1, True, "White")
        data.player_2_surface = data.font_logo.render(data.player_2, True, "White")
        data.screen.blit(data.player_1_surface, (40, 430))
        data.screen.blit(data.player_2_surface, (730, 430))
        data.screen.blit(data.paddle_1, data.paddle_1_rect)
        data.screen.blit(data.paddle_2, data.paddle_2_rect)
        #przyciski gry
        data.screen.blit(data.play_button, (350, 425))
        data.screen.blit(data.exit_button, (375, 437))
        data.screen.blit(data.play_button, (225, 425))
        data.screen.blit(data.restart_button, (234, 437))
        data.screen.blit(data.play_button, (475, 425))
        data.screen.blit(data.menu_button, (493, 437))
        #licznik
        speed_text = data.clock_font.render("Speed: "+str(data.clock_speed), True, "White")
        data.screen.blit(speed_text, (350, 405))
        
        #przyspiesz z uplywem rozgrywki
        data.speed_up += 1
        if data.speed_up == 20 and data.clock_speed < 450:
            data.clock_speed += 1
            data.speed_up = 0
            
        #poczekaj przy poczatku gry
        if data.start_guard == 2:
                data.start_guard = 3
                time.sleep(1)
        
        #logika pilki      
        if data.move_x == 1:
            data.ball_rect.x += 2
            if data.start_guard == 1:data.start_guard = 2 #tylko do spowalniania na poczatku gry
        elif data.move_x == -1:
            data.ball_rect.x -= 2  
            if data.start_guard == 1:data.start_guard = 2 #tylko do spowalniania na poczatku gry
        if data.move_y == 1:
            data.ball_rect.y += 2
            if data.start_guard == 1:data.start_guard = 2 #tylko do spowalniania na poczatku gry
        elif data.move_y == -1:
            data.ball_rect.y -= 2
            if data.start_guard == 1:data.start_guard = 2 #tylko do spowalniania na poczatku gry       
        
        if data.ball_rect.y == 400 - 20:
            data.move_y = -1
        if data.ball_rect.x == 800 - 20:
            time.sleep(2)
            data.player_1 = str(int(data.player_1) + 1)
            data.game_start()
        if data.ball_rect.y == 0:
            data.move_y = 1
        if data.ball_rect.x == 0:
            time.sleep(2)
            data.player_2 = str(int(data.player_2) + 1)
            data.game_start()
                
        if data.ball_rect.x == 50 and data.ball_rect.y <= data.paddle_1_rect.y + data.paddle_1_height and data.ball_rect.y >= data.paddle_1_rect.y - 20:
            data.move_x = 1
                
        if data.ball_rect.x == 730 and data.ball_rect.y <= data.paddle_2_rect.y + data.paddle_2_height and data.ball_rect.y >= data.paddle_2_rect.y - 20:
            data.move_x = -1
        
        #logika paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and data.paddle_1_rect.y >= 0:
            data.paddle_1_rect.y -= 2
        if keys[pygame.K_s] and data.paddle_1_rect.y + data.paddle_1_height <= 400:
            data.paddle_1_rect.y += 2
                
        if keys[pygame.K_UP] and data.paddle_2_rect.y >= 0:
            data.paddle_2_rect.y -= 2
        if keys[pygame.K_DOWN] and data.paddle_2_rect.y + data.paddle_2_height <= 400:
            data.paddle_2_rect.y += 2

class Main():
    def __init__(self, data: Data, game_strategy) -> None:
        pygame.init()
        pygame.display.set_caption("Ping pong")
        self.game_strategy = game_strategy #strategia gry
        self.data = data #obiekt klasy data
        self.data_game = data.data_game()
    
    def build_program(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and str(self.game_strategy) == "Menu": # __str__ w Menu()
                    if 150 <= event.pos[0] <= 250 and 200 <= event.pos[1] <= 250:
                        self.game_strategy = Game()
                        self.data.screen = pygame.display.set_mode((800, 500))#800x400 - game, 800x100 - bottom panel
                    if 150 <= event.pos[0] <= 250 and 300 <= event.pos[1] <= 350:
                        pygame.quit()
                        exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and str(self.game_strategy) == "Game": # __str__ w Game()
                    if 475 <= event.pos[0] <= 575 and 425 <= event.pos[1] <= 475: #menu
                        self.game_strategy = Menu()
                        self.data.screen = pygame.display.set_mode((400, 800))
                        self.data.start_guard = 0
                        self.data.player_1 = "0"
                        self.data.player_2 = "0"
                    if 350 <= event.pos[0] <= 450 and 425 <= event.pos[1] <= 475: #exit
                        pygame.quit()
                        exit()
                    if 225 <= event.pos[0] <= 325 and 425 <= event.pos[1] <= 475: #restart
                        self.data.start_guard = 0
                        self.data.player_1 = "0"
                        self.data.player_2 = "0"
            
            self.data.screen.fill((0,0,0))
            
            self.game_strategy.build_game(self.data) #gra dziala wedlug aktualnej strategi
                    
            pygame.display.flip()
            self.data.clock.tick(self.data.clock_speed) #100 tps to wartosc poczatkowa predkosci gry   

def main() -> None:
    main = Main(Data(), Menu())
    main.build_program()
   
if __name__ == '__main__':
    main()