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

'''

import time, hashlib, string, sys, os, atexit, argparse
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

class SigilDaemon:
	"""
	Adapted from http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/
	"""

	# network
	_ADDR = "127.0.0.1"
	_PORT = 5005# work out arcane features later
	_CONSTANCE = 5
	_SIGIL = Sigil()

	def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
		self.stdin = stdin
		self.stdout = stdout
		self.stderr = stderr
		self.pidfile = pidfile
	
	def daemonize(self):
		try: 
			pid = os.fork() 
			if pid > 0:
				# exit first parent
				sys.exit(0) 
		except OSError, e: 
			sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
			sys.exit(1)
	
		# decouple from parent environment
		os.chdir("/tmp") 
		os.setsid() 
		os.umask(0) 
	
		# do second fork
		try: 
			pid = os.fork() 
			if pid > 0:
				# exit from second parent
				sys.exit(0) 
		except OSError, e: 
			sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
			sys.exit(1) 
	
		# redirect standard file descriptors
		sys.stdout.flush()
		sys.stderr.flush()

		# Comment out to debug:
		# si = file(self.stdin, 'r')
		# so = file(self.stdout, 'a+')
		# se = file(self.stderr, 'a+', 0)
		# os.dup2(si.fileno(), sys.stdin.fileno())
		# os.dup2(so.fileno(), sys.stdout.fileno())
		# os.dup2(se.fileno(), sys.stderr.fileno())
	
		# write pidfile
		atexit.register(self.delpid)
		pid = str(os.getpid())
		file(self.pidfile,'w+').write("%s\n%s" % (pid, self._SIGIL.admire()))
	
	def delpid(self):
		os.remove(self.pidfile)

	def start(self):
		"""
		Start the daemon
		"""
		# Check for a pidfile to see if the daemon already runs
		try:
			os.chdir("/tmp")  
			pf = file(self.pidfile,'r')
			pid = int(pf.read().strip())
			pf.close()
		except IOError:
			pid = None

		if pid:
			message = "pidfile %s already exist. Daemon already running?\n"
			sys.stderr.write(message % self.pidfile)
			sys.exit(1)
		
		# Start the daemon
		self.daemonize()
		self.run()

	def stop(self):
		"""
		Stop the daemon
		"""
		# Get the pid from the pidfile
		try:
			os.chdir("/tmp") 
			pf = file(self.pidfile,'r')

			# Grab firstline
			pid = int(pf.readline().strip())
			pf.close()
		except IOError:
			pid = None
	
		if not pid:
			message = "pidfile %s does not exist. Daemon not running?\n"
			sys.stderr.write(message % self.pidfile)
			return # not an error in a restart

		# Try killing the daemon process	
		try:
			while 1:
				os.kill(pid, SIGTERM)
				time.sleep(0.1)
		except OSError, err:
			err = str(err)
			if err.find("No such process") > 0:
				if os.path.exists(self.pidfile):
					os.remove(self.pidfile)
			else:
				print str(err)
				sys.exit(1)

	def restart(self):
		"""
		Restart the daemon
		"""
		self.stop()
		self.start()

	def run(self):
		if self._SIGIL.is_made():
			while True:
				#broadcast
				daemon_socket = socket(AF_INET, SOCK_DGRAM)
				daemon_socket.sendto(self._SIGIL.admire(), (self._ADDR, self._PORT))
				time.sleep(self._CONSTANCE)
		else:
			self._SIGIL.conjure()
			self.run()

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

if __name__ == "__main__":

	sigil_path = conjure_sigil_pidfile_name()

	#(Re)Construct Daemon
	daemon = SigilDaemon(sigil_path) #we'll write a routine to get a new one of these so multiples can run
	conjure_bool = False

	parser = argparse.ArgumentParser(description='Conjure cryptographic sigils and regularly broadcast them on the network via UDP.')
	sp = parser.add_subparsers()
	sp_start = sp.add_parser('start', help='Conjure sigil and Daemonize UDP server', dest=)
	sp_stop = sp.add_parser('stop', help='Stop previous daemon')
	sp_dry = sp.add_parser('dry', help='Conjure and print signal and exit')
	parser.add_argument('--port', help='UDP broadcast port (Default 5005)')
	parser.add_argument('--interface', help='UDP broadcast interface (Default: 0.0.0.0)')

	args = parser.parse_args()

	if sp.start == :
		os.chdir("/tmp")
		if not (os.path.exists(sigil_path)):
			if daemon.sigilStatus() is False:
				daemon.conjureSigil()
		daemon.start()

	if args.stop:
			daemon.stop()

	if args.dry:
		# Construct and output sigil witout daemonization
		sigil = Sigil()
		sigil.conjure()
