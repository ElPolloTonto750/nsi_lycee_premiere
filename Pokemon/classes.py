import pygame
import pokedex
import csv

chart = []
with open("pokedex.csv") as f:
    c = csv.DictReader(f, delimiter=',')
    for line in c:
        chart.append(line)



class Pokemon():
    def __init__(self, pokemon: str):
        pok_nbr = pokedex.pok_index(pokemon)
        pok_atk = pokedex.atk(pokemon)
        pok_def = pokedex.defense(pokemon)
        pok_HP = pokedex.HP(pokemon)
        pok_sprite = pokedex.sprite(pokemon)
        pok_speed = pokedex.speed(pokemon)
        pok_name = str(chart[pok_nbr]['Pokemon'])
        pok_desc = str(chart[pok_nbr]['Description'])

    def description(self, pokemon: str):
        pok_nbr = pokedex.pok_index(pokemon)
        pok_atk = pokedex.atk(pokemon)
        pok_def = pokedex.defense(pokemon)
        pok_HP = pokedex.HP(pokemon)
        pok_speed = pokedex.speed(pokemon)
        pok_desc = "Your pokemon's name is "+str(chart[pok_nbr]['Pokemon'])+" and his pokedex number is #"+str(pok_nbr)+'. '+str(chart[pok_nbr]['Description'])
        pok_stats = [['Index', pok_nbr], ['ATK', pok_atk], ['DEF', pok_def], ['HP', pok_HP], ['Speed', pok_speed]]
        print(*pok_stats, sep="\n") and print(pok_desc)

# button class
class Button():
    def __init__(self, x, y , image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action