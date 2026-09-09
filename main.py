import pygame
import game_field
import consts
import screen
from os import environ
import random
environ['PYGAME_HIDE_SUPPORT_PROMPT']='1'
pygame.mixer.init()
state = {
    "is_window_open": True,
    "state": consts.RUNNING_STATE,

}
def main():
    while state["is_window_open"]:
        game_field.create()
        game_field.generate_grass_positions()
        game_field.generate_mines_positions()
        handle_user_events(game_field.find_solder())



def handle_user_events(solider_loc):
    row = solider_loc[0]
    col = solider_loc[1]

    grid_visible = False
    grid_shown_at = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # KEYDOWN - key was pressed, KEYUP - key was pressed/release
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_UP or event.key ==  pygame.K_w):
                if event.key in (pygame.K_UP, pygame.K_w) and row>0:
                    row -= 1
                if event.key in (pygame.K_DOWN, pygame.K_s) and row<=(consts.BOARD_ROWS-consts.SOLDIER_ROWS)-1:
                    row += 1
                if event.key in (pygame.K_LEFT, pygame.K_a) and col>0:
                    col -= 1
                if event.key in (pygame.K_RIGHT, pygame.K_d)and col<=(consts.BOARD_COLS-consts.SOLDIER_COLS)-1:
                    col += 1
                if event.key == pygame.K_RETURN:
                    grid_visible = True
                    grid_shown_at = pygame.time.get_ticks()

        if grid_visible and pygame.time.get_ticks() - grid_shown_at >= consts.GRID_DURATION_MS:
            grid_visible = False

        if grid_visible:
            screen.draw_lasereye_game((row, col))
        else:
            screen.draw_day_game((row, col))

if __name__ == '__main__':
    main()