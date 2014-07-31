#!/usr/bin/python

# Usage visualize_moodbar.py <path to music file>

import cv, os
import sys
import subprocess

# Generate Mood file.
song_location = sys.argv[1]
mood_file = song_location[:-3]+'mood'
mood_process = subprocess.Popen(["moodbar", song_location, "-o", mood_file],
                                stdout=subprocess.PIPE)
mood_process.communicate()

# Visualize Mood file
img = cv.CreateImage((1000, 50), 8, 3)
moodFile = open(mood_file, 'rb')
(x1, y1) = (0, 0)
(x2, y2) = (0, 50)
while os.path.exists(song_location):
    data = moodFile.read(3)
    color = ((ord(data[2]), ord(data[1]), ord(data[0])))
    cv.Line(img, (x1, y1), (x2, y2), color, 1, 8, 0)
    x1 += 1
    x2 = x1
    if x1 == 1000:
        break

cv.ShowImage(song_location, img)
cv.WaitKey()
