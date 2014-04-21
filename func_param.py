#!/usr/bin/env python
# Filename: func_param.py
#encoding=utf-8
__author__ = 'MrLiu'

def printMax(a, b):
    if a > b:
        print a, 'is maximum'
    else:
        print b, 'is maxium'

a = raw_input('Enter the 1st number: ')
b = raw_input('Enter the 2nd number: ')
printMax(a, b) # directly give literal values

