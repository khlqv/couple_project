import pygame

import consts
import screen
from os import environ
import random
environ['PYGAME_HIDE_SUPPORT_PROMPT']='1'
pygame.mixer.init()
state = {
    "original_arrow": screen.create_arrow(consts.ARROW_IMG),
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
}
def main():
    while state["is_window_open"]:
        handle_user_events()
    screen.draw_game(state)


def handle_user_events(solider_loc):
    col=solider_loc[1]
    row=solider_loc[0]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # KEYDOWN - key was pressed, KEYUP - key was pressed/release
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_UP or event.key ==  pygame.K_w):
                if event.key in (pygame.K_UP, pygame.K_w):
                    row -= 1
                if event.key in (pygame.K_DOWN, pygame.K_s):
                    row += 1
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    col -= 1
                if event.key in (pygame.K_RIGHT, pygame.K_d):
                    row -= 1


if __name__ == '__main__':
    main()
