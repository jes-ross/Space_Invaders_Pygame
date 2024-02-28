#Libraries.
import sys

import pygame as pg



class AlienInvasion:#Creating the game class.


    def __init__(self):#Initialize the game.
        
        pg.init()

        self.screen = pg.display.set_mode((1200, 800)) #Screen size.
        pg.display.set_caption('Space Invaders')
        
        self.bg_color = (230, 230, 230)#Configuration of colors.
    
    def run_game(self):#Run the game.
        
        while True:#Start the loop.
            
            for event in pg.event.get():#Searching for users inputs.
                if event.type == pg.QUIT:
                    sys.exit()
            
            self.screen.fill(self.bg_color)#Adding colors.
            
            pg.display.flip()#Last screen.

if __name__ == '__main__':#Instance the game and run it.
    AI = AlienInvasion()
    AI.run_game()