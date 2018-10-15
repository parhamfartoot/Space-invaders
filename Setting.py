import pygame

class Settings():
    "A class to store all setting for Alien Invasion"
    def __init__(self):

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800



        # Ships speed
        self.ship_speed_factor = 1.3
        self.ships_limit = 2
        self.bullets_allowed = 4

        # Alien settings
        #self.alien_speed_factor = 1
        #self.fleet_drop_speed = 30
        # fleet_direction of 1 represents right ; -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.3
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):

        " Initialize settings that change throughout the game."
        self.ship_speed_factor = 1.3
        self.bullet_speed_factor = 20
        self.alien_speed_factor = 7
        self.fleet_drop_speed = 30

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (1200, 800))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
