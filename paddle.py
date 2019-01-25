import pygame

class Paddle:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.width = 7
        self.height = 100
        self.color = (200, 200, 200)

        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
