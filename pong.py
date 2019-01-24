import pygame
from ball import Ball
pygame.init()

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 256

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Pong")


ball = Ball(256, 128, 5, 10, 10)
run = True

while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if(ball.xpos <= 0):
        ball.reverseXVel()
    if(ball.xpos >= SCREEN_WIDTH):
        ball.reverseXVel()
    if(ball.ypos <= 0):
        ball.reverseYVel()
    if(ball.ypos >= SCREEN_HEIGHT):
        ball.reverseYVel()
        
    ball.updatePosition()


    win.fill((55,55,55))
    pygame.draw.circle(win, (200, 200, 200), (ball.xpos, ball.ypos), ball.rad, 0)
    pygame.display.update()

pygame.quit()

