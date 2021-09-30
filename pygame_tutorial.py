# TUTORIAL https://www.youtube.com/watch?v=AY9MnQ4x3zk

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Title of Your Game') # you can also change the icon
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
score_surface = test_font.render('My Game', False, (64,64,64)) # change AA argument to True to smooth text (i.e. if you are using a non-pixel art font)
score_rect = score_surface.get_rect(center = (400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha() # respect empty space behind the snail (so it doesn't end up with a white square around it)
snail_rect = snail_surface.get_rect(bottomright = (600,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # closes window
            exit()  # stops running the program
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800

    if game_active:
        screen.blit(sky_surface,(0,0)) # BLIT = block image transfer
        screen.blit(ground_surface,(0,300))
        pygame.draw.rect(screen,'#c0e8ec',score_rect)
        pygame.draw.rect(screen,'#c0e8ec',score_rect,10) # the argument 10 is for "width" and defines the width of the line surrounding the shape - also deletes the fill
        screen.blit(score_surface, score_rect)

        # pygame.draw.line(screen, 'White', (0,0), (800,400), 4)

        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Blue')

    pygame.display.update()
    clock.tick(60) # tells pygame not to run the loop faster than 60 times per sec

# -------------- zombie code ----------------
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')

#    if player_rect.colliderect(snail_rect):
    #    print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print('collision')
