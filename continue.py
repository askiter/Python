#!/usr/bin/env python
# Filename: continue.py
#encoding=utf-8
__author__ = 'MrLiu'

while True:
    s = raw_input('Enter something: ')
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    print 'Input is of sufficient length'
    # Do other kinds of processing here...
