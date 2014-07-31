#!/usr/bin/python
#coding: utf-8

import re

# Parse .srt file and return a list of (start_time, end_time, subtitle_content)

def parse(filePath):
    f = open(filePath, 'rU')
    string = f.read()

    srtList = []

    RE_ITEM = re.compile(r'(?P<start>\d+:\d+:\d+,\d+) --> '
                         r'(?P<end>\d+:\d+:\d+,\d+)\n'
                         r'(?P<subs>.*?)(\n\n|$)', re.DOTALL)
    for x in RE_ITEM.finditer(string):
        srtList.append((x.group('start'), x.group('end'), x.group('subs').replace("\n", " ")))

    return srtList
