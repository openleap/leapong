import os
import pygame

from .boundingbox import BoundingBox

class BaseSprite():

    def __init__(self, start_pos, size):
        self.boundingbox = BoundingBox(*(start_pos + size))

    def collide(self, base_sprite):
        return self.boundingbox.collide(base_sprite.boundingbox)

    def update(self):
        pass

    def render(self):
        pass

    def set_position(self, x, y):
        self.boundingbox.set_position(x, y)