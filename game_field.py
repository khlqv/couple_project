# game_field.py
import consts
import random

import player_action

# from main import handle_user_events

flag_row = consts.BOARD_ROWS - consts.FLAG_ROWS
flag_col = consts.BOARD_COLS - consts.FLAG_COLS

field_grid = []

grass_positions = []

def generate_grass_positions():
    global grass_positions
    grass_positions = []
    for _ in range(consts.MINES_COUNT):
        x = random.randrange(consts.WINDOW_WIDTH)
        y = random.randrange(consts.WINDOW_HEIGHT)
        grass_positions.append((x, y))

def generate_mines_positions():
    mine_position_lst=fill_mines()
    return mine_position_lst

# create matrix 20 on 50 and inserts free
def create():
    global field_grid
    for row in range(consts.BOARD_ROWS):
        field_grid.append([])
        for col in range(consts.BOARD_COLS):
            field_grid[row].append([])
            field_grid[row][col] = consts.FREE
    field_grid[0][0] = consts.SOLDIER


def put_mine(row, col_start):
    for col in range(col_start, col_start + 3):
        field_grid[row][col] = consts.MINE


def is_free_from_mine(row, col):
    for i in range(3):
        if field_grid[row][i + col] == consts.MINE:
            return False
    return True


def fill_mines():
    pos=[]
    for i in range(consts.MINES_COUNT):
        x_random = random.randint(consts.SOLDIER_COLS,
                                  consts.BOARD_COLS - 3) - 1
        y_random = random.randint(consts.SOLDIER_ROWS, consts.BOARD_ROWS) - 1
        if field_grid[y_random][x_random] == consts.FREE and is_free_from_mine(
                y_random, x_random):
            put_mine(y_random, x_random)
            pos.append((x_random,y_random))
        else:
            while field_grid[y_random][
                x_random] != consts.FREE or not is_free_from_mine(y_random,
                                                                  x_random):
                x_random = random.randint(consts.SOLDIER_COLS,
                                          consts.BOARD_COLS)
                y_random = random.randint(consts.SOLDIER_ROWS,
                                          consts.BOARD_ROWS)
            put_mine(y_random, x_random)
            pos.append((x_random,y_random))
    return pos

def put_flag():
    for row in range(consts.BOARD_COLS - consts.FLAG_COLS,
                     consts.BOARD_COLS):
        for col in range(consts.BOARD_ROWS - consts.FLAG_ROWS,
                         consts.BOARD_ROWS):
            field_grid[col][row] = consts.FLAG


def find_solder():
    row_r = 0
    col_r = 0
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            if field_grid[row][col] == consts.SOLDIER:
                row_r = row
                col_r = col
    return row_r, col_r


def update_soldier(new_loc):
    old_loc = find_solder()
    field_grid[old_loc[1]][old_loc[0]] = consts.FREE
    field_grid[new_loc[1]][new_loc[0]] = consts.SOLDIER


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()
