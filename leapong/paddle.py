from basesprite import BaseSprite

class Paddle(BaseSprite):
    bitmap_filename = 'paddle.png'
    UP = -1
    DOWN = 1
    STATIONARY = 0

    def __init__(self, start_pos, boundary):

        BaseSprite.__init__(self, start_pos)
        self.boundary = boundary

    def update(self):

        if self.pos[1] < self.boundary.top:
            self.pos = (self.pos[0], self.boundary.top)

        elif self.pos[1] > self.boundary.bottom:
            self.pos = (self.pos[0], self.boundary.bottom)

        self.rect.topleft = self.pos