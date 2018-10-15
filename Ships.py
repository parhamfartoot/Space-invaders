import pygame

class Ship():

    def __init__(self, screen, ai_setting):

        "initialize the ship and set its starting position"
        self.screen = screen

        # Load the ship and get its rect
        self.image = pygame.image.load('Models/Space ships/spaceship1.png')
        self.image = pygame.transform.scale(self.image, (90,70))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Movement flag
        self.moving_right = False
        self.moving_left = False

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the ship's center.

        self.center = float(self.rect.centerx)
        # Speed setting
        self.ship_speed = 3
        self.ship_speed_factor = ai_setting.ship_speed_factor

    def blitme(self):
        "Draw the ship at its current location"
        self.screen.blit(self.image, self.rect)

    def update(self):
        "Update the ship's position based on the movement flag"
        if self.moving_right and self.rect.right + 29 < self.screen_rect.right:
            self.rect.centerx += self.ship_speed
        #    self.ship_speed += self.ship_speed_factor
        if self.moving_left and self.rect.left - 29 > 0:
            self.rect.centerx -= self.ship_speed
        self.ship_speed += self.ship_speed_factor

    def center_ship(self):
        " Center the ship on screen"
        self.center = self.screen_rect.centerx
