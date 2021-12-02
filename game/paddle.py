"""
    Holds the variables of the paddle and it uses abstraction/inheritance of the Draw_Actor class. It does that by sending in the variables that it needs form the Draw_Actor class and only allows the user to see what is needed.
"""
import pygame
from pygame import constants
from game.draw_actor import Draw_Actor


class Paddle(Draw_Actor):
    def __init__(self, left, top, up, down):
        self.set_height(100)
        self.set_width(20)
        self.new_width = self.get_width()
        self.upKey = up
        self.downKey = down
    
        super().__init__(left, top, self.new_width, self.paddle_height())
    @staticmethod
    def paddle_height():
        return 100
    
    def paddle_up(self):
        return self.upKey

    def paddle_down(self):
        return self.downKey

