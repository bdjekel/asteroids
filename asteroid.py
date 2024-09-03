import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

# Commented out lines below. Solution code did not have these. I believe these properties are defined in the inherited class, so they're not needed here unless they need to be overridden.
        # self.position = pygame.Vector2(x, y)
        # self.rotation = 0
        # self.radius = radius
        # self.velocity = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

