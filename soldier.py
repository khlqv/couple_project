import pygame
import consts
import screen
def put_soldier_in_the_beginning():
    soldier_image = image_grass = pygame.image.load('C:\\Users\\jbt\\PycharmProjects\\couple_project\\bin\\bin\\soldier.png')
    soldier_image = pygame.transform.scale(soldier_image,
                                           (consts.X_SIZE_SOLDIER,consts.Y_SIZE_SOLDIER))
    screen.screen.blit(soldier_image, [0,0])
#def update_day_soldier(x_pos,y_pos):

    # put him on a given place
#    screen.blit(soldier_image, [x_pos,y_pos])