"""
    Uses abstraction to only allow the user to see waht is needed and nothing else. All this class does is handles the other classes to update the game board.
"""

import pygame
from game.collisions import Collisions

from game.draw_actor import Draw_Actor
from game.draw_screen import Draw_screen
from game.input_service import Input_Service
from game.move_actors import Move_Actors
from game.output_service import Output_Service
from game.paddle import Paddle
from game.ball import Ball
from game import constants
import sys
class Director(Input_Service):
    def __init__(self):
        super().__init__()
        self.update = Draw_screen()
        self.output = Output_Service()
        self.event = Move_Actors()
        self.collisions = Collisions()
        self.paddle = []
        self.ball = []
        self.left_paddle()
        self.right_paddle()
        self.create_ball()

    
    def left_paddle(self):
        self.paddle.append(Paddle(
            25,
            constants.HEIGHT/2 - Paddle.paddle_height()/2,
            self.left_up(),
            self.left_down() 
        ))
    
    def right_paddle(self):
        self.paddle.append(Paddle(
            750,
            constants.HEIGHT/2 - Paddle.paddle_height()/2,
            self.right_up(),
            self.right_down() 
        ))
    
    def create_ball(self):
        self.ball.append(Ball(
            constants.WIDTH / 2 - Ball.new_ball_width() / 2,
            constants.HEIGHT / 2 - Ball.new_ball_width() / 2,
            constants.HEIGHT/100
        ))

    def start_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            self.event.move_paddle(self.paddle)
            self.event.move_ball(self.ball)
            self.collisions.ball_hit_paddle(self.ball, self.paddle)
            self.collisions.ball_hit_wall(self.ball, self.paddle)
            self.update.draw_to_screen(self.paddle, self.ball)