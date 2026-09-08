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
    image_grass= pygame.image.load('C:\\Users\\jbt\\PycharmProjects\\couple_project\\bin\\bin\\grass.png')
    image_grass=pygame.transform.scale(image_grass,(consts.GRASS_WIDTH,consts.GRASS_HEIGHT))
    for index in range(consts.MINES_COUNT):
        screen.blit(image_grass,[random_x(),random_y()])


def draw_flag():
    # get img, save and transform
    image_grass= pygame.image.load('C:\\Users\\jbt\\PycharmProjects\\couple_project\\bin\\bin\\flag.png')
    flag_image=pygame.transform.scale(image_grass,(consts.X_SIZE_FLAG,consts.Y_SIZE_FLAG))
    #put him on a const place
    screen.blit(flag_image, [consts.WINDOW_WIDTH - consts.X_SIZE_FLAG,consts.WINDOW_HEIGHT- consts.Y_SIZE_FLAG])


def draw_xray_vision_screen():
    #new background
    laser_screen.fill(consts.BACKGROUND_COLOR_LASER_VISION)
    #create grid

    #show soldier
    """BLACK = (0, 0, 0)
    WHITE = (200, 200, 200)
    WINDOW_HEIGHT = 400
    WINDOW_WIDTH = 400

    def main():
        global SCREEN, CLOCK
        pygame.init()
        SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        CLOCK = pygame.time.Clock()
        SCREEN.fill(BLACK)

        while True:
            drawGrid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def drawGrid():
        blockSize = 20  # Set the size of the grid block
        for x in range(0, WINDOW_WIDTH, blockSize):
            for y in range(0, WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)"""


    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            pygame.draw.line(laser_screen, consts.LASERS_COLOR, (row, 0),(row, consts.WINDOW_WIDTH))
            pygame.draw.line(laser_screen, consts.LASERS_COLOR, (0, col),(row, consts.WINDOW_HEIGHT))
    # show mines
    mine_image=pygame.image.load('C:\\Users\\jbt\\PycharmProjects\\couple_project\\bin\\bin\\mine.png')
    mine_image = pygame.transform.scale(mine_image, (consts.X_SIZE_MINE,consts.Y_SIZE_MINE))
    count=0
    for i in range(consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS):
            if game_field.field_grid[i][j]==consts.MINE:
                count+=1
                if count==3:
                    laser_screen.blit(mine_image,[(i * (j-3)) * consts.CELL_SIZE,(i * j) * consts.CELL_SIZE])

def draw_day_game():
    screen.fill(consts.BACKGROUND_COLOR_BLIND_MINES)
    draw_grass_on_screen()
    draw_flag()
    pygame.display.flip()
    time.sleep(3)
#draw_day_game()

def draw_lasereye_game():
    draw_xray_vision_screen()
    pygame.display.flip()
    time.sleep(3)
draw_lasereye_game()