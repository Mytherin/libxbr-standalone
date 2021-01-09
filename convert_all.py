import sys
import os

target_program = './a.out'
methods = ['xbr2x', 'xbr3x', 'xbr4x', 'hq2x', 'hq3x', 'hq4x']

import sys
if len(sys.argv) < 2:
	print('python3 convert_all.py [input.png]')
	exit(1)

input_file = sys.argv[1]

for method in methods:
	output_file = input_file.split('.')[0] + '-' + method + '.png'
	os.system('%s %s %s %s' % (target_program, input_file, output_file, method))
