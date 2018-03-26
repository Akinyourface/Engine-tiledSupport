from Globals import *
from Wall import *
class Entrance(pygame.sprite.Sprite):
    def __init__(self, startingx, startingy, width, height, location, player):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.rect = pygame.Rect(startingx, startingy, self.width, self.height)
        self.location = location
        camera_sprite.add(self)
