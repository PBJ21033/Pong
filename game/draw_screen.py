"""
    This class gives instances of inheritance from the Input Service class and it controls the drawing of the actors to the screen. It also uses abstraction and polymorphism in the code. It uses abstraction because we do not want this class messed with as much and the user does not need to know any of the paremeters for this class to work. We use polymorphism because we only need to go through one array to display the paddles and the ball since they are both actors. This class does not care who the actors are but as long as they are there.
"""


from game.draw_actor import Draw_Actor
from game.paddle import Paddle
from game.ball import Ball
from game.output_service import Output_Service
from game import constants
from game.move_actors import Move_Actors
import pygame
    
class Draw_screen:
    def __init__(self):
        super().__init__()
        self.output = Output_Service()
        self.COLOUR = (255,255,255)
        self.central_line = pygame.Rect(constants.WIDTH/2, 0, 1, constants.HEIGHT)

    def draw_to_screen(self, actors):
        self.output.get_screen().fill((0, 0, 0))
        for actor in actors:
            pygame.draw.rect(self.output.get_screen(),self.COLOUR, actor)
        
        pygame.draw.rect(self.output.get_screen(), self.COLOUR, self.central_line)
        pygame.display.flip()
        self.output.clock.tick(60)