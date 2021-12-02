"""
    Holds the variables of the ball and it uses abstraction/inheritance of the Draw_Actor class. It does that by sending in the variables that it needs form the Draw_Actor class and only allows the user to see what is needed.
"""
from game.draw_actor import Draw_Actor
from game import constants
class Ball(Draw_Actor):
    def __init__(self, left, top, height):
        self.set_width(10)
        super().__init__(left, top, self.new_ball_width(), height)

    @staticmethod
    def new_ball_width():
        return 10

