import pygame
from ball import Ball
from settings import Settings
import game_functions as gf

def run_game():
    pygame.init()
    settings = Settings()
    window = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.title)

    ball = Ball(256, 128)
    
    while True:
        pygame.time.delay(30)
        
        # get inputs/events
        gf.check_events()
        # update ball and paddle
        ball.update(settings)
        # draw/update the screen
        gf.update_window(settings, window, ball)

run_game()
        

