import os
import pygame

class BaseSprite():

    def __init__(self, start_pos, size):
        self.pos = start_pos
        self.size = size

    def collide(self, base_sprite):
        left1 = self.pos[0]
        left2 = base_sprite.pos[0]
        right1 = self.pos[0] + self.size[0]
        right2 = base_sprite.pos[0] + base_sprite.size[0]
        top1 = self.pos[1]
        top2 = base_sprite.pos[1]
        bottom1 = self.pos[1] + self.size[1]
        bottom2 = base_sprite.pos[1] + base_sprite.size[1]

        if bottom1 < top2:
            return True
        if top1 > bottom2:
            return True
        if right1 < left2:
            return True
        if left1 > right2:
            return True

        return False

    def update(self):
        pass

    def render(self):
        pass

    def set_position(self, x, y):
        self.pos = (x, y)