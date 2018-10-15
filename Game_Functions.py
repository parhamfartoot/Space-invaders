import sys
import pygame
from Bullets import Bullet
from Setting import Settings
#set = Settings()
from Alien import Alien
from Effects import Explosion
from time import  sleep
from Game_stats import GameStats


# Helper functions
def check_fire(event,screen, ship, bullets,set):
    "check for Firing"
    if event.key == pygame.K_SPACE:
        fire_bullet(screen,ship,bullets, set)


def fire_bullet(screen, ship, bullets, set):

    if len(bullets) <= set.bullets_allowed:
        new_bullet = Bullet(screen, ship,set)
        bullets.add(new_bullet)

def check_keydown_events(event,ship):
    "Respond to key presses"
        # Moving
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event,ship):
    "Respond to key releases"
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    ship.ship_speed = 1


def check_events(ship,screen, bullets, stats, play_button,aliens, set):
    "respond to Keypresses and mouse events"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
            check_fire(event,screen,ship,bullets, set)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, aliens, bullets, ship, screen, set)

def check_play_button(stats, play_button, mouse_x, mouse_y, aliens, bullets, ship, screen, set):
    " Start a new game when the player clicks play"
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_Active:

        set.initialize_dynamic_settings()

        # Reset game statistics.
        stats.reset_stats()
        stats.game_Active = True

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new fleet and center ship
        create_fleet(set,screen, aliens, ship)
        ship.center_ship()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)


# --------------------

def get_number_aliens_x(set, alien_width):
    " Determine the number of aliens that fit in a row"
    available_space_x = set.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return  number_aliens_x

def get_number_rows(set, ship_height, alien_height):
    " Determine the number of rows of aliens that fit the screen"
    available_space_y = (set.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(set, screen, aliens, alien_number, row_number):
    " Create an alien and place it in a row."
    alien = Alien(set, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(set, screen, aliens, ship):
    "create a fleet of aliens"
    alien = Alien(set, screen)
    number_aliens_x = get_number_aliens_x(set, alien.rect.width)
    number_rows = get_number_rows(set, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(set, screen, aliens, alien_number, row_number)

def check_fleet_edges(set, aliens):
    " Respond appropriately if any aliens have reached the edge."
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(set, aliens)
            break


def change_fleet_direction(set, aliens):
    " Drop the entire fleet and change the fleets direction."
    for alien in aliens.sprites():
        alien.rect.y += set.fleet_drop_speed
    set.fleet_direction *= -1
# -----------------------
def create_expo(screen, explosions,alien):
    " Create an alien and place it in a row."
    explosion = Explosion(screen,alien)
    explosions.add(explosion)

def explo(screen, explosions):
    explosion = Explosion(screen)

# -----------------------

def update_screen(BackGround,screen,ship,bullets, aliens,explosions, stats, play_button,sb):
    "Update the images on the screen"

    # Redraw the screen during each pass through the loop.
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    ship.blitme()
    aliens.draw(screen)
    explosions.draw(screen)
    sb.show_score()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #for explosion in explosions.sprites():
        #explosion.blitme()

    for explosion in explosions.copy():
        if explosion.stop():
            explosions.remove(explosion)

    # Draw button
    if not stats.game_Active:
        play_button.draw_button()

    # Make the most recent drawn screen visible
    pygame.display.flip()

def update_bullets(bullets, aliens, explosions, screen,ship,set,stats , sb):
    bullets.update()

    # Get rid of bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check for any bullets that have hit aliens.
    # if so get rid of the bullet and the alien
        check_bullet_alien_collision(set,screen,ship,aliens,bullets,explosions,stats,sb)

def check_bullet_alien_collision(set, screen, ship, aliens, bullets, explosions,stats,sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions :
        for aliens in collisions.values():
            stats.score += set.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
        for key in collisions.keys():
            create_expo(screen,explosions,collisions[key][0])

       # Repopulating the fleet
    if len(aliens) == 0:
        # Destroy existing bullets and create a new fleet.
        bullets.empty()
        set.increase_speed()
        create_fleet(set,screen,aliens,ship)


def update_aliens(aliens,set,ship,stats,screen,bullets):
    " Update the position of all aliens in the fleet"
    check_fleet_edges(set, aliens)
    aliens.update()


    #look for alien_ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(set,stats,screen,ship,aliens,bullets)

    # Look if aliens have reached the bottom
    check_aliens_bottom(set,stats,screen,ship,aliens,bullets)



# ----------------------------------

def ship_hit(set,stats, screen, ship, aliens, bullets):
    "Respond to ship being hit by aliens."

    if stats.ships_left > 0:
        # Decrement ships left
        stats.ships_left -= 1

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(set, screen,aliens, ship)
        ship.center_ship()

        # Pause.
        sleep(1)
    else:
        stats.game_Active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(set,stats,screen,ship,aliens,bullets):
    " Check if any alien has reached the bottom"
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as ship getting hit
            ship_hit(set,stats,screen,ship,aliens,bullets)
            break


# -------------------------------------
def check_high_score(stats, sb):
    "Check to see if there is a new high score."
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()