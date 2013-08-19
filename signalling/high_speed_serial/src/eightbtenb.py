#!/usr/bin/env python

five_six_code = {
	0b00000: ("D.00",   (0b111001,0b000110)),
	0b00001: ("D.01",   (0b101110,0b010001)),
	0b00010: ("D.02",   (0b101101,0b010010)),
	0b00011: ("D.03",   (0b100011,)       ),
	0b00100: ("D.04",   (0b101011,0b010100)),
	0b00101: ("D.05",   (0b100101,)       ),
	0b00110: ("D.06",   (0b100110,)       ),
	0b00111: ("D.07",   (0b000111,0b111000)),
	0b01000: ("D.08",   (0b100111,0b011000)),
	0b01001: ("D.09",   (0b101001,)       ),
	0b01010: ("D.10",   (0b101010,)       ),
	0b01011: ("D.11",   (0b001011,)       ),
	0b01100: ("D.12",   (0b101100,)       ),
	0b01101: ("D.13",   (0b001101,)       ),
	0b01110: ("D.14",   (0b001110,)       ),
	0b01111: ("D.15",   (0b111010,0b000101)),
	0b10000: ("D.16",   (0b110110,0b001001)),
	0b10001: ("D.17",   (0b110001,)       ),
	0b10010: ("D.18",   (0b110010,)       ),
	0b10011: ("D.19",   (0b010011,)       ),
	0b10100: ("D.20",   (0b110100,)       ),
	0b10101: ("D.21",   (0b010101,)       ),
	0b10110: ("D.22",   (0b010110,)       ),
	0b10111: ("D.23",   (0b010111,0b101000)),
	0b11000: ("D.24",   (0b110011,0b001100)),
	0b11001: ("D.25",   (0b011001,)       ),
	0b11010: ("D.26",   (0b011010,)       ),
	0b11011: ("D.27",   (0b011011,0b100100)),
	0b11100: ("D.28",   (0b011100,)       ),
	0b11101: ("D.29",   (0b011101,0b100010)),
	0b11110: ("D.30",   (0b011110,0b100001)),
	0b11111: ("D.31",   (0b110101,0b001010)),
	# K Chars                             
	"<comma>": ("K.28", (0b111100,0b110000)),
}

three_four_code = {
	0b000: (".0",  (0b1101,0b0010)),
	0b001: (".1",  (0b0101,      )),
	0b010: (".2",  (0b0110,      )),
	0b011: (".3",  (0b0011,0b1100)),
	0b100: (".4",  (0b0111,0b0100)),
	0b101: (".5",  (0b1001,      )),
	0b110: (".6",  (0b1010,      )),
	0b111: (".P7", (0b1011,0b1000)),
	0b111: (".A7", (0b1110,0b0001)),
	
	# K chars
	#0b000: (".0", (0b1101,0b0010)),
	#"<comma>":(".1", (0b1010,0b1001)),
	#0b010: (".2", (0b1001,0b1010)),
	#0b011: (".3", (0b0011,0b1100)),
	#0b100: (".4", (0b0111,0b0100)),
	#0b101: (".5", (0b0110,0b0101)),
	#0b110: (".6", (0b0101,0b0110)),
	#0b111: (".7", (0b1110,0b0001)),
}

def get_code(code, symb, disparity = 0):
	name, encodings = code[symb]
	
	if disparity < 0:
		encoding   = encodings[-1]
		disparity += 1 if len(encodings) > 1 else 0
	else:
		encoding   = encodings[0]
		disparity -= 1 if len(encodings) > 1 else 0
	
	return (name, encoding, disparity)


def enc_char(char, cur_disparity = 0):
	"""
	Returns (code name, 10bit code, new_disparity)
	"""
	name_1, abcdei, _             = get_code(five_six_code,   (char>>0)&0b11111, cur_disparity)
	name_2, fghj,   cur_disparity = get_code(three_four_code, (char>>5)&0b111,   cur_disparity)
	
	return (name_1+name_2, fghj | abcdei<<4, cur_disparity)


def enc_str(s, cur_disparity = 0):
	"""
	Returns (arr of code names, arr of bits, new_disparity)
	"""
	names = []
	bits  = []
	
	for char in s:
		name, code, cur_disparity = enc_char(ord(char), cur_disparity)
		names.append(name)
		bits.append([int(bool(code&(1<<n))) for n in range(10)])
	
	return (names, bits, cur_disparity)


def dec_code(code, code_bits):
	for bits, (name, code_bits_pos) in code.iteritems():
		if code_bits in code_bits_pos:
			return bits


def dec_char(code_bits):
	bits1 = dec_code(five_six_code,   (code_bits>>4) & 0b111111)
	bits2 = dec_code(three_four_code, (code_bits>>0) & 0b1111)
	
	if bits1 == "<comma>" and bits2 in (0b101,0b110):
		return "<comma>"
	elif bits1 is None or bits2 is None or bits1 == "<comma>":
		return None
	else:
		return (bits2<<5) | bits1


if __name__=="__main__":
	for char in map(chr, range(32,127)):
		c_name0, code0, disp0 = enc_char(ord(char), -1)
		c_name1, code1, disp1 = enc_char(ord(char), 0)
		c_name2, code2, disp2 = enc_char(ord(char), 1)
		
		if code0 != code1 or code1 != code2:
			print char, code0, code1, code2
