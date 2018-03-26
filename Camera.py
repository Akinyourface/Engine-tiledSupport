from Globals import *
class Camera:
    def __init__(self):
        self. offset = 16 * 16
    def update(self, player):
        if player.rect.x < (0 + self.offset):
            for ent in camera_sprite:
                ent.rect.x += 4
        if player.rect.x > (SCREEN_WIDTH - self.offset):
            for ent in camera_sprite:
                ent.rect.x -= 4
        if player.rect.y < (0 + self.offset):
            for ent in camera_sprite:
                ent.rect.y += 4
        if player.rect.y > (SCREEN_HEIGHT - self.offset):
            for ent in camera_sprite:
                ent.rect.y -= 4
