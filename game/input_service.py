"""
    This class uses encapsulation and handles the input given to the game from the keyboard. Encapsulation is used because if the variables are messed with for the keys, then the game will not function properly because the paddles will not move. 
"""
import pygame
class Input_Service:
    def __init__(self):
        self._left_paddleUp = pygame.K_w
        self._left_paddleDown = pygame.K_s
        self._right_paddleUp = pygame.K_UP
        self._right_paddleDown = pygame.K_DOWN

    def left_up(self):
        return self._left_paddleUp
    def left_down(self):
        return self._left_paddleDown
    def right_up(self):
        return self._right_paddleUp
    def right_down(self):
        return self._right_paddleDown