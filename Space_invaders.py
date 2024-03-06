#Libraries.
import sys
from time import sleep
import pygame as pg

from settings import Settings 
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button


class AlienInvasion:#Creating the game class.


    def __init__(self):#Initialize the game.
        
        pg.init()

        self.settings = Settings()#Instance settings.

        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        #Game statistics
        self.stats = GameStats(self)
        
        pg.display.set_caption('Space Invaders')
        
        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()
        self.aliens = pg.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, 'Play')

    def _create_fleet(self):

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        avialable_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = avialable_space_x // (2 * alien_width)

        #Number of lines
        ship_height = self.ship.rect.height
        avialable_space_y = (self.settings.screen_height - 
                             (3 * alien_height) - ship_height)
        number_rows = avialable_space_y // (2 * alien_height)

        for row_number in range(number_rows):

            for alien_number in range(number_aliens_x):#Create first line of aliens

                self._create_alien(alien_number, row_number)

    def _ship_hit(self):
        
        if self.stats.ship_left > 0:

            self.stats.ship_left -= 1

            if self.stats.ship_left == 2:
                self.ship.image = pg.image.load('img/Nave_Pro_Golpe.bmp')

            if self.stats.ship_left == 1:
                self.ship.image = pg.image.load('img/Nave_Pro_Golpe_final.bmp')
        
        
        else:
            self.stats.game_active = False
            pg.mouse.set_visible(True)
                
            

        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.ship.center_ship()

        sleep(0.5)


    def _create_alien(self, alien_number, row_number):#Create alien and add it to a line

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


        
    
    def run_game(self):#Run the game.
    
        while True:#Start the loop.

            self._check_events()
            if self.stats.game_active:

                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _update_bullets(self):

        self.bullets.update()

        for bullet in self.bullets.copy():

            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):

        collisions = pg.sprite.groupcollide(
            self.bullets, self.aliens, True, True 
        )
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _update_aliens(self):

        self._check_fleet_edges()
        self.aliens.update()

        if pg.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        self._check_aliens_bottom()

    def _check_events(self):

        for event in pg.event.get():#Searching for users inputs.

            if event.type == pg.QUIT:
                sys.exit()

            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _check_keydown_events(self, event):

        if event.key == pg.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pg.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pg.K_SPACE:
            self._fire_bullet()

        elif event.key == pg.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
            
            if event.key == pg.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pg.K_LEFT:
                self.ship.moving_left = False
    
    def _check_fleet_edges(self):

        for alien in self.aliens.sprites():

            if alien.check_edges():

                self._change_fleet_direction()
                break
    def _check_aliens_bottom(self):

        screen_rect = self.screen.get_rect()

        for alien in self.aliens.sprites():

            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
    
    def _check_play_button(self, mouse_pos):

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            pg.mouse.set_visible(False)

        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.reset_stats()
            self.stats.game_active = True
            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()


    def _change_fleet_direction(self):

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _fire_bullet(self):#Create a new bullet

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_screen(self):
        
        self.screen.fill(self.settings.bg_color)#Adding colors.
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        if not self.stats.game_active:
            self.play_button.draw_button()
            
        pg.display.flip()#Last screen.

if __name__ == '__main__':#Instance the game and run it.
    ai = AlienInvasion()
    ai.run_game()