from Globals import *
from Inventory import *
class Player(pygame.sprite.Sprite):
    def __init__(self, startingx, startingy, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.velocity = 4
        self.deltax = 0
        self.deltay = 0
        self.rect.x = startingx
        self.rect.y = startingy
        self.inventoryToggle = False
        self.inventory = Inventory()
        self.dir = 0 #down 1: left 2: right 3: up
        self.stamina = 100 #power used to swing the sword
        self.magic = 100 #power used to use the damage shield
        #maybe ill add a fireball as well
        player_sprite.add(self)
        camera_sprite.add(self)
    def _update_keypressed(self, event, tilemap):
        if event.key == pygame.K_a:
            self.deltax = -self.velocity
            self.dir = 1
        if event.key == pygame.K_d:
            self.deltax = self.velocity
            self.dir = 2
        if event.key == pygame.K_w:
            self.deltay = -self.velocity
            self.dir = 3
        if event.key == pygame.K_s:
            self.deltay = self.velocity
            self.dir = 0
        if event.key == pygame.K_SPACE:
            self.tree_hit = pygame.sprite.spritecollide(self, self.trees, False)
            for tree in self.tree_hit:
                tree.hit_tree()
                if tree.health == 0:
                    self.inventory.add_closest_item("wood")

            if (self.dir == 0):
                #down
                print("you swung downwards")
            if (self.dir == 1):
                print("you swung leftwards")
                #left
            if (self.dir == 2):
                print("you swung rightwards")
                #right
            if (self.dir == 3):
                print("you swung upwards")
                #up
        if event.key == pygame.K_i:
            if self.inventoryToggle == True:
                self.inventoryToggle = False
            else:
                self.inventoryToggle = True
            print(self.inventoryToggle)
    def _update_keyup(self, event):
        if event.key == pygame.K_a:
            self.deltax = 0
        if event.key == pygame.K_d:
            self.deltax = 0
        if event.key == pygame.K_w:
            self.deltay = 0
        if event.key == pygame.K_s:
            self.deltay = 0
    def _update(self, tilemap):
        self.ent_hit_list = pygame.sprite.spritecollide(self, self.entrance, False)
        for col in self.ent_hit_list:
            tilemap.change_map(col.location)        
        self.rect.x += self.deltax
        self.block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        self.rect.y += self.deltay
        for block in self.block_hit_list:
            if self.deltax > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        self.block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in self.block_hit_list:
            if self.deltay > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
                
    def _late_update(self):
        pass
    def change_map(self, tilemap):
        tilemap.change_map(tilemap)
    #for anything that needs to come at the end of each frame
