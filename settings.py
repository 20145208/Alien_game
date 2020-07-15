# @Time  : 2020/6/18 0018 22:56
# @Author: CaiYe
# @File  : settings.py


class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.big_bullet_width = 500
        self.big_bullet_height = 2
        self.bullet_color = 60, 60, 60
        self.big_bullet_color = 160, 60, 60
        self.bullets_allowed = 4
        self.big_bullets_allowed = 1

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5

        # fleet_direction=1 right//fleet_direction=-1 left
        self.fleet_direction = 1

        self.alien_points = 10

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
