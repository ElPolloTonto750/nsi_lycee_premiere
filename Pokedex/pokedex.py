from math import *

import csv
chart = []
with open('pokemon.csv') as f:
    c = csv.DictReader(f, delimiter=',')
    for line in c:
        chart.append(line)

def pokemon_index(pokemon: str)-> int:
    """takes a pokemon name and returns his index number"""
    l = []
    f = open("pokemon.csv", "r")
    c = csv.DictReader(f, delimiter=',')
    for line in c:
        if line['Name'] == pokemon:
            pokemon_nbr = int(line['#'])
    return pokemon_nbr

def damage(pokemon):
    pokemon_nbr = pokemon_index(pokemon)
    atk = int(chart[pokemon_nbr]['Attack'])
    defense = int(chart[pokemon_nbr]['Defense'])
    print(atk)
    print(defense)
    dmg = ((2.4*atk)/(defense/5))
    return dmg
