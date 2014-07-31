#!/usr/bin/python

import sys

fl = open('/dev/input/event7', 'r')
msg = []

while 1:
    for char in fl.read(1):
        msg += [ord(char)]
        if len(msg) == 8:
            print msg
            msg = []