#from graphics import *
import socket
s = socket.socket()
ip = input('IP> ')
port = 9090
s.bind((ip, port))
s.listen((5))
while True:
    x, addr = s.accept()
    rec = s.recv(4096)
    s.send(rec)


    #w = GraphWin('inventory', 2000, 1000)
    #words = Text(Point(w.getWidth()/2, 20), '%s' % messgae)
    #inv.draw(w)
    #w.getMouse()
    #w.close()
