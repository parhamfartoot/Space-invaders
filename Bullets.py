import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    "A class that manages the fired bullets from the ship"

    def __init__(self,screen, ship, settings):
        "Create a bullet object at the ship's current position"
        super(Bullet, self).__init__()
        self.screen = screen
        self.settings = settings
        # Bullet settings
        self.bullet_width = 6
        self.bullet_hight = 15
        self.color = 165, 35, 7


        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_hight)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = self.rect.y
        self.x = self.rect.x


    def update(self):
        "Move bullet up the screen"

        self.y -= self.settings.bullet_speed_factor

        self.rect.y = self.y
    def draw_bullet(self):
        "Draw the bullet on the screen"
        pygame.draw.rect(self.screen, self.color, self.rect)
