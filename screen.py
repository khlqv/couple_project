import time
import pygame
import consts
import random

pygame.init()
screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def random_x():
    x=random.randrange(consts.WINDOW_WIDTH)
    return x
def random_y():
    y=random.randrange(consts.WINDOW_HEIGHT)
    return y

def draw_grass_on_screen():
    image_grass= pygame.image.load('C:\\Users\\jbt\\PycharmProjects\\couple_project\\bin\\bin\\grass.png')
    image_grass=pygame.transform.scale(image_grass,(consts.GRASS_WIDTH,consts.GRASS_HEIGHT))
    for index in range(consts.MINES_COUNT):
        screen.blit(image_grass,[random_x(),random_y()])

def draw_soldier():

    pass

def draw_matrix():

    pass

def draw_flag():
    # get img, save and transform
    flag_image= image_grass= pygame.image.load('C:\\Users\\jbt\\PycharmProjects\\couple_project\\bin\\bin\\flag.png')
    flag_image=pygame.transform.scale(image_grass,(consts.X_SIZE_FLAG,consts.Y_SIZE_FLAG))
    #put him on a const place
    screen.blit(flag_image, [consts.WINDOW_WIDTH - consts.X_SIZE_FLAG,consts.WINDOW_HEIGHT- consts.Y_SIZE_FLAG])

def draw_mines():

    pass


def draw_day_game():
    screen.fill(consts.BACKGROUND_COLOR_BLINDMINES)
    draw_grass_on_screen()
    draw_flag()

    pygame.display.flip()
    time.sleep(3)
draw_day_game()

def draw_lasereye_game():

    pass