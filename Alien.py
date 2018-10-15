import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    "A class representing a single alien ship"
    def __init__(self,setting,screen):
        "create a new ship and set its position"
        super(Alien,self).__init__()
        self.screen = screen
        self.setting = setting
        self.screen_rect = screen.get_rect()

        # load an alien image and set its rect
        self.image = pygame.image.load('Models/Space ships/spaceship 5.png')
        self.image = pygame.transform.scale(self.image, (75, 70))
        self.rect = self.image.get_rect()



    def blitme(self):
        "Draw the alien ship"
        self.screen.blit(self.image, self.rect)

    def update(self):
        " Move the alien right or left"
        self.x += (self.setting.alien_speed_factor * self.setting.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        " Return true if alien is at the edge of screen."
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0 :
            return True
