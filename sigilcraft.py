#!/usr/bin/python

'''


RUNECRAFT

"i feel better now more than ever"

9fc9b6229b539
3020b4745d969
43debdb86ec5a
54b9414ef2960
2787221967e0c
c277a9c1f04c9
39b33462258b6
9219ce7670214
c05b5af868a8f
79a8dc72ceb

OK, day 1:
	Basic stuff implemented / bootstrapped.
	There are dependencies I want gone... really just 'daemon'. (Or is it python-daemon...?)
	Beginning to think that it's cruft-y and I should just implement the few features I need. 


	...also: 
	I think this might be the opportunity to learn how to package up python projects. 

	basically, this is small enough:
		is_pid? 
			shout RUNE at PORT 
			wait
			repeat
		no is_pid?
			gen RUNE, set pid, restart
		is stop?
			rm pid, die

Day 2:
	Stole daemon code from internet to drop gnarly, obtuse, crufty dependency. 
	retooled sigilcraft implementation from 'drop-out' sigilcraft (someone's method, look 
	this up later) to additive hash-seed method (arden's method, kekeke)

	sigilcraft parts seem to work pretty well. getting the daemon to play well is something else...
	it's not daemonizing?? maybe permission errors? gotta look into that later.

	goodnight for now....[]

Day 3:
	Lost to time.

Day 4:
	Restructuring. I do not need a generic daemon, I must construct one to my own specification.
	This pre-fab stuff is too error prone. I am attempting to adapt the old master's design,
	and to also correct all of the mis-steps he has lain in his craft. 

	I have decided to attempt to use argparse in order to best align to His Serpentine Methods.

	It's night now. You try to get work done and the little demons come to bother you.
	ArgParse slowly being slotted in to place. Still needs coercion. 

Day 5:
	I will get these damnable arguments to yield yet!

'''

import time, hashlib, string, sys, os, atexit, getopt
from socket import *
from signal import SIGTERM

class Sigil:
	'''
	API bindings for sigilcraft. 
	'''

	sigil_hash_bind = hashlib.sha512()
	made = False

	def __init__(self):
		'''
		'''

	def conjure(self):
		# user input appends to seed
		print "will"
		self.sigil_hash_bind.update( raw_input("> ") )
		print ""
		print "refine"
		self.sigil_hash_bind.update( raw_input("> ") )
		print ""
		print "refine one last time"
		self.sigil_hash_bind.update( raw_input("> ") )

		print "the sigil is so: "
		print "" 
		print self.admire() + "\n"

		print ""
		print "verify with `nc -ul [port]`"

		self.made = True

	def admire(self):
		return self.sigil_hash_bind.hexdigest()

	def is_made(self):
		return self.made 

	def conjureSigil(self):
		self._SIGIL.conjure()

	def sigilStatus(self):
		return self._SIGIL.is_made()

def conjure_sigil_pidfile_name():
	'''
	Ought to invoke an arcana somehow 
	'''
	return 'sigil.pid'

def conjure_sigil_portnum():
	'''
	We can use some
	'''
	return 5005

def daemon_ctl(_daemon,_action="start"):
	if _action is "start":
		os.chdir("/tmp")
		if not (os.path.exists(sigil_path)):
			if _daemon.sigilStatus() is False:
				_daemon.conjureSigil()
		_daemon.start()
	if _action is "stop":
		_daemon.stop()

def dry_run():
		sigil = Sigil()
		sigil.conjure()



if __name__ == "__main__":

	sigil_path = conjure_sigil_pidfile_name()

	#(Re)Construct Daemon
	daemon = SigilDaemon(sigil_path) #we'll write a routine to get a new one of these so multiples can run
	conjure_bool = False

	try:
		opts, args = getopt.getopt(sys.argv[1:], "xkdp:i:", ["start", "stop", "dry", "port=", "interface="])
	except getopt.GetoptError as err:
		print str(err)
		usage()
		sys.exit(2)
	output = None
	for o, a in opts:
		if o in ('-p', '--port'):
			daemon.setport(a)
		elif o in ('-i'  '--interface'):
			daemon.setinterface(a)
		elif o in ('-x', '--start'):
			daemon_ctl(daemon, "start")
		elif o in ('-k', '--stop'):
			daemon_ctl(daemon, "stop")
		elif o in ('-d', '--dry'):
			dry_run()

	parser = argparse.ArgumentParser(description='Conjure cryptographic sigils and regularly broadcast them on the network via UDP.')
	sp = parser.add_subparsers()
	sp_start = sp.add_parser('start', help='Conjure sigil and Daemonize UDP server', dest=daemon_ctl)
	sp_stop = sp.add_parser('stop', help='Stop previous daemon')
	sp_dry = sp.add_parser('dry', help='Conjure and print signal and exit')
	parser.add_argument('--port', help='UDP broadcast port (Default 5005)')
	parser.add_argument('--interface', help='UDP broadcast interface (Default: 0.0.0.0)')

	args = parser.parse_args()


	if args.dry:
		# Construct and output sigil witout daemonization

