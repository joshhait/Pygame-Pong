import sys

import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update_screen(settings, window, ball):
    window.fill(settings.bg_color)
    pygame.draw.circle(window, ball.color, (ball.xpos, ball.ypos), ball.rad, 0)

    pygame.display.update()
