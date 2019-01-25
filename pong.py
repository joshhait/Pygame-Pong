import pygame
from ball import Ball
from paddle import Paddle
from settings import Settings
import game_functions as gf

def run_game():
    pygame.init()
    settings = Settings()
    window = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.title)

    # initialize paddles and balls
    ball = Ball(256, 128)
    pad1 = Paddle(50, 206)
    pad2 = Paddle(974, 206)
    
    while True:
        pygame.time.delay(30)
        
        # get inputs/events
        gf.check_events(pad1, pad2)
        # update ball and paddle
        ball.update(settings)
        pad1.update()
        pad2.update()
        # draw/update the screen
        gf.update_window(settings, window, ball, pad1, pad2)
        

run_game()
        

