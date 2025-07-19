import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0      # Delta time
    clock = pygame.time.Clock()

    player1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)   

    game = True
    while game == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player1.update(dt)

        screen.fill((0, 0, 0))
        player1.draw(screen)
        pygame.display.flip() # Refresh the screen

        dt = clock.tick(60) / 1000
        

 




if __name__ == "__main__":
    main()
