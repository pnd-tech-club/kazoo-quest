# -*- coding: latin-1 -*-
import sys, os, argparse
from Tkinter import *
from ttk import *
from graphics import *
parser = argparse.ArgumentParser(description='Kazoo Quest!')
args = parser.parse_args()
strtpnt= 195
l = 0
w = GraphWin('Kazoo Quest', 1000, 200)
os.system('clear')
desu = ""
wait = 0
os.system('clear')
outline = Text(Point(500, 100), """
 _________________________________________LOADING GAME__________________________________________
|											|""")
outline.setTextColor('yellow3')
outline.draw(w)
while len(desu) < 123:
    wait += 1
    if wait >= 90000:
        wait = 0
        desu += '|'
        bar = Text(Point(strtpnt + 5, 115), "|")
        bar.setTextColor('green3')
        bar.draw(w)
        strtpnt += 5
w.close()
import kazooquest
