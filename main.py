import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True 

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    splitting = pygame.sprite.Group()

 
    #setting the container of players, now all players have this
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable, splitting)
    AsteroidField.containers = (updatable)

    #instance of a player, and automatically adds itself to the container above
    test_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 
 
    test_astrofield = AsteroidField()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")

        #update everything in the group which now has test_player
        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check(test_player):
                    print("Game over!")
                    pygame.quit()
                    sys.exit()
                
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split()
                    asteroid.kill()




       


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


