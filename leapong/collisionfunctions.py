import math
from random import random

def ball_to_ball(element_1, element_2):
    pass

def ball_to_paddle(element_1, element_2):
    # check future collision
    old_angle = element_1.angle
    old_x = element_1.boundingbox.x1
    old_y = element_1.boundingbox.y1

    element_1.angle = - element_1.angle
    delta_y = element_1.speed * math.cos(element_1.angle)
    delta_x = element_1.speed * math.sin(element_1.angle)
    element_1.set_position(
        element_1.boundingbox.x1 + delta_x,
        element_1.boundingbox.y1 - delta_y
    )
    set_angle = False
    if element_1.boundingbox.collide(element_2.boundingbox):
        set_angle = True
    element_1.angle = old_angle
    element_1.set_position(
        old_x, old_y
    )
    if set_angle:
        element_1.angle = math.pi - element_1.angle
    else:
        element_1.angle = - element_1.angle


def paddle_to_ball(element_1, element_2):
    ball_to_paddle(element_2, element_1)

def ball_to_goal(element_1, element_2):
    rand = int(random() * 100) % 2
    if rand:
        element_1.angle = math.pi - element_1.angle
    else:
        element_1.angle = - element_1.angle
    element_1.set_position (300, 300)
    element_2.points += 1

def goal_to_ball(element_1, element_2):
    ball_to_goal(element_2, element_1)

def ball_to_border(element_1, element_2):
    element_1.angle = math.pi - element_1.angle

def border_to_ball(element_1, element_2):
    ball_to_border(element_2, element_1)

def paddle_to_border(element_1, element_2):
    if element_2.top:
        if element_1.boundingbox.y1 <= element_2.boundingbox.y2:
            element_1.set_position (
                element_1.boundingbox.x1,
                element_2.boundingbox.y2
            )
    else:
        if element_1.boundingbox.y2 >= element_2.boundingbox.y1:
            element_1.set_position (
                element_1.boundingbox.x1,
                element_1.boundingbox.y1 - (element_1.boundingbox.y2 - element_2.boundingbox.y2)
            )

def border_to_paddle(element_1, element_2):
    paddle_to_border(element_2, element_1)

collision_functions = {
    "Ball-Ball" : ball_to_ball,
    "Ball-Paddle" : ball_to_paddle,
    "Paddle-Ball" : paddle_to_ball,
    "Ball-Goal" : ball_to_goal,
    "Goal-Ball" : goal_to_ball,
    "Ball-Border" : ball_to_border,
    "Border-Ball" : border_to_ball,
    "Paddle-Border" : paddle_to_border,
    "Border-Paddle" : border_to_paddle
}