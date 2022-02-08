from math import *
from random import *

import csv
chart = []
with open("pokedex.csv") as f:
  c = csv.DictReader(f, delimiter=',')
  for line in c:
		chart.append(line)



def pokemon_index(pokemon: str)-> int:
  """takes a pokemon name and returns his index number"""
  l = []
  f = open("pokedex.csv", "r")
  c = csv.DictReader(f, delimiter=',')
	for line in c:
    if line['Pokemon'] == pokemon:
       pokemon_nbr = int(line['Number'])
  return pokemon_nbr



def pokemon_check(pokemon: int):
	"""Takes a pokemon index number, checks if it exists and returns info"""
  l = []
  f = open("pokedex.csv", "r")
  c = csv.DictReader(f, delimiter=',')
	if pokemon['Pokemon'] != '':
		pok_name = (pokemon-1)['Pokemon']
		pok_nbr = pokemon
	else:
		return "Pokemon not found. Please enter a correct value."
	return "Your pokemon's name is " + pok_name + " and his pokedex number is " + pok_nbr + '.'



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



def sprite(pokemon: str)-> str:
	"""takes a pokemon string and returns the link of his sprite png"""
	pokemon


    
def raw_damage(pokemon: str)-> float:
	"""takes a pokemon string and returns his damage"""
  pokemon_nbr = pokemon_index(pokemon)
  atk = int(chart[pokemon_nbr]['Attack'])
  defense = int(chart[pokemon_nbr]['Defense'])
  raw_dmg = ((2.4*atk)/(defense/5))
  return raw_dmg



def fastest_pokemon(pokemon1: str, pokemon2: str)-> str:
	"""takes 2 pokemon strings and returns the fastest pokemon"""
	randlist = [pokemon1; pokemon2]
	pokemon1_nbr = pokemon_index(pokemon)
	pokemon2_nbr = pokemon_index(pokemon)
	atksp1 = int(chart[pokemon1_nbr]['Speed']
	atksp2 = int(chart[pokemon2_nbr]['Speed']
	if atksp1 > atksp2:
		fastestpok = pokemon1
	elif atksp1 = atksp2:
		fastestpok = random.choice(randlist)
	return fastestpok



def battle_HP(HP: int, dmg: int)->int:
	new_HP = HP - dmg
	return new_HP



def flinching():
	return "Sorry, your pokemon is unable to fight, please let him alone"



def battle():
	pok1 = int(input("What pokemon do you choose for the fight? (number)"))
	pok2 = int(input("What pokemon do you choose for the fight? (number)"))
	start_pok = fastest_pokemon(pok1, pok2)
	return winner