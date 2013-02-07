import os
import pygame
from pygame import sprite

class BaseSprite(sprite.Sprite):
    bitmap_filename = None
    image = None
    groups = None

    @classmethod
    def load_image(cls):
        path = os.path.join('assets', cls.bitmap_filename)
        cls.image = pygame.image.load(path)
        cls.image.convert()

    def __init__(self, start_pos):
        sprite.Sprite.__init__(self, self.groups)
        self.pos = start_pos
        self.image = self.image
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.topleft = self.pos