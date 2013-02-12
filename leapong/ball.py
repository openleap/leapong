from basesprite import BaseSprite
import math

class Ball(BaseSprite):
    bitmap_filename = 'ball.png'

    def __init__(self, start_pos, boundary):
        BaseSprite.__init__(self, start_pos)
        self.boundary = boundary
        self.angle = math.radians(45)
        self.speed = 0.3

    def update(self):
        MAXBOUNCEANGLE = 5*3.14/12

        """if self.pos[1] < self.boundary.top:
            self.angle = 180 - self.angle    

        elif self.pos[1] > self.boundary.bottom:
            self.angle = 180 - self.angle

        elif self.pos[0] < self.boundary.left:
            self.angle = 180 - self.angle    

        elif self.pos[0] > self.boundary.right:
            self.angle = 180 - self.angle


        relativeIntersectY = (640/2) - self.pos[1]
        normalizedRelativeIntersectionY = (relativeIntersectY/(640/2))
        print normalizedRelativeIntersectionY"""

        """if(self.pos[0] > 630):
            self.angle = math.radians(360) - self.angle
            self.speed *= -1

        elif(self.pos[0] < 0):
            self.angle = math.radians(360) - self.angle
            self.speed *= -1

        elif(self.pos[1] > 470):
            self.angle = math.radians(360) - self.angle
            self.speed *= 1

        elif(self.pos[1] < 0):
            self.angle = math.radians(360) - self.angle
            self.speed *= 1"""

        if self.pos[0] > 630:
            self.angle = - self.angle

        elif self.pos[0] < 0:
            self.angle = - self.angle

        if self.pos[1] > 480:
            self.angle = math.pi - self.angle

        elif self.pos[1] < 0:
            self.angle = math.pi - self.angle

        """delta_x = self.speed * math.cos(self.angle)
        delta_y = self.speed * math.sin(self.angle)
        self.set_position(self.pos[0] + delta_x, self.pos[1] + delta_y)
        self.rect.topleft = self.pos"""

        delta_y = self.speed * math.cos(self.angle)
        delta_x = self.speed * math.sin(self.angle)
        self.set_position(self.pos[0] + delta_x, self.pos[1] - delta_y)
        self.rect.topleft = self.pos

