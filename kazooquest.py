#Credits:
#Written by Matthew Knecht
#Written in Python 2.7

#CHANGELOG
#Version 0.0.1: 
# -Basic ideas and laying out of variables
#Version 0.0.2:
# -Laying out rooms and plotline
#Version 0.0.3:
# -Bug fixing
# -Added additional commands
# -Added more rooms
#Version 0.0.4:
# -More bug fixing
#Version 0.0.5:
# -Added some more basic ideas
# -Added more commands
#Version 0.0.6:
# -Added basic (aka broken) layout for enemy encounters
# -Fixed some little bugs pertaining to walking through walls
#Version 0.0.7
# -Added more to encounter system- currently still very buggy
#Version 0.1.0 (Major Update!)
# -Added lots to the encounter system
# -Removed some code for a dodge mechanic due to it causing bugs (code can be found nearly unmodified, just commented out)
# -FIXED ALL KNOWN BUGS, EXPLOITS, AND ISSUES (yay)
#Version 0.1.1
# -Fixed/added in the "run away" mechanic during encounters
#Version 0.1.2 (aka "The Remembering")
# -Added a changelog
#Version 0.1.3
# -Added a semi-broken time system
#Version 0.1.4
# -Completely removed the time system until later notice
#Version 0.1.5
# -Changed the "take" command to allow things like "take torch"
# -Fixed some minor bugs
#Version 0.2.0 (Major update!)
# -Added TONS of rooms
# -Added base for armor code
# -Added slightly better encounter math
# -Added some other minor things
# -Fixed some bugs
#Version 0.2.1
# -Fixed dodging
# -Added more rooms
# -Added better formatting for some stuff
# -Removed junk
#Version 0.2.5 (Semi-major update)
# -Reworked inventory system to allow item removal
# -Changed some other minor things
# -Condensed some code
# -Threw out some junk
# -Laid out groundwork for better things and stuff
#Version 0.2.6
# -Added in "clear" command
# -Bug fixes
#Version 0.2.7
# -Added more rooms
#Version 0.3 (Major update! :^)
# -Added basic magic functionality
# -Implemented parrying into the dodge mechanic
# -Official game rename- from "Dumpster Quest" to "Kazoo Quest"
# -Added many rooms
# -Added new enemies
# -Testing re-implementation of time functionality
# -Balanced enemy/player health and damage
# -Made some other minor functionality changes
# -Set some groundwork for later ideas
# -Fixed some spelling mistakes (including a misspelling of "type" :P )
# -Attempted some layout of cool future features- including updating from command-line
#Version 0.3.1
# -Added loading bar that works
# -Moved the location of game files to a unique repo
# -Re-worked the dodging mechanic
# -Completely added the loading bar feature (First totally finished feature)
#Version 0.4 (Major update!)
# -Added LEVELS!!!!!!!! :D
# -Added rooms
# -Added more sotry
# -Reworked some features like healing
# -A few other minor changes
#Version 0.4.1
# -Major rework of level system due to it being incredibly OP
# -Reworked healing
# -Fixed being able to activate encounters while not in encounter zone using heal
# -Removed old time code due to it being a stupid idea in the first place
#Version 0.4.2
# -lol42
# -Fixed some typos that were causing issues
# -Condensed some stuff
#Version 0.5 (WUUTT, HOWSOSOON!?!??!?)
# -Added in a basic points system, it's been there for a while but I haven't bothered with it until now
# -Fixed so many little issues/typos
# -Reworked encounter system (unknown if it will work very well)
import os, random, time
import argparse
os.system('clear')
import Loadingbar
#A lot of code here was removed for a while in Version 0.3 (Reworked and implemented as loadingbar.py)
def update():
	ping_test = os.system('ping -q -c3 http://www.github.com >/dev/null')
	if ping_test == 0:
		pstatus = "Connection to Github available.  Downloading update."
		os.system('git pull')
		print "Done!"
	else:
		print "Connection failed.  Check your internet connection and try again."
#This code may be severely broken, I really don't have a clue at the time of writing it as I wrote it using online documentation and couldn't test it (yes, yes it is broken)
#parser = argparse.ArgumentParser(description='Kazoo Quest')
#parser.add_argument('--update', update = update())
#args = parser.parse_args()
global wait
wait = 0
print "Welcome to Kazoo Quest!  For help type \"help\"!"
current_version = "v0.4.2"
global weapon
weapon = 0
#Weapon list: 0 = hands, 1 = branch, 2 = dagger, 3 = dull sword, 4 = Blade Staff, 5 = sharp spear, 6 = polished axe, 7 = The Blade of Honking
global armor
armor = 0
#Armor list: 0 = Cloth shirt, 1 = Leather Breastplate, 2 = Chainmail Breastplate, 3 = Scale Breastplate, 4 = Crystal Breastplate, 5 = Cloak of Shadows, 6 = Shield of Honking, 7 = Kazoo shield of Death
global dodges
dodges = 0
global dodge_act
dodge_act = 1
global damage
damage = 3
global max_hp
max_hp = 20
global max_mana
max_mana = 5
global level
level = 0
global levels
levels = ""
global exp
exp = 0
global points
points = 0
#Note to add all needed triggers after here
global trapdoor_true
trapdoor_true = 0
triggers = []
global torch_true
torch_true = 0
global lights_true
lights_true = 0
global branch_true
branch_true = 0
global letter_true
letter_true = 0
global underground_door_true
underground_door_true = 0
#Add all needed triggers before here
global inventory
inventory = []
global stop
stop = 0
global letter
letter = """The letter reads as follows:
Dear [The name is smudged out]
	We have recently heard about your ideas with our company.  We would like to officially meet with you on the fourth [The rest of the paragraph is blacked out].
We would also appreciate if you could begin to proceed with your ideas(at least planning) until our meeting.

                                                                               Sincerely,
                                                                                    A.L.
[There appears to be a large chunk of the page torn out]
"""
global enemy_set
enemy_set = 0
#Time removed in v0.1.4 (Re-implementation being tested in v0.3)
global time
time = 0
global encounter_time
encounter_time = random.randint(0, 100)
global lamp_true
lamp_true = 0
global skip
skip = 0
global enemy_hp
enemy_hp = 1
global enemy_dam
enemy_dam = 0
global enemy_dodge
enemy_dodge = 0
global enemy_info
enemy_info = ""
global enemy_type
global fight_p
fight_p = enemy_info + "What do you want to do?\n1: Attack\n2: Magic\n3: Dodge\n4: Enemy Info\n5: Run Away"
global f_act
global hp
hp = 20
global defe
defe = 1
global mana
mana = 5
global exp_limit
exp_limit = 10
global kills
kills = []
global enemy_dam_info
global encounter
encounter = 0
global x
global y
global z
x = 0
y = 0
z = 0
print "You have found yourself in a dimly lit cave.  You have no memory of how you got here or who you are.  There is a path to the north and south You see a torch on the ground."
act = raw_input('> ')
words = act.split(" ")
stop = 0
while stop != 1:
#Map info for ease of access while debugging:
#Variable 'x' is west/east(ex. -1 would be to the west and +1 would be to the east)
#Variable 'y' is south/north(ex. -1 would be to the south and +1 would be to the north)
#Variable "z" is an inverted height (+1 would be down and -1 would be up)
	if act == "n":
		y += 1
	elif act == "s":
		y -= 1
	elif act == "e":
		x += 1
	elif act == "w":
		x -= 1
	elif act == "d":
		z += 1
	elif act == "u":
		z -= 1
#Debugging command
	if act == "num":
		print x
		print y
	if "use" in words:
		if "switch" in words and x == 3 and y == 7 and z == 0:
			lights_true = 1
			print "You flip the switch and the lights in the house suddenly turn on."
		elif "switch" in words and x == 3 and y == 7 and z == 0 and lights_true == 1:
			print "You wiggle the switch but nothing happens."
		elif "crowbar" in words and x == 3 and y == 12 and z == 1:
			print "You use the crowbar to open the door."
			triggers.append("doorw/crowbar")
		elif "crowbar" in words and x == 2 and y == 8 and z == 0:
			print "You use the crowbar to open the trapdoor."
			triggers.append("trapdooropen")
	if "take" in words:
		if "torch" in words and x == 0 and y == 0 and torch_true == 0:
			items = "torch"
			inventory.append(items)
			torch_true = 1
			print "You pick up the torch and are able to see better."
		elif "shuriken" in words and x == 0 and y == -1 and "shuriken" not in inventory:
			items = "shuriken"
			inventory.append(items) * 7
			print "You pick up seven shuriken."
		elif "branch" in words and x == 2 and y == 1 and branch_true == 0:
			items = "branch"
			inventory.append(items)
			branch_true = 1
			print "You pick up the branch and hold it like a spear."
		elif "letter" in words and x == 2 and y == 6 and letter_true == 0:
			items = "letter"
			inventory.append(items)
			letter_true = 1
			print "You take the letter out of the mailbox."
			print letter
		elif "dagger" in words and x == 3 and y == 7 and z == 1 and weapon < 2:
			items = "dagger"
			inventory.append(items)
			weapon = 2
			print "You wield the dagger and feel stronger."
			items = "branch"
			inventory.remove(items)
		elif "armor" in words and x == 3 and y == 7 and z == 1 and armor < 1:
			items = "leather armor"
			inventory.append(items)
			armor = 1
			print "You put on the leather armor."
		elif "lamp" in words and x == 3 and y == 7 and z == 1 and "lamp" not in inventory:
			items = "lamp"
			inventory.append(items)
			lamp_true = 1
			items = "torch"
			inventory.remove(items)
			print "Your torch happens to burn out as you pick up the lamp."
		elif "armor" in words and x == -1 and y == 15 and z == 1 and armor <= 1:
			items = "Chainmail armor"
			inventory.append(items)
			armor = 2
			print "You put on the chainmail armor."
			items = "leather armor"
			inventory.remove(items)
		elif "crowbar" in words and x == 9 and y == 9 and z == 1 and "crowbar" not in inventory:
			items = "crowbar"
			inventory.append(items)
			print "You pick up the crowbar."
		elif "key" in words and x == 2 and y == 8 and z == 0 and "key" not in inventory and "trapdooropen" in triggers:
			items = "key"
			inventory.append(items)
			print "You pick up a mysterious key."
		else:
			print "You don't see that here."
	if act == "clear":
		os.system('clear')
	if act == "inv":
		print '\n'.join(inventory)
	if act == "look":
		skip = 0
	elif act == "debug.update":
		update()
	elif act == "quit":
		print "Are you sure you want to quit? (yes/no)"
		quit_response = raw_input('> ')
		if quit_response == "yes":
			quit()
		else:
			skip = 0
#Debugging command
	elif act == "OP420":
		weapon = 7
		armor = 7
#Debugging command
	elif act == "etime":
		print encounter
	elif act == "heal":
		hp = hp + hp * random.randint(1, 2) /2
		encounter = random.randint(25, 75)
	elif act == "time":
		skip = 0
#Debugging command
	elif act == "rtime":
		print time
#Debugging command
	elif act == "tp":
		x = int(raw_input('> '))
		y = int(raw_input('> '))
		z = int(raw_input('> '))
		torch_true = 1
		lights_true = 1
	elif act == "info":
		print "Damage: %r\nHealth:%r\nDefense:%r\nMana:%r" % (damage, hp, defe, mana)
		
	elif act == "credits":
		print "This game was written by Matthew Knecht in Python 2.7.  It is currently in %r  The story of the game revolves around a player who has lost his memory and has to find his Golden Kazoo.  The game doesn't have much content- but that will be resolved shortly.  Thanks for playing!" % current_version
		
	if act == "help":
		print "-help \n -look \n -wait \n -use \n -take \n -move(n, s, e, w, u, d) \n -back \n -info"
		
	if x == 0 and y == 0 and torch_true == 0:
		encounter = 0
		roominfo = "You have found yourself in a dimly lit cave.  You have no memory of how you got here or who you are.  There is a path to the north and south.  You see a torch on the ground."
		print roominfo
	elif x == 0 and y == 0 and torch_true == 1:
		roominfo = "Your torch lights up the walls of the cave.  There is a path to the north and south."
		print roominfo
	elif x == 0 and y == 1 and torch_true == 0:
		roominfo = "You start walking to the north yet find that the mysterious light is dimming rapidly.  You decide to turn back until you find a light source."
		print roominfo
		y -= 1
	elif x == 0 and y == 1 and torch_true == 1:
		roominfo = "You begin to walk to the north, allowing your torch to light the way.  As you walk you begin to hear a slight howl of wind from ahead of you.  There is a path to the east."
		print roominfo
	elif x == 1 and y == 1:
		roominfo = "You walk to the east and begin to feel the breeze picking up.  You look ahead of you and see outside a little bit ahead."
		print roominfo
	elif x == 2 and y == 1 and branch_true == 0:
		encounter = 0
		roominfo = "You reach the end of the tunnel and feel the heat of the sun around you.  The trees tower over you and you hear the sound of rushing water to the north.  You see a good sized tree branch with a pointed end."
		print roominfo
	elif x == 2 and y == 1 and branch_true == 1:
		encounter = 0
		roominfo = "You reach the end of the tunnel and see a forest to the east.  You hear the sound of rushing water to the north."
		print roominfo
	elif x == 2 and y == 2:
		encounter = 1
		enemy_type = "wolf"
		roominfo = "There is a swiftly flowing stream here.  To the east is a path to the forest.  You think you see a small cottage far to the north."
		print roominfo
	elif x == 2 and y == 3:
		roominfo = "You keep walking around the side of the mountain.  There is a cottage far to the north and a cave to the south.  There is a forest to the east."
		enemy_type = "wolf"
		print roominfo
	elif x == 2 and y == 4:
		roominfo = "The mountain path seems to be rougher here.  You see that the stream flows from a grate in the mountain.  There is a forest to the east, a cave to the south, and a cottage to the north."
		enemy_type = "wolf"
		print roominfo
	elif x == 2 and y == 5:
		roominfo = "You are nearing the cottage.  There is a cave far to the south and a forest to the east."
		enemy_type = "wolf"
		print roominfo
	elif x == 2 and y == 6 and z == 0 and letter_true == 0:
		encounter = 1
		roominfo = "You stand in front of the mailbox of the cottage.  There appears to be a letter in the mailbox.  There is a cave far to the south and a forest to the east."
		print roominfo
	elif x == 2 and y == 6 and z == 0 and letter_true == 1:
		encounter = 1
		roominfo = "You stand in front of the mailbox of the cottage.  There is a cave far to the south and a forest to the east."
		enemy_type = "wolf"
		print roominfo
	elif x == 2 and y == 7 and lights_true == 0:
		encounter = 0
		roominfo = "The inside of the house is cold and dark.  You have an unexplainable feeling of gloom.  There are rooms to the east and the north."
		print roominfo
	elif x == 2 and y == 7 and lights_true == 1:
		encounter = 0
		roominfo = "There is a bright red stain on the rug in front of the door.  You have an unexplainable feeling of dread.  The kitchen is to the east and the living room is to the north."
		print roominfo
	elif x == 3 and y == 7 and z == 0 and lights_true == 0:
		roominfo = "The room is lit up slightly by a window.  You can see a switch by the window.  The doorway is to the west."
		print roominfo
	elif x == 2 and y == 8 and lights_true == 0:
		roominfo = "It's way too dark in here for you to see anything.  The doorway is to the south."
		print roominfo
	elif x == 2 and y == 8 and lights_true == 1 and trapdoor_true == 0:
		roominfo = "The living room is completely barren.  There appears to be a locked trapdoor in the floor.  The doorway is to the south."
		print roominfo
	elif x == 2 and y == 8 and lights_true == 1 and trapdoor_true == 1 and "key" not in inventory:
		roominfo = "The trapdoor in this room has a key inside.  The doorway is to the south."
		print roominfo
	elif x == 2 and y == 8 and lights_true == 1 and trapdoor_true == 1 and "key" in inventory:
		roominfo = "The trapdoor in the center of the room is empty.  The doorway is to the south."
		print roominfo
#Variable "z" is an inverted height (+1 would be down and -1 would be up)
	elif x == 3 and y == 7 and z == 1 and lights_true == 0:
		roominfo = "Your torch isn't enough to let you see down the stairs."
		print roominfo
		z += 1
	elif x == 3 and y == 7 and z == 0 and lights_true == 1:
		roominfo = "The light shows that there are stairs going down.  The entrance is to the west."
		print roominfo
#I know there is someway to make this more efficient, but oh well I don't have time for thinking right now :^ )
	elif x == 3 and y == 7 and z == 1 and lights_true == 1 and "lamp" not in inventory and weapon < 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north.  There is a lamp on the ground.  There is a dagger on the ground.  There is leather armor on the ground."
		print roominfo
#Player has nothing
	elif x == 3 and y == 7 and z == 1 and "lamp" in inventory and armor < 1 and "dagger" not in inventory:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north.  There is a dagger on the ground.  There is leather armor on the ground."
		print roominfo
#Player has lamp ^
	elif x == 3 and y == 7 and z == 1 and "lamp" in inventory and armor >= 1 and "dagger" not in inventory:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north.  There is a dagger on the ground."
		print roominfo
#Player has lamp and armor ^
	elif x == 3 and y == 7 and z == 1 and "lamp" in inventory and armor < 1 and "dagger" in inventory:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north.  There is leather armor on the ground."
		print roominfo
#Player has lamp and dagger ^
	elif x == 3 and y == 7 and z == 1 and "lamp" in inventory and armor >= 1 and "dagger" in inventory:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north."
		print roominfo
#Player has all items ^
	elif x == 3 and y == 7 and z == 1 and "lamp" not in inventory and armor >= 1 and "dagger" in inventory:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north.  There is a lamp on the ground.  There is a dagger on the ground."
		print roominfo
#Player has leather armor ^
	elif x == 3 and y == 7 and z == 1 and "dagger" in inventory and "lamp" not in inventory and armor >= 1:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north.  There is a lamp on the ground."
		print roominfo
#Player has dagger and armor ^
	elif x == 3 and y == 7 and z == 1 and "dagger" in inventory and "lamp" not in inventory and armor != 1:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north.  There is a lamp on the ground.  There is leather armor on the ground."
		print roominfo
#Player has dagger ^
	elif x == 3 and y == 8 and z == 1:
		encounter = 0
		enemy_type = "orc"
		roominfo = "As you walk, an ominous presence overwhelms you."
		print roominfo
	elif x == 3 and y == 9 and z == 1:
		encounter = 1
		enemy_type = "orc"
		print "There are paths to the north, east, and west."
	elif x == 2 and y == 9 and z == 1:
		roominfo = "You hear dripping water in the distance.  There is a path to the west"
		print roominfo
		triggers.append("westpath")
	elif x == 2 and y == 9 and z == 1:
		roominfo = "You hear dripping water in the distance.  There is a path to the west."
		print roominfo
	elif x == 1 and y == 9 and z == 1:
		roominfo = "The strange dripping sound seems a short distance away.  There is a path to the north and east."
		print roominfo
	elif x == 1 and y == 10 and z == 1:
		roominfo = "The dripping sound appears to be just around the corner up ahead.  You hear a deep moaning sound.  There is a path to the west and south."
		print roominfo
	elif x == 0 and y == 10 and z == 1:
		roominfo = "The dripping sound is very audible now and the moaning sound seems to be rapidly increasing in volume.  There are paths to the west and east."
		print roominfo
	elif x == -1 and y == 10 and z == 1:
		enemy_type = "wraith"
		roominfo = "You notice a rapidly dripping spot on the ceiling.  You can hear the moaning sound ahead.  There is a path to the east and north."
		print roominfo
	elif x == -1 and y == 11 and z == 1:
		roominfo = "As you look north, you can't see the end of the passage.  There is a path to the south and north."
		print roominfo
	elif x == -1 and y == 12 and z == 1:
		roominfo = "Something seems off around you..."
		print roominfo
	elif x == -1 and y == 13 and z == 1:
		roominfo = "You think you can see a light to the north."
		print roominfo
	elif x == -1 and y == 14 and z == 1:
		roominfo = "The light to the north grows in brightness."
		print roominfo
	elif x == -1 and y == 15 and z == 1 and armor <= 1:
		roominfo = "You almost trip on the chainmail armor that lays on the ground."
		print roominfo
	elif x == -1 and y == 15 and z == 1 and armor >= 2:
		roominfo = "The silence here is intense.  The light ahead seems to be getting brighter."
		print roominfo
	elif x == -1 and y == 16 and z == 1:
		roominfo = "The light to the north appears to be a wall of solid light."
		print roominfo
	elif x == -1 and y == 17 and z == 1:
		roominfo = "You feel yourself being whisped away to somewhere else."
		print roominfo
		x = 3
		y = 9
		z = 1
#East path split
	elif x == 4 and y == 9 and z == 1:
		roominfo = "There is a slight clanking noise in the distance.  There is a path that stretches far ahead of you."
		print roominfo
		triggers.append("eastpath")
	elif x == 5 and y == 9 and z == 1:
		enemy_type = "dwarf"
		roominfo = "You sense something small nearby."
		print roominfo
	elif x == 6 and y == 9 and z == 1:
		roominfo = "You smell something foreign to you... Then again you don't really remember anything..."
		print roominfo
	elif x == 7 and y == 9 and z == 1:
		roominfo = "This passage seems absurdly long..."
		print roominfo
	elif x == 8 and y == 9 and z == 1:
		roominfo = "There seems to be something far ahead of you in."
		print roominfo
	elif x == 9 and y == 9 and z == 1 and "crowbar" not in inventory:
		roominfo = "There appears to be a crowbar on the ground."
		print roominfo
	elif x == 9 and y == 9 and z == 1 and "crowbar" in inventory:
		roominfo = "The passageway a bit ahead appears to be very bright."
		print roominfo
	elif x == 10 and y == 9 and z == 1:
		roominfo = "The wall in front of you seems to be made of solid light..."
		print roominfo
	elif x == 11 and y == 8 and z == 1:
		roominfo = "You feel yourself being taken somewhere else..."
		print roominfo
		x == 3
		y == 9
		z == 1
#North path split
	elif x == 3 and y == 10 and z == 1:
		roominfo = "All you see to the north is darkness."
		print roominfo
	elif x == 3 and y == 11 and z == 1:
		roominfo = "..."
		print roominfo
	elif x == 3 and y == 12 and z == 1 and underground_door_true == 0:
		roominfo = "There is suddenly a door in front of you.  You can't open it with your hands."
		print roominfo
	elif x == 3 and y == 12 and z == 1 and underground_door_true == 1:
		roominfo = "The door is open."
		print roominfo
	elif x == 3 and y == 13 and z == 1 and underground_door_true == 0:
		y -= 1
	elif x == 3 and y == 13 and z == 1 and underground_door_true == 1:
		roominfo = "The path to the north continues for a while."
		print roominfo
	elif x == 3 and y == 14 and z == 1:
		roominfo = ""
#This is used to undo movement into an unexisting room V
	else:
		if act == "n":
			y -= 1
		elif act == "s":
			y += 1
		elif act == "w":
			x += 1
		elif act == "e":
			x -= 1
		elif act == "d":
			z -= 1
		elif act == "u":
			z += 1
	if encounter != 0:
		encounter_time = random.randint(0,0)
	if weapon == 0:
		damage = 3
	elif weapon == 1:
		damage = 5
		points += 1
	elif weapon == 2:
		damage = 8
		points += 3
	elif weapon == 3:
		damage = 10
		points += 5
	elif weapon == 4:
		damage = 15
		points += 10
	elif weapon == 5:
		damage = 20
		points += 20
	elif weapon == 6:
		damage = 30
		points += 25
#This weapon is going to be available for debugging through the input of "OP420"
	elif weapon == 7:
		damage = 1337
	if armor == 0:
		defe = 1
		max_hp = 20
		mana = 5
	elif armor == 1:
		defe = 5
		max_hp = 25
		mana = 10
		points += 2
	elif armor == 2:
		defe = 9
		max_hp = 30
		mana = 15
		points += 4
	elif armor == 3:
		defe = 15
		max_hp = 40
		mana = 20
		points += 5
	elif armor == 4:
		defe = 23
		max_hp = 50
		mana = 30
		points += 10
	elif armor == 5:
		defe = 30
		max_hp = 60
		mana = 40
		points += 15
	elif armor == 6:
		defe = 45
		max_hp = 75
		mana = 50
		points += 20
	elif armor == 7:
		defe = 420
		max_hp = 9001
		mana = 6.9e+42
	if exp >= exp_limit:
		print "Level up!"
		exp = 0
		if level == 1:
			exp_limit = 25
		elif level == 2:
			exp_limit = 35
		elif level == 3:
			exp_limit = 50
		elif level == 4:
			exp_limit = 65
		elif level == 5:
			exp_limit = 80
		elif level == 6:
			exp_limit = 100
		elif level == 7:
			exp_limit = 125
		elif level == 8:
			exp_limit = 150
		elif level == 9:
			exp_limit = 175
		elif level == 10:
			exp_limit = 200
		levels += "!"
		points += 10
	if len(levels) == 1:
		damage += 2
		max_hp += 5
		max_mana += 2
	elif len(levels) == 2:
		damage += 3
		max_hp += 5
		max_mana += 3
	elif len(levels) == 3:
		damage += 3
		max_hp += 8
		max_mana += 5
	elif len(levels) == 4:
		damage += 5
		max_hp += 10
		max_mana += 5
	elif len(levels) == 5:
		damage += 8
		max_hp += 10
		max_mana += 7
	elif len(levels) == 6:
		damage += 10
		max_hp += 10
		max_mana += 8
	elif len(levels) == 7:
		damage += 10
		max_hp += 15
		max_mana += 9
	elif len(levels) == 8:
		damage += 10
		max_hp += 15
		max_mana += 10
	elif len(levels) >= 9:
		damage += 5
		max_hp += 5
		max_mana += 5
#For some reason this code seems to be giving everything strange effects (removed in v0.1.4) (Re-implementation testing beginning in v0.3- testing produced no good results) (Code completely removed in v0.4.1)
	stop = 1
	act = ""
	act = raw_input('> ')
	words = act.split(" ")
	stop = 0
	while encounter_time >= 40 and encounter_time <= 55 and encounter != 0:
		stop = 1
		while enemy_set != 1:
			if enemy_type == "wolf":
				enemy_hp = 15
				enemy_dam = random.randint(1, 3)
				enemy_dam_info = "1 to 3"
				enemy_dodge = 0
			elif enemy_type == "orc":
				enemy_hp = 25
				enemy_dam = random.randint(5, 7)
				enemy_dam_info = "5 to 7"
				enemy_dodge = 1
			elif enemy_type == "wraith":
				enemy_hp = 30
				enemy_dam = random.randint(6, 8)
				enemy_dam_info = "6 to 8"
				enemy_dodge = 3
			elif enemy_type == "dwarf":
				enemy_hp = 35
				enemy_dam = random.randint(6, 9)
				enemy_dam_info = "6 to 9"
				enemy_dodge = 1
			elif enemy_type == "spirit":
				enemy_hp = 40
				enemy_dam = random.randint(7, 10)
				enemy_dam_info = "7 to 10"
				enemy_dodge = 0
			elif enemy_type == "slime":
				enemy_hp = 75
				enemy_dam = random.randint(5, 8)
				enemy_dam_info = "5 to 8"
				enemy_dodge = 0
#Remember to fix this silly grammar thingy here
			enemy_info = "A "+enemy_type+" suddenly appears!."
			print enemy_info
			enemy_set = 1
		fight_act = raw_input(fight_p + "\n")
		dodges = 0
		if fight_act == "1":
			enemy_hp = enemy_hp - damage
			print "You dealt %d damage to the %s!" % (damage, enemy_type)
		elif fight_act == "2":
			print inventory
		elif fight_act == "3":
			dodge_act = random.randint(0, 100)
			if dodge_act <= 25:
				print "You dodged the attack!"
				dodges = 1
			if dodge_act >= 75:
				parrypowa = damage * 2
				enemy_hp -= parrypowa
				print "You parried the attack and dealt %d damage!" % parrypowa
				dodges = 1
		elif fight_act == "4":
			print "Enemy Health: %d\nEnemy Damage: %s" % (enemy_hp, enemy_dam_info)
		elif fight_act == "5":
			run_success = random.randint(0, 3)
			if run_success == 1:
				encounter_time = random.randint(0, 100)
				enemy_hp = 0
				dodges = 0
				print "You ran away!"
		else:
			print "You can't do that!"
		if enemy_hp > 0 and dodges == 0 and fight_act != "4":
			hp = hp - enemy_dam + defe
			dodges = 0
			print "The "+enemy_type+" dealt %r damage to you!" % enemy_dam
			if enemy_type == "wolf":
				enemy_dam = random.randint(1, 3)
			elif enemy_type == "orc":
				enemy_dam = random.randint(4, 6)
			elif enemy_type == "wraith":
				enemy_dam = random.randint(5, 8)
			elif enemy_type == "dwarf":
				enemy_dam = random.randint(6, 9)
			elif enemy_type == "spirit":
				enemy_dam = random.randint(7, 10)
			elif enemy_type == "slime":
				enemy_dam = random.randint(5, 8)
		if enemy_hp <= 0 and fight_act != "5":
			enemy_set = 0
			print "You killed the " + enemy_type +"!"
			kills.append(enemy_type)
			encounter_time = random.randint(0, 100)
			if enemy_type == "wolf":
				exp += 2
				points += 2
			elif enemy_type == "orc":
				exp += 3
				points += 3
			elif enemy_type == "wraith":
				exp += 4
				points += 4
			elif enemy_type == "dwarf":
				exp += 6
				points += 6
			elif enemy_type == "spirit":
				exp += 8
				points += 8
			elif enemy_type == "goo":
				exp += 10
				points += 10
		if hp <= 0:
			print "You have died!"
			print "Do you want to see your final stats?"
			dead_p = raw_input('y/n ')
			if dead_p == "y":
				print "You killed these enemies:"
				print ', '.join(kills) + '\n'
				print "These are your final stats:"
				print "Damage: %r\nHealth:%r\nDefense:%r\nMana:%r\nLevel:%r" % (damage, hp, defe, mana, level)
				print "\nYour final score was %r" % points
				quit()
			elif dead_p == "n":
				quit()
		stop = 0
	if hp > max_hp:
		hp = max_hp
	if mana > max_mana:
		mana = max_mana
