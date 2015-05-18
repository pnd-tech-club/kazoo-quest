def room():
    from kazooquest import x, y, z, triggers, inventory, roominfo, weapon, armor, words
    n_words = ['n', 'north']
    s_words = ['s', 'south']
    e_words = ['e', 'east']
    w_words = ['w', 'west']
    u_words = ['u', 'up']
    d_words = ['d', 'down']
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
        roominfo = "You reach the end of the tunnel and feel the heat of the sun around you. The trees tower over you and you hear the sound of rushing water to the north. You see a good sized tree branch with a pointed end."
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
        roominfo = "There is a mysterious pool of water in the center of this clearing. Various flowers surround it in a circle. There are runes on the ground next to the pool that say \"Ye who seeks power, stand here and read from the book which you find set in stone.\""
    elif x == 5 and y == 2 and z == 0 and "boss1" in triggers and "mysterious charm" not in inventory and max_level != 5:
        encounter = 0
        roominfo = "The pool of water appears to be glowing a slight orange. The flowers around the pool are also glowing a faint orange. You see a purple charm where the slime has killed."
    elif x == 5 and y == 2 and z == 0 and "mysterious charm" in inventory:
        encounter = 0
        roominfo = "The pool of water appears to be glowing a slight orange. The flowers around the pool are also glowing a faint orange. The strange charm you have is also glowing orange..."
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
        roominfo = "There is a bright red stain on the rug in front of the door. You have an unexplainable feeling of dread. The kitchen is to the east and the living room is to the north."
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
        roominfo = "You reach the bottom of the stairs and see a path leading to the north. There is a lamp on the ground. There is a dagger on the ground. There is leather armor on the ground."
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
    print roominfo
