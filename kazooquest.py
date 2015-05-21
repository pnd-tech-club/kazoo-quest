#Credits:
#Written by Matthew Knecht
#Written in Python 2.7
from Tkinter import *
from ttk import *
import ttk
import os, random, time, pickle, sys, signal
import argparse
from collections import Counter
current_version = "v1.0.6"
os.system('clear')
#import Loadingbar
act = ""
def prompt()
root = Tk()
root.title("Testing")
mainframe = ttk.Frame(root, padding="50 50 200 200")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
act = StringVar()
act_entry = ttk.Entry(mainframe, width=70, textvariable=act)
act_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=roominfo).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Boop?").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="thing").grid(column=3, row=1, sticky=W)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
act_entry.focus()
root.bind('<Return>', texted)
root.mainloop()
def update():
	ping_test = os.system('ping -q -c3 http://www.github.com >/dev/null')
	if ping_test == 0:
		pstatus = "Connection to Github available. Downloading update."
	else:
		print "Connection failed. Check your internet connection and try again."
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
parser = argparse.ArgumentParser(description='Kazoo Quest!')
args = parser.parse_args()
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
    'darkmagenta': "\033[0;35m",
    'darkblack':  "\033[0;30m",
    'off':        "\033[0;0m"
}
weapon = 0
#Weapon list: 0 = hands, 1 = branch, 2 = dagger, 3 = dull sword, 4 = Blade Staff, 5 = sharp spear, 6 = polished axe, 7 = The Blade of Honking
armor = 0
#Armor list: 0 = Cloth shirt, 1 = Leather Breastplate, 2 = Chainmail Breastplate, 3 = Scale Breastplate, 4 = Crystal Breastplate, 5 = Cloak of Shadows, 6 = Magic Shield, 7 = Kazoo Shield of Death
min_dam = 0
max_dam = 0
dodges = 0
dodge_act = 1
damage = 0
max_hp = 20
max_mana = 5
level = 0
max_level = 5
skills = []
skills_thing = []
skill_energy = 5
max_energy = 5
spells = []
spells_thing = []
exp = 0
evolve_count = 0
points = 0
thatonething = 0
boss = 0
triggers = []
inventory = []
n_words = ['n', 'north']
s_words = ['s', 'south']
e_words = ['e', 'east']
w_words = ['w', 'west']
u_words = ['u', 'up']
d_words = ['d', 'down']
yes_words = ['yes', 'y', 'true', 'indeed', 'yeah', 'afirmative']
lights_words = ['switch', 'lights', 'light']
spellbook_words = ['spellbook', 'book', 'runebook']
take_words = ['take', 'grab', 'pick', 'get', 'aquire', 'nab', 'steal']
use_words = ['use', 'eat', 'read', 'drink', 'flip', 'turn', 'hit']
stop = 0
letter = """The letter reads as follows:
Dear [The name is smudged out]
	We have recently heard about your ideas with our company. We would like to officially meet with you on the fourth [The rest of the paragraph is blacked out].
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
resetrimer = 10
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
heal_level = 0
stun_level = 0
exp_limit = 10
kills = []
encounter = 0
history = []
tut_finished = 0
loadyload = 0
dothing = ""
acted = 0
global screen1
global words
words = ""
def prompt():
	global act
	acte = Entry(Point(w.getWidth()/6, 100), 15)
	acte.setText("")
	acte.draw(w)
	boop = Rectangle(Point(w.getWidth()/4, 90), Point(w.getWidth()/3.5, 110))
	boop.draw(w)
	w.getMouse()
	act = acte.getText()
	print act
	words = act.split(" ")
	print words
def death():
	print color['darkred'] + "You have died!" + color['off']
	print color['blue'] + "Do you want to see your final stats?" + color['off']
	dead_p = raw_input('y/n ')
	if dead_p == "y":
		print color['darkmagenta'] + "You killed these enemies: " + color['off']
		cnt = Counter()
		for word in kills:
			cnt[word] += 1
		print dict(cnt)
		print "These are your final stats: "
		print color['darkgreen'] + "Damage: %r\nHealth:%r\nDefense:%r\nMana:%r\nLevel:%r/%r" % (damage, max_hp, defe, max_mana, level, max_level) + color['off']
		print color['darkgreen'] + "\nYour final score was %r" % points + color['off']
		quit()
	elif dead_p == "n":
		quit()
	else:
		death()
def selectdiff():
	screen = Text(Point(w.getWidth()/2, 100), "What difficulty do you want to play on?")
	screen.draw(w)
	screen = Text(Point(w.getWidth()/2, 115), "1. Easy")
	screen.setTextColor('green3')
	screen.draw(w)
	screen = Text(Point(w.getWidth()/2, 130), "2. Normal")
	screen.setTextColor('yellow')
	screen.draw(w)
	screen = Text(Point(w.getWidth()/2, 145), "3. Hard")
	screen.setTextColor('orange')
	screen.draw(w)
	screen = Text(Point(w.getWidth()/2, 160), "4. Actually insane")
	screen.setTextColor('red4')
	screen.draw(w)
	#prompt()
	game_diff = raw_input('> ')
	if game_diff == "1":
		hp = 25
		defe = 2
		mana = 8
		damage = 2
		weapon = 0
		w.close()
	elif game_diff == "2":
		hp = 20
		defe = 1
		mana = 5
		damage = 1
		weapon = 0
		w.close()
	elif game_diff == "3":
		hp = 15
		defe = 1
		mana = 5
		weapon = 0
		w.close()
	elif game_diff == "4":
		print color['red'] + "I hope you know what you're doing..." + color['off']
		hp = 10
		defe = 0
		mana = 0
		damage = 2
		w.close()
	else:
		print "lolnope"
		selectdiff()
def selectclass():
	w = GraphWin('Kazoo Quest', 1000, 200)
	screen = Text(Point(w.getWidth()/2, 85), "What class would you like to be?")
	screen.setTextColor('yellow3')
	screen.draw(w)
	screen = Text(Point(w.getWidth()/2, 100), "1. Warrior-   Has the Rage skill")
	screen.setTextColor('blue2')
	screen.draw(w)
	screen = Text(Point(w.getWidth()/2, 115), "2. Cleric-   Has the heal spell")
	screen.setTextColor('blue2')
	screen.draw(w)
	screen = Text(Point(w.getWidth()/2, 130), "3. Assassin-   Has the Sneak skill")
	screen.setTextColor('blue2')
	screen.draw(w)
	screen = Text(Point(w.getWidth()/2, 145), "4. Ninja-   Has the Stun spell")
	screen.setTextColor('blue2')
	screen.draw(w)
	screen = Text(Point(w.getWidth()/2, 160), "5. Wizard-   Has higher spell damage")
	screen.setTextColor('blue2')
	screen.draw(w)
	#prompt()
	classsc = raw_input('> ')
	if classsc == "1":
		skills.append("rage")
		skills_thing.append("%r. Rage" % (len(skills_thing) + 1))
		silly = 1
		w.close()
	elif classsc == "2":
		spells.append("heal")
		spells_thing.append("%r. Heal" % (len(spells_thing) + 1))
		silly = 1
		max_mana = 10
		mana = 10
		w.close()
	elif classsc == "3":
		skills.append("stealth")
		skills_thing.append("%r. Stealth" % (len(skills_thing) + 1))
		silly = 1
		w.close()
	elif classsc == "4":
		spells.append("stun")
		spells_thing.append("%r. Stun" % (len(spells_thing) + 1))
		silly = 1
		w.close()
	elif classsc == "5":
		skills.append("magic boost")
		silly = 1
		w.close()
	else:
		print "lolnope"
		selectclass()
x = 0
y = 0
z = 0
import os.path
autoload = os.path.isfile('game_save.dat')
if autoload == True:
	tut_finished = 1
	if os.stat("game_save.dat").st_size != 0:
		with open('game_save.dat', 'rb') as f:
			hp, damage, defe, mana, inventory, spells, spells_thing, skills, max_hp, max_mana, x, y, z, triggers, kills, points, armor, weapon, encounter, encounter_time,  enemy_type, level, max_level, firebolt_level, frost_level, poison_level, lifesteal_level, heal_level, game_diff, roominfo, exp, exp_limit = pickle.load(f)
		f.close()
		loadyload = 1
		os.system('clear')
		screen1 = Text(Point(w.getWidth()/2, w.getHeight()/6), "Game loaded!")
		screen1.setTextColor("cyan4")
		screen1.draw(w)
		screen = Text(Point(w.getWidth()/2, w.getHeight()/4), roominfo)
		screen.setTextColor("black")
		screen.draw(w)
else:
	import Tutorial
silly = 0
if silly != 1 and loadyload != 1 and tut_finished == 1:
#Gah, this is gross
	selectdiff()
	w = GraphWin('Kazoo Quest', 1000, 200)
	screen = Text(Point(w.getWidth()/2, 85), "What class would you like to be?")
	screen.setTextColor('yellow3')
	screen.draw(w)
	screen = Text(Point(w.getWidth()/2, 100), "1. Warrior-   Has the Rage skill")
	screen.setTextColor('blue2')
	screen.draw(w)
	screen = Text(Point(w.getWidth()/2, 115), "2. Cleric-   Has the heal spell")
	screen.setTextColor('blue2')
	screen.draw(w)
	screen = Text(Point(w.getWidth()/2, 130), "3. Assassin-   Has the Sneak skill")
	screen.setTextColor('blue2')
	screen.draw(w)
	screen = Text(Point(w.getWidth()/2, 145), "4. Ninja-   Has the Stun spell")
	screen.setTextColor('blue2')
	screen.draw(w)
	screen = Text(Point(w.getWidth()/2, 160), "5. Wizard-   Has higher spell damage")
	screen.setTextColor('blue2')
	screen.draw(w)
	#prompt()
	classsc = raw_input('> ')
	if classsc == "1":
		skills.append("rage")
		skills_thing.append("%r. Rage" % (len(skills_thing) + 1))
		silly = 1
	elif classsc == "2":
		spells.append("heal")
		spells_thing.append("%r. Heal" % (len(spells_thing) + 1))
		silly = 1
		max_mana = 10
		mana = 10
	elif classsc == "3":
		skills.append("stealth")
		skills_thing.append("%r. Stealth" % (len(skills_thing) + 1))
		silly = 1
	elif classsc == "4":
		spells.append("stun")
		spells_thing.append("%r. Stun" % (len(spells_thing) + 1))
		silly = 1
	elif classsc == "5":
		skills.append("magic boost")
		silly = 1
	w.close()
	w = GraphWin('Kazoo Quest', 1000, 200)
	screen = Text(Point(w.getWidth()/2, w.getHeight()/4),"Welcome to Kazoo Quest! For help type \"help\"! Click to continue!")
	screen.setTextColor('cyan3')
	screen.draw(w)
	screen.setTextColor('black')
	roominfo = "You have found yourself in a dimly lit cave. You have no memory of how you got here or who you are. There is a path to the north and south. You see a torch on the ground."
	w.getMouse()
	screen.setText(roominfo)
#prompt()
click()
act = raw_input('> ')
words = act.split(' ')
stop = 0
while stop != 1:
#Map info for ease of access while debugging:
#Variable 'x' is west/east(ex. -1 would be to the west and +1 would be to the east)
#Variable 'y' is south/north(ex. -1 would be to the south and +1 would be to the north)
#Variable "z" is an inverted height (+1 would be down and -1 would be up)
#Debugging command
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
	if list(set(use_words) & set(words)):
		if list(set(lights_words) & set(words)):
			if x == 3 and y == 7 and z == 0 and "lights" not in triggers:
				triggers.append("lights")
				dothing = "You flip the switch and the lights in the house suddenly turn on."
				acted = 1
			elif x == 3 and y == 7 and z == 0 and "lights" in triggers:
				dothing = "You wiggle the switch but nothing happens."
				acted = 1
		elif "crowbar" in words and x == 3 and y == 12 and z == 1:
			dothing = "You use the crowbar to open the door."
			triggers.append("underground_door")
			acted = 1
		elif "crowbar" in words and x == 2 and y == 8 and z == 0:
			dothing = "You use the crowbar to open the trapdoor."
			triggers.append("trapdoor")
			acted = 1
#I know this prioritizes certain spellbooks over others but who actually cares?
		elif list(set(spellbook_words) & set(words)):
			if "spellbook- Fire" in inventory:
				dothing = "You read the book and it bursts into flame."
				spells.append("firebolt")
				inventory.remove("spellbook- Fire")
				spells_thing.append("%s. Firebolt" % str(len(spells_thing) + 1))
				acted = 1
			elif "spellbook- Frost" in inventory:
				dothing = "As you finish reading the mysterious runes, the book freezes over and shatters into ice fragments."
				spells.append("frost")
				inventory.remove("spellbook- Frost")
				spells_thing.append("%s. Frost" % str(len(spells_thing) + 1))
				acted = 1
			elif "spellbook- Poison" in inventory:
				dothing = "As you read the book, it suddenly sprouts poison ivy and you drop it."
				spells.append("posion")
				inventory.remove("spellbook- Poison")
				spells_thing.append("%s. Poison" % str(len(spells_thing) + 1))
				acted = 1
			elif "spellbook- Life Steal" in inventory:
				dothing = "As you finish reading the runes, the spellbook glows pink and vanishes."
				spells.append("life steal")
				inventory.remove("spellbook- Life Steal")
				spells_thing.append("%s. Life Steal" % str(len(spells_thing) + 1))
				acted = 1
			elif "old book" in inventory and x == 5 and y == 2 and z == 0 and "boss1" not in triggers:
				dothing = "As you read the old book, the runes by the pool of water begin to glow orange."
				dothing = "Suddenly, a strange looking blob comes out of the pool!"
				acted = 1
				inventory.remove("old book")
				encounter = 1
				encounter_time = 0
				boss = 1
		elif "key" in words and x == 2 and y == 8 and z == 0 and "trapdoor" in triggers and "trapdoor_lock" not in triggers:
			dothing = "You use the key to open the lock."
			triggers.append("trapdoor_lock")
			acted = 1
		elif "charm" in words and "mysterious charm" in inventory:
			os.system('clear')
			inventory.remove("mysterious charm")
			dothing = "You begin to feel funny. You suddenly black out..."
			max_level = 10
			dothing = "You wake up and realize that the charm must have been the legendary \"Element of Harmony\".\nIt grants whoever uses it a beautiful voice!"
			acted = 1
		elif "portal" in words and "boss1" in triggers and max_level != 5:
			os.system('clear')
			acted = 1 #GAHGAHGAHGAHAGHAGAHHGAHGAHGAHGAHGAHGAHGAHGAHGAHGAH
			dothing = "You won't be able to come back here after you go through. Are you still sure you want to proceed?"
			portal_p = raw_input('> ')
			words = portal_p.split(' ')
			if list(set(yes_words) & set(words)):
				dothing = "Okie dokie, let's gooooooo..."
				acted = 1
				x = 0
				y = 0
				z = 10
	if list(set(take_words) & set(words)):
		if "torch" in words and x == 0 and y == 0 and z == 0 and "torch" not in triggers:
			inventory.append("torch")
			triggers.append("torch")
			dothing = "You pick up the torch and are able to see better."
			acted = 1
		elif "branch" in words and x == 2 and y == 1 and z == 0 and weapon < 1:
			inventory.append("branch")
			triggers.append("branch")
			weapon = 1
			var_set = 1
			dothing = "You pick up the branch and hold it like a spear."
			acted = 1
		elif "letter" in words and x == 2 and y == 6 and z == 0 and "letter" not in triggers:
			inventory.append("letter")
			triggers.append("letter")
			dothing = "You take the letter out of the mailbox."
			acted = 1
			print letter
		elif "dagger" in words and x == 3 and y == 7 and z == 1 and weapon < 2:
			inventory.append("dagger")
			weapon = 2
			var_set = 1
			dothing = "You wield the dagger and feel stronger."
			acted = 1
			inventory.remove("branch")
		elif "armor" in words and x == 3 and y == 7 and z == 1 and armor < 1:
			inventory.append("leather armor")
			armor = 1
			dothing = "You put on the leather armor."
			acted = 1
		elif "lamp" in words and x == 3 and y == 7 and z == 1 and "lamp" not in inventory:
			inventory.append("lamp")
			triggers.append("lamp")
			inventory.remove("torch")
			dothing = "Your torch happens to burn out as you pick up the lamp."
			acted = 1
		elif "armor" in words and x == -1 and y == 15 and z == 1 and armor <= 1:
			inventory.append("Chainmail armor")
			armor = 2
			dothing = "You put on the chainmail armor."
			acted = 1
			inventory.remove("leather armor")
		elif "crowbar" in words and x == 9 and y == 9 and z == 1 and "crowbar" not in inventory:
			inventory.append("crowbar")
			dothing = "You pick up the crowbar."
			acted = 1
		elif "key" in words and x == 2 and y == 8 and z == 0 and "key" not in inventory and "trapdoor" in triggers:
			inventory.append("key")
			dothing = "You pick up a mysterious key."
			acted = 1
		elif "book" in words and x == 2 and y == 8 and z == 0 and "old book" not in inventory and "trapdoor_lock" in triggers and "boss1" not in triggers:
			inventory.append("old book")
			triggers.append("old_book")
			dothing = "You take the mysterious book and wonder what it could be."
			acted = 1
		elif "charm" in words and x == 5 and y == 2 and z == 0 and "boss1" in triggers and "charm" not in triggers:
			inventory.append("mysterious charm")
			triggers.append("charm")
			dothing = "You pick up the strange charm. It is in the shape of a purple diamond."
			acted = 1
		elif list(set(spellbook_words) & set(words)):
			if x == 3 and y == 13 and z == 1 and "spellbook- Fire" not in inventory and "firebolt" not in spells:
				inventory.append("spellbook- Fire")
				dothing = "You pick up the mysterious spellbook."
			acted = 1
		else:
			dothing = "You don't see that here."
		screen1 = Text(Point(w.getWidth()/2, w.getHeight()/2), dothing)
	if act == "num":
		print x
		print y
		print z
		if encounter >= 1:
			encounter_time += 1
	elif act == "debug.addt":
		triggers.append(raw_input(''))
	elif act == "clear":
		if encounter >= 1:
			encounter_time += 1
		os.system('clear')
	elif act == "inv":
		i = 0
		try:
			for i in range(len(inventory)):
				screen2.undraw()
				screen2 = Text(Point(invs.getWidth()/2, invs.getWidth()/2), '\n'.join(inventory))
				screen2.setText('\n'.join(inventory))
				screen2.draw(invs)
		except:
			invs = GraphWin('inventory', 100, 300)
			for i in range(len(inventory)):
				screen2 = Text(Point(invs.getWidth()/2, invs.getWidth()/2), '\n'.join(inventory))
				screen2.draw(invs)
		#print '\n'.join(inventory)
	  	if encounter >= 1:
			encounter_time += 1
		elif act == "restart":
			while wait == 0:
				print color['red'] + "Are you sure you want to delete your save and restart all progress?" + color['off']
				response = raw_input('(y/n) >')
				if response == "y":
					print "Okay, deleting your save and restarting..."
					os.system('rm game_save.dat')
					os.system('touch game_save.dat')
					quit()
					os.system('python kazooquest.py')
					wait = 1
				elif response == "n":
					wait = 1
	elif act == "look":
	  	skip = 0
	  	if encounter >= 1:
			encounter_time += 1
	elif act == "skills":
		print '\n'.join(skills_thing)
		skill_act = raw_input('What skill do you want to use?\n> ')
		if act == "sneak" and "Stealth" in skills and skill_energy >= 5:
			encounter_time += 6
			skill_energy -= 5
	#Debugging commands
	elif act == "debug.update":
	  update()
	elif act == "debug.triggers":
	  print triggers
	elif act == "debug.evolveitem":
	  inventory.append("mysterious charm")
	elif act == "debug.sp":
	  print spells
	  print spells_thing
	  print skills
	  print skills_thing
	elif act == "debug.xp":
	  exp += 100
	elif act == "save":
	  with open('game_save.dat', 'wb') as f:
	    pickle.dump([hp, damage, defe, mana, inventory, spells, spells_thing, skills, max_hp, max_mana, x, y, z, triggers, kills, points, armor, weapon, encounter, encounter_time,  enemy_type, level, max_level, firebolt_level, frost_level, poison_level, lifesteal_level, heal_level, game_diff, roominfo, exp, exp_limit], f, protocol = 2)
	  f.close()
	  screen1 = Text(Point(w.getWidth()/2, w.getHeight()/6), "Game saved!")
	  screen1.setTextColor('cyan4')
	  screen1.draw(w)
	  if encounter >= 1:
	    encounter_time += 1
	elif act == "load":
	  with open('game_save.dat', 'rb') as f:
	    hp, damage, defe, mana, inventory, spells, spells_thing, skills, max_hp, max_mana, x, y, z, triggers, kills, points, armor, weapon, encounter, encounter_time,  enemy_type, level, max_level, firebolt_level, frost_level, poison_level, lifesteal_level, heal_level, game_diff, roominfo, exp, exp_limit = pickle.load(f)
	  f.close()
	  os.system('clear')
	  print color['cyan'] + "Game loaded!" + color['off']
	  print roominfo
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
	  skills = []
	  skills_thing = []
	  spells.append("firebolt")
	  spells.append("frost")
	  spells.append("poison")
	  spells.append("life steal")
	  spells.append("heal")
	  spells_thing.append("%s. Firebolt" % str(len(spells_thing) + 1))
	  spells_thing.append(color['darkblue'] + "%s. Frost" % str(len(spells_thing) + 1) + color['off'])
	  spells_thing.append(color['darkgreen'] + "%s. Poison" % str(len(spells_thing) + 1) + color['off'])
	  spells_thing.append(color['darkmagenta'] + "%s. Life Steal" % str(len(spells_thing) + 1) + color['off'])
	  spells_thing.append(color['magenta'] + "%s. Heal" % str(len(spells_thing) + 1) + color['off'])
	  skills.append("stealth")
	  skills_thing.append("%s. Stealth" % str(len(skills_thing) + 1))
	  skills.append("rage")
	  skills_thing.append("%s. Rage" % str(len(skills_thing) + 1))
	  var_set = 1
	#Debugging command
	elif act == "etime":
	  print encounter
	  print encounter_time
	  if encounter >= 1:
	    encounter_time += 1
	elif act == "spells":
	  print '\n'.join(spells_thing)
	  if encounter >= 1:
	    encounter_time += 1
	elif act == "heal":
	#Reminder to redo this- needs to be reworked
	  hp_heal = max_hp / 2
	  mana_heal = max_mana / 4 * random.randint(1, 2)
	  skill_heal = max_energy / 4 * random.randint(0, 2)
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
	  print "Damage: %r\nHealth: %r\nDefense: %r\nMana: %r\nLevel: %r/%r\nExp: %r/%r" % (damage, hp, defe, mana, level, max_level, exp, exp_limit)
	  encounter_time += 1
	elif act == "credits":
	  print "This game was written by Matthew Knecht in Python 2.7. It is currently in %r. The story of the game revolves around a player who has lost his memory and has to find his Golden Kazoo. The game doesn't have much content- but that will be resolved shortly. Thanks for playing!" % current_version
	elif act == "help":
	  print color['darkwhite']+ " -help (Shows this screen) \n -look (Shows you your surroundings) \n -heal (Heals you but draws monsters nearby) \n -use (Uses an item or object) \n -take (Takes an item)\n -n, s, e, w, u, d (Moves you in its respective direction)\n -clear (Clears the screen)\n -stats (Shows your your stats)" + color['off']
	  if encounter >= 1:
		encounter_time += 1
	else:
		pass #Will eventually fix this
	if x == 0 and y == 0 and z == 0 and "torch" not in triggers:
		encounter = 0
		roominfo = "You have found yourself in a dimly lit cave. You have no memory of how you got here or who you are. There is a path to the north and south. You see a torch on the ground."
	elif x == 0 and y == 0 and z == 0 and "torch" in triggers:
		roominfo = "Your torch lights up the walls of the cave. There is a path to the north and south."
	elif x == 0 and y == 1 and z == 0 and "torch" not in triggers:
		roominfo = "You start walking to the north yet find that the mysterious light is dimming rapidly. You decide to turn back until you find a light source."
		y -= 1
	elif x == 0 and y == 1 and z == 0 and "torch" in triggers:
		roominfo = "You begin to walk to the north, allowing your torch to light the way. As you walk you begin to hear a slight howl of wind from ahead of you. There is a path to the east."
	elif x == 1 and y == 1 and z == 0 and "outside1" not in triggers:
		roominfo = "You walk to the east and begin to feel the breeze picking up. You look ahead of you and see outside a little bit ahead."
		triggers.append("outside1")
	elif x == 1 and y == 1 and z == 0 and "outside1" in triggers:
		roominfo = "The exit to the cave is to the east."
	elif x == 2 and y == 1 and z == 0 and "branch" not in triggers:
		encounter = 0
		roominfo = "You reach the end of the tunnel and feel the heat of the sun around you.\nThe trees tower over you and you hear the sound of rushing water to the north. You see a good sized tree branch with a pointed end."
		enemy_type = "wolf"
	elif x == 2 and y == 1 and z == 0 and "branch" in triggers:
		encounter = 0
		roominfo = "You reach the end of the tunnel and see a forest to the east. You hear the sound of rushing water to the north."
		enemy_type = "wolf"
	elif x == 2 and y == 2 and z == 0:
		encounter = 1
		enemy_type = "wolf"
		roominfo = "There is a swiftly flowing stream here. To the east is a path to the forest. You think you see a small cottage far to the north."
	elif x == 2 and y == 3 and z == 0:
		roominfo = "You keep walking around the side of the mountain. There is a cottage far to the north and a cave to the south. There is a forest to the east."
		enemy_type = "wolf"
	elif x == 2 and y == 4 and z == 0:
		roominfo = "The mountain path seems to be rougher here. You see that the stream flows from a grate in the mountain. There is a forest to the east, a cave to the south, and a cottage to the north."
		enemy_type = "wolf"
	elif x == 2 and y == 5 and z == 0:
		roominfo = "You are nearing the cottage. There is a cave far to the south."
#Forest area follows
#To prevent a lot of mistakes here, I'm spliting the forest into 3 rows(at least for now)
#Row 1
	elif x == 3 and y == 1 and z == 0:
		encounter = 0
		roominfo = "The sunlight is slightly filtered by the trees above. There is a cave to the west."
	elif x == 4 and y == 1 and z == 0:
		encounter = 1
		enemy_type = "elf"
		roominfo = "The trees here are denser than around the edge of the forest."
	elif x == 5 and y == 1 and z == 0:
		roominfo = "The forest seems to only get darker further to the east. There is a clearing to the north."
	elif x == 6 and y == 1 and z == 0:
		roominfo = "The trees here are wat too thick to even get by, you turn around and go back."
		x -= 1
#Row 2
	elif x == 3 and y == 2 and z == 0:
		encounter = 0
		roominfo = "The sunlight is slightly filtered by the trees above. There is a stream to the west."
	elif x == 4 and y == 2 and z == 0:
		encounter = 1
		enemy_type = "elf"
		roominfo = "There appears to be an opening in the trees to the east."
	elif x == 5 and y == 2 and z == 0 and "boss1" not in triggers:
		if boss == 0:
			encounter = 0
		if boss == 1:
			encounter = 1
		enemy_type = "slime"
		roominfo = "There is a mysterious pool of water in the center of this clearing. Various flowers surround it in a circle.\nThere are runes on the ground next to the pool that say \"Ye who seeks power, stand here and read from the book which you find set in stone.\""
	elif x == 5 and y == 2 and z == 0 and "boss1" in triggers and "charm" not in triggers and evolve_count != 1:
		encounter = 0
		roominfo = "The pool of water appears to be glowing a slight orange. The flowers around the pool are also glowing a faint orange.\nYou see a purple charm where the slime was killed."
	elif x == 5 and y == 2 and z == 0 and "mysterious charm" in inventory:
		encounter = 0
		roominfo = "The pool of water appears to be glowing a slight orange. The flowers around the pool are also glowing a faint orange.\nThe strange charm you have is also glowing orange..."
	elif x == 5 and y == 2 and z == 0 and max_level != 5:
		encounter = 0
		roominfo = "The pool of water appears to have opened into a strange portal-ish thing.  You know you won't be able to get back if you go in..."
	elif x == 6 and y == 2 and z == 0:
		encounter = 1
		roominfo = "The trees are too dense for you to go east.  There is a clearing to the west."
#Row 3
	elif x == 3 and y == 3 and z == 0:
		enemy_type = "elf"
		encounter = 0
		roominfo = "The sunlight is slightly filtered by the trees above. There is a mountain to the west."
	elif x == 4 and y == 3 and z == 0:
		encounter = 1
		enemy_type = "elf"
		roominfo = "The trees here are denser than around the edge of the forest."
	elif x == 5 and y == 3 and z == 0:
		enemy_type = "elf"
		encounter = 1
		roominfo = "There is a clearing in the trees to the south."
	elif x == 6 and y == 3 and z == 0:
		enemy_type = "elf"
		encounter = 1
		roominfo = "The trees here block your way to the east and north."
#House area follows
	elif x == 2 and y == 6 and z == 0 and "letter" not in triggers:
		encounter = 1
		roominfo = "You stand in front of the mailbox of the cottage. There appears to be a letter in the mailbox. There is a cave far to the south."
	elif x == 2 and y == 6 and z == 0 and "letter" in triggers:
		encounter = 1
		roominfo = "You stand in front of the mailbox of the cottage. There is a cave far to the south."
		enemy_type = "wolf"
	elif x == 2 and y == 7 and z == 0 and "lights" not in triggers:
		encounter = 0
		roominfo = "The inside of the house is cold and dark. You have an unexplainable feeling of gloom. There are rooms to the east and the north."
	elif x == 2 and y == 7 and z == 0 and "lights" in triggers:
		enemy_type = "wolf"
		encounter = 0
		roominfo = "There is a bright red stain on the rug in front of the door. You have an unexplainable feeling of dread.\nThe kitchen is to the east and the living room is to the north."
	elif x == 3 and y == 7 and z == 0 and "lights" not in triggers:
		roominfo = "The room is lit up slightly by a window. You can see a switch by the window. The doorway is to the west."
	elif x == 2 and y == 8 and z == 0 and "lights" not in triggers:
		roominfo = "It's way too dark in here for you to see anything. The doorway is to the south."
	elif x == 2 and y == 8 and z == 0 and "lights" in triggers and "trapdoor" not in triggers:
		roominfo = "The living room is completely barren. There appears to be a locked trapdoor in the floor. The doorway is to the south."
	elif x == 2 and y == 8 and z == 0 and "lights" in triggers and "trapdoor" in triggers and "key" not in inventory and "trapdoor_lock" not in triggers:
		roominfo = "The trapdoor in this room has a key inside. The doorway is to the south."
	elif x == 2 and y == 8 and z == 0 and "trapdoor" in triggers and "key" in inventory and "trapdoor_lock" not in triggers:
		roominfo = "The trapdoor in the center of the room is empty except for a little notch. The doorway is to the south."
	elif x == 2 and y == 8 and z == 0 and "trapdoor_lock" in triggers and "old_book" not in triggers:
		roominfo = "There is an old book layered with dust in the safe in the trapdoor."
	elif x == 2 and y == 8 and z == 0 and "old_book" in triggers:
		roominfo = "This room is completely empty."
#Variable "z" is an inverted height (+1 would be down and -1 would be up)
	elif x == 3 and y == 7 and z == 0 and z == 1 and "lights" not in triggers:
		roominfo = "Your torch isn't enough to let you see down the stairs."
		z += 1
	elif x == 3 and y == 7 and z == 0 and "lights" in triggers:
		roominfo = "The light shows that there are stairs going down. The entrance is to the west."
#I know there is someway to make this more efficient, but oh well I don't have time for thinking right now :^ )
	elif x == 3 and y == 7 and z == 1 and "lights" in triggers and "lamp" not in inventory and armor < 1 and weapon < 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north. There is a lamp on the ground.\nThere is a dagger on the ground. There is leather armor on the ground."
#Player has nothing ^
	elif x == 3 and y == 7 and z == 1 and "lamp" in inventory and armor < 1 and weapon < 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north. There is a dagger on the ground. There is leather armor on the ground."
#Player has lamp ^
	elif x == 3 and y == 7 and z == 1 and "lamp" in inventory and armor >= 1 and weapon < 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north. There is a dagger on the ground."
#Player has lamp and armor ^
	elif x == 3 and y == 7 and z == 1 and "lamp" in inventory and armor < 1 and weapon >= 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north. There is leather armor on the ground."
#Player has lamp and dagger ^
	elif x == 3 and y == 7 and z == 1 and "lamp" in inventory and armor >= 1 and weapon >= 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north."
#Player has all items ^
	elif x == 3 and y == 7 and z == 1 and "lamp" not in inventory and armor >= 1 and weapon < 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north. There is a lamp on the ground. There is a dagger on the ground."
#Player has leather armor ^
	elif x == 3 and y == 7 and z == 1 and "lamp" not in inventory and armor >= 1 and weapon >= 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north. There is a lamp on the ground."
#Player has dagger and armor ^
	elif x == 3 and y == 7 and z == 1 and "lamp" not in inventory and armor < 1 and weapon < 2:
		roominfo = "You reach the bottom of the stairs and see a path leading to the north. There is a lamp on the ground. There is leather armor on the ground."
#Player has dagger ^
	elif x == 3 and y == 8 and z == 1:
		encounter = 0
		enemy_type = "orc"
		roominfo = "As you walk, an ominous presence overwhelms you."
	elif x == 3 and y == 9 and z == 1:
		encounter = 1
		enemy_type = "orc"
		roominfo = "There are paths to the north, east, and west."
	elif x == 2 and y == 9 and z == 1:
		roominfo = "You hear dripping water in the distance. There is a path to the west"
	elif x == 1 and y == 9 and z == 1:
		roominfo = "The strange dripping sound seems a short distance away. The path continues to the north."
	elif x == 1 and y == 10 and z == 1:
		roominfo = "The dripping sound appears to be just around the corner up ahead. You hear a deep moaning sound. The path continues to the west."
	elif x == 0 and y == 10 and z == 1:
		roominfo = "The dripping sound is very audible now and the moaning sound seems to be rapidly increasing in volume. The path continues to the west."
	elif x == -1 and y == 10 and z == 1:
		enemy_type = "wraith"
		roominfo = "You notice a rapidly dripping spot on the ceiling. You can hear the moaning sound ahead. The path continues to the north."
	elif x == -1 and y == 11 and z == 1:
		roominfo = "As you look north, you can't see the end of the passage. The path continues to the north."
	elif x == -1 and y == 12 and z == 1:
		roominfo = "Something seems off around you..."
	elif x == -1 and y == 13 and z == 1:
		roominfo = "You think you can see a light to the north."
	elif x == -1 and y == 14 and z == 1:
		roominfo = "The light to the north grows in brightness."
	elif x == -1 and y == 15 and z == 1 and armor <= 1:
		roominfo = "You almost trip on the chainmail armor that lays on the ground."
	elif x == -1 and y == 15 and z == 1 and armor >= 2:
		roominfo = "The silence here is intense. The light ahead seems to be getting brighter."
	elif x == -1 and y == 16 and z == 1:
		roominfo = "The light to the north appears to be a wall of solid light."
	elif x == -1 and y == 17 and z == 1:
		roominfo = "You feel yourself being whisped away to somewhere else."
		x = 3
		y = 8
		z = 1
#East path split
	elif x == 4 and y == 9 and z == 1:
		roominfo = "There is a slight clanking noise in the distance. There is a path that stretches far ahead of you."
	elif x == 5 and y == 9 and z == 1:
		enemy_type = "dwarf"
		roominfo = "You sense something small nearby."
	elif x == 6 and y == 9 and z == 1:
		roominfo = "You smell something foreign to you... Then again you don't really remember anything..."
	elif x == 7 and y == 9 and z == 1:
		roominfo = "This passage seems absurdly long..."
	elif x == 8 and y == 9 and z == 1:
		roominfo = "There seems to be something far ahead of you."
	elif x == 9 and y == 9 and z == 1 and "crowbar" not in inventory:
		roominfo = "There appears to be a crowbar on the ground."
	elif x == 9 and y == 9 and z == 1 and "crowbar" in inventory:
		roominfo = "The passageway a bit ahead appears to be very bright."
	elif x == 10 and y == 9 and z == 1:
		roominfo = "The wall in front of you seems to be made of solid light..."
	elif x == 11 and y == 9 and z == 1:
		roominfo = "You feel yourself being taken somewhere else..."
		x = 3
		y = 8
		z = 1
#North path split
	elif x == 3 and y == 10 and z == 1:
		roominfo = "All you see to the north is darkness."
	elif x == 3 and y == 11 and z == 1:
		roominfo = "..."
	elif x == 3 and y == 12 and z == 1 and "underground_door" not in triggers:
		roominfo = "There is suddenly a door in front of you. You can't open it with your hands."
	elif x == 3 and y == 12 and z == 1 and "underground_door" in triggers:
		roominfo = "The door is open."
	elif x == 3 and y == 13 and z == 1 and "underground_door" not in triggers:
		y -= 1
	elif x == 3 and y == 13 and z == 1 and "spellbook- Fire" not in inventory and "firebolt" not in spells:
		roominfo = "There is a book lying on the ground."
	elif x == 3 and y == 13 and z == 1 and "spellbook- Fire" in inventory:
		roominfo = "There is an empty room here."
	elif x == 3 and y == 13 and z == 1 and "firebolt" in spells:
		roominfo = "There is an empty room here."
#AREA 1 ENDS HERE
#AREA 2 STARTS HERE
	elif x == 0 and y == 0 and z == 10 and "area2" not in triggers:
		roominfo = "The area around you seems much drier than where you came from. You seem to be in a cave again.  The exit is to the north."
		triggers.append("area2")
	elif x == 0 and y == 0 and z == 10 and "area2" in triggers:
		roominfo = "You are in a cave. The exit is to the north."
	elif x == 0 and y == 1 and z == 10:
		roominfo = "The area around you seems vastly different from before, but something also seems familiar..."
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
	if acted == 1:
		acted = 0
		screen1.draw(w)
	if acted == 0:
		try:
			screen1.undraw()
		except:
			pass
		screen.setText(roominfo)
	if encounter != 0:
		encounter_time -= 1
	if var_set == 1:
		if weapon == 0:
			damage += 3
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
	if exp >= exp_limit and level != max_level:
		exp_extra = exp - exp_limit
		print color['blue'] + "Level up!" + color['off']
		exp = 0
		exp += exp_extra
#EXP limits are weird- needs to be reworked
		if level != max_level:
			if level == 1:
				exp_limit = 25
			elif level == 2:
				exp_limit = 50
			elif level == 3:
				exp_limit = 85
			elif level == 4:
				exp_limit = 125
			elif level == 5:
				exp_limit = 150
			elif level == 6 and max_level > 5:
				exp_limit = 180
			elif level == 7:
				exp_limit = 210
			elif level == 8:
				exp_limit = 245
			elif level == 9:
				exp_limit = 275
			elif level == 10:
				exp_limit = 325
		level += 1
#Levels OP, pls nurf?- needs to be reworked
		points += 10
		if level == 1:
			damage += 2
			max_hp += 5
			max_mana += 2
		elif level == 2:
			damage += 3
			max_hp += 5
			max_mana += 3
		elif level == 3:
			damage += 3
			max_hp += 8
			max_mana += 5
		elif level == 4:
			damage += 5
			max_hp += 10
			max_mana += 5
		elif level == 5:
			damage += 8
			max_hp += 10
			max_mana += 7
#Limits level until certain item is used, I think
		elif level == 6 and max_level > 5:
			damage += 10
			max_hp += 10
			max_mana += 8
		elif level == 7:
			damage += 10
			max_hp += 15
			max_mana += 9
		elif level == 8:
			damage += 10
			max_hp += 15
			max_mana += 10
		elif level >= 9:
			damage += 5
			max_hp += 5
			max_mana += 5
	stop = 1
	#prompt()
	screen3 = Rectangle(Point(900, 100), Point(1000, 200))
	screen3.draw(w)
	click()
	act = raw_input('> ')
	words = act.split(' ')
	stop = 0
	while encounter != 0 and encounter_time <= 0 and "dead" not in triggers:
		stop = 1
		while enemy_set != 1:
#Some enemies have too high/too low of stats- needs to be reworked
#Area 1 enemies
			if enemy_type == "wolf":
				enemy_hp = 15
				enemy_dam = random.randint(2, 4)
				min_dam = 2 - defe
				max_dam = 4 - defe
				enemy_dam_info = "%r to %r" % (min_dam, max_dam)
			elif enemy_type == "elf":
				enemy_hp = 20
				enemy_dam = random.randint(3, 5)
				min_dam = 3 - defe
				max_dam = 5 - defe
				enemy_dam_info = "%r to %r" % (min_dam, max_dam)
			elif enemy_type == "orc":
				enemy_hp = 25
				enemy_dam = random.randint(6, 8)
				min_dam = 6 - defe
				max_dam = 8 - defe
				enemy_dam_info = "%r to %r" % (min_dam, max_dam)
				enemy_dodge = 1
			elif enemy_type == "wraith":
				enemy_hp = 30
				enemy_dam = random.randint(7, 9)
				min_dam = 7 - defe
				max_dam = 9 - defe
				enemy_dam_info = "%r to %r" % (min_dam, max_dam)
				enemy_dodge = 3
			elif enemy_type == "dwarf":
				enemy_hp = 35
				enemy_dam = random.randint(7, 10)
				min_dam = 7 - defe
				max_dam = 10 - defe
				enemy_dam_info = "%r to %r" % (min_dam, max_dam)
				enemy_dodge = 1
			elif enemy_type == "slime":
				enemy_hp = 150
				enemy_dam = random.randint(10, 25)
				min_dam = 10 - defe
				max_dam = 25 - defe
				enemy_dam_info = "%r to %r" % (min_dam, max_dam)
				enemy_dodge = 0
#Area 2 enemies
			elif enemy_type == "vulture":
				enemy_hp = 40
				enemy_dam = random.randint(12, 15)
				min_dam = 12 - defe
				max_dam = 15 - defe
				enemy_dam_info = "%r to %r" % (min_dam, max_dam)
			elif enemy_type == "sand rat":
				enemy_hp = 35
				enemy_dam = random.randint(11, 14)
				min_dam = 11 - defe
				max_dam = 14 - defe
				enemy_dam_info = "%r to %r" % (min_dam, max_dam)
			elif enemy_type == "spirit":
				enemy_hp = 40
				enemy_dam = random.randint(13, 16)
				min_dam = 8 - defe
				max_dam = 11 - defe
				enemy_dam_info = "%r to %r" % (min_dam, max_dam)
				enemy_dodge = 0
			elif enemy_type == "golem":
				enemy_hp = 400
				enemy_dam = random.randint(25, 40)
				min_dam = 25 - defe
				max_dam = 40 - defe
				enemy_dam_info = "%r to %r" % (min_dam, max_dam)
			if min_dam < 0:
				min_dam = 0
			if max_dam < 0:
				max_dam = 0
#Remember to fix this silly grammar thingy here
			os.system('clear')
			enemy_info = color['red'] + "A "+enemy_type+" suddenly appears!." + color['off']
			print enemy_info
			enemy_set = 1
		#fight_act = prompt()
		fight_act = raw_input(color['blue'] + "What do you want to do?" + color['yellow'] + "\n1: Attack" + color['green'] + "\tHealth: %r" % hp + color['red'] + "\tEnemy Health: %r" % enemy_hp + color['yellow'] + "\n2: Magic" + color['green'] + "\tMana: %r" % mana + color['red'] + "\t\tEnemy Damage: %s" % enemy_dam_info + color['yellow'] + "\n3: Dodge\n4: Enemy Info\n5: Run Away\n" + color['off'])
		dodges = 0
		if fight_act == "1":
			enemy_hp = enemy_hp - damage
			os.system('clear')
			print color['green'] + "You dealt %d damage to the %s!" % (damage, enemy_type) + color['off']
		elif fight_act == "2":
			print "Available spells:\n" + '\n'.join(spells_thing)
			#prompt()
			magic_attack = raw_input('> ')
#Magic is(as usual) OP- needs to be reworked
			try:
				if magic_attack == str(spells.index('firebolt') + 1) and "firebolt" in spells and mana >= 5:
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
					os.system('clear')
					print color['red'] + "You dealt %r magic damage to the enemy and set it on fire!" % magic_dam + color['off']
			except ValueError:
				skip = 0
			try:
				if magic_attack == str(spells.index('frost') + 1) and "frost" in spells and mana >= 8:
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
					os.system('clear')
					print color['blue'] + "You dealt %r magic damage and froze the enemy!" % magic_dam + color['off']
			except ValueError:
				skip = 0
			try:
				if magic_attack == str(spells.index('poison') + 1) and "poison" in spells and mana >= 13:
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
					os.system('clear')
					print color['green'] + "You dealt %r magic damage and poisoned the enemy!" % magic_dam + color['off']
			except ValueError:
				skip = 0
			try:
				if magic_attack == str(spells.index("life steal") + 1) and "life steal" in spells and mana >= 20:
					if lifesteal_level == 0:
						drain_dam = random.randint(15, 30)
					elif lifesteal_level == 1:
						drain_dam = random.randint(18, 33)
					elif lifesteal_level == 2:
						drain_dam = random.randint(20, 35)
					elif lifesteal_level == 3:
						drain_dam = random.randint(23, 38)
					elif lifesteal_level == 4:
						drain_dam = random.randint(25, 40)
					elif lifesteal_level == 5:
						drain_dam = random.randint(28, 43)
					mana -= 20
					enemy_hp -= drain_dam
					hp += drain_dam
					os.system('clear')
					print color['green'] + "You stole %r health from the %r!" % (drain_dam, enemy_type) + color['off']
			except ValueError:
				skip = 0
			try:
				if magic_attack == str(spells.index('heal') + 1) and "heal" in spells and mana >= 8:
					mana -= 8
					hp_heal = random.randint(10, 30)
					hp += hp_heal
					os.system('clear')
					print "You healed %r health!" % hp_heal
			except ValueError:
				skip = 0
			try:
				if magic_attack == str(spells.index('stun') + 1) and "stun" in spells and mana >= 5:
					if stun_level == 0:
						stun_time = 5
					mana -= 5
					enemy_debuffs.append("Stunned")
					enemy_debuff_timer = stun_time
					print color['yellow'] + "You stunned the enemy!" + color['off']
			except ValueError:
				skip = 0
		elif fight_act == "3":
			dodge_act = random.randint(0, 100)
			if dodge_act <= 25:
				os.system('clear')
				print color['green'] + "You dodged the attack!" + color['off']
				dodges = 1
			if dodge_act >= 75:
				parrypowa = damage * 2
				enemy_hp -= parrypowa
				print color['green'] + "You parried the attack and dealt %d damage!" % parrypowa  + color['off']
				dodges = 1
		elif fight_act == "4":
			os.system('clear')
			print color['darkgreen'] + "Enemy Health: %d\nEnemy Damage: %s" % (enemy_hp, enemy_dam_info) + color['off']
		elif fight_act == "5":
			run_success = random.randint(0, 3)
			if run_success == 1:
				enemy_set = 0
				encounter_time = random.randint(5, 7)
				enemy_hp = 0
				dodges = 0
				enemy_debuffs = []
				os.system('clear')
				print color['darkyellow'] + "You ran away!" + color['off']
		else:
			os.system('clear')
		if enemy_hp > 0 and dodges == 0 and fight_act != "4" and "Frozen" not in enemy_debuffs and "Stunned" not in enemy_debuffs and fight_act != "":
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
				if fight_act == "3":
					os.system('clear')
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
			if "Stunned" in enemy_debuffs:
				print "The enemy can't attack because it is stunned!"
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
			elif enemy_type == "slime":
				exp += 30
				points += 50
				triggers.append("boss1")
		if hp > max_hp:
			hp = max_hp
		if hp <= 0:
			death()
		stop = 0
	if hp > max_hp:
		hp = max_hp
	if mana > max_mana:
		mana = max_mana
	if skill_energy > max_energy:
		skill_energy = max_energy
	if hp <= 0:
		death()
