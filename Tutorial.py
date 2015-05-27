#This was annoying and I know it looks bad but it works, nvm it works but can't be properly implemented yet
import os, sys, os.path
os.system('clear')
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
    'darkmagenta': "\033[0;35m",
    'darkblack':  "\033[0;30m",
    'off':        "\033[0;0m"
}
stop = 0
inventory = []
y = 0
triggers = []
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=120))
take_words = ['take', 'grab', 'pick', 'get', 'aquire']
use_words = ['use', 'throw', 'toss', 'drop', 'eat', 'kick', 'drink', 'puree', 'skip', 'travel']
n_words = ['n', 'north']
while stop != 1:
	if "started" not in triggers:
		print color['cyan'] + "Hello! Welcome to Kazoo Quest! This tutorial will run you through the mechanics of the game. You should note that this entire game is text-based and still in development - so be sure to not have too high of expectations. You can type \"skip\" at any point to skip this tutorial." + color['off']
		print color['darkblue'] + "Here's how this is going to work: you will be shown examples of what to expect in the game and how you should react. All of these examples will look (mostly) as they would in the game. All of the tips from this tutorial will appear in " + color['darkwhite'] + "this grey-ish text" + color['darkblue'] + ". Okay! Let's get started - type anything and press enter to continue." + color['off']
		act = raw_input('> ')
		os.system('clear')
	if act == "skip":
		os.system('touch game_save.dat')
		print "Run \"python kazooquest.py\" to continue."
		quit()
	else:
		if "thing" not in triggers:
			print color['darkblue'] + "Alright! First we're going to go over basic movement. You need to go North, so try typing something like \"go north\" (The \"go\" isn't needed)" + color['off']
		triggers.append("started")
		act = raw_input('> ')
		words = act.split(" ")
		if list(set(n_words) & set(words)):
			y += 1
		if list(set(take_words) & set(words)):
			if y == 1 and "rock" not in inventory:
				inventory.append("rock")
		if y == 1 and "room" not in triggers:
			print color['darkblue'] + "Good job! Now let's try picking up that rock. Try typing something like \"take rock\"!" + color['off']
			triggers.append("room")
			triggers.append("thing")
		elif y == 1 and "room" in triggers and "rock" not in inventory:
			print color['darkblue'] + "Try picking up that rock. Try typing something like \"take rock\"!" + color['off']
		elif y == 1 and "rock" in inventory:
			print color['darkblue'] + "Good job! Now try to use the rock - I bet you can figure out what to type." + color['off']
			if list(set(use_words) & set(words)):
				if "rock" in inventory:
					print color['darkblue'] + "Nice! Okay, now we're going to talk about combat. Enter anything to continue." + color['off']
					y = 3
		elif y == 3 and "fight" not in triggers:
			os.system('clear')
			print color['darkblue'] + "Here's what you'll see when you fight an enemy in the game: " + color['off']
			print color['red'] + "A bat suddenly appears!." + color['off']
			print color['blue'] + "What do you want to do?" + color['yellow'] + "\n1: Attack" + color['green'] + "\tHealth: 10" + color['red'] + "\tEnemy Health: 5"+ color['yellow'] + "\n2: Magic" + color['green'] + "\tMana: 5" + color['red'] + "\t\tEnemy Damage: 1 to 3" + color['yellow'] + "\n3: Dodge\n4: Enemy Info\n5: Run Away\n" + color['off']
			print color ['darkblue'] + "\nMost of these are pretty obvious in what they do, so I won't bother explaining it other than that it is turn-based." + color['off']
			triggers.append("fight")
			y = 5
		elif y == 5 and "bosses" not in triggers:
			os.system('clear')
			print color['darkblue'] + "Bosses have the same combat system as normal enemies, expect they are much tougher. In order to fight a boss, you must first find the area to summon the boss at. Next you need a certain item to summon it. All bosses will drop an item that is used to \"evolve\" and continue game progress." + color['off']
			y = 7
			triggers.append("bosses")
		elif y == 7 and "areas" not in triggers:
			print color['darkblue'] + "When you evolve, you can progress to a new area of the game. To do this you have to use the portal provided after killing the boss. There are different areas that each have different enemies than others. YOU CANNOT RETURN TO AN AREA ONCE YOU HAVE LEFT IT WITHOUT AN CERTAIN ITEM." + color['off']
			y = 9
			triggers.append("areas")
		elif y == 9 and "death" not in triggers:
			os.system('clear')
			print color['darkblue'] + "Now to the final point of this tutorial - dying. This is pretty simple - when your health reaches \"0\" you will lose. Here's an example of a game over screen in the game: " + color['off']
			print color['darkred'] + "You have died!" + color['off']
			print color['blue'] + "Do you want to see your final stats?" + color['off']
			print "(y/n) y"
			print color['darkmagenta'] + "You killed these enemies: " + color['off']
			print "{\'Bat\': 1, \'Wolf\': 2}"
			print "These are your final stats: "
			print color['darkgreen'] + "Damage: 5\nHealth: 10\nDefense: 3\nMana: 5\nLevel:1" + color['off']
			print color['darkgreen'] + "\nYour final score was 50" + color['off']
			print color['darkblue'] + "\nThat's it! I hope you enjoy Kazoo Quest! Press enter to continue to the game." + color['off']
			triggers.append("death")
			y = 100
		elif y == 100:
			os.system('touch game_save.dat')
			print "Run \"python kazooquest.py\" to continue."
			quit()
		else:
			if list(set(n_words) & set(words)):
				y -= 1
