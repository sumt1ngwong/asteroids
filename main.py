import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True 

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #setting the container of players, now all players have this
    Player.containers = (updateable, drawable)

    #instance of a player, and automatically adds itself to the container above
    test_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")

        #update everything in the group which now has test_player
        updateable.update(dt)

        #draw everthing in the group which now has test player
        for objects in drawable:
            objects.draw(screen)
        
        #this actually draws everything to the screen, right now we are drawing evertyhing off screen then 'flip' the whole thing and draw everything at once to the screen
        #this is better for game smoothness, no flickering and more efficiency 
        pygame.display.flip()
        
        
        clock.tick(60)
        dt = clock.tick(60) / 1000 #uses less resources as we decouple games speed from the speed its being drawing to the screen 
        
  
if __name__ == "__main__":
    main()


