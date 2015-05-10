#Credits:
#Written by Matthew Knecht
#Written in Python 2.7
#Storyline help by Ethan Copeland

#CHANGELOG
#Version 0.0.1: -Basic ideas and laying out of variables
#Version 0.0.2: -Laying out rooms and plotline
#Version 0.0.3: -Bug fixing, added additional commands, added more rooms
#Version 0.0.4: -More bug fixing
#Version 0.0.5: -Added some more basic ideas, added more commands
#Version 0.0.6: -Added basic (aka broken) layout for enemy encounters, fixed some little bugs pertaining to walking through walls
#Version 0.0.7: -Added more to encounter system- currently still very buggy

#Version 0.1.0 (Major Update!): -Added lots to the encounter system, removed some code for a dodge mechanic due to it causing bugs (code can be found nearly unmodified, just commented out), FIXED ALL KNOWN BUGS, EXPLOITS, AND ISSUES (yay)
#Version 0.1.1: -Fixed/added in the "run away" mechanic during encounters
#Version 0.1.2 (aka "The Remembering"): -Added a changelog
#Version 0.1.3: -Added a semi-broken time system
#Version 0.1.4: -Completely removed the time system until later notice
#Version 0.1.5: -Changed the "take" command to allow things like "take torch", fixed some minor bugs

#Version 0.2.0 (Major update!): -Added TONS of rooms, added base for armor code, added slightly better encounter math, added some other minor things, fixed some bugs
#Version 0.2.1: -Fixed dodging, added more rooms, added better formatting for some stuff, removed junk
#Version 0.2.5 (Semi-major update): -Reworked inventory system to allow item removal, changed some other minor things, condensed some code, threw out some junk, laid out groundwork for better things and stuff
#Version 0.2.6: -Added in "clear" command, bug fixes
#Version 0.2.7: -Added more rooms

#Version 0.3 (Major update!): -Added basic magic functionality, implemented parrying into the dodge mechanic, official game rename- from "Dumpster Quest" to "Kazoo Quest", added many rooms, added new enemies, testing re-implementation of time functionality, balanced enemy/player health and damage, made some other minor functionality changes, set some groundwork for later ideas, fixed some spelling mistakes (including a misspelling of "type" :P ), attempted some layout of cool future features- including updating from command-line
#Version 0.3.1: -Added loading bar that works, moved the location of game files to a unique repo, re-worked the dodging mechanic, completely added the loading bar feature (First totally finished feature)

#Version 0.4 (Major update!): -Added LEVELS!!!!!!!! :D, added rooms, added more story, reworked some features like healing, a few other minor changes
#Version 0.4.1: -Major rework of level system due to it being incredibly OP, reworked healing, fixed being able to activate encounters while not in encounter zone using heal, removed old time code due to it being a stupid idea in the first place
#Version 0.4.2: -Fixed some typos that were causing issues, condensed some stuff

#Version 0.5 (WUUTT, HOWSOSOON!?!??!?): -Added in a basic points system, it's been there for a while but I haven't bothered with it until now, fixed so many little issues/typos, reworked encounter system (unknown if it will work very well)
#Version 0.5.1: -Fixed encounter system that was causing massive issues and crashing

#Version 0.6 (Major update): -Added magicz, added basic saving, fixed some bugs, fixed some typos, loading is WIP as hell
#Version 0.6.1: -Broke loading more
#Version 0.6.5 (Semi-major update): -Fixed loading to make it work, condensed some code, reworked the trigger system, game may be slightly faster now
#Version 0.6.6: -Fixed a handful of bugs that restricted some items/rooms
#Version 0.6.7: -Added in some more spells, you just can't get them legitimately yet, removed some useless comments, minor fixes with magic/fight mechanics

#Version 0.7 (Major update!): -Added kinda classes, added some other things, documentation...? I guess...?

#Version 0.8 (Major update!): -Added colors!?!?!?, added fancier things in general
#Version 0.8.1: -Added in autoloading, reworked the changelog for reasons of inaccurate code length measurement and readability, ideas for balancing levels: area limits, item evolution/or/other, really freaking low xp rates, start everything over... from scratch
#Version 0.8.2: -Reworked some stuff, fixed some bugs, reworked colors, added some more sillies, random things
#Version 0.8.3: -Added "restart" command, various changes, defense rebalancing, small idea layouts, fixed some minor bugs
#Version 0.8.4: -Reworked/condensed some of the code(may have unpredicted results)
#Version 0.8.5: -Managed to allow for better user input
#Version 0.8.6: -Added some spell level stuff, fixed some minor bugs, changed some commands slightly due to enemy triggering issues

#Version 0.9 (Major update!): -Added basic layout for difficulties, various things, will probably fix balance issues in the next update
#Version 0.9.1: -Added comments to make it easier for people who want to help with the game
#Version 0.9.2: -Added more to the leveled spell system, fixed enemies dealing negative damage
#Version 0.9.3: -Added more spellbooks- usable but not accessable yet, 
import os, random, time, pickle, sys, signal
import argparse
from collections import Counter
current_version = "v0.9.3"
os.system('clear')
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=120))
import Loadingbar
def update():
	ping_test = os.system('ping -q -c3 http://www.github.com >/dev/null')
	if ping_test == 0:
		pstatus = "Connection to Github available.  Downloading update."
	else:
		print "Connection failed.  Check your internet connection and try again."
#		try:
#			os.system('git pull')
#			if False:
#				print "Would you like to clone the game to your current directory?"
#				thing = raw_input('y/n ')
#				if thing == "y":
#					os.system('git clone https://github.com/pnd-tech-club/kazoo-quest.git')
#					print "Done!"
#				break
#			elif True:
#				os.system('git pull')
#				print "Done!"
#				break
#This code may be severely broken, I really don't have a clue at the time of writing it as I wrote it using online documentation and couldn't test it (yes, yes it is broken)
#parser = argparse.ArgumentParser(description='Kazoo Quest')
#parser.add_argument('--update', update = update())
#args = parser.parse_args()
wait = 0
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
weapon = 0
#Weapon list: 0 = hands, 1 = branch, 2 = dagger, 3 = dull sword, 4 = Blade Staff, 5 = sharp spear, 6 = polished axe, 7 = The Blade of Honking
armor = 0
#Armor list: 0 = Cloth shirt, 1 = Leather Breastplate, 2 = Chainmail Breastplate, 3 = Scale Breastplate, 4 = Crystal Breastplate, 5 = Cloak of Shadows, 6 = Magic Shield, 7 = Kazoo Shield of Death
dodges = 0
dodge_act = 1
damage = 3
max_hp = 20
max_mana = 5
level = 0
levels = ""
skills = []
skill_energy = 5
max_energy = 5
spells = []
spells_thing = []
exp = 0
evolve_count = 0
points = 0
triggers = []
inventory = []
take_words = ['take', 'grab', 'pick', 'get', 'aquire']
use_words = ['use', 'eat', 'read', 'drink']
n_words = ['n', 'north']
s_words = ['s', 'south']
e_words = ['e', 'east']
w_words = ['w', 'west']
u_words = ['u', 'up']
d_words = ['d', 'down']
stop = 0
letter = """The letter reads as follows:
Dear [The name is smudged out]
	We have recently heard about your ideas with our company.  We would like to officially meet with you on the fourth [The rest of the paragraph is blacked out].
We would also appreciate if you could begin to proceed with your ideas(at least planning) until our meeting.

                                                                               Sincerely,
                                                                                    A.L.
[There appears to be a large chunk of the page torn out]
"""
enemy_set = 0
#Time removed in v0.1.4 (Re-implementation being tested in v0.3)
time = 0
encounter_time = 5
skip = 0
enemy_type = ""
enemy_dam = 0
enemy_dodge = 0
enemy_buffs = []
enemy_debuffs = []
enemy_buff_timer = 5
enemy_debuff_timer = 5
enemy_info = ""
enemy_dam_info = ""
hp = 20
defe = 1
mana = 5
var_set = 0
player_buffs = []
player_debuffs = []
player_buff_timer = 5
player_debuff_timer = 5
firebolt_level = 0
frost_level = 0
poison_level = 0
lifesteal_level = 0
recover_level = 0
exp_limit = 10
kills = []
encounter = 0
history = []
class CleanExit(object):
	def __enter__(self):
		return self
	def __exit__(self, exc_type, exc_value, exc_tb):
		if exc_type is KeyboardInterrupt:
			return True
		return exc_type is None
x = 0
y = 0
z = 0
import os.path
autoload = os.path.isfile('game_save.dat')
if autoload == True:
	with open('game_save.dat', 'rb') as f:
		hp, damage, defe, mana, inventory, spells, spells_thing, skills, max_hp, max_mana, x, y, z, triggers, kills, points, armor, weapon, encounter, encounter_time,  enemy_type, levels, firebolt_level, frost_level, poison_level, lifesteal_level, recover_level, game_diff, roominfo = pickle.load(f)
	f.close()
	os.system('clear')
	print color['cyan'] + "Game loaded!" + color['off']
	print roominfo
else:
	pass
silly = 0
while silly != 1 and autoload != True:
	game_diff = raw_input(color['blue'] + "What difficulty do you want to play on?" + color['green'] + "\n1. Easy" + color['yellow'] + "\n2. Normal" + color['red'] + "\n3. Hard" + color['darkmagenta'] + "\n4. Actually insane" + color['off'] + "\n> ")
	if game_diff == "1":
		hp = 25
		defe = 2
		mana = 8
	elif game_diff == "2":
		hp = 20
		defe = 1
		mana = 5
	elif game_diff == "3":
		hp = 15
		defe = 1
		mana = 5
	elif game_diff == "4":
		print color['red'] + "I hope you know what you're doing..." + color['off']
		hp = 10
		defe = 0
		mana = 0
	classsc = raw_input(color['blue'] + "What class would you like to be?" + color['yellow'] + "\n1. Warrior\n2. Mage\n3. Assassin\n" + color['off'])
	if classsc == "1":
		skills.append("Rage")
		silly = 1
	elif classsc == "2":
		spells.append("recover")
		silly = 1
	elif classsc == "3":
		skills.append("Stealth")
		silly = 1
	print color['cyan'] + "Welcome to Kazoo Quest!  For help type \"help\"!" + color['off']
#The line below will be commented out when current version is known to be stable
print color['red'] + "THIS VERSION IS IN DEVELOPMENT. PLEASE REPORT ANY AND ALL POSSIBLE BUGS!" + color['off']
act = raw_input('> ')
words = act.split(" ")
stop = 0
while stop != 1:
#Map info for ease of access while debugging:
#Variable 'x' is west/east(ex. -1 would be to the west and +1 would be to the east)
#Variable 'y' is south/north(ex. -1 would be to the south and +1 would be to the north)
#Variable "z" is an inverted height (+1 would be down and -1 would be up)
	if list(set(n_words) & set(words)):
		y += 1
	elif list(set(s_words) & set(words)):
		y -= 1
	elif list(set(e_words) & set(words)):
		x += 1
	elif list(set(w_words) & set(words)):
		x -= 1
	elif list(set(d_words) & set(words)):
		z += 1
	elif list(set(u_words) & set(words)):
		z -= 1
#Debugging command
	if act == "num":
		print x
		print y
		print z
		if encounter >= 1:
			encounter_time += 1
	if list(set(use_words) & set(words)):
		if "switch" in words and x == 3 and y == 7 and z == 0:
			triggers.append("lights")
			print color['magenta'] + "You flip the switch and the lights in the house suddenly turn on." + color['off']
		elif "switch" in words and x == 3 and y == 7 and z == 0 and "lights" in triggers:
			print color['magenta'] + "You wiggle the switch but nothing happens." + color['off']
		elif "crowbar" in words and x == 3 and y == 12 and z == 1:
			print color['magenta'] + "You use the crowbar to open the door." + color['off']
			triggers.append("underground_door")
		elif "crowbar" in words and x == 2 and y == 8 and z == 0:
			print color['magenta'] + "You use the crowbar to open the trapdoor." + color['off']
			triggers.append("trapdoor")
#I know this prioritizes certain spellbooks over others but who actually cares?
		elif "spellbook" in words and "spellbook- Fire" in inventory:
			print color['magenta'] + "You read the book and it bursts into flame." + color['off']
			spells.append("firebolt")
			spells_thing.append("1. Firebolt" + "\tDamage: 10 to 25")
		elif "spellbook" in words and "spellbook- Frost" in inventory:
			print color['magenta'] + "As you finish reading the mysterious runes, the book freezes over and shatters into ice fragments." + color['off']
			spells.append("frost")
			spells_thing.append("2. Frost" + "\tDamage: 25 to 35")
		elif "spellbook" in words and "spellbook- Poison" in inventory:
			print color['magenta'] + "As you read the book, it suddenly sprouts poison ivy and you drop it." + color['off']
			spells.append("posion")
			spells_thing.append("3. Poison" + "\tDamage: 10 to 18")
		elif "spellbook" in words and "spellbook- Life Steal" in inventory:
			print color['magenta'] + "As you finish reading the runes, the spellbook glows pink and vanishes." + color['off']
			spells.append("life steal")
			spells_thing.append("4. Life Steal" + "\tDamage/Heal: 15 to 30")
			
#Yeah this thing :3
		elif "charm" in words and "mysterious charm" in inventory:
			print color['magenta'] + "You begin to feel funny.  You suddenly black out..." + color['off']
			evolve_count += 1
			print color['green'] + "You wake up and realize that the charm must have been the legendary \"Element of Harmony\".  It grants whoever uses it a beautiful voice!" + color['off']
		else:
			print color['magenta'] + "You don't have that item!" + color['off']
	if list(set(take_words) & set(words)):
		if "torch" in words and x == 0 and y == 0 and z == 0 and "torch" not in triggers:
			items = "torch"
			inventory.append(items)
			triggers.append(items)
			print color['magenta'] + "You pick up the torch and are able to see better." + color['off']
		elif "shuriken" in words and x == 0 and y == -1 and z == 0 and "shuriken" not in inventory:
			items = "shuriken"
			inventory.append(items) * 7
			print color['magenta'] + "You pick up seven shuriken." + color['off']
		elif "branch" in words and x == 2 and y == 1 and z == 0 and weapon < 1:
			items = "branch"
			inventory.append(items)
			triggers.append(items)
			weapon = 1
			var_set = 1
			print color['magenta'] + "You pick up the branch and hold it like a spear." + color['off']
		elif "letter" in words and x == 2 and y == 6 and z == 0 and "letter" not in triggers:
			items = "letter"
			inventory.append(items)
			triggers.append(items)
			print color['magenta'] + "You take the letter out of the mailbox." + color['off']
			print letter
		elif "dagger" in words and x == 3 and y == 7 and z == 1 and weapon < 2:
			items = "dagger"
			inventory.append(items)
			weapon = 2
			var_set = 1
			print color['magenta'] + "You wield the dagger and feel stronger." + color['off']
			items = "branch"
			inventory.remove(items)
		elif "armor" in words and x == 3 and y == 7 and z == 1 and armor < 1:
			items = "leather armor"
			inventory.append(items)
			armor = 1
			print color['magenta'] + "You put on the leather armor." + color['off']
		elif "lamp" in words and x == 3 and y == 7 and z == 1 and "lamp" not in inventory:
			items = "lamp"
			inventory.append(items)
			triggers.append(items)
			items = "torch"
			inventory.remove(items)
			print color['magenta'] + "Your torch happens to burn out as you pick up the lamp." + color['off']
		elif "armor" in words and x == -1 and y == 15 and z == 1 and armor <= 1:
			items = "Chainmail armor"
			inventory.append(items)
			armor = 2
			print color['magenta'] + "You put on the chainmail armor." + color['off']
			items = "leather armor"
			inventory.remove(items)
		elif "crowbar" in words and x == 9 and y == 9 and z == 1 and "crowbar" not in inventory:
			items = "crowbar"
			inventory.append(items)
			print color['magenta'] + "You pick up the crowbar." + color['off']
		elif "key" in words and x == 2 and y == 8 and z == 0 and "key" not in inventory and "trapdoor" in triggers:
			items = "key"
			inventory.append(items)
			print color['magenta'] + "You pick up a mysterious key." + color['off']
		elif "book" in words and x == 3 and y == 13 and z == 1 and "spellbook- Fire" not in inventory and "firebolt" not in spells:
			items = "spellbook- Fire"
			inventory.append(items)
			print color['magenta'] + "You pick up the mysterious spellbook." + color['off']
		else:
			print color['magenta'] + "You don't see that here." + color['off']
	if act == "clear":
		if encounter >= 1:
			encounter_time += 1
		os.system('clear')
	elif act == "inv":
		print '\n'.join(inventory)
		if encounter >= 1:
			encounter_time += 1
	elif act == "restart":
		while wait == 0:
			print color['red'] + "Are you sure you want to delete your save and restart all progress?" + color['off']
			response = raw_input('(y/n) >')
			if response == "y":
				print "Okay, deleting your save and restarting..."
				os.system('rm game_save.dat')
				os.system('python kazooquest.py')
				wait = 1
			elif response == "n":
				wait = 1
	elif act == "look":
		skip = 0
		if encounter >= 1:
			encounter_time += 1
	elif act == "sneak" and "Stealth" in skills and skill_energy >= 5:
		encounter_time += 6
		skill_energy -= 5
#Debugging commands
	elif act == "debug.update":
		update()
	elif act == "debug.triggers":
		print triggers
	elif act == "debug.evolveitem":
		inventory.append("mysterious charm")
	elif act == "save":
		with open('game_save.dat', 'wb') as f:
			pickle.dump([hp, damage, defe, mana, inventory, spells, spells_thing, skills, max_hp, max_mana, x, y, z, triggers, kills, points, armor, weapon, encounter, encounter_time,  enemy_type, levels, firebolt_level, frost_level, poison_level, lifesteal_level, recover_level, game_diff, roominfo], f, protocol = 2)
		f.close()
		print color['cyan'] + "Save successful!" + color['off']
		if encounter >= 1:
			encounter_time += 1
	elif act == "load":
		with open('game_save.dat', 'rb') as f:
			hp, damage, defe, mana, inventory, spells, spells_thing, skills, max_hp, max_mana, x, y, z, triggers, kills, points, armor, weapon, encounter, encounter_time,  enemy_type, levels, firebolt_level, frost_level, poison_level, lifesteal_level, recover_level, game_diff, roominfo = pickle.load(f)
		f.close()
		os.system('clear')
		print color['cyan'] + "Game loaded!" + color['off']
	elif act == "quit":
		print color['blue'] + "Are you sure you want to quit? (yes/no)" + color['off']
		quit_response = raw_input('> ')
		if quit_response == "yes":
			quit()
		else:
			skip = 0
#Debugging command
	elif act == "OP420":
		weapon = 7
		armor = 7
		spells = []
		spells_thing = []
		spells.append("firebolt")
		spells.append("frost")
		spells.append("poison")
		spells.append("life steal")
		spells.append("recover")
		spells_thing.append("1. Firebolt" + "\tDamage: 10 to 25")
		spells_thing.append("2. Frost")
		spells_thing.append("3. Poison")
		spells_thing.append("4. Life Steal")
		spells_thing.append("5. ") #Need an idea for this spell
		skills.append("Stealth")
		skills.append("Rage")
#Debugging command
	elif act == "etime":
		print encounter
		print encounter_time
		if encounter >= 1:
			encounter_time += 1
	elif act == "spells":
		print '\n'.join(spells)
		if encounter >= 1:
			encounter_time += 1
	elif act == "heal":
#Reminder to redo this- needs to be reworked
		hp_heal = max_hp / 2
		mana_heal = max_mana / 4 * random.randint(1, 2)
		skill_heal = max_energy / 4 * random.randint(1, 2)
		hp += hp_heal
		mana += mana_heal
		skill_energy += skill_heal
		print color['darkblue'] + "You have healed %r health, %r mana and %r energy!" % (hp_heal, mana_heal, skill_heal) + color['off']
		if hp > max_hp:
			hp = max_hp
		encounter_time -= 3
#	elif act == "time":
#		skip = 0
#Debugging command
	elif act == "tp":
		x = int(raw_input('> '))
		y = int(raw_input('> '))
		z = int(raw_input('> '))
	elif act == "stats":
		print "Damage: %r\nHealth: %r\nDefense: %r\nMana: %r\nLevel: %r\nExp: %r/%r" % (damage, hp, defe, mana, len(levels), exp, exp_limit)
		encounter_time += 1
	elif act == "credits":
		print "This game was written by Matthew Knecht in Python 2.7.  It is currently in %r  The story of the game revolves around a player who has lost his memory and has to find his Golden Kazoo.  The game doesn't have much content- but that will be resolved shortly.  Thanks for playing!" % current_version
	if act == "help":
		print color['darkwhite']+ " -help (Shows this screen) \n -look (Shows you your surroundings) \n -heal (Heals you but draws monsters nearby) \n -use (Uses an item or object) \n -take (Takes an item)\n -n, s, e, w, u, d (Moves you in its respective direction)\n -clear (Clears the screen)\n -info (Shows your your stats)" + color['off']	
		if encounter >= 1:
			encounter_time += 1
	if x == 0 and y == 0 and z == 0 and "torch" not in triggers:
		encounter = 0
		roominfo = "You have found yourself in a dimly lit cave.  You have no memory of how you got here or who you are.  There is a path to the north and south.  You see a torch on the ground."
		print roominfo
	elif x == 0 and y == 0 and z == 0 and "torch" in triggers:
		roominfo = "Your torch lights up the walls of the cave.  There is a path to the north and south."
		print roominfo
	elif x == 0 and y == 1 and z == 0 and "torch" not in triggers:
		roominfo = "You start walking to the north yet find that the mysterious light is dimming rapidly.  You decide to turn back until you find a light source."
		print roominfo
		y -= 1
	elif x == 0 and y == 1 and z == 0 and "torch" in triggers:
		roominfo = "You begin to walk to the north, allowing your torch to light the way.  As you walk you begin to hear a slight howl of wind from ahead of you.  There is a path to the east."
		print roominfo
	elif x == 1 and y == 1 and z == 0:
		roominfo = "You walk to the east and begin to feel the breeze picking up.  You look ahead of you and see outside a little bit ahead."
		print roominfo
	elif x == 2 and y == 1 and z == 0 and "branch" not in triggers:
		encounter = 0
		roominfo = "You reach the end of the tunnel and feel the heat of the sun around you.  The trees tower over you and you hear the sound of rushing water to the north.  You see a good sized tree branch with a pointed end."
		enemy_type = "wolf"
		print roominfo
	elif x == 2 and y == 1 and z == 0 and "branch" in triggers:
		encounter = 0
		roominfo = "You reach the end of the tunnel and see a forest to the east.  You hear the sound of rushing water to the north."
		enemy_type = "wolf"
		print roominfo
	elif x == 2 and y == 2 and z == 0:
		encounter = 1
		enemy_type = "wolf"
		roominfo = "There is a swiftly flowing stream here.  To the east is a path to the forest.  You think you see a small cottage far to the north."
		print roominfo
	elif x == 2 and y == 3 and z == 0:
		roominfo = "You keep walking around the side of the mountain.  There is a cottage far to the north and a cave to the south.  There is a forest to the east."
		enemy_type = "wolf"
		print roominfo
	elif x == 2 and y == 4 and z == 0:
		roominfo = "The mountain path seems to be rougher here.  You see that the stream flows from a grate in the mountain.  There is a forest to the east, a cave to the south, and a cottage to the north."
		enemy_type = "wolf"
		print roominfo
	elif x == 2 and y == 5 and z == 0:
		roominfo = "You are nearing the cottage.  There is a cave far to the south."
		print roominfo
#Forest area follows
	elif x == 3 and y == 1 and z == 0:
		encounter = 0
		roominfo = "The sunlight is slightly filtered by the trees above.  There is a cave to the west."
		print roominfo
	elif x == 4 and y == 1 and z == 0:
		encounter = 1
		enemy_type = "elf"
		roominfo = "The trees here are denser than around the edge of the forest."
		print roominfo
	elif x == 3 and y == 2 and z == 0:
		encounter = 0
		roominfo = "The sunlight is slightly filtered by the trees above.  There is a stream to the west."
		print roominfo
	elif x == 3 and y == 4 and z == 0:
		encounter = 1
		enemy_type = "elf"
		roominfo = "There appears to be an opening in the trees to the east."
		print roominfo
	elif x == 3 and y == 3 and z == 0:
		encounter = 0
		roominfo = "The sunlight is slightly filtered by the trees above.  There is a mountain to the west."
		print roominfo
	elif x == 4 and y == 3 and z == 0:
		encounter = 1
		enemy_type = "elf"
		roominfo = "The trees here are denser than around the edge of the forest."
		print roominfo
	
#House area follows
	elif x == 2 and y == 6 and z == 0 and "letter" not in triggers:
		encounter = 1
		roominfo = "You stand in front of the mailbox of the cottage.  There appears to be a letter in the mailbox.  There is a cave far to the south and a forest to the east."
		print roominfo
	elif x == 2 and y == 6 and z == 0 and "letter" in triggers:
		encounter = 1
		roominfo = "You stand in front of the mailbox of the cottage.  There is a cave far to the south and a forest to the east."
		enemy_type = "wolf"
		print roominfo
	elif x == 2 and y == 7 and z == 0 and "lights" not in triggers:
		encounter = 0
		roominfo = "The inside of the house is cold and dark.  You have an unexplainable feeling of gloom.  There are rooms to the east and the north."
		print roominfo
	elif x == 2 and y == 7 and z == 0 and "lights" in triggers:
		encounter = 0
		roominfo = "There is a bright red stain on the rug in front of the door.  You have an unexplainable feeling of dread.  The kitchen is to the east and the living room is to the north."
		print roominfo
	elif x == 3 and y == 7 and z == 0 and "lights" not in triggers:
		roominfo = "The room is lit up slightly by a window.  You can see a switch by the window.  The doorway is to the west."
		print roominfo
	elif x == 2 and y == 8 and z == 0 and "lights" not in triggers:
		roominfo = "It's way too dark in here for you to see anything.  The doorway is to the south."
		print roominfo
	elif x == 2 and y == 8 and z == 0 and "lights" in triggers and "trapdoor" not in triggers:
		roominfo = "The living room is completely barren.  There appears to be a locked trapdoor in the floor.  The doorway is to the south."
		print roominfo
	elif x == 2 and y == 8 and z == 0 and "lights" in triggers and "trapdoor" in triggers and "key" not in inventory:
		roominfo = "The trapdoor in this room has a key inside.  The doorway is to the south."
		print roominfo
	elif x == 2 and y == 8 and z == 0 and "lights" in triggers and "trapdoor" in triggers and "key" in inventory:
		roominfo = "The trapdoor in the center of the room is empty.  The doorway is to the south."
		print roominfo
#Variable "z" is an inverted height (+1 would be down and -1 would be up)
	elif x == 3 and y == 7 and z == 0 and z == 1 and "lights" not in triggers:
		roominfo = "Your torch isn't enough to let you see down the stairs."
		print roominfo
		z += 1
	elif x == 3 and y == 7 and z == 0 and "lights" in triggers:
		roominfo = "The light shows that there are stairs going down.  The entrance is to the west."
		print roominfo
#I know there is someway to make this more efficient, but oh well I don't have time for thinking right now :^ )
	elif x == 3 and y == 7 and z == 1 and "lights" in triggers and "lamp" not in inventory and armor < 1 and weapon < 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north.  There is a lamp on the ground.  There is a dagger on the ground.  There is leather armor on the ground."
		print roominfo
#Player has nothing ^
	elif x == 3 and y == 7 and z == 1 and "lamp" in inventory and armor < 1 and weapon < 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north.  There is a dagger on the ground.  There is leather armor on the ground."
		print roominfo
#Player has lamp ^
	elif x == 3 and y == 7 and z == 1 and "lamp" in inventory and armor >= 1 and weapon < 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north.  There is a dagger on the ground."
		print roominfo
#Player has lamp and armor ^
	elif x == 3 and y == 7 and z == 1 and "lamp" in inventory and armor < 1 and weapon >= 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north.  There is leather armor on the ground."
		print roominfo
#Player has lamp and dagger ^
	elif x == 3 and y == 7 and z == 1 and "lamp" in inventory and armor >= 1 and weapon >= 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north."
		print roominfo
#Player has all items ^
	elif x == 3 and y == 7 and z == 1 and "lamp" not in inventory and armor >= 1 and weapon < 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north.  There is a lamp on the ground.  There is a dagger on the ground."
		print roominfo
#Player has leather armor ^
	elif x == 3 and y == 7 and z == 1 and "lamp" not in inventory and armor >= 1 and weapon >= 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north.  There is a lamp on the ground."
		print roominfo
#Player has dagger and armor ^
	elif x == 3 and y == 7 and z == 1 and "lamp" not in inventory and armor < 1 and weapon < 2:
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
	elif x == 11 and y == 9 and z == 1:
		roominfo = "You feel yourself being taken somewhere else..."
		print roominfo
		x = 3
		y = 9
		z = 1
#North path split
	elif x == 3 and y == 10 and z == 1:
		roominfo = "All you see to the north is darkness."
		print roominfo
	elif x == 3 and y == 11 and z == 1:
		roominfo = "..."
		print roominfo
	elif x == 3 and y == 12 and z == 1 and "underground_door" not in triggers:
		roominfo = "There is suddenly a door in front of you.  You can't open it with your hands."
		print roominfo
	elif x == 3 and y == 12 and z == 1 and "underground_door" in triggers:
		roominfo = "The door is open."
		print roominfo
	elif x == 3 and y == 13 and z == 1 and "underground_door" not in triggers:
		y -= 1
	elif x == 3 and y == 13 and z == 1 and "spellbook- Fire" not in inventory and "firebolt" not in spells:
		roominfo = "There is a book lying on the ground."
		print roominfo
	elif x == 3 and y == 13 and z == 1 and "spellbook- Fire" in inventory:
		roominfo = "There is an empty room here."
		print roominfo
	elif x == 3 and y == 13 and z == 1 and "firebolt" in spells:
		roominfo = "There is an empty room here."
		print roominfo
#This is used to undo movement into an unexisting room V
	else:
		if list(set(n_words) & set(words)):
			y -= 1
		elif list(set(s_words) & set(words)):
			y += 1
		elif list(set(e_words) & set(words)):
			x -= 1
		elif list(set(w_words) & set(words)):
			x += 1
		elif list(set(d_words) & set(words)):
			z -= 1
		elif list(set(u_words) & set(words)):
			z += 1
	if encounter != 0:
		encounter_time -= 1
	while var_set == 1:
		if weapon == 0:
			damage == 3
		elif weapon == 1:
			damage += 2
			points += 1
		elif weapon == 2:
			damage += 3
			points += 3
		elif weapon == 3:
			damage += 3
			points += 5
		elif weapon == 4:
			damage += 5
			points += 10
		elif weapon == 5:
			damage += 8
			points += 20
		elif weapon == 6:
			damage += 10
			points += 25
#This weapon is going to be available for debugging through the input of "OP420"
		elif weapon == 7:
			damage = 1337
		var_set = 0
	if game_diff == "1":
		if armor == 0:
			defe = 2
			max_hp = 25
			max_mana = 8
		elif armor == 1:
			defe = 5
			max_hp = 30
			max_mana = 10
		elif armor == 2:
			defe = 8
			max_hp = 35
			max_mana = 15
		elif armor == 3:
			defe = 9
			max_hp = 40
			max_mana = 20
		elif armor == 4:
			defe = 12
			max_hp = 50
			max_mana = 30
		elif armor == 5:
			defe = 15
			max_hp = 60
			max_mana = 40
		elif armor == 6:
			defe = 20
			max_hp = 75
			max_mana = 50
		elif armor == 7:
			defe = 420
			max_hp = 9001
			max_mana = 6.9e+42
	if game_diff == "2":
		if armor == 0:
			defe = 1
			max_hp = 20
			max_mana = 5
		elif armor == 1:
			defe = 4
			max_hp = 25
			max_mana = 10
		elif armor == 2:
			defe = 6
			max_hp = 30
			max_mana = 15
		elif armor == 3:
			defe = 9
			max_hp = 40
			max_mana = 20
		elif armor == 4:
			defe = 12
			max_hp = 50
			max_mana = 30
		elif armor == 5:
			defe = 15
			max_hp = 60
			max_mana = 40
		elif armor == 6:
			defe = 20
			max_hp = 75
			max_mana = 50
		elif armor == 7:
			defe = 420
			max_hp = 9001
			max_mana = 6.9e+42
	if game_diff == "3":
		if armor == 0:
			defe = 1
			max_hp = 15
			max_mana = 5
		elif armor == 1:
			defe = 3
			max_hp = 20
			max_mana = 8
		elif armor == 2:
			defe = 5
			max_hp = 25
			max_mana = 10
		elif armor == 3:
			defe = 8
			max_hp = 30
			max_mana = 15
		elif armor == 4:
			defe = 10
			max_hp = 40
			max_mana = 20
		elif armor == 5:
			defe = 13
			max_hp = 50
			max_mana = 30
		elif armor == 6:
			defe = 18
			max_hp = 70
			max_mana = 45
		elif armor == 7:
			defe = 420
			max_hp = 9001
			max_mana = 6.9e+42
	if game_diff == "4":
		if armor == 0:
			defe = 0
			max_hp = 10
			max_mana = 0
		elif armor == 1:
			defe = 3
			max_hp = 20
			max_mana = 5
		elif armor == 2:
			defe = 5
			max_hp = 25
			max_mana = 10
		elif armor == 3:
			defe = 8
			max_hp = 30
			max_mana = 15
		elif armor == 4:
			defe = 10
			max_hp = 35
			max_mana = 20
		elif armor == 5:
			defe = 15
			max_hp = 40
			max_mana = 25
		elif armor == 6:
			defe = 20
			max_hp = 50
			max_mana = 35
		elif armor == 7:
			defe = 420
			max_hp = 9001
			max_mana = 6.9e+42
	if exp >= exp_limit:
		print color['blue'] + "Level up!" + color['off']
		exp = 0
#EXP limits are weird- needs to be reworked
		if len(levels) == 1:
			exp_limit = 25
		elif len(levels) == 2:
			exp_limit = 50
		elif len(levels) == 3:
			exp_limit = 85
		elif len(levels) == 4:
			exp_limit = 125
		elif len(levels) == 5:
			exp_limit = 150
		elif len(levels) == 6 and evolve_count >= 1:
			exp_limit = 180
		elif len(levels) == 7:
			exp_limit = 210
		elif len(levels) == 8:
			exp_limit = 245
		elif len(levels) == 9:
			exp_limit = 275
		elif len(levels) == 10:
			exp_limit = 325
#Levels OP, pls nurf?- needs to be reworked
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
#Limits level until certain item is used, I think
	elif len(levels) == 6 and evolve_count >= 1:
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
	words = ""
	act = raw_input('> ')
	words = act.split(" ")
	stop = 0
	while encounter != 0 and encounter_time <= 0:
		stop = 1
		while enemy_set != 1:
#Some enemies have too high/too low of stats- needs to be reworked
			if enemy_type == "wolf":
				enemy_hp = 15
				enemy_dam = random.randint(2, 4)
				enemy_dam_info = "2 to 4"
				enemy_dodge = 0
			elif enemy_type == "orc":
				enemy_hp = 25
				enemy_dam = random.randint(6, 8)
				enemy_dam_info = "6 to 8"
				enemy_dodge = 1
			elif enemy_type == "wraith":
				enemy_hp = 30
				enemy_dam = random.randint(7, 9)
				enemy_dam_info = "7 to 9"
				enemy_dodge = 3
			elif enemy_type == "dwarf":
				enemy_hp = 35
				enemy_dam = random.randint(7, 10)
				enemy_dam_info = "7 to 10"
				enemy_dodge = 1
			elif enemy_type == "spirit":
				enemy_hp = 40
				enemy_dam = random.randint(8, 11)
				enemy_dam_info = "8 to 11"
				enemy_dodge = 0
			elif enemy_type == "slime":
				enemy_hp = 100
				enemy_dam = random.randint(5, 15)
				enemy_dam_info = "5 to 15"
				enemy_dodge = 0
#Remember to fix this silly grammar thingy here
			enemy_info = color['red'] + "A "+enemy_type+" suddenly appears!." + color['off']
			print enemy_info
			enemy_set = 1
		fight_act = raw_input(color['blue'] + "What do you want to do?" + color['yellow'] + "\n1: Attack" + color['green'] + "\tHealth: %r" % hp + color['red'] + "\tEnemy Health: %r" % enemy_hp + color['yellow'] + "\n2: Magic" + color['green'] + "\tMana: %r" % mana + color['red'] + "\t\tEnemy Damage: %s" % enemy_dam_info + color['yellow'] + "\n3: Dodge\n4: Enemy Info\n5: Run Away\n" + color['off'])
		dodges = 0
		if fight_act == "1":
			enemy_hp = enemy_hp - damage
			print color['green'] + "You dealt %d damage to the %s!" % (damage, enemy_type) + color['off']
		elif fight_act == "2":
			print "Available spells:\n" + '\n'.join(spells_thing)
			magic_attack = raw_input('> ')
#Magic is(as usual) OP- needs to be reworked
			if magic_attack == "1" and "firebolt" in spells and mana >= 5:
				if firebolt_level == 0:
					magic_dam = random.randint(10, 25)
				elif firebolt_level == 1:
					magic_dam = random.randint(15, 30)
				elif firebolt_level == 2:
					magic_dam = random.randint(20, 35)
				elif firebolt_level == 3:
					magic_dam = random.randint(25, 40)
				elif firebolt_level == 4:
					magic_dam = random.randint(30, 45)
				elif firebolt_level == 5:
					magic_dam = random.randint(35, 50)
				mana -= 5
				enemy_hp -= magic_dam
				enemy_debuffs.append("Burning")
				enemy_debuff_timer = 5
				print color['red'] + "You dealt %r magic damage to the enemy and set it on fire!" % magic_dam + color['off']
			elif magic_attack == "2" and "frost" in spells and mana >= 8:
				if frost_level == 0:
					magic_dam = random.randint(25, 35)
				elif frost_level == 1:
					magic_dam = random.randint(30, 40)
				elif frost_level == 2:
					magic_dam = random.randint(35, 45)
				elif frost_level == 3:
					magic_dam = random.randint(40, 50)
				elif frost_level == 4:
					magic_dam = random.randint(45, 55)
				elif frost_level == 5:
					magic_dam = random.randint(50, 60)
				mana -= 8
				enemy_hp -= magic_dam
				enemy_debuffs.append("Frozen")
				enemy_debuff_timer = 5
				print color['blue'] + "You dealt %r magic damage and froze the enemy!" % magic_dam + color['off']
			elif magic_attack == "3" and "poison" in spells and mana >= 13:
				if poison_level == 0:
					magic_dam = random.randint(10, 18)
				elif poison_level == 1:
					magic_dam = random.randint(12, 20)
				elif poison_level == 2:
					magic_dam = random.randint(14, 22)
				elif poison_level == 3:
					magic_dam = random.randint(16, 24)
				elif poison_level == 4:
					magic_dam = random.randint(18, 26)
				elif poison_level == 5:
					magic_dam = random.randint(20, 28)
				mana -= 13
				enemy_hp -= magic_dam
				enemy_debuffs.append("Poisoned")
				enemy_debuff_timer = 8
				print color['green'] + "You dealt %r magic damage and poisoned the enemy!" % magic_dam + color['off']
			elif magic_attack == "4" and "life steal" in spells and mana >= 20:
				if lifedrain_level == 0:
					drain_dam = random.randint(15, 30)
				elif lifedrain_level == 1:
					drain_dam = random.randint(18, 33)
				elif lifedrain_level == 2:
					drain_dam = random.randint(20, 35)
				elif lifedrain_dam == 3:
					drain_dam = random.randint(23, 38)
				elif lifedrain_level == 4:
					drain_dam = random.randint(25, 40)
				elif lifedrain_level == 5:
					drain_dam = random.randint(28, 43)
				mana -= 20
				enemy_hp -= drain_dam
				hp += drain_dam
				print color['green'] + "You stole %r health from the %r!" % (drain_dam, enemy_type) + color['off']
			elif magic_attack == "5" and "recover" in spells and mana >= 8:
				mana -= 8
				hp_heal = random.randint(10, 30)
				hp += hp_heal
				print "You healed %r health!" % hp_heal
			else:
				print color['darkyellow'] + "You can't do that!" + color['off']
		elif fight_act == "3":
			dodge_act = random.randint(0, 100)
			if dodge_act <= 25:
				print color['green'] + "You dodged the attack!" + color['off']
				dodges = 1
			if dodge_act >= 75:
				parrypowa = damage * 2
				enemy_hp -= parrypowa
				print color['green'] + "You parried the attack and dealt %d damage!" % parrypowa  + color['off']
				dodges = 1
		elif fight_act == "4":
			print color['darkgreen'] + "Enemy Health: %d\nEnemy Damage: %s" % (enemy_hp, enemy_dam_info) + color['off']
		elif fight_act == "5":
			run_success = random.randint(0, 3)
			if run_success == 1:
				encounter_time = random.randint(5, 7)
				enemy_hp = 0
				dodges = 0
				enemy_debuffs = []
				print color['darkyellow'] + "You ran away!" + color['off']
		else:
			print color['darkyellow'] + "You can't do that!" + color['off']
		if enemy_hp > 0 and dodges == 0 and fight_act != "4" and "Frozen" not in enemy_debuffs:
#It seems like some enemies deal too much damage while some don't deal enough- needs to be reworked
			if enemy_type == "wolf":
				enemy_dam = random.randint(2, 4)
			elif enemy_type == "orc":
				enemy_dam = random.randint(6, 8)
			elif enemy_type == "wraith":
				enemy_dam = random.randint(7, 9)
			elif enemy_type == "dwarf":
				enemy_dam = random.randint(7, 10)
			elif enemy_type == "spirit":
				enemy_dam = random.randint(8, 11)
			elif enemy_type == "slime":
				enemy_dam = random.randint(5, 15)
			if enemy_dam - defe <= 0:
				print color['magenta'] + "The enemy missed!" + color['off']
			else:
				hp = hp - enemy_dam + defe
				dodges = 0
				print color['magenta'] + "The %s dealt %r damage to you!" % (enemy_type, enemy_dam-defe) + color['off']
		if len(enemy_debuffs) > 0:
#Randomly gets the amount of damage to deal to the enemy while specific debuff is active
			if "Burning" in enemy_debuffs:
				if firebolt_level == 0:
					burn_dam = random.randint(3, 5)
				elif firebolt_level == 1:
					burn_dam = random.randint(5, 8)
				elif firebolt_level == 2:
					burn_dam = random.randint(8, 12)
				elif firebolt_level == 3:
					burn_dam = random.randint(10, 15)
				enemy_hp -= burn_dam
				print "The enemy took %r damage from burning!" % burn_dam
			if "Poisoned" in enemy_debuffs:
				if poison_level == 0:
					poison_dam = random.randint(5, 10)
				elif poison_level == 1:
					poison_dam = random.rantint(10, 15)
				elif poison_level == 2:
					poison_dam = random.randint(15, 20)
				elif poison_level == 3:
					poison_dam = random.randint(20, 25)
				elif poison_level == 4:
					poison_dam = random.randint(25, 30)
				elif poison_level == 5:
					poison_dam = random.randint(30, 35)
				enemy_hp -= poison_dam
				print "The enemy took %r damage from poison!" % poison_dam
			if "Frozen" in enemy_debuffs:
				print "The enemy can't attack because it is frozen!"
			enemy_debuff_timer -= 1
#Clears the enemy's debuffs after 5 turns of not using a spell
			if enemy_debuff_timer <= 0:
				enemy_debuffs = []
		if enemy_hp <= 0 and fight_act != "5":
			enemy_set = 0
			enemy_debuffs = []
			print color['blue'] + "You killed the " + enemy_type +"!" + color['off']
#Prepare for inefficiency : 3
			kills.append(enemy_type)
			skill_energy += 1
			encounter_time = random.randint(5, 8)
#EXP points might be a bit unbalanced, needs to be reworked
			if enemy_type == "wolf":
				exp += 1
				points += 2
			elif enemy_type == "orc":
				exp += 2
				points += 3
			elif enemy_type == "wraith":
				exp += 3
				points += 4
			elif enemy_type == "dwarf":
				exp += 4
				points += 6
			elif enemy_type == "elf":
				exp += 5
				points += 5
			elif enemy_type == "spirit":
				exp += 8
				points += 8
			elif enemy_type == "goo":
				exp += 10
				points += 10
		if hp > max_hp:
			hp = max_hp
		if hp <= 0:
			print color['darkred'] + "You have died!" + color['off']
			print color['blue'] + "Do you want to see your final stats?" + color['off']
			dead_p = raw_input('y/n ')
			if dead_p == "y":
				print color['darkmagenta'] + "You killed these enemies:" + color['off']
				cnt = Counter()
				for word in kills:
					cnt[word] += 1
				print dict(cnt)
				print "These are your final stats:"
				print color['darkgreen'] + "Damage: %r\nHealth:%r\nDefense:%r\nMana:%r\nLevel:%r" % (damage, hp, defe, mana, level) + color['off']
				print color['darkgreen'] + "\nYour final score was %r" % points + color['off']
				quit()
			elif dead_p == "n":
				quit()
		stop = 0
	if hp > max_hp:
		hp = max_hp
	if mana > max_mana:
		mana = max_mana
	if skill_energy > max_energy:
		skill_energy = max_energy
