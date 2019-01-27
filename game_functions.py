import sys

import pygame

def check_keydown_events(event, pad1, pad2):
    if event.key == pygame.K_w:
        pad1.movingUp = True
    if event.key == pygame.K_UP:
        pad2.movingUp = True
    if event.key == pygame.K_s:
        pad1.movingDown = True
    if event.key == pygame.K_DOWN:
        pad2.movingDown = True

def check_keyup_events(event, pad1, pad2):
    if event.key == pygame.K_w:
        pad1.movingUp = False
    if event.key == pygame.K_UP:
        pad2.movingUp = False
    if event.key == pygame.K_s:
        pad1.movingDown = False
    if event.key == pygame.K_DOWN:
        pad2.movingDown = False

def check_events(pad1, pad2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, pad1, pad2)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, pad1, pad2)
         

def update_window(settings, window, ball, pad1, pad2):
    window.fill(settings.bg_color)
    pygame.draw.rect(window, ball.color, ball.rect, 0)
    pygame.draw.rect(window, pad1.color, pad1.rect, 0)
    pygame.draw.rect(window, pad2.color, pad2.rect, 0)
    pygame.display.update()
