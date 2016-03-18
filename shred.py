'''

shred.py

TO-DO
	CLI Interface
		--file
	Methods
		read file
		cut(axis)
			split file on axis (horiz, vert)
			save halves
		delete original

'''


import ArgumentParser, sys

if __name__ == "__main__":
	cli_desc = ''

	parser = argparse.ArgumentParser(description=cli_desc)
	parser.add_argument('--file=', type='string', 
		help='')

	args = parser.parse_args()

	if args.file:
		print ''