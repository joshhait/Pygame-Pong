import sys

import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update_window(settings, window, ball, pad1, pad2):
    window.fill(settings.bg_color)
    pygame.draw.circle(window, ball.color, (ball.xpos, ball.ypos), ball.rad, 0)
    pygame.draw.rect(window, pad1.color, pad1.rect, 0)
    pygame.draw.rect(window, pad2.color, pad2.rect, 0)
    pygame.display.update()
