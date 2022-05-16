import pygame
from Screen_Settings import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
Font = pygame.font.Font(None, 50)
game_active = True

text_surface = Font.render('Flappy Bird', False, (250, 250, 250))
text_rect = text_surface.get_rect(center=(250, 50))

sky = pygame.Surface((window_width, window_height))

# convert makes it into something pygame can work with more easily so the game can run faster
# Having _alpha removes the alpha values, which is the black stuff that appears between transparent parts of the png
flappybird = pygame.image.load('flappy_bird.png').convert_alpha()
flappybird_rect = flappybird.get_rect(midbottom=(300, 100))
flappybird_gravity = 0
tube_surface = pygame.image.load("tube_tube.png").convert_alpha()

ground = pygame.image.load('ground.png').convert_alpha()
# get_rect draws a rectangle around the image/text you input
tube_rect = tube_surface.get_rect(bottomleft=(0, 520))
sky.fill((135, 206, 250))
# Now we're going have a "while true" loop so that the game runs forever
# It will run until the while loop is false, in which case the game will end
# The loop will equal false within the main loop so that only under certain circumstances the game will end
# i.e. getting hit by an enemy
# In this loop we will draw all the elements and update
while True:
    for event in pygame.event.get():
        # The pygame.event.get function gives us all the possible events in pygme
        # The "for event in" part just loops through all of them so that the computer knows them
        if game_active:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # and flappybird_rect.bottom >= 520:
                    flappybird_gravity = -15

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # and flappybird_rect.bottom >= 520:
                    game_active = True

    if game_active:
        # blit is basically a fancy way of saying you want to put one surface on another
        # It needs two arguments, the surface and the location of the surface on the display surface
        screen.blit(sky, (0, 0))
        # When adding a rectangle onto the display, the surface must be the first argument followed by the rectangle
        # This is because it's basically taking the two variables and making them one
        # It's basically a rectangle with the surface inside it
        screen.blit(flappybird, flappybird_rect)
        # += makes something go right, -= makes something go left
        tube_rect.x -= 5
        if tube_rect.right <= 0: tube_rect.left = 500
        screen.blit(tube_surface, tube_rect)
        # The draw module can be used to draw any kind of line, polygon, or elipse
        # In this case we are drawing a rectangle
        # The rect module needs three arguments
        # 1. The display surface (the entire screen) 2. The color of the shape  3. The area you want the rectangle drawn
        # You could add a fourth and fifth argument stating the width of the border and how rounded the edges are
        # We don't need to add those though
        pygame.draw.rect(screen, (0, 0, 0), text_rect)
        screen.blit(text_surface, text_rect)
        screen.blit(ground, (0, 300))
        # The + makes the bird go down, whereas - makes it go up
        flappybird_gravity += 1
        flappybird_rect.y += flappybird_gravity
        if flappybird_rect.bottom >= 520: flappybird_rect.bottom = 520

        if flappybird_rect.colliderect(tube_rect):
            game_active = False

    else:
        screen.fill((0, 0, 0))

    pygame.display.update()

    # This tells the while loop not to run faster than 60 frames per second
    # That way the while loop won't run too fast
    clock.tick(60)
