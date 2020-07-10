# @Time  : 2020/7/10 0010 21:47
# @Author: CaiYe
# @File  : game_stats.py


class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit