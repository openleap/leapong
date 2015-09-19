from basesprite import BaseSprite
from OpenGL.GL import *
from OpenGL.GLU import *
import math

class Ball(BaseSprite, object):

    def __init__(self, start_pos, size):
        BaseSprite.__init__(self, start_pos, (size, size))
        self.angle = math.radians(45)
        self.speed = 6.0

    def update(self):
        delta_y = self.speed * math.cos(self.angle)
        delta_x = self.speed * math.sin(self.angle)
        self.set_position(
            self.boundingbox.x1 + delta_x,
            self.boundingbox.y1 - delta_y
        )

    def render(self):
        glBegin(GL_QUADS)
        glColor3ub(255, 255, 255);
        glVertex2f(self.boundingbox.x1, self.boundingbox.y1);
        glVertex2f(self.boundingbox.x1, self.boundingbox.y2);
        glVertex2f(self.boundingbox.x2, self.boundingbox.y2);
        glVertex2f(self.boundingbox.x2, self.boundingbox.y1);
        glEnd()
