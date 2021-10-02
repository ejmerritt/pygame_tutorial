# Tutorial https://www.youtube.com/watch?v=Qf3-aDXG8q4&list=PL8ui5HK3oSiEk9HaKoVPxSZA03rmr9Z0k&index=1 

import pygame, sys

# General setup
pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
