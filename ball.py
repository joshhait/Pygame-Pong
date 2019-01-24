class Ball:
    def __init__(self, xpos, ypos, rad, xvel, yvel):
        self.xpos = xpos
        self.ypos = ypos
        self.rad = rad
        self.xvel = xvel
        self.yvel = yvel
        self.color = (200, 200, 200)

    def update(self, settings):
        if self.xpos <= 0:
            self.xvel = -self.xvel
        elif self.xpos >= settings.screen_width:
            self.xvel = -self.xvel
        elif self.ypos <= 0:
            self.yvel = -self.yvel
        elif self.ypos >= settings.screen_height:
            self.yvel = -self.yvel

        self.xpos += self.xvel
        self.ypos += self.yvel
