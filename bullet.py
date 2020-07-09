# @Time  : 2020/6/23 0023 23:21
# @Author: CaiYe
# @File  : bullet.py


import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Big_bullet(Bullet):
    def __init__(self, ai_settings, screen, ship):
        super().__init__(ai_settings, screen, ship)
        self.rect = pygame.Rect(0, 0, ai_settings.big_bullet_width, ai_settings.big_bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.color = ai_settings.big_bullet_color


