# -*- coding: latin-1 -*-
from __future__ import print_function
import sys, os
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=120))
os.system('clear')
global desu
desu = []
color = {
    'white':    "\033[1;37m",
    'yellow':   "\033[1;33m",
    'green':    "\033[1;32m",
    'blue':     "\033[1;34m",
    'cyan':     "\033[1;36m",
    'red':      "\033[1;31m",
    'magenta':  "\033[1;35m",
    'black':      "\033[1;30m",
    'darkwhite':  "\033[0;37m",
    'darkyellow': "\033[0;33m",
    'darkgreen':  "\033[0;32m",
    'darkblue':   "\033[0;34m",
    'darkcyan':   "\033[0;36m",
    'darkred':    "\033[0;31m",
    'darkmagenta':"\033[0;35m",
    'darkblack':  "\033[0;30m",
    'off':        "\033[0;0m"
}
global wait
wait = 0
os.system('clear')
print(color['yellow'] + """
 _________________________________________LOADING GAME__________________________________________
|												|""" + color['off'], end = '\r')
while len(desu) < 289:
	wait += 1
	if wait >= 6000:
		desu.extend('◼')
		wait = 0
	print(color['cyan'] + ''.join(desu), end = '\r' + color['off'])
print('\n')
import kazooquest
