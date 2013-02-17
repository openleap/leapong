def ball_to_ball(element_1, element_2):
    pass

def ball_to_paddle(element_1, element_2):
    element_1.angle = - element_1.angle

def paddle_to_ball(element_1, element_2):
    ball_to_paddle(element_2, element_1)

collision_functions = {"Ball-Ball" : ball_to_ball, 
                        "Ball-Paddle" : ball_to_paddle,
                        "Paddle-Ball" : paddle_to_ball}