import pygame
pygame.init()

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 256

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Pong")

class Ball:
    def __init__(self, xpos, ypos, rad, xvel, yvel):
        self.xpos = xpos
        self.ypos = ypos
        self.rad = rad
        self.xvel = xvel
        self.yvel = yvel 


ball = Ball(256, 128, 5, 10, 10)
run = True

while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if(ball.xpos <= 0):
        ball.xvel = -ball.xvel
    if(ball.xpos >= 512):
        ball.xvel = -ball.xvel
    if(ball.ypos <= 0):
        ball.yvel = -ball.yvel
    if(ball.ypos >= 256):
        ball.yvel = -ball.yvel
        
    ball.xpos += ball.xvel
    ball.ypos += ball.yvel


    win.fill((55,55,55))
    pygame.draw.circle(win, (200, 200, 200), (ball.xpos, ball.ypos), ball.rad, 0)
    pygame.display.update()

pygame.quit()

