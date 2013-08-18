#!/usr/bin/env python

"""
Generates a tikzpicture containing three plots showing the incoming spikes to a
neuron, the charge intergrated in it and the spikes it produces.
"""

import random

random.seed(10)

WIDTH = 8
HEIGHT = 1.4

DURATION = 100
SPIKE_PROB = 0.15

THRESHOLD    = 1
SPIKE_CHARGE = 0.4
DECAY        = 0.90

# A list of bools saying whether a spike is emitted at this time step
spikes = [(t%2 or random.random()) < SPIKE_PROB for t in range(DURATION)]

# Simulate the neuron
charges = [0]
out_spikes = [False]
new_charge = charges[0]
for time, spike in enumerate(spikes):
	new_charge *= DECAY
	if spike:
		new_charge += SPIKE_CHARGE
	
	charges.append(new_charge)
	
	# Spike?
	if new_charge > THRESHOLD:
		out_spikes.append(True)
		new_charge = 0
	else:
		out_spikes.append(False)

################################################################################

def chart(d, y_label, x_label = "Time", threshold = None):
	"""
	Generate the tikz for a chart.
	"""
	d_min = min(min(d),threshold or 0) * 1.2
	d_max = max(max(d),threshold or 1) * 1.2
	d_rng = (d_max - d_min)
	d_len = len(d) or 1
	
	def t(x,y):
		x = x / float(d_len)
		y = (y - d_min) / float(d_rng)
		return "(%f,%f)"%(x,y)
	
	print r"\begin{scope}[node distance=0.5ex]"
	
	# Axes
	print r"\draw [->,thick] %s -- coordinate(y-axis) %s;"%(t(0,d_min), t(0,d_max))
	print r"\draw [->,thick] %s -- coordinate(x-axis) %s;"%(t(0,0), t(d_len,0))
	
	# Labels
	print r"\node [below=of x-axis] {%s};"%x_label
	print r"\node [left=of y-axis] {%s};"%y_label
	
	# Data
	print r"\draw %s;"%(
		" -- ".join(t(time,v) for (time,v) in enumerate(d))
	)
	
	if threshold is not None:
		print r"\draw [help lines] %s -- %s node [right] {Threshold};"%(
			t(0, threshold),
			t(d_len, threshold),
		)
	
	print r"\end{scope}"

################################################################################

print r"\begin{tikzpicture}"

# Draw the incoming spikes
print r"\begin{scope}[xscale=%f,yscale=%f]"%(WIDTH,HEIGHT)
chart(spikes, "Input Spikes")
print r"\end{scope}"

# Draw the neuron charge
print r"\begin{scope}[xscale=%f,yshift=-2cm,yscale=%f]"%(WIDTH,HEIGHT)
chart(charges, "Neuron Charge", threshold = THRESHOLD)
print r"\end{scope}"

# Draw the outgoing spikes
print r"\begin{scope}[xscale=%f,yshift=-4cm,yscale=%f]"%(WIDTH,HEIGHT)
chart(out_spikes, "Output Spikes")
print r"\end{scope}"

print r"\end{tikzpicture}"
