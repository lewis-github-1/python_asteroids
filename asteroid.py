import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.center = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.center, 2)

    def update(self, dt):
        movement = (self.velocity * dt)
        self.center += movement


