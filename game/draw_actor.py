"""This is the super class the controls the Paddle and Ball class. It sets the heights, widths, and velocity that will be used later in the program.
It inherits from the Rect class from pygame and it also is a super class to the paddle and ball classes. One other thing that this class does is show the instances of encapsulation because if these variables get ruiend, then the game will not work.
"""

import pygame


from game import constants



class Draw_Actor(pygame.Rect):
    def __init__(self, left, top, width, height):
        self._height = 0
        self._width = 10
        self._velocity = 5
        self._angle = 0
        super().__init__(left, top, width, height)

    def set_height(self, other):
         self._height = other
    
    def set_width(self, other):
        self._width = other

    def get_height(self):
        return self._height
    
    def get_width(self):
        return self._width
    
    def set_angle(self, other):
        self._angle = other

    def get_angle(self):
        return self._angle
    

