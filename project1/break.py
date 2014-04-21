#!/usr/bin/env python
# Filename: break.py
#encoding=utf-8
__author__ = 'MrLiu'

while True:
    s = raw_input('Enter something: ')
    if s == 'quit':
        break
    print 'Length of the string is', len(s)
print 'Done'
