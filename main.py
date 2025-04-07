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
    test_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 
    dt = 0
    running = True 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        screen.fill("black")
        test_player.update(dt)
        test_player.draw(screen)
        
        #this actually draws everything to the screen, right now we are drawing evertyhing off screen then 'flip' the whole thing and draw everything at once to the screen
        #this is better for game smoothness, no flickering and more efficiency 
        pygame.display.flip()
        
        
        clock.tick(60)
        dt = clock.tick(60) / 1000 #uses less resources as we decouple games speed from the speed its being drawing to the screen 
        
  
if __name__ == "__main__":
    main()


