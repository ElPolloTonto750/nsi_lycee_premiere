from math import *

import csv
chart = []
with open('pokemon.csv') as f:
    c = csv.DictReader(f, delimiter=',')
    for line in c:
        chart.append(line)

def pokemon_nbr(pokemon: str)-> int:
    """takes a pokemon name and returns his index number"""
    l = []
    f = open("pokemon.csv", "r")
    c = csv.DictReader(f, delimiter=',')
    for line in c:
        if line['Name'] == pokemon:
            pokemon_index = line['#']
    return pokemon_index

def damage(pokemon):
    atk = chart[pokemon]['Attack']
    defense = chart[pokemon]['Defense']
    dmg = ((12/5)*atk/defense)
    return dmg
