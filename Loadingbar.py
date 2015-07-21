# -*- coding: latin-1 -*-
import sys, os, argparse
import Tkinter as tk
from ttk import *
import ttk
parser = argparse.ArgumentParser(description='Kazoo Quest')
args = parser.parse_args()
root = tk.Tk()
root.geometry('{}x{}'.format(1000, 100))
root.title("Kazoo Quest")
f1="black"
f2="SpringGreen3"
desu = ""
wait = 0
i1 = tk.StringVar()
i2 = tk.StringVar()
l1 = tk.Label(root, textvariable=i1, fg=f1)
l1.pack()
l2 = tk.Label(root, textvariable=i2, fg=f2)
l2.pack()
i1.set("________________________________________Loading game________________________________________")
while len(desu) < 205:
    wait += 1
    if wait >= 90000:
        wait = 0
        desu += '|'
    i2.set(desu)
tk.mainloop()
