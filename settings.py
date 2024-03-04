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
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
    

    