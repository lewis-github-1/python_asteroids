import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import *
import sys

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Initialize delta time and frame rate control
    dt = 0      # Delta time
    clock = pygame.time.Clock()    

    # Groups for updating and drawing
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create the player at the center of the screen
    player1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)   
    asteroid1 = AsteroidField()

    # Game loop
    game = True
    while game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit game
            
        updatable.update(dt)    # Updates updatable sprites
        
        # Collision check between player and asteroids
        for asteroid in asteroids:
            if player1.collision_check(asteroid):
                print("Game Over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_check(asteroid):
                    shot.kill()
                    asteroid.kill()


        screen.fill((0, 0, 0))  # Clear screen to black

        # Draw all drawable sprites
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()   # Refresh the screen

        dt = clock.tick(60) / 1000      #60 FPS cap
        

 




if __name__ == "__main__":
    main()
