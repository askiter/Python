#!/usr/bin/env python
# Filename: func_local.py
#encoding=utf-8
__author__ = 'MrLiu'

def func(x):
    print 'x is ', x
    x = 2
    print 'Changed local x to', x

x = 50
func(x)
print 'x is still ', x
