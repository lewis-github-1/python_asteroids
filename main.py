import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0      # Delta time
    clock = pygame.time.Clock()

    game = True
    while game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        pygame.display.flip() # Refresh the screen
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
