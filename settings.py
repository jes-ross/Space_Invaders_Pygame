'''
With this module configure what you need 
about the game and others.
'''




class Settings: #A class to save all the game configuration.

    def __init__(self):#Initialize the game configuration.
        
        self.screen_width:int = 1200
        self.screen_height:int = 800
        self.bg_color:tuple = (255, 255, 255)

        #Ship configuration.
        self.ship_speed = 1.5
        
        #Bullets configuration
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #Alien configuration
        self.alien_speed = 0.2
        self.fleet_drop_speed = 10
        

        
        
        self.speedup_scale = 0.4
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):

        self.ship_speed = 1.5
        self.ship_limit = 3.0
        self.alien_speed = 0.2
        self.fleet_direction = 1
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        




    

    