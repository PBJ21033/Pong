"""
    This class gives instances of inheritance from the Input Service class and it controls the drawing of the actors to the screen. 
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

    def draw_to_screen(self, paddles, balls):
        self.output.get_screen().fill((0, 0, 0))
        for paddle in paddles:
            pygame.draw.rect(self.output.get_screen(),self.COLOUR, paddle)
        for ball in balls:
            pygame.draw.rect(self.output.get_screen(), self.COLOUR, ball)
        
        pygame.draw.rect(self.output.get_screen(), self.COLOUR, self.central_line)
        pygame.display.flip()
        self.output.clock.tick(60)