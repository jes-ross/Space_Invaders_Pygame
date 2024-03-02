import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):# Class to manage bullets
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a rectangle for the bullet
        self.rect = pg.Rect(0, 0, self.settings.bullet_width,
                            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Save the position
        self.y = float(self.rect.y)

    def update(self):#Move the bullet up and update position
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    def draw_bullet(self):
        pg.draw.rect(self.screen, self.color, self.rect)


