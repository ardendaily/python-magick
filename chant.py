#!/usr/bin/python
'''

chant.py

'''

import argparse, sys, fileinput, socket, time

class SimpleUDP:

	def __init__(self):
		self.addr = ''
		self.port = 0

	def setAddress(self,_address):
		self.addr = _address

	def getAddress(self):
		return self.addr

	def setPort(self,_port):
		self.port = int(_port)

	def getPort(self):
		return int(self.port)

	def run(self,_message):
		udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		udp_socket.sendto(_message, ( self.getAddress(), self.getPort() ))

def chant(_message, _address, _port, _interval):
	try:
		#Set up UDP
		udp = SimpleUDP()
		udp.setAddress(_address)
		udp.setPort(_port)

		#Pad message
		_message = _message + "\r\n"

		print "Chanting your message on %s:%s." % (_address,_port)
		print "Optionally verify this with netcat."
		print "^C to exit."

		while True:
			udp.run(_message)
			time.sleep(_interval)

	except KeyboardInterrupt:
		exit(0)

if __name__ == "__main__":
	cli_desc = 'Chants message from file or stdin as UDP message on specified address and port.'

	parser = argparse.ArgumentParser(description=cli_desc)
	parser.add_argument('--address', 
		help='Address to which your message will be broadcast.')
	parser.add_argument('--port', type=int, 
		help='Port on which your message will be broadcast.')
	parser.add_argument('--interval', type=int,
		help='Time between chants, in seconds.')	
	parser.add_argument('file', nargs="?", metavar='FILE',
		type=argparse.FileType('r'), default=sys.stdin, 
		help='File to read. If empty, STDIN is used.')

	args = parser.parse_args()

	if args.address == None:
		address = "0.0.0.0"
	else:
		address = args.address

	if args.port == None:
		port = 5005
	else:
		port = args.port

	if args.interval == None:
		interval = 5
	else:
		interval = args.interval

	# Close if stdin is empty
	if args.file.isatty():
		print "Must provide data!"
		exit(2)

	chant(args.file.read(), address, port, interval)