from math import *

import csv
chart1 = []
with open('pokemon.csv') as f:
    c = csv.DictReader(f, delimiter=',')
    for line in c:
        chart.append(line)

atk = chart[pokemon]['nb_hab_2012']

def pokemon_nbr(pokemon: str)-> int:
	"""takes a pokemon name and returns his index number"""
    l = []
    f = open("pokemon.csv", "r")
    c = csv.DictReader(f, delimiter=',')
    for line in c:
        if line['name'] == pokemon
            pokemon_index = line['#']
	return pokemon_index

def damage(pokemon):
	dmg = ((12/5)*/def)*type