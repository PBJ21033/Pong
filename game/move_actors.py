"""
    This class controls the movement of the ball and the paddle.  This just uses abstraction from the director class, limiting what the user can see in this class. This is used because this class does not care what the variable paremeters are as long as it is either a paddle or a ball.
"""


from game.draw_actor import Draw_Actor
from game.paddle import Paddle
from game.ball import Ball
from game import constants
import pygame

class Move_Actors:
    def __init__(self):
        pass

    def move_paddle(self, paddles):
        key_pressed = pygame.key.get_pressed()

        for paddle in paddles:
            if key_pressed [paddle.paddle_up()]:
                if paddle.y - paddle._velocity > 0:
                   paddle.y -= paddle._velocity

            elif key_pressed [paddle.paddle_down()]:
                if paddle.y + paddle._velocity < constants.HEIGHT -Paddle.paddle_height():
                    paddle.y += paddle._velocity
    
    def move_ball(self, balls):
        for ball in balls:
            ball.x += constants.velocity
            ball.y += ball.get_angle()

