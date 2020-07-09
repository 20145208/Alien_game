# @Time  : 2020/6/18 0018 22:56
# @Author: CaiYe
# @File  : settings.py


class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 4
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction=1 right//fleet_direction=-1 left
        self.fleet_direction = 1
