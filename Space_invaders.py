#Libraries.
import sys

import pygame as pg

#Creating the game class.

class AlienInvasion:
    def __init__(self):
        #Initialize the game.
        pg.init()

        self.screen = pg.display.set_mode((1200, 800)) #Screen size.
        pg.display.set_caption('Space Invaders')

    #Run the game.
    def run_game(self):
        #Start the loop.
        while True:
            #Searching for users inputs.
            for event in pg.event.get():
                if event.type == pg.QUIT():
                    sys.exit()

            #Last screen.
            pg.display.flip()

if __name__ == '__main__':
    #Instance the game and run it
    AI = AlienInvasion()
    AI.run_game()