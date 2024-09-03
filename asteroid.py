import pygame
import random
from constants import *
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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            asteroid_vector = self.velocity.rotate(random_angle)
            asteroid_vector_inverse = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = ASTEROID_ACCELERATION * asteroid_vector
            new_asteroid_2.velocity = ASTEROID_ACCELERATION * asteroid_vector_inverse


