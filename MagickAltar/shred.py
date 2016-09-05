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


import argparse, sys

if __name__ == "__main__":
	cli_desc = ''

	parser = argparse.ArgumentParser(description=cli_desc)
	parser.add_argument('--file=', type='string', 
		help='')

	args = parser.parse_args()

	if args.file: #load file
		#args.file.read() #does the job

	# Close if stdin is empty
	if args.file.isatty():
		print "Must provide data!"
		exit(2)
