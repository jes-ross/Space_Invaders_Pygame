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
            
            for event in pg.event.get():#Searching for users inputs.
                if event.type == pg.QUIT:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)#Adding colors.
            self.ship.blitme()
            
            pg.display.flip()#Last screen.

if __name__ == '__main__':#Instance the game and run it.
    AI = AlienInvasion()
    AI.run_game()