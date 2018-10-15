


class GameStats():
    "Track statistic"

    def __init__(self,ai_setting):

        self.ai_setting = ai_setting
        self.reset_stats()
        self.game_Active = False
        self.ships_left = 3
        self.high_score = 0

    def reset_stats(self):

        self.ships_left = self.ai_setting.ships_limit
        self.score = 0
        self.level = 1
