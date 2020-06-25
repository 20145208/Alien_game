# @Time  : 2020/6/25 0025 22:58
# @Author: CaiYe
# @File  : alien.py

import pygame
from pygame.sprite import Sprite
import os


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load(os.path.join('images', 'alien.bmp'))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)