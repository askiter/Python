#!/usr/bin/env python
# Filename: func_key.py
#encoding=utf-8
__author__ = 'MrLiu'

def func(a, b = 5, c = 10):
    print 'a is', a, 'and b is', b, 'and c is', c

func(3, 7)
func(25, c = 100)
func(c = 50, a = 99)
