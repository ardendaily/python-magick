#!/usr/bin/python
'''

chalice.py

a 256kB instrument of holding.

'''

import argparse, time, sys, os

class Chalice():

	def __init__(self):
		self.vessel = ""
		self.size = 256
		self.filename = ""

	def fill_from_file(self, _kb, _file):
		'''
		The cup dips into the file, and withdraws precisely what it needs to... 
		at a cost to the file.
		'''
		self.filename = _file.name
		self.vessel = _file.read( _kb * 1000 )
		filename = _file.name
		_file.seek( (_kb * 1000) + 1 ) 
		rest_of_file = _file.read()
		_file.close()
		os.remove(filename)
		newfile = open(filename, "w")
		newfile.write(rest_of_file)
		newfile.close()

	def fill_from_stdin(self, _kb, _pipe):
		'''
		The cup drinks from the flow, withdrawing what it needs. The remaining 
		data runs down the drain.
		'''
		self.filename = '<stdin>'
		self.vessel = _pipe.read( _kb * 1000 )
		drain = open("/dev/null", "w")
		drain.write( _pipe.read() )
		drain.close()
		_pipe.close()
		print ""
		print "Some bytes run into /dev/null"
		print ""

	def empty(self):
		drain = open("/dev/null", "w")
		drain.write( self.vessel )
		self.vessel = ""
		drain.close()

		print ""
		print "chalice.py emptied."
		print ""
		exit(0)

	def hold(self):
		try:
			print "The chalice holds about %s kilobytes from %s." % ( 
				int( len( self.vessel ) / 1000), self.filename) 
			print "" 
			print "^C to exit."

			while True:
				time.sleep(1)

		except KeyboardInterrupt:
			self.empty()

def kilobytes_from_fraction(_fraction):
	from fractions import Fraction
	fraction = Fraction(_fraction)

	if fraction.numerator > fraction.denominator:
		fraction = Fraction(1)
		print "Your bytes runneth over."

	ret_bytes = (256 * fraction.numerator) / fraction.denominator
	return int(ret_bytes) #precision is not the stuff of magick

if __name__ == "__main__":
	cli_desc = '''A 256kB instrument of holding. Accepts message from file or 
	stdin until closed, when its contents are discarded. You may specify how 
	much you would like to fill chalice.py in fractions; otherwise it will be
	filled to the brim. Removes bytes from given file.
	'''

	cli_epilog = '''e.g.\n\n `./chalice.py sigil.jpg --fillto "1/2"` fills 
	chalice.py with 128kb of sigil.jpg.'''

	parser = argparse.ArgumentParser(description=cli_desc, epilog=cli_epilog)
	parser.add_argument('file', nargs="?", metavar='FILE',
		type=argparse.FileType('rw'), default=sys.stdin, 
		help='File to read. If empty, STDIN is used.')
	parser.add_argument('--fillto', help='Amount of chalice to fill, in fractions.')

	args = parser.parse_args()

	if args.fillto != None:
		num_kb = kilobytes_from_fraction(args.fillto)
	else:
		num_kb = 256

	# Close if stdin is empty
	if args.file.isatty():
		print "Must provide data!"
		exit(2)

	chalice = Chalice()

	if args.file.name == '<stdin>':
		chalice.fill_from_stdin( num_kb, args.file )
	else:
		chalice.fill_from_file( num_kb, args.file )

	chalice.hold()