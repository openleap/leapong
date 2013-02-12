from basesprite import BaseSprite
from OpenGL.GL import *
from OpenGL.GLU import *
import math

class Ball(BaseSprite):

    def __init__(self, start_pos, size):
        BaseSprite.__init__(self, start_pos, (size, size))
        self.angle = math.radians(45)
        self.speed = 0.5

    def update(self):

        if self.pos[0] > 800:
            self.angle = - self.angle

        elif self.pos[0] < 0:
            self.angle = - self.angle

        if self.pos[1] > 600:
            self.angle = math.pi - self.angle

        elif self.pos[1] < 0:
            self.angle = math.pi - self.angle

        delta_y = self.speed * math.cos(self.angle)
        delta_x = self.speed * math.sin(self.angle)
        self.set_position(self.pos[0] + delta_x, self.pos[1] - delta_y)

    def render(self):
        glBegin(GL_QUADS)
        glColor3ub(155, 0, 0);
        glVertex2f(self.pos[0], self.pos[1]);
        glVertex2f(self.pos[0], self.pos[1] + self.size[0]);
        glVertex2f(self.pos[0] + self.size[0], self.pos[1] + self.size[0]);
        glVertex2f(self.pos[0] + self.size[0], self.pos[1]);
        glEnd()
