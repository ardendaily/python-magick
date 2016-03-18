#!/usr/bin/python
'''

burn.py

'''

import argparse, sys
from random import random
from time import sleep

def str2bool(v):
  #susendberg's function
  return v.lower() in ("yes", "true", "t", "1")

class Burnable:
	'''
	Holds a message until invoked to destroy it.
	'''
	def __init__(self):
		self.message = ""
		self.destroyed = False

	def set_message(self, _message):
		self.message = _message

	def set_is_animated(self, _bool):
		self.is_animated = _bool

	def destroy_chaotic(self):
		fire = open("/dev/urandom")

		while len(self.message) > 0:
			#Change a letter
			rand_int = int(random() * len(self.message))
			t_list = list(self.message)
			t_list[rand_int] = fire.read(1)
			self.message = ''.join(c for c in t_list)

			#Lose a letter
			rand_int = int(random() * len(self.message))
			t_list = list(self.message)
			t_list.pop(rand_int)
			self.message = ''.join(c for c in t_list)

			if self.is_animated:
				print self.message
				sleep(0.1)

		fire.close()
		self.destroyed = True

	def destroy_orderly(self):
		fire = open("/dev/urandom")

		destroy_pass = 0

		while destroy_pass < 2:
			i = 0

			if destroy_pass == 0:
				while i < len(self.message):
					t_list = list(self.message)
					t_list[i] = fire.read(1)
					i += 1
					self.message = ''.join(c for c in t_list)
					if self.is_animated:
						print self.message
						sleep(0.1)

			elif destroy_pass == 1:
				while len(self.message) > 0:
					t_list = list(self.message)
					t_list.pop(0)
					self.message = ''.join(c for c in t_list)
					if self.is_animated:
						print self.message
						sleep(0.1)

			destroy_pass += 1

		fire.close()
		self.destroyed = True

	def run(self, _bool):
		if _bool:
			self.destroy_orderly()
		else:
			self.destroy_chaotic()

if __name__ == "__main__":
	cli_desc = ''

	parser = argparse.ArgumentParser(description=cli_desc)
	parser.register('type', 'bool', str2bool) #extend argparse types
	parser.add_argument('file', nargs="?", metavar='FILE',
		type=argparse.FileType('rw'), default=sys.stdin, 
		help='File to read. If empty, STDIN is used.')
	parser.add_argument('--burntype', default="orderly",
		help='Type of burn, either orderly or chaotic. Defaults to orderly.')
	parser.add_argument('--animated', default=True, type='bool', 
		help='Animate process to <stdout>, true or false. Defaults to true.')
	args = parser.parse_args()

	# Close if stdin is empty
	if args.file.isatty():
		print "Must provide data!"
		exit(2)

	paper = Burnable()
	paper.set_message(args.file.read())
	paper.set_is_animated(args.animated)
	paper.run( True if args.burntype == 'orderly' else False )