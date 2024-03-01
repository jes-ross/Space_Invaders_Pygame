'''
With this module configure what you need 
about the game and others.
'''




class Settings: #A class to save all the game configuration.

    def __init__(self):#Initialize the game configuration.
        
        self.screen_width:int = 1200
        self.screen_height:int = 800
        self.bg_color:tuple = (255, 255, 255)
    

    