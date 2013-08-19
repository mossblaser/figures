#!/usr/bin/env python

from random import gauss
from itertools import izip_longest

from eightbtenb import enc_str

def grouper(n, iterable, fillvalue=None):
	"Collect data into fixed-length chunks or blocks"
	# grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
	args = [iter(iterable)] * n
	return izip_longest(fillvalue=fillvalue, *args)

def b2a(c):
	"""
	Bits (1 char) to array
	"""
	return [int(bool(ord(c)&(1<<n))) for n in range(8)]

def a2b(a):
	return chr(sum(b<<n for n,b in enumerate(a)) & 0xFF)

def clean_char(c):
	return repr(c)[1:-1].replace("\\\\","\\").replace("\\x","0x")

def string_to_bits(s):
	"""
	For each char, an array of bits.
	"""
	return [[int(bool(ord(c)&(1<<n))) for n in range(8)] for c in s]





def bits_to_waveform(label, bits, noise, opts=""):
	
	min_noise = min(noise)
	max_noise = max(noise)
	
	out = r"\begin{scope}[yshift=0.5cm]"
	
	out += r"\draw %s (0,0) node[anchor=east] {%s}"%(
		opts,
		label
	)
	
	for num, bit in enumerate(bits):
		if max_noise == min_noise:
			mag = (bit+noise[num]-min_noise)
			mag -= 0.5
		else:
			mag = (bit+noise[num]-min_noise)/(max_noise-min_noise)
			mag -= (1)/(max_noise-min_noise)
		out += "+(%fcm,%fcm) -- +(%fcm,%fcm) -- "%(num, mag, num+1, mag)
	
	return (r"%s;\end{scope}"+"\n")%out.rstrip(" -")


def draw_characters(chars, bad_chars, opts="", brace_size=0.25, char_width=8):
	out = r"\begin{scope}%s"%opts + "\n"
	
	for num, (char,bad_char) in enumerate(zip(chars,bad_chars)):
		out += r"  \draw [shorten >=1pt,shorten <=1pt,decorate,decoration={brace,amplitude=%fcm,mirror}]"%(
			brace_size
		)
		out += r" (%fcm,%fcm) -- (%fcm,%fcm) node [%smidway,below=%fcm,text height=1.5ex] {\texttt{%s}};"%(
			num*char_width,     0,
			(num+1)*char_width, 0,
			"red," if char != bad_char else "",
			brace_size,
			clean_char(bad_char)
		) + "\n"
	
	out += r"\end{scope}"
	return out


def generate_noise(length, noise_sigma):
	return [max(min(gauss(0, noise_sigma), 1+noise_sigma), -1-noise_sigma)
	        for _ in range(length)]


def string_to_serial(wave_label, s, show_labels = True, noise_sigma = 0.0, just_noise = False, negate = False, encode=False, scale = 0.5, brace_size = 0.25):
	out = ""
	
	s = s.replace("*","\0")
	
	bits = sum(string_to_bits(s), [])
	
	if encode:
		char_width = 10
		s, bits, _ = enc_str(s)
		s = [r"\footnotesize{}" + x for x in s]
		bits = sum(bits,[])
	else:
		char_width = 8
	
	n_bits = [(b+1)%2 for b in bits]
	
	noise = generate_noise(len(bits), noise_sigma)
	
	# Get corrupted string
	bad_bits = [int(b+n+0.5) for (b,n) in zip(bits,noise)]
	bad_s = "".join(map(a2b, grouper(char_width,bad_bits)))
	
	if just_noise:
		bits     = [0]*len(bits)
		bad_bits = [1]*len(bits)
		bad_s    = s
		noise    = [n+0.5 for n in noise]
	
	if encode:
		bad_s = s
	
	# Waveform
	out += bits_to_waveform(wave_label,
	                        n_bits  if negate else bits,
	                        noise,
	                        "[xscale=%f]"%scale)
	
	# Char labels
	if show_labels:
		out += draw_characters(s,bad_s, "[yshift=%fcm,xscale=%f]"%(-(0.1+noise_sigma*3), scale), brace_size, char_width)
	
	return out


if __name__=="__main__":
	import sys
	
	from random import seed
	seed(2)
	
	print r"\begin{scope}[yscale=1.2,scale=0.35, thick]"
	print string_to_serial(sys.argv[1], sys.argv[2], *map(float, sys.argv[3:]))
	print r"\end{scope}"

