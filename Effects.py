import pygame
from time import gmtime, strftime
from pygame.sprite import Sprite

class Explosion(Sprite):
    def __init__(self,screen, alien):
        super(Explosion, self).__init__()
        self.screen = screen

        self.image = pygame.image.load('Models/Effects/Explosion-FX-royalty-free-game-art-.png')
        self.image = pygame.transform.scale(self.image, (75, 70))
        self.rect = self.image.get_rect()
        self.rect.centerx= alien.rect.centerx
        self.rect.centery = alien.rect.centery
        self.start_time = int(strftime("%S", gmtime()))



    def blitme(self):
        "Draw the explosion"
        self.screen.blit(self.image, self.rect)

    def stop(self):
        self.current_time = int(strftime("%S", gmtime()))
        if abs(self.current_time - self.start_time) >= 1:
            return True
        else:
            return False




