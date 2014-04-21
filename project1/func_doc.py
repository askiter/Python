#!/usr/bin/env python
# Filename: func_doc.py
#encoding=utf-8
__author__ = 'MrLiu'

def printMax(x, y):
    '''Prints the maxmium of two numbers.

    The two values must be integers.'''
    x = int(x) # convert to integer, if possible
    y = int(y)

    if x > y:
        print x, 'is maxmium'
    else:
        print y, 'is maxmium'

printMax(3, 6)
print printMax.__doc__
help(printMax)