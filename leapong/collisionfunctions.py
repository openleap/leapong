import math


def ball_to_ball(element_1, element_2):
    pass

def ball_to_paddle(element_1, element_2):
    element_1.angle = - element_1.angle

def paddle_to_ball(element_1, element_2):
    ball_to_paddle(element_2, element_1)

def ball_to_goal(element_1, element_2):
    element_1.angle = - element_1.angle
    element_2.points += 1

def goal_to_ball(element_1, element_2):
    ball_to_goal(element_2, element_1)

def ball_to_border(element_1, element_2):
    element_1.angle = math.pi - element_1.angle

def border_to_ball(element_1, element_2):
    ball_to_border(element_2, element_1)

def paddle_to_border(element_1, element_2):
    print "BORDER!!!"

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