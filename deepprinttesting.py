# -*- coding: latin-1 -*-
x = 0
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
    'dimyellow':  "\033[2:33m",
    'off':        "\033[0;0m"
}
for x in range(x, 10):
    x += 1
    i = '◼'
    print color['darkyellow'] + i,
test = raw_input('> ')
if test == \033[A:
    print "sjdnfsj"
