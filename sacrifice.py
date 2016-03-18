'''

sacrifice.py

bleed bytes from file to stdout. pipeable to /dev/null or wherever.

TO-DO
	CLI interface
		--file
	Method
		while len(File)>0:
			read file
			find 'middle bytes'
			bytes to stdout
			save file, close
		else:
			unlink file from filesystem
'''


import argparse, sys

if __name__ == "__main__":
	cli_desc = ''

	parser = argparse.ArgumentParser(description=cli_desc)
	parser.add_argument('--file=', type='string', 
		help='')

	args = parser.parse_args()

	if args.file:
		print ''