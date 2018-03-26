import pygame
import pytmx
from pygame.locals import *
#a file containing all of the global variables
FPS = 60
TILEMAP_WIDTH = 16
TILEMAP_HEIGHT = 16
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
FULLSCREEN = False

#defining the groups
all_sprite = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
camera_sprite = pygame.sprite.Group() # a group to tell the game what's going to ve movable by the camera
map_sprite = pygame.sprite.Group()
wall_sprite = pygame.sprite.Group()
tree_sprite = pygame.sprite.Group()
entrance_sprite = pygame.sprite.Group()
#defining the colors
BLACK = (0, 0, 0)
GREEN = (0, 0, 255)
RED = (255, 255, 255)
BLUE = (0, 255, 0)

