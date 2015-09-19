""" Leapong """

import sys
sys.path.insert(0, "lib")

import Leap
import math
import pygame

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from pygame import sprite
from pygame.locals import *

from leapong.basesprite import BaseSprite

from leapong.paddle import Paddle
from leapong.ball import Ball
from leapong.goal import Goal
from leapong.border import Border

from leapong.collisionfunctions import collision_functions

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


SCREEN_SIZE = (800, 600)

WHOLE_SCREEN_SIZE = (800, 650)

def glut_print(x, y, font, text, r, g, b, a):

    blending = False
    if glIsEnabled(GL_BLEND) :
        blending = True

    glColor3f(1,1,1)
    glRasterPos2f(x,y)
    for ch in text :
        glutBitmapCharacter( font , ctypes.c_int( ord(ch) ) )

    if not blending :
        glDisable(GL_BLEND)


def enable2D():
    glViewport (0, 0, WHOLE_SCREEN_SIZE[0], WHOLE_SCREEN_SIZE[1]);
    glMatrixMode (GL_PROJECTION);
    glLoadIdentity();
    glOrtho (0, WHOLE_SCREEN_SIZE[0], WHOLE_SCREEN_SIZE[1], 0, -10, 10);
    glMatrixMode (GL_MODELVIEW);
    glLoadIdentity();
    glClear(GL_COLOR_BUFFER_BIT)


def main():

    pygame.init()
    screen = pygame.display.set_mode(WHOLE_SCREEN_SIZE, OPENGL|DOUBLEBUF)

    clock = pygame.time.Clock()

    elements_ball = []
    elements_paddle = []
    elements_goal = []
    elements_border = []

    margin = 20
    left_paddle = Paddle((0 + margin, 20), (10, 80))
    right_paddle = Paddle((SCREEN_SIZE[0] - 10 - margin, 20), (10, 80))
    elements_paddle.append(left_paddle)
    elements_paddle.append(right_paddle)
    ball1 = Ball((50, 50), 10)
    elements_ball.append(ball1)

    goal_pl_1 = Goal((0, 0), (5, 600))
    elements_goal.append(goal_pl_1)

    goal_pl_2 = Goal((795, 0), (5, 600))
    elements_goal.append(goal_pl_2)

    border_top = Border((5, 0), (795, 5))
    elements_border.append(border_top)

    border_bottom = Border((5, 595), (795, 5))
    elements_border.append(border_bottom)

    going = True

    controller = Leap.Controller()

    while going:

        frame = controller.frame()
        if not frame.hands.is_empty and len(frame.hands) == 2:
            hand_left = frame.hands[0]
            hand_right = frame.hands[1]
            hand_left_direction = hand_left.direction[1] if hand_left.direction[1] >= 0 else 0
            hand_right_direction = hand_right.direction[1] if hand_right.direction[1] >= 0 else 0
            left_paddle.set_position(
                left_paddle.boundingbox.x1, (1.0 - hand_left_direction) * (SCREEN_SIZE[1] - 10)
            )
            right_paddle.set_position(
                right_paddle.boundingbox.x1, (1.0 - hand_right_direction) * (SCREEN_SIZE[1] - 10)
            )

        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False

        for element in elements_paddle:
            for element2 in elements_border:
                if element.collide(element2):
                    resolve_collision(element, element2)

        for element in elements_ball:
            for element2 in elements_border:
                if element.collide(element2):
                    resolve_collision(element, element2)

        for element in elements_ball:
            for element2 in elements_goal:
                if element.collide(element2):
                    resolve_collision(element, element2)
                    print "{0} - {1}".format(goal_pl_1.points, goal_pl_2.points)

        for element in elements_paddle:
            for element2 in elements_ball:
                if element.collide(element2):
                    resolve_collision(element, element2)

        enable2D()

        ball1.render()
        ball1.update()

        left_paddle.render()
        right_paddle.render()
        goal_pl_1.render()
        goal_pl_2.render()
        border_top.render()
        border_bottom.render()
        glut_print(
            50 , 630 , GLUT_BITMAP_9_BY_15 ,
            "Player 1: {0}".format(goal_pl_2.points) ,
            1.0 , 1.0 , 1.0 , 1.0
        )
        glut_print(
            650 , 630 , GLUT_BITMAP_9_BY_15 ,
            "Player 2: {0}".format(goal_pl_1.points) ,
            1.0 , 1.0 , 1.0 , 1.0
        )
        pygame.display.flip()

    pygame.quit()

def resolve_collision(element_1, element_2):
    try:
        collision_functions["%s-%s" % (element_1.__class__.__name__, element_2.__class__.__name__)](element_1, element_2)
    except KeyError:
        pass

if __name__ == '__main__':
    main()
