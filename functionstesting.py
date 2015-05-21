from graphics import *
w = GraphWin(500, 1000)
def prompt():
	acte = Entry(Point(w.getWidth()/6, 100), 15)
	acte.setText("")
	acte.draw(w)
	boop = Rectangle(Point(w.getWidth()/4, 10), Point(w.getWidth()/3.5, 15))
	boop.draw(w)
	w.getMouse()
	i = acte.getText()
	return i
	words = i.split(" ")
	return words
x = prompt()
if x != "":
    print "gah"
    if x == "kek":
        print "yeah"
