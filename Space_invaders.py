#Libraries.
import sys

import pygame as pg

from settings import Settings 
from ship import Ship



class AlienInvasion:#Creating the game class.


    def __init__(self):#Initialize the game.
        
        pg.init()

        self.settings = Settings()#Instance settings.

        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pg.display.set_caption('Space Invaders')
        
        self.ship = Ship(self)
        
    
    def run_game(self):#Run the game.
    
        while True:#Start the loop.
            self._check_events()
            self.ship.update()
            self._update_screen()


    def _check_events(self):

        for event in pg.event.get():#Searching for users inputs.
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pg.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pg.K_LEFT:
                    self.ship.moving_left = False
                

    def _update_screen(self):
        
        self.screen.fill(self.settings.bg_color)#Adding colors.
        self.ship.blitme()
            
        pg.display.flip()#Last screen.

if __name__ == '__main__':#Instance the game and run it.
    AI = AlienInvasion()
    AI.run_game()