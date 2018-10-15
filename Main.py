from Game_stats import GameStats
import pygame
from Setting import Settings,Background
from Ships import Ship
import Game_Functions as gf
from pygame.sprite import Group
from Buttons import  Button
from Alien import Alien
from Scoreboard import  Scoreboard

health = 3

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    # Set the background
    background = Background('Models/Space/Space1.png', [0, 0])

    # Make a ship
    ship = Ship(screen, ai_settings)

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats,background)

    # Make a bullet group
    bullets = Group()

    # Make an alien group
    aliens = Group()

    # make a Explosion group
    explosions = Group()

    # create an alien fleet
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # Start the main loop for the game
    while True:


        gf.check_events(ship, screen, bullets,stats, play_button,aliens, ai_settings)
        gf.update_screen(background, screen, ship, bullets, aliens, explosions, stats, play_button,sb)
        if stats.game_Active:
            ship.update()
            gf.update_bullets(bullets, aliens,explosions,screen, ship,ai_settings, stats,sb)
            gf.update_aliens(aliens, ai_settings, ship, stats,screen,bullets)







run_game()