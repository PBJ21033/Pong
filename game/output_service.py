"""
This class controls the screen clock and all screen sizes. It uses abstraction by taking the vairbles from the constants file. The user does not need to know what the screen size is so it is not included in this class.

"""
import pygame

from game.input_service import Input_Service
from game import constants
class Output_Service:
#drawing the game board and setting the parameters
     def __init__(self):
        pygame.init()#pygame instance
        size = (constants.WIDTH, constants.HEIGHT)
        # defines the size of the screen and displays it to the console
        self.clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Pong')
      
     def get_screen(self):
         return self.__screen