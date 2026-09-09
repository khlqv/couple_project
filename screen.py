import time
import pygame
import consts
import random
import game_field
pygame.init()
screen = pygame.display.set_mode(
       (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
laser_screen= pygame.display.set_mode(
       (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def random_x():
    x=random.randrange(consts.WINDOW_WIDTH)
    return x
def random_y():
    y=random.randrange(consts.WINDOW_HEIGHT)
    return y

def draw_grass_on_screen():
    image_grass= pygame.image.load(consts.GRASS_IMAGE)
    image_grass=pygame.transform.scale(image_grass,(consts.GRASS_WIDTH,consts.GRASS_HEIGHT))
    for index in range(consts.MINES_COUNT):
        screen.blit(image_grass,[random_x(),random_y()])


def draw_flag():
    # get img, save and transform
    image_grass= pygame.image.load(consts.FLAG_IMAGE)
    flag_image=pygame.transform.scale(image_grass,(consts.X_SIZE_FLAG,consts.Y_SIZE_FLAG))
    #put him on a const place
    screen.blit(flag_image, [consts.WINDOW_WIDTH - consts.X_SIZE_FLAG,consts.WINDOW_HEIGHT- consts.Y_SIZE_FLAG])


def draw_xray_vision_screen():
    #new background
    laser_screen.fill(consts.BACKGROUND_COLOR_LASER_VISION)
    #create grid


    for r in range(consts.BOARD_ROWS + 1):
        y = r * consts.CELL_SIZE
        pygame.draw.line(laser_screen, consts.LASERS_COLOR, (0, y),
                             (consts.WINDOW_WIDTH, y))
    for c in range(consts.BOARD_COLS + 1):
        x = c * consts.CELL_SIZE
        pygame.draw.line(laser_screen, consts.LASERS_COLOR, (x, 0),
                            (x, consts.WINDOW_HEIGHT))

    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            pygame.draw.line(laser_screen, consts.LASERS_COLOR, (row, 0),(row, consts.WINDOW_WIDTH))
            pygame.draw.line(laser_screen, consts.LASERS_COLOR, (0, col),(row, consts.WINDOW_HEIGHT))
    # show flag
    draw_flag()
    # show soldier

    # show mines
    mine_image=pygame.image.load(consts.MINE_IMAGE)
    mine_image = pygame.transform.scale(mine_image, (consts.X_SIZE_MINE,consts.Y_SIZE_MINE))
    count=0
    for i in range(consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS):
            if game_field.field_grid[i][j] == consts.MINE:
                is_left_edge = (j == 0) or (
                            game_field.field_grid[i][j - 1] != consts.MINE)
                if is_left_edge:
                    laser_screen.blit(mine_image, [j * consts.CELL_SIZE,
                                                   i * consts.CELL_SIZE])



def show_day_soldier(location):
    soldier_image = pygame.image.load(consts.SOLDIER_IMAGE)
    soldier_image = pygame.transform.scale(soldier_image,(consts.X_SIZE_SOLDIER,consts.Y_SIZE_SOLDIER))
    screen.blit(soldier_image, [location[1] * consts.CELL_SIZE,location[0] * consts.CELL_SIZE])


def show_night_soldier(location):
    night_soldier_image = pygame.image.load(consts.SOLDIER_NIGHT_IMAGE)
    night_soldier_image = pygame.transform.scale(night_soldier_image,(consts.X_SIZE_SOLDIER,consts.Y_SIZE_SOLDIER))
    laser_screen.blit(night_soldier_image, [location[1] * consts.CELL_SIZE, location[0] * consts.CELL_SIZE])

def draw_day_game():
    screen.fill(consts.BACKGROUND_COLOR_BLIND_MINES)
    draw_grass_on_screen()
    draw_flag()
    show_day_soldier((0,0))
    pygame.display.flip()
    time.sleep(3)
draw_day_game()

def draw_lasereye_game():
    draw_xray_vision_screen()
    show_night_soldier((0,0))
    pygame.display.flip()
    time.sleep(3)
#draw_lasereye_game()