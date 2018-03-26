from Globals import *
from GameStateManager import *
from Player import *
from Camera import *
from TileMap import *
def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gsm = GameStateManager()
    clock = pygame.time.Clock()
    player = Player(10, 10, 16, 32)
    player.walls = wall_sprite
    player.trees = tree_sprite
    player.entrance = entrance_sprite
    camera = Camera()
    gsm.def_states()
    gsm.set_state("MainMenu")
    isRunning = True
    all_sprite.add(player)
    map = TileMap("./assets/test_map32.tmx", 0, 0, player)
    #map_surface = map.make_map(player)
    #map_rect = map_surface.get_rect()
    while isRunning:
        clock.tick(FPS)

        #Checking the Games Game state!
        if gsm.currentState == "MainMenu": # Main Menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isRunning = False
                if event.type == pygame.KEYDOWN:
                    gsm.currentState = "MainGame"
        if gsm.currentState == "MainGame": #Main Game State
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    player._update_keypressed(event, map)
                if event.type == pygame.KEYUP:
                    player._update_keyup(event)
                if event.type == pygame.QUIT:
                    isRunning = False
            camera.update(player)       
            for ent in player_sprite:
                ent._update(map)
            for ent in player_sprite:
                ent._late_update()
            map_sprite.draw(screen)
            all_sprite.draw(screen)
            tree_sprite.draw(screen)
            pygame.display.flip()
    pygame.quit() #end of code and exit the libary

if __name__ == "__main__":
    main()
