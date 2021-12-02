"""This class handles when the ball hits the boundaries or the paddle and then changes the angle of the ball. It uses abstraction by only giving the parameters from the director class, limiting what is viewed by the user."""
from game import constants
import pygame
import random
import sys

class Collisions:
    def __init__(self):
        pass

    def ball_hit_paddle(self, balls, paddles):
        for ball in balls:
            for paddle in paddles:
                if ball.colliderect(paddle):
                    constants.velocity = -constants.velocity
                    ball.set_angle(random.randint(-10, 10))
                    break
    
    def ball_hit_wall(self, balls, paddles):
        for ball in balls:
            if ball.x > constants.WIDTH or ball.x < 0:
                sys.exit(1)
            if ball.y > constants.HEIGHT - ball.new_ball_width() or ball.y < 0:
                ball.set_angle(-ball.get_angle())