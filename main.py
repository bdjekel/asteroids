import sys
import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

# GAME LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()

        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()            

        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()