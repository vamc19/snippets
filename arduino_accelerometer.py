#!/usr/bin/python

# Upload accelerometer sketch from examples before using this program.

import serial

interface = serial.Serial('/dev/ttyUSB0', 9600)

xDef = 350
yDef = 350
zDef = 350

while True:
    n = interface.readline()
    [x, y, z] = n.split()
    if int(x) < 330:
        print "Banking Left"
    if int(x) > 370:
        print "Banking Right"
    if int(y) > 370:
        print "Nose Diving"
    if int(y) < 330:
        print "Gaining Altitude"