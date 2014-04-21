#!/usr/bin/env python
# Filename: pickling.py
#encoding=utf-8
__author__ = 'MrLiu'

import cPickle as p

listfile = 'edge.status'

list = ['223.203.212.15|61.54.29.45','223.203.212.15|61.54.29.44']

f = file(listfile, 'w')
p.dump(list, f)
f.close()

f = file(listfile)
storedlist = p.load(f)

print storedlist