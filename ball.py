import pygame

class Ball:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.width = 7
        self.height = 7
        self.xvel = 16
        self.yvel = 16
        self.color = (200, 200, 200)

        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)

    def update(self, settings, pad1, pad2):
        if self.xpos <= 0:
            self.xvel = -self.xvel
        elif self.xpos >= settings.screen_width:
            self.xvel = -self.xvel
        elif self.ypos <= 0:
            self.yvel = -self.yvel
        elif self.ypos >= settings.screen_height:
            self.yvel = -self.yvel
        if self.rect.colliderect(pad1):
            self.xvel = -self.xvel
        if self.rect.colliderect(pad2):
            self.xvel = -self.xvel
            
        self.xpos += self.xvel
        self.ypos += self.yvel
        self.rect = pygame.Rect(self.xpos, self.ypos, self.width, self.height)
        
