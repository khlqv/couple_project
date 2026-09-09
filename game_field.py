# game_field.py
import consts
import random

import player_action
# from main import handle_user_events

flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
flag_col = consts.BOARD_COLS - consts.FLAG_COLS

field_grid = []


# create matrix 20 on 50 and inserts free
def create():
    global field_grid
    for row in range(consts.BOARD_ROWS):
        field_grid.append([])
        for col in range(consts.BOARD_COLS):
            field_grid[row].append([])
            field_grid[row][col] = consts.FREE


def put_mine(row, col_start):
    for col in range(col_start, col_start + 3):
        field_grid[row][col] = consts.MINE


def is_free_from_mine(row, col):
    for i in range(3):
        if field_grid[row][i + col] == consts.MINE:
            return False
    return True


def fill_mines():
    for i in range(consts.MINES_COUNT):
        x_random = random.randint(consts.SOLDIER_COLS,
                                  consts.BOARD_COLS - 3) - 1
        y_random = random.randint(consts.SOLDIER_ROWS, consts.BOARD_ROWS) - 1
        if field_grid[y_random][x_random] == consts.FREE and is_free_from_mine(
                y_random, x_random):
            put_mine(y_random, x_random)
        else:
            while field_grid[y_random][
                x_random] != consts.FREE or not is_free_from_mine(y_random,
                                                                  x_random):
                x_random = random.randint(consts.SOLDIER_COLS,
                                          consts.BOARD_COLS)
                y_random = random.randint(consts.SOLDIER_ROWS,
                                          consts.BOARD_ROWS)
            put_mine(y_random, x_random)


def put_flag():
    for row in range(consts.BOARD_COLS - consts.FLAG_COLS,
                     consts.BOARD_COLS):
        for col in range(consts.BOARD_ROWS - consts.FLAG_ROWS,
                         consts.BOARD_ROWS):
            field_grid[col][row] = consts.FLAG


def put_soldier():
    # for row in range(consts.SOLDIER_ROWS):
    #     for col in range(consts.SOLDIER_COLS):
    #         field_grid[row][col] = consts.SOLDIER
    field_grid[0][0]=consts.SOLDIER


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()


create()
fill_mines()
put_flag()
put_soldier()
print_matrix(field_grid)
# handle_user_events(5,5)