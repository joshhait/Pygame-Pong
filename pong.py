import pygame
pygame.init()

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 256

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Pong")

# ball conditions
ball_x = 256
ball_y = 128
ball_rad = 5
ball_x_vel = 10
ball_y_vel = 10

run = True

while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    if(ball_x <= 0):
        ball_x_vel = -ball_x_vel
    if(ball_x >= 512):
        ball_x_vel = -ball_x_vel
    if(ball_y <= 0):
        ball_y_vel = -ball_y_vel
    if(ball_y >= 256):
        ball_y_vel = -ball_y_vel
    ball_x += ball_x_vel
    ball_y += ball_y_vel


    win.fill((55,55,55))
    pygame.draw.circle(win, (200, 200, 200), (ball_x, ball_y), ball_rad, 0)
    pygame.display.update()

pygame.quit()

