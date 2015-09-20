from basesprite import BaseSprite

from OpenGL.GL import *
from OpenGL.GLU import *

class Border(BaseSprite, object):

    def __init__(self, start_pos, size):
        BaseSprite.__init__(self, start_pos, size)
        self.top = False

    def update(self):
        pass

    def render(self):
        glBegin(GL_QUADS)
        glColor3ub(0, 0, 255);
        glVertex2f(self.boundingbox.x1, self.boundingbox.y1);
        glVertex2f(self.boundingbox.x1, self.boundingbox.y2);
        glVertex2f(self.boundingbox.x2, self.boundingbox.y2);
        glVertex2f(self.boundingbox.x2, self.boundingbox.y1);
        glEnd()