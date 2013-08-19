#!/usr/bin/env python

from random import random
from copy   import deepcopy

def b2a(c):
	"""
	Bits (1 char) to array
	"""
	return [int(bool(ord(c)&(1<<n))) for n in range(8)]

def a2b(a):
	return chr(sum(b<<n for n,b in enumerate(a)))

def string_to_bits(s):
	"""
	For each char, an array of bits.
	"""
	return [[int(bool(ord(c)&(1<<n))) for n in range(8)] for c in s]

def bits_to_waveform(bits, opts="", pre="", post=""):
	out = "\draw %s %s"%(opts, pre)
	
	for num, bit in enumerate(bits):
		out += "+(%d,%d) -- +(%d,%d) -- "%(num, bit, num+1, bit)
	
	return "%s %s;"%(out.rstrip(" -"), post)


def skew_string(s, sample_offset, skews):
	# Find the character to print after skewing
	
	skewed_s_bits = string_to_bits(s)
	for bit_num, skew in enumerate(skews):
		skew_bits = int(skew + sample_offset)
		
		for char_bits, prev_char_bits in zip(skewed_s_bits, ([[0]*8]*skew_bits) + skewed_s_bits)[::-1]:
			char_bits[bit_num] = prev_char_bits[bit_num]
	s = map(a2b, skewed_s_bits)
	
	return s


def clean_char(c):
	return repr(c)[1:-1].replace("\\x","")


def differing_bits(*strs):
	strs_bits = map(string_to_bits, strs)
	diffs = []
	for s in zip(*strs):
		diffs.append(b2a(chr(reduce((lambda a,b: a^b), map(ord, s)))))
	return diffs


def string_to_waveform(s_orig, spacing=0.5, scale=1.8, max_skew = 2, lines = True, chars = True):
	s_bits = string_to_bits(s_orig)
	
	# Scale the max skew so that no matter what the scale the skew is the same
	# amount on screen
	max_skew /= scale
	
	skews = [random()*max_skew for _ in range(8)]
	
	s = skew_string(s_orig, 0.5, skews)
	
	d_bits = differing_bits(s, s_orig)
	
	for num, char in enumerate(s):
		if lines:
			print r"\draw [gray,very thin] (%fcm,%fcm) -- (%fcm,%fcm);"%(
				scale*num + (scale/2.0),
				(8*(1+spacing)) - 0.5,
				scale*num + (scale/2.0),
				-0.5,
			)
		
		if chars:
			print r"\node at (%fcm,%fcm) [text height=3em] {\verb|%s|};"%(
				scale*num + (scale/2.0),
				-0.5,
				clean_char(char)
			)
	
	for bit_num in range(8)[::-1]:
		opts = "[xscale=%f]"%scale
		pre = r"(0, %fcm) node[yshift=-0.5ex,anchor=south east] {\footnotesize\texttt{d[%d]}} -- "%(
			(bit_num*(1+spacing)),
			bit_num
		)
		pre += "++(%fcm,0) -- "%(skews[bit_num])
		post = "-- +(%fcm,0) -- +(%fcm,0)"%(
			len(s_bits),
			len(s_bits)+(max_skew-skews[bit_num]),
		)
		print bits_to_waveform((bits[bit_num] for bits in s_bits), opts, pre, post)
	
	for char_num, char in enumerate(d_bits):
		for bit_num, bit_differs in enumerate(char):
			if bit_differs:
				print "\draw [red] (%fcm,%fcm) ellipse (%f and %f);"%(
					scale*(skews[bit_num]+char_num),
					(bit_num*(1+spacing) + 0.5),
					0.3,
					0.6
				)


if __name__=="__main__":
	import sys
	
	from random import seed
	seed(2)
	
	print r"\begin{tikzpicture}[scale=0.35, thick]"
	string_to_waveform(sys.argv[1], *map(float, sys.argv[2:]))
	print r"\end{tikzpicture}"

