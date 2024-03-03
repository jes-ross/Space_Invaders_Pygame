import pygame as pg #Importing the library.

'''
In this doc what we are going to do is define the 
class SHIP
'''

class Ship:#Creating ship class.

    def __init__(self, ai_game):#Initialize the ship and configure it start position.
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        
        #Upload the image of the ship.
        self.image = pg.image.load('img/Nave_Pro.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom #Position of the ship.


        self.x = float(self.rect.x)#Save a decimal value for the ship horizontal position.
        #Movement flags.
        self.moving_right = False
        self.moving_left = False
        
        self.rect.x = self.x
    def update(self):#Update ship position.
        

        
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

        
        


    def blitme(self):#Draw the ship in the screen.
        self.screen.blit(self.image, self.rect)


        