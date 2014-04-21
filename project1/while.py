#!/usr/bin/env python
# Filename: while.py
#encoding=utf-8
__author__ = 'MrLiu'

number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer: '))

    if guess == number:
        print 'Congratulations, you guessed it.'
        running = False #this cause the while loop to stop
    elif guess < number:
        print 'No, it is a little higher than that'
    else:
        print 'No, it is a little lower than that'
else:
    print 'The while loop is over.'
    # Do anything else you want to do here

print 'Done'
