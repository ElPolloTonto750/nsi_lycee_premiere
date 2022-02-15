import pygame
import classes

#display window
screen_height = 500
screen_width = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pokemon')

#load button images
start_img = pygame.image.load('resources/start_btn.png').convert_alpha()
exit_img = pygame.image.load('resources/exit_btn.png').convert_alpha()

#create button instances
start_button = classes.Button(100, 200, start_img, 0.5)
exit_button = classes.Button(450, 200, exit_img, 0.5)

#game loop
run = True
game = False

while run:

    screen.fill((253,234,254))

    if start_button.draw(screen):
        game = True
        print('START')

    if exit_button.draw(screen):
        run = False

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()