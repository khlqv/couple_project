import pygame
import game_field
import consts
import player_action
import screen
from os import environ
import soldier
import time

environ['PYGAME_HIDE_SUPPORT_PROMPT']='1'
pygame.init()
pygame.mixer.init()

state = {
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
}

def main():
    game_field.create()
    game_field.generate_grass_positions()
    game_field.generate_mines_positions()
    game_field.put_flag()

    solider_loc = game_field.find_solder()
    row = solider_loc[0]
    col = solider_loc[1]

    grid_visible = False
    grid_shown_at = 0
    clock = pygame.time.Clock()

    while state["is_window_open"]:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state["is_window_open"] = False
                pygame.quit()
                exit()

            if state["state"] == consts.RUNNING_STATE:
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_UP, pygame.K_w) and row > 0:
                        row -= 1
                    if event.key in (pygame.K_DOWN, pygame.K_s) and row <= (consts.BOARD_ROWS - consts.SOLDIER_ROWS) - 1:
                        row += 1
                    if event.key in (pygame.K_LEFT, pygame.K_a) and col > 0:
                        col -= 1
                    if event.key in (pygame.K_RIGHT, pygame.K_d) and col <= (consts.BOARD_COLS - consts.SOLDIER_COLS) - 1:
                        col += 1
                    if event.key == pygame.K_RETURN:
                        grid_visible = True
                        grid_shown_at = pygame.time.get_ticks()



        if state["state"] == consts.RUNNING_STATE:
            game_field.update_soldier((row, col))

            if grid_visible and pygame.time.get_ticks() - grid_shown_at >= consts.GRID_DURATION_MS:
                grid_visible = False

            body_cells = soldier.get_body_cells(row, col)
            feet_cells = soldier.get_feet_cells(row, col)

            if player_action.does_touch_mine(game_field.field_grid, feet_cells):
                state["state"] = consts.LOSE_STATE
                try:
                    consts.LOSE_SOUND.play()
                except AttributeError:
                    pass

            elif player_action.does_touch_flag(game_field.field_grid, body_cells):
                state["state"] = consts.WIN_STATE
                try:
                    consts.WIN_SOUND.play()
                except AttributeError:
                    pass

        if grid_visible:
            screen.draw_lasereye_game((row, col))
            time.sleep(1)
        else:
            screen.draw_day_game((row, col))
        if state["state"] == consts.WIN_STATE:
            screen.draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE, consts.WIN_COLOR, consts.WIN_LOCATION)
            pygame.display.flip()
        elif state["state"] == consts.LOSE_STATE:
            screen.draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE, consts.LOSE_COLOR, consts.LOSE_LOCATION)
            pygame.display.flip()

if __name__ == '__main__':
    main()
