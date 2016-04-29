#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from random import shuffle
# CL Simplex 2016
# Levon Zadravec-Powell
# Free Beer License
# As is - no warranty. Go away.

FACTIONS = ['BRITAIN', 'RUSSIA', 'UNITED STATES', 'JAPAN', 'GERMANY']

def randomize(names):
	"""
	You need 5 players.
	"""
	number_of_players = len(names)

	if number_of_players != 5:
		raise Exception('Incorrect number of players. You need 5.')

	shuffle(FACTIONS)

	return { player:FACTIONS.pop() for player in names }

if __name__ == '__main__':
	print( randomize(sys.argv[1:]) )