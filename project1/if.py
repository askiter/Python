#!/usr/bin/env python
# Filename: if.py
#encoding=utf-8
__author__ = 'MrLiu'

number = 23
guess = int(raw_input('Enter an integer: '))

if guess == number:
    print 'Congratulations, you guess it.' #New block starts here
    print "(but you do not win any prizes!)" #New block ends here
elif guess < number:
    print 'No, it is a little higher than that' #Another block
    #You can do whatever you want in a block ...
else:
    print 'No, it is a little lower than that'
    #you must have guess > number to reach here

print 'Done'
#This last statement is always executed, after the if statement is executed

