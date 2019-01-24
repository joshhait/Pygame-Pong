class Ball:
    def __init__(self, xpos, ypos, rad, xvel, yvel):
        self.xpos = xpos
        self.ypos = ypos
        self.rad = rad
        self.xvel = xvel
        self.yvel = yvel

    def updatePosition(self):
        self.xpos += self.xvel
        self.ypos += self.yvel

    def reverseXVel(self):
        self.xvel = -self.xvel

    def reverseYVel(self):
        self.yvel = -self.yvel
