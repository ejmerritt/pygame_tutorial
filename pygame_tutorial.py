# TUTORIAL https://www.youtube.com/watch?v=AY9MnQ4x3zk

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Title of Your Game') # you can also change the icon
clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/Ground.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # closes window
            exit()  # stops running the program

    screen.blit(sky_surface,(0,0)) # BLIT = block image transfer

    pygame.display.update()
    clock.tick(60) # tells pygame not to run the loop faster than 60 times per sec
