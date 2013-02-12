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

    def collide(self, base_sprite):
        if self == base_sprite:
            return False
        return pygame.sprite.collide_mask(self, base_sprite)
        """dx = pos[0] - base_sprite.pos[0] 
        dy = pos[1] - base_sprite.pos[1]
        
        distance = math.hypot(dx, dy)
        if distance < p1.size + p2.size:
            return True
        return False"""


    def update(self):
        self.rect.topleft = self.pos

    def set_position(self, x, y):
        self.pos = (x, y)