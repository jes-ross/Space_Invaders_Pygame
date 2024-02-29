import pygame as pg #Importing the library.

'''
In this doc what we are going to do is define the 
class SHIP
'''

class Ship:#Creating ship class.

    def __init__(self, ai_game):#Initialize the ship and configure it start position.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Upload the image of the ship.
        self.image = pg.image.load('img/nave.bmp')
        self.rect = self.image.get_rect()

        #Position of the ship.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):#Draw the ship in the screen.
        self.screen.blit(self.image, self.rect)


        