#A fun, dumb adventure remake in Python 2.7
#Written by Matthew Knecht
#NOTE: THIS IS NOT THE ACTUAL GAME, THIS IS ONLY THE ORIGINAL FAILURE
import random
print "NOTE: THIS IS NOT THE ACTUAL GAME, THIS IS ONLY MY ORIGINAL CODE THAT DIDN'T WORK.  THE REAL GAME IS CALLED \"Kazoo Quest\" AND IS AVAILABLE THROUGH GITHUB
global stop
global start
stop = 0
start = 0
p = '> '
global x
global y
x = 0
y = 0
global roominfo
roominfo = ''
def objectives():
	global torch_true
	torch_true = 0
	global rock_true
	rock_true = 0
global do
global help
global look
global inventory
global use
global take
global move
global back
#Map info for ease of access while debugging:
#Variable 'x' is west/east(ex. -1 would be to the west and +1 would be to the east)
#Variable 'y' is south/north(ex. -1 would be to the south and +1 would be to the north)
global n
global s
global e
global w
global wait
if x == 0 and y == 0:
	roominfo = "You have found yourself in a dimly lit cave.  You have no memory of how you got here or who you are.  You see some items on the ground."
	print roominfo
elif x == 0 and y == 1:
	roominfo = "You start walking to the north yet find that the mysterious light is dimming rapidly.  You decide to turn back until you find a light source."
	print roominfo
elif x == 0 and y == 2:
	print "test"
elif x == 1 and y == 0:
	roominfo = "stuff"
	print roominfo
stop = 1
do = ''
stop = 0
while stop != 1:
	do = raw_input(p)
	if do == 'help':
		print "-help \n -look \n -wait \n -inventory \n -use \n -take \n -move(n,s,e,w) \n -back \n -info"
	elif do == 'info':
		print "This game was written by Matthew Knecht in Python 2.7.  It is currently in V0.0.4.  The story of the game revolves around a player who has lost his memory and has to find his way back to his ?????.  The game is currently not very functional and doesn't have much content- but that will be resolved shortly.  Thanks for playing!"
	elif do == 'quit':
		quit()
	elif do == 'numdebug':
		print x
		print y
	elif do == 'look':
		print roominfo
	elif do == 'n' or 'north':
		y += 1
		print roominfo
	elif do == 's' or 'south':
		y -= 1
		print roominfo
	elif do == 'e' or 'east':
		do = ''
		x += 1
		print roominfo
	elif do == 'w' or 'west':
		do = ''
		x -= 1
		print roominfo
	else:
		print "You can't do that!"
def items():
	global worn_sword
	global lantern
	global rock
print "Welcome to Quest!"
