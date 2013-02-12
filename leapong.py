""" Leapong """
import Leap, sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from pygame import sprite

from leapong.basesprite import BaseSprite

from leapong.paddle import Paddle
from leapong.ball import Ball
import math


screen_width = 640
screen_height = 480

class PongListener(Leap.Listener):

    def __init__(self, pad_left, pad_right):
        Leap.Listener.__init__(self)
        self.pad_left = pad_left
        self.pad_right = pad_right

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        global screen_width
        global screen_height
        frame = controller.frame()
        if not frame.hands.empty and len(frame.hands) == 2:
            if frame.hands[0].direction[0] > frame.hands[1].direction[0]:
                hand_left = frame.hands[0]
                hand_right = frame.hands[1]
            else:
                hand_left = frame.hands[1]
                hand_right = frame.hands[0]
            self.pad_left.set_position(self.pad_left.pos[0], (1.0 - hand_left.direction[1]) * screen_height)
            self.pad_right.set_position(self.pad_right.pos[0], (1.0 - hand_right.direction[1]) * screen_height)

def main():

    global screen_width
    global screen_height

    elements_ball = []
    elements_paddle = []

    paddle_width = 10
    paddle_height = 100
    padding = 20 

    pygame.init()
    pygame.mouse.set_visible(0)
    screen = pygame.display.set_mode((screen_width, screen_height))
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    paddle_range = screen.get_rect().copy()
    paddle_range.width -= 2 * padding 
    paddle_range.height -= 2 * padding
    paddle_range.height -= paddle_height
    paddle_range.left += padding
    paddle_range.top += padding

    sprites = sprite.Group()
    Paddle.groups = sprites
    Ball.groups = sprites

    Paddle.load_image()
    left_paddle = Paddle((paddle_range.left, paddle_range.top), paddle_range)
    right_paddle = Paddle((paddle_range.right - paddle_width, paddle_range.top), paddle_range)
    elements_paddle.append(left_paddle)
    elements_paddle.append(right_paddle)
    Ball.load_image()
    ball1 = Ball((400, 120), paddle_range)
    ball2 = Ball((200, 120), paddle_range)
    elements_ball.append(ball1)
    elements_ball.append(ball2)
    
    going = True

    listener = PongListener(left_paddle, right_paddle)
    controller = Leap.Controller()

    controller.add_listener(listener)

    while going:
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False

        for element in elements_paddle:
            for element2 in elements_ball:
                if element.collide(element2):
                    resolve_collision(element, element2)
        sprites.clear(screen, background)
        sprites.update()
        sprites.draw(screen)
        pygame.display.flip()

    controller.remove_listener(listener)
    pygame.quit()

def ball_to_ball(element_1, element_2):
    #element_1.angle = -element_1.angle
    #element_2.angle = -element_2.angle

    pass

def ball_to_paddle(element_1, element_2):
    element_1.angle = - element_1.angle

def paddle_to_ball(element_1, element_2):
    ball_to_paddle(element_2, element_1)

collision_functions = {"BallBall" : ball_to_ball, 
                        "BallPaddle" : ball_to_paddle,
                        "PaddleBall" : paddle_to_ball}

def resolve_collision(element_1, element_2):
    global collision_functions
    try:
        collision_functions["%s%s" % (element_1.__class__.__name__, element_2.__class__.__name__)](element_1, element_2)
    except KeyError:
        pass
if __name__ == '__main__':
    main()