#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CL Simplex
# 2016
# Levon Zadravec-Powell
# Eric Moolin
# Free Beer License
# As is - no warranty. Go away.
import sys
from random import shuffle

players = sys.argv[1:]

if len(players) < 3:
	raise Exception('Not enough players. You need 3-6.')

HOUSES = ['STARK', 'LANNISTER', 'BARATHEON', 'GREYJOY', 'TRYELL', 'MARTELL']

result = {}

HOUSES = HOUSES[:len(players)]

shuffle(HOUSES)

for player in players:
	result[ player ] = HOUSES.pop()

print(result)