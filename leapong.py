""" Leapong """
import Leap, sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from pygame import sprite

from leapong.paddle import Paddle

screen_width = 640
screen_height = 480

class PongListener(Leap.Listener):

    def __init__(self, pad1, pad2):
        Leap.Listener.__init__(self)
        self.pad1 = pad1
        self.pad2 = pad2

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
            hand = frame.hands[0]
            self.pad1.pos = (self.pad1.pos[0], (1.0 - hand.direction[1]) * screen_height)
            hand = frame.hands[1]
            self.pad2.pos = (self.pad2.pos[0], (1.0 - hand.direction[1]) * screen_height)

def main():

    global screen_width
    global screen_height

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

    Paddle.load_image()
    left_paddle = Paddle((paddle_range.left, paddle_range.top), paddle_range)
    right_paddle = Paddle((paddle_range.right - paddle_width, paddle_range.top), paddle_range)
    
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

        sprites.clear(screen, background)
        sprites.update()
        sprites.draw(screen)
        pygame.display.flip()

    controller.remove_listener(listener)
    pygame.quit()


if __name__ == '__main__':
    main()