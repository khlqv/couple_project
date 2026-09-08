import pygame.event

import consts
import game_field


# soldier_position = pygame.Rect(0, 0, 40, 160)


#def move_soldier(soldier_position, event):


def does_touch_flag(field_grid,soldier_location ):
    for row in range(consts.SOLDIER_BODY_ROWS):
        for col in range(consts.SOLDIER_COLS):
            if field_grid[soldier_location[1]+row][soldier_location[0]+col]==consts.FLAG:
                return True
    return False

def does_touch_mine(field_grid,soldier_location):
    for row in range(consts.SOLDIER_FEET_ROWS):
        for col in range(consts.SOLDIER_COLS):
            if field_grid[soldier_location[1]+row][soldier_location[0]+col]==consts.MINE:
                return True
    return False

def clear_from_soldier(field_grid):
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            if field_grid[row][col]==consts.SOLDIER:
                field_grid[row][col]=consts.FREE
