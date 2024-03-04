import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):#Class for one alien.

    def __init__(self, ai_game):#Initialize the game.
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Upload the alien and configure their 'rect' atribute.
        self.image = pg.image.load('img/Alien_Pro.bmp')
        self.rect = self.image.get_rect()

        #Alien position.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        #Save the position.
        self.x = float(self.rect.x)


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):#Alien movement
        self.x += (self.settings.alien_speed * 
                    self.settings.fleet_direction)
        self.rect.x = self.x



        
