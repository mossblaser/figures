#!/usr/bin/env python

import random

import sys

# Should a single neuron and its synapsese be highlighted?
HIGHLIGHT_ONE = bool(int(sys.argv[1]))

random.seed(6)

WIDTH = 65
HEIGHT = 40
CROP = 5

NUM_NEURONS = 300
NUM_CON  = 20
PROB_THRESH = 0.1
NEURON_SHIFT = 0.5

# List of (x,y, [targets]) where targets are (x,y) pairs. Insert one token
# central one which be our example neuron
neurons = [(WIDTH/2, HEIGHT/2, [])]

# Produce a random set of neurons
for n in range(NUM_NEURONS):
	while True:
		x = random.randrange(0,WIDTH-1)
		y = random.randrange(0,HEIGHT-1)
		if (x, y, []) not in neurons:
			neurons.append((x,y, []))
			break

# Randomly connect neurons
for x,y, connections in neurons:
	possible_connections = neurons[:]
	random.shuffle(possible_connections)
	for _ in range(NUM_CON):
		for x2,y2,_ in possible_connections:
			weight = (float((x-x2)**2 + (y-y2)**2) / (WIDTH**2 + HEIGHT**2)) ** 0.5
			if PROB_THRESH > weight and (x2,y2) not in connections:
				connections.append((x2,y2))
				break

print r"\begin{tikzpicture}[scale=0.3,inner sep=0]"

if HIGHLIGHT_ONE:
	print r"\tikzset{example/.style={red,thick,minimum width=0.5em},nonexample/.style={ultra thin,white!90!black}}"
else:
	print r"\tikzset{example/.style={ultra thin},nonexample/.style={ultra thin}}"

print r"\clip (%d,%d) rectangle (%d,%d);"%(CROP, CROP, WIDTH-CROP, HEIGHT-CROP)
print r"\begin{pgfonlayer}{background}"
print r"\clip (%d,%d) rectangle (%d,%d);"%(CROP, CROP, WIDTH-CROP, HEIGHT-CROP)
print r"\end{pgfonlayer}"

print r"\draw (0,0) rectangle ++(%d,%d);"%(WIDTH,HEIGHT)

# Neuron positions
for x,y,_ in neurons:
	x_pos = x + random.gauss(0.0, NEURON_SHIFT)
	y_pos = y + random.gauss(0.0, NEURON_SHIFT)
	print r"\node (neuron %d %d) at (%f,%f) {};"%(x, y, x_pos, y_pos)

# Synapses
for x,y,connections in neurons:
	for x2,y2 in connections:
		if (x,y) == (WIDTH/2, HEIGHT/2):
			print r"\draw [example] (neuron %d %d) -- (neuron %d %d);"%(x,y, x2,y2)
		else:
			print r"\begin{pgfonlayer}{background}"
			print r"\draw [nonexample] (neuron %d %d) -- (neuron %d %d);"%(x,y, x2,y2)
			print r"\end{pgfonlayer}"

# Neurons
for x,y,_ in neurons:
	if (x,y) == (WIDTH/2, HEIGHT/2):
		print r"\node [fill,circle,minimum width=0.5ex,example] at (neuron %d %d) {};"%(x,y)
	else:
		print r"\begin{pgfonlayer}{background}"
		print r"\node [nonexample,fill,circle,minimum width=0.5ex] at (neuron %d %d) {};"%(x,y)
		print r"\end{pgfonlayer}"

print r"\end{tikzpicture}"
