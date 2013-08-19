#!/usr/bin/env python

import sys
sys.path.append("/home/jonathan/Programing/Python/SpiNNer")

import diagram

from model import board
from model import transforms
from model import topology

d = diagram.Diagram()

# Create a small system of boards on a hexagonal coordinate system
boards = board.create_torus(4,4)

# Create a dictionary which maps boards to coordinates to use for labelling
# boards in the diagram.
board2coord = dict(boards)

# Draw the boards on the diagram as a hexagons
for board, coords in boards:
	d.add_board_hexagon(board, coords)
	
	# Draw only long wires
	for direction, colour in ( (topology.NORTH,      "red")
	                         , (topology.NORTH_EAST, "green")
	                         , (topology.EAST,       "blue")):
		if sum(map(abs, board2coord[board.follow_wire(direction)] - board2coord[board])) > 2:
			d.add_wire(board, direction, [colour])

# Output the TikZ code for the diagram
print r"\begin{tikzpicture}[thick]"
print d.get_tikz()
print r"\end{tikzpicture}"
