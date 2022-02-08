from math import *
from random import *
import csv
chart = []
with open("pokemon.csv") as f:
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



def atk(pokemon: str)-> int:
	"""takes a pokemon string and returns his attack"""
    pokemon_nbr = pokemon_index(pokemon)
    atk = int(chart[pokemon_nbr]['Attack'])
    return atk



def defense(pokemon: str)-> int:
	"""takes a pokemon string and returns his defense"""
    pokemon_nbr = pokemon_index(pokemon)
    defense = int(chart[pokemon_nbr]['Defense'])
    return defense


    
def raw_damage(pokemon: str)-> float:
	"""takes a pokemon string and returns his damage"""
    pokemon_nbr = pokemon_index(pokemon)
    atk = int(chart[pokemon_nbr]['Attack'])
    defense = int(chart[pokemon_nbr]['Defense'])
    print(atk)
    print(defense)
		print(bonus_dmg)
    raw_dmg = ((2.4*atk)/(defense/5))
    return raw_dmg



def fastest_pokemon(pokemon1: str, pokemon2: str)-> str:
	"""takes 2 pokemon strings and returns the fastest pokemon"""
	randlist = [pokemon1; pokemon2]
	pokemon1_nbr = pokemon_index(pokemon)
	pokemon2_nbr = pokemon_index(pokemon)
	atksp1 = int(chart[pokemon1_nbr]['Sp. Atk']
	atksp2 = int(chart[pokemon2_nbr]['Sp. Atk']
	if atksp1 > atksp2:
		fastestpok = pokemon1
	elif atksp1 = atksp2:
		fastestpok = random.choice(randlist)
	return fastestpok

def battle_HP(HP: int, dmg: int)->int:
	new_HP = HP - dmg
	return new_HP


