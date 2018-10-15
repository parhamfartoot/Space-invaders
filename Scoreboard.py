import pygame.font
from Setting import  Background
class Scoreboard():
    " A class to report the score"
    def __init__(self,ai_settings, screen, stats, BackGround):
        " Initialize scorekeeping attributes"




        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.back = BackGround

        # Font settings for scoring information
        self.text_color = (0, 30, 0)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        " Turn the score into a rendered image"
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)

        self.score_image = self.font.render(score_str, True, self.text_color, self.back.image)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.screen_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        "Turn the highscore into a renderd image"
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,self.back.image)

        #Center high score at the top of the screen

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        " Turn the level into a renderd image."
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.back.image)

        # Position the level below the score
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.left = self.score_rect.left
        self.level_image_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        " Draw score to the screen"
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_image_rect)