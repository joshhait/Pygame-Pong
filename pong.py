import pygame
from ball import Ball
from settings import Settings
import game_functions as gf

def run_game():
    pygame.init()
    settings = Settings()
    window = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.title)

    ball = Ball(256, 128, 5, 10, 10)
    
    while True:
        pygame.time.delay(30)

        gf.check_events()

        ball.update(settings)

        gf.update_screen(settings, window, ball)

run_game()
        

