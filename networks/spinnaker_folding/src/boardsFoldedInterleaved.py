#!/usr/bin/env python

import sys
sys.path.append("/home/jonathan/Programing/Python/SpiNNer")

import diagram

from model import board
from model import coordinates
from model import transforms
from model import topology

d = diagram.Diagram()

# Create a small system of boards on a hexagonal coordinate system
boards = board.create_torus(4,4)
boards = transforms.hex_to_cartesian(boards)
boards = transforms.rhombus_to_rect(boards)
boards = transforms.compress(boards)
#boards = transforms.space_folds(boards, (4,2), (0.7,1))
boards = transforms.fold(boards, (4,2))

# Create a dictionary which maps boards to coordinates to use for labelling
# boards in the diagram.
board2coord = dict(boards)

# Draw the boards on the diagram as a hexagons
for b, coords in boards:
	d.add_board_square(b, coords)
	
	for direction, colour in ( (topology.NORTH,      "red")
	                         , (topology.NORTH_EAST, "green")
	                         , (topology.EAST,       "blue")):
		if sum(map(abs, board2coord[b.follow_wire(direction)] - board2coord[b])) > 2:
			d.add_curved_wire(b, direction, [colour])
		else:
			d.add_wire(b, direction, [colour])


# Output the TikZ code for the diagram
print r"\begin{tikzpicture}[thick,scale=0.9]"
print r"\clip (-0.7,-0.7) rectangle ++(8.4,6.4);"
print d.get_tikz()
print r"\end{tikzpicture}"
