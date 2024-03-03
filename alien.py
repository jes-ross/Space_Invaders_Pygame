import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):#Class for one alien.

    def __init__(self, ai_game):#Initialize the game.
        super().__init__()
        self.screen = ai_game.screen

        #Upload the alien and configure their 'rect' atribute.
        self.image = pg.image.load('img/alien.bmp')
        self.rect = self.image.get_rect()

        #Alien position.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        #Save the position.
        self.x = float(self.rect.x)


        
