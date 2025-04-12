import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update the player properties based on keyboard inputs    
        for entity in updatable:
            entity.update(dt)

        # draw the blank background, then add the ship
        screen.fill((0,0,0))
        for entity in drawable:
            entity.draw(screen)

        for ast in asteroid:
            if player.collision_huh(ast):
                print("Game Over!")
                return
            
        for ast in asteroid:
            for shot in shots:
                if ast.collision_huh(shot):
                    ast.split()
                    shot.kill()
            
        # update the clock and reset the display
        time = clock.tick(60)
        dt = time / 1000.0
        pygame.display.flip()

if __name__ == "__main__":
    main()