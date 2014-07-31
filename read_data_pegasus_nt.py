#!/usr/bin/python

# Snippet to read data from a Pegasus Digital Pen.

import sys
import os
import StringIO

fd = os.open("/dev/hidraw0", os.O_RDONLY)
block = StringIO.StringIO()

while True:
	input = os.read(fd, 8)
	#print "Length of input block:", len(input)

	if input == "":
		#EOF
		print "End Of File"

	if ord(input[0]) & 128:
		#End block.
		#Pen Up event.
		# NOt every event is pen up.
		#
		print "Pen Up!"
		print [ord(a) for a in input]

	else:
		block.write(input)
	#print block

