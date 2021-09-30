# TUTORIAL https://www.youtube.com/watch?v=AY9MnQ4x3zk

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Title of Your Game') # you can also change the icon
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My Game', False, 'Black') # change AA argument to True to smooth text (i.e. if you are using a non-pixel art font)

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha() # respect empty space behind the snail (so it doesn't end up with a white square around it)
snail_rect = snail_surface.get_rect(bottomright = (600,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(bottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # closes window
            exit()  # stops running the program

    screen.blit(sky_surface,(0,0)) # BLIT = block image transfer
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface, (300,50))
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    pygame.display.update()
    clock.tick(60) # tells pygame not to run the loop faster than 60 times per sec
