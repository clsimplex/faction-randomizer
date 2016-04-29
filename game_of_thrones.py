#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from random import shuffle
# CL Simplex 2016
# Levon Zadravec-Powell
# Eric Moolin
# Free Beer License
# As is - no warranty. Go away.

# This is a companion for the second edition of the Game of Thrones board game.
# This is the part where we disclaim any affliation with their copyright and stuff.


# Order matters.
HOUSES = ['STARK', 'LANNISTER', 'BARATHEON', 'GREYJOY', 'TRYELL', 'MARTELL']

def randomize(names):
	"""
	Given a list of names assign GOT houses to them.

	Needs minimum of 3 names. Max of 6.

	Returns a dictionary of the form: { PLAYER: HOUSE }
	"""
	number_of_players = len(names)

	if number_of_players < 3 or number_of_players > 6:
		raise Exception('Incorrect number of players. You need 3-6.')

	# This enforces which houses are available based on the number of players.
	houses_in_use = HOUSES[:number_of_players]

	shuffle(houses_in_use)

	# Generates dictionary using Python list comprehension
	return { player:houses_in_use.pop() for player in names }

# Main support.

if __name__ == '__main__':
	print( randomize(sys.argv[1:]) )
