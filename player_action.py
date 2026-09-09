import pygame.event
import consts

def does_touch_flag(field_grid,soldier_location ):
    for tuple_loc in soldier_location:
        if field_grid[tuple_loc[1]][tuple_loc[0]]==consts.FLAG:
                return True
    return False

def does_touch_mine(field_grid,soldier_location):
    for tuple_loc in soldier_location:
        if field_grid[tuple_loc[1]][tuple_loc[0]] == consts.MINE:
                return True
    return False