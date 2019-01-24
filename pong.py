import pygame
from ball import Ball
from settings import Settings
pygame.init()

settings = Settings()

win = pygame.display.set_mode((settings.screen_width, settings.screen_height))

pygame.display.set_caption(settings.title)


ball = Ball(256, 128, 5, 10, 10)
run = True

while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if(ball.xpos <= 0):
        ball.reverseXVel()
    if(ball.xpos >= settings.screen_width):
        ball.reverseXVel()
    if(ball.ypos <= 0):
        ball.reverseYVel()
    if(ball.ypos >= settings.screen_height):
        ball.reverseYVel()
        
    ball.updatePosition()


    win.fill((55,55,55))
    pygame.draw.circle(win, (200, 200, 200), (ball.xpos, ball.ypos), ball.rad, 0)
    pygame.display.update()

pygame.quit()

