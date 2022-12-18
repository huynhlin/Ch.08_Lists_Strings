'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import random
done = False
dead = False
defeated = False
breaktest = False
fighting = False
organizing = False
stair_unlocked = False
brewing_unlocked = False
library_unlocked = False
records_unlocked = False
first_time = False
brewing = False
breakflag = False
#  room format: name + directions + result of an inspection + description + boolean to see if its already inspected +
#  name of item to append it to the inventory + image
room_list = []
room = ["SPAWN ROOM", None, None, 1, None, "\nYou broke one of the vases and found a key!", "Just a room.", False,
        "Key"]  # 0
room_list.append(room)
fists = {
    "name": "Fists",
    "type": "Close Combat",
    "damage": 5,
}
room = ["HALL 1", 0, 2, 5, 3, "\nMissing posters are scattered about, it's a little ominous...",
        "\nSeems like just another hallway.", False]  # 1
room_list.append(room)
lance = {
    "name": "\033[0;31;22mLance of Longinus\033[0m",
    "type": "Hybrid",
    "damage": 25,
    "image":" \033[0;31;22mx x\033[0m\n"
            " \033[31;1;22mx x\033[0m\n"
            " \033[31;1;22mx x\033[0m\n"
            " \033[31;1;22mx x\033[0m\n"
            "\033[31;1;22mx   x\033[0m\n"
            "\033[31;1;22mx   x\033[0m\n"
            " \033[31;1;4mx x\033[0m\n"
            "  \033[31;1;4mx\033[0m\n"
            " \033[31;1;4mx x\033[0m\n"
            "  \033[31;1;22mx\033[0m\n"
            "  \033[31;1;22mx\033[0m\n"
            "  \033[31;1;22mx\033[0m\n"
            "  \033[31;1;22mx\033[0m\n"
            "  \033[31;1;22mx\033[0m\n"
            "  \033[31;1;22mx\033[0m\n"
            "  \033[31;1;22mx\033[0m\n"
            "  \033[31;1;22mx\033[0m\n"
            "  \033[31;1;22mx\033[0m\n"
            "  \033[31;1;22mx\033[0m\n"
            "  \033[31;1;22mx\033[0m\n"
            "  \033[31;1;22mx\033[0m\n"
            }
#  lance = [25, "Close-Combat"]
#  learned how to use dicts ezgg
room = ["CHAPEL", None, None, None, 1, "\nLeaned against the back wall of the Chapel is a giant spear, at least 10 "
                                       "meters tall. Despite its length it's light so you might be able to wield it.",
        "\nThe room looks like a Chapel, candles are lit but the pews are all empty.", False, lance]  # 2
room_list.append(room)
flower_weapon = {
    "name": "\033[1;35mFlowers\033[0m",
    "type": "Hybrid",
    "damage": 15,
    "image": ""
}
room = ["GARDEN", None, 1, None, 4, "\nYou stole all the flowers!", "\nA nice garden, although a lack of maintenance "
                                                                    "seems to have caused weeds to start growing.",
        False, flower_weapon, "Spare Flowers"]  # 3
flower_types = ["\033[31;1;22mRose\033[0m", "\033[31;1;22mLily\033[0m", "\033[33mSunflower\033[0m",
                "\033[0;31mTulip\033[0m", "\033[0;35mHyacinth\033[0m", "\033[0;37mDaisy\033[0m",
                "\033[1;35mLilac\033[0m", "\033[1;34mOrchid\033[0m"]
overalls = {
    "name": "\033[32mGardener's Overalls\033[0m",
    "type": "Mid",
    "defense": 5,
    "image": ""
}
chainsaw = {
    "name": "\033[33mOrange Chainsaw\033[0m",
    "type": "Close Combat",
    "damage": 35,
    "image": ""
}
room_list.append(room)
room = ["SHED", None, 3, None, None, "\nYou found a pair of overalls!\nYou found an orange chainsaw!\n", "\nA shed with"
        " various tools.",
        False, overalls, chainsaw]  # 4

#  armor stat format: DEF, Type
room_list.append(room)
room = ["HALL 2", 1, None, 6, None, "\nAn altar with a book on it.", "\nA hallway.", False]  # 5
room_list.append(room)
room = ["HALL 3", 5, 8, 9, 7, "\nThe walls are plastered with missing person posters. Besides that, nothing catches "
                              "your eye.", "\nSeems like just another hallway.", False]  # 6
room_list.append(room)
room = ["APOTHECARY", None, 6, None, None, "\nYou took some herbs and fully healed!", "\nIt looks like the apothecary "
                                                                                      "is away right now; you wonder if"
                                                                                      " he'll come back soon.", False]  # 7
room_list.append(room)
room = ["SHOP", None, None, None, 6, "\nThere's a shopkeeper. He's old and has a long grey beard, but he seems "
                                     "friendly."]  # 8
room_list.append(room)
room = ["HALL 4", 6, None, 10, None, "\nThe walls are plastered with missing person posters. Besides that, nothing "
                                     "catches your eye.", "\nSeems like just another hallway.", False]  # 9
room_list.append(room)
room = ["STAIRWELL (FLOOR ONE)", 9, None, 11, None, "\nIt's a large descending staircase. It's made entirely of"
                                                    "concrete, it's a little ominous..", "It's a staircase.", False]  # 10
room_list.append(room)
room = ["STAIRWELL EXIT (FLOOR TWO)", 10, 16, 12, None, ""]  # 11
room_list.append(room)
room = ["BLACKSMITH", 11, 15, 13, None]  # 12
room_list.append(room)
room = ["RECORDS ROOM", 12, 14, None, None, "\nLORE"]  # 13
room_list.append(room)
room = ["GYM", 15, 19, None, 13]  # 14
room_list.append(room)
room = ["HALL 5", 16, 18, 14, 12]  # 15
room_list.append(room)
room = ["DWELLING ONE", None, 17, 15, 11]  # 16
room_list.append(room)
room = ["DWELLING TWO", None, 20, 18, 16]  # 17
room_list.append(room)
room = ["HALL 6", 17, 23, 19, 15]  # 18
room_list.append(room)
room = ["ARMORY", 9, 11, None, 25]  # 19
room_list.append(room)
room = ["STAIRWELL TO COLOSSEUM", 21, None, 10, 24]  # 20
room_list.append(room)
room = ["COLOSSEUM", 22, None, 20, None]  # 21
room_list.append(room)
room = ["VAULT", None, None, 21, None]  # 22
room_list.append(room)
room = ["LIBRARY", 20, 31, 24, 18, "\nLORE"]  # 23
room_list.append(room)
room = ["HALL 7", 23, None, 25, 19]  # 24
room_list.append(room)
room = ["HALL 8", 24, None, 26, None]  # 25
room_list.append(room)
room = ["HALL 9", 25, None, 27, None]  # 26
room_list.append(room)
room = ["HALL 10", 26, 29, None, 28]  # 27
room_list.append(room)
room = ["BREWERY", None, 27, None, None, "\nYou took some of the alcohol, it might prove useful for favors.",
                                         "\nA brewery of some sorts, alcohol and unmarked glass bottles with vibrant "
                                         "substances adorn the shelves.", False, "Bottle of Whiskey", False]  # 28
room_list.append(room)
room = ["HALL 11", None, 30, None, 27]  # 29
room_list.append(room)
room = ["MAZE", None, None, None, 29]  # 30
room_list.append(room)
room = ["THRONE ROOM", None, None, None, 23]  # 31
room_list.append(room)


current_room = room_list[0]
next_room = room_list[0]
#  room config done
inventory = []
weapons = []
armor = []
misc_items = []
equipped = [fists, "", "", ""]
gold = 0
current_health = 100
base_health = 100
base_attack = 10
weapon_attack = 0
bonus_attack = 0
base_defense = 10
armor_defense = 0
bonus_defense = 0
stats = [current_health, base_health, base_attack + weapon_attack + bonus_attack, base_defense + armor_defense +
         bonus_defense, gold]
save_data = []
#  equipped order = weapon, top armor, middle armor, bottom armor


def died(gold_lost):
    global current_room, stats, inventory, weapons, armor, equipped, stair_unlocked, brewing_unlocked, records_unlocked
    global first_time, library_unlocked, dead, gold, breakflag, current_health
    dead = False
    try:
        current_room = save_data[0]
        stats = save_data[1]
        inventory = save_data[2]
        weapons = save_data[3]
        armor = save_data[4]
        equipped = save_data[5]
        stair_unlocked = save_data[6]
        brewing_unlocked = save_data[7]
        records_unlocked = save_data[8]
        first_time = save_data[9]
        library_unlocked = save_data[10]
        current_health = save_data[11]
        if gold > 0:
            gold = gold - gold_lost
            print("\nYou lost \033[1;33m{}\033[0m gold!")
        print("You will now be returned to your last save point.")
        breakflag = True
    except IndexError:
        print("\nYou didn't save your data so you'll have to restart the game. Try utilizing a save room next time!")
        exit()


def weapon_inventory_adjust(amount):
    global organizing
    try:
        equipped[0] = weapons[amount]  # sets equipped to selected
        organizing = False
        print("\nYou have equipped the {}.".format(equipped[0]["name"]))
    except IndexError:
        print("\nYou have no weapons to equip!")


def armor_inventory_adjust(amount):
    global organizing, armor_id, armor
    try:
        equipped[armor_id] = armor[amount]  # sets equipped to selected
        organizing = False
        print("\nYou have equipped the {}.".format(armor[amount]["name"]))
    except IndexError:
        print("")


# monster stats lay out: name, health, attack, enemy type, attack line, gold dropped,
# image, low health image, and if it is negotiable

# being on floor 2 will increase monster difficulty and add a new, strong creature
# which also has a unique debuff attack
floor = room_list.index(current_room)
if floor > 10:
    floor_multiplier = 1.5
else:
    floor_multiplier = 1
zombie = {
    "name": "Zombie",
    "health": 50 * floor_multiplier,
    "attack": 10 * floor_multiplier,
    "type": "Close Combat",
    "line": "\nThe zombie clawed at you!",
    "gold": 5,
    "image": "",
    "low_health_image": "",
    "negotiable": True
}
bat = {
    "name": "Bat",
    "health": 25 * floor_multiplier,
    "attack": 15 * floor_multiplier,
    "type": "Ranged",
    "line": "\nThe bat rushed you!",
    "gold": 8,
    "image": "",
    "low_health_image": "",
    "negotiable": False
}
dino = {
    "name": "Cave Dinosaur",
    "health": 100 * floor_multiplier,
    "attack": 20 * floor_multiplier,
    "type": "Close Combat",
    "line": "\nThe dinosaur bit you!",
    "gold": 10,
    "image":"\n            #############"
            "\n           ##  ###########"
            "\n           ###############"
            "\n           ###############"
            "\n           ###############"
            "\n           #######"
            "\n           ###########"
            "\n#         ######"
            "\n#       ########"
            "\n##    ##########"
            "\n###  #############"
            "\n################ #"
            "\n################"
            "\n #############"
            "\n  ############"
            "\n   ##########"
            "\n    ########"
            "\n     ### ###"
            "\n     ##   ##"
            "\n     #    ##"
            "\n     ##   ###",
    "low_health_image": "",
    "negotiable": False
}
abyssal_being = {
    "name": "Abyssal Being",
    "health": 75,
    "attack": 25,
    "type": "Close Combat",
    "line": "\nThe abyssal being attacked you! You can feel the void eating away at your body.",
    "gold": 20,
    "image": "a",
    "low_health_image": "a",
    "negotiable": False,
    "secondary_attack": "Taunt",
    "debuff": "Defense Shred"
}

monsters = [zombie, bat, dino]


def damage_taken():
    global current_health
    damage_reduction = int(round(stats[3] * 0.10))
    enemy_damage = random.randint(monster["attack"] - 3, monster["attack"] + 3) - damage_reduction
    current_health -= enemy_damage
    print(monster["line"])
    print("Your armor protected you from {} damage!".format(damage_reduction))
    print("\nIt did {} damage to you!".format(enemy_damage))

def win_check():  # checks if monster dead
    global monster_health, fighting, in_battle, defeated, breakcheck
    if monster_health < 1:
        if debuffed:
            stats[2] += def_decrease
        print("\nYou defeated the {}!".format(monster["name"]))
        gained_gold = random.randint(monster["gold"] - 3, monster["gold"] + 3)
        print("You got \033[1;33m{}\033[0m gold from it!".format(gained_gold))
        gold += gained_gold
        fighting = False
        in_battle = False
        defeated = True
        if floor > 10:
            unique = monsters.index(abyssal_being)
            monsters.pop(unique)
        breakcheck = True


def death_check():  # checks if user dead
    global debuffed, def_decrease, fighting, dead, in_battle, breakcheck
    if current_health < 1:
        print("\nYou died!")
        if debuffed:
            stats[2] += def_decrease
        fighting = False
        dead = True
        in_battle = False
        gold_lost = random.randint(int(round((gold / 5) - 10)), int(round((gold / 5) + 10)))
        died(gold_lost)
        breakcheck = True


def fight(monster):
    global floor_multiplier, fighting, dead, weapon_attack, current_health, defeated, in_battle, gold, breakcheck
    in_battle = True
    stun = False
    debuffed = False
    defeated = False
    monster_health = monster["health"]
    print("\nWhile wandering around, a(n) {} attacked you!".format(monster["name"]))
    print(monster["image"])
    while in_battle:
        # stat check to update in case swapped weapon mid fight or something
        stats = [current_health, base_health, base_attack + weapon_attack + bonus_attack, base_defense + armor_defense +
                 bonus_defense, gold]
        death_check()
        if breakcheck == True:
            breakcheck = False
            break
        win_check()
        if breakcheck == True:
            breakcheck = False
            break
        print("\nThe enemy has {} /".format(monster_health), "{} HP!".format(monster["health"]))
        print("You have {} /".format(current_health), "{} HP!".format(base_health))
        print("\n1) ATTACK")
        print("2) ACT")
        print("3) SWITCH WEAPON")
        user_turn = int(input("\nWhat will you do?"))
        if user_turn == 1:
            if equipped[0]["type"] != "Hybrid":
                if equipped[0]["type"] == monster["type"]:
                    if equipped[0] == flower_weapon:
                        print("\nYou threw a {} and a".format(random.choice(flower_types)),
                              "{} at the".format(random.choice(flower_types)), "{}!".format(monster["name"]))
                    else:
                        print("\nYou attacked the enemy with the {}!".format(equipped[0]["name"]))
                    damage = random.randint(stats[2]-3, stats[2]+3)
                    monster_health -= damage
                    print("It did {} damage!".format(damage))
                else:
                    print("\nYou cannot damage this enemy with your current weapon!")
            else:
                if equipped[0] == flower_weapon:
                    print("\nYou threw a {} and a".format(random.choice(flower_types)),
                          "{} at the".format(random.choice(flower_types)), "{}!".format(monster["name"]))
                else:
                    print("\nYou attacked the enemy with the {}!".format(equipped[0]["name"]))
                damage = random.randint(stats[2] - 3, stats[2] + 3)
                monster_health -= damage
                print("It did {} damage!".format(damage))
            if not stun:
                if monster == abyssal_being:
                    if not debuffed:
                        win_check()
                        if breakcheck == True:
                            breakcheck = False
                            break
                        print("\nThe abyssal being taunts you!")
                        print("Your DEFENSE decreased by 5!")
                        def_decrease = int(round(stats[3] * 0.15))
                        stats[2] -= def_decrease
                        debuffed = True
                    else:
                        win_check()
                        if breakcheck == True:
                            breakcheck = False
                            break
                        damage_taken()
                else:
                    win_check()
                    if breakcheck == True:
                        breakcheck = False
                        break
                    damage_taken()
            else:
                print("\nThe enemy was idle this turn!")
                stun = False
        elif user_turn == 2:
            print("\nYou tried to reason with the enemy!")
            if monster["negotiable"] == True:
                print("\nThe enemy seems to have faltered for a second, it will not attack next turn!")
                stun = True
            else:
                print("The enemy ignored you!")
                win_check()
                if breakcheck == True:
                    breakcheck = False
                    break
                damage_taken()
        elif user_turn == 3:
            counter = 1
            try:
                for i in range(len(weapons)):
                    print("{})".format(counter), "{}".format(weapons[counter - 1]["name"]))
                    counter += 1
            except TypeError:
                print("goddamnit")
            part = int(input("\nWhich weapon would you like to equip? 0 to cancel."))
            try:
                try:
                    weapon_inventory_adjust(part - 1)
                    weapon_attack = equipped[0]["damage"]
                except IndexError:
                    print("That is not a valid option, try again.")
            except TypeError:
                print("That is not a valid option, try again.")
        else:
            print("That is not a valid option, try again.")


instruct = input("Would you like instructions?")
if instruct.lower().strip() == "yes" or instruct == "y":
    print("\nIn this game, you find yourself in some sort of underground society and you must find your way out.\n"
          "You can find items that will aid you, however you must be wary of the creatures lurking within the "
          "depths.\nGood luck!\n")
username = input("\nWhat is your name?\n")
while not done:
    if breaktest:
        break
    current_room = next_room
    print("\nYou are in the {}.".format(current_room[0]))
    if current_health > 70:
        color = "\033[1;32m"
    elif current_health > 40:
        color = "\033[1;33m"
    else:
        color = "\033[1:31m"
    print(color, "   You have {} /".format(current_health), "{} health.\033[0m".format(base_health))
    room_index = room_list.index(current_room)
    if room_index == 5 or room_index == 0 or room_index == 7 or room_index == 12 or room_index == 29:
        immune = True
    else:
        immune = False
    if not immune:
        mob_generator = random.randint(1, 12)
        if mob_generator == 12:
            fighting = True
            monster = random.choice(monsters)
            while fighting:
                while not dead:
                    floor = room_list.index(current_room)
                    if floor > 10:
                        floor_multiplier = 1.5
                        monsters.append(abyssal_being)
                    else:
                        floor_multiplier = 1
                    fight(monster)
                    if defeated == True:
                        break
                    if breakflag == True:
                        breakflag = False
                        break

    turn = True
    while turn:
        if current_room[1] == None:
            ncolor = "\033[1:31m"
        else:
            ncolor = "\033[1;32m"
        if current_room[2] == None:
            ecolor = "\033[1:31m"
        else:
            ecolor = "\033[1;32m"
        if current_room[3] == None:
            scolor = "\033[1:31m"
        else:
            scolor = "\033[1;32m"
        if current_room[4] == None:
            wcolor = "\033[1:31m"
        else:
            wcolor = "\033[1;32m"
        print("\nWould you like to go", ncolor, "North,", ecolor, "East,", scolor, "South,", "\033[0m", "or", wcolor,
              "West? \033[0m", "\nNote that you can also inspect the current room by typing F or manage your inventory "
                               "by typing I.")
        action = input("")
        if current_room == "":
            print("SPECIFIC INTERACTIONS FOR THE SPEAKABLE NPC'S, BLACKSMITH, SHOP")
            # WHISKEY CAN LOWER PRICES + GIVE EXTRA LOOT/REP
        if current_room == room_list[21]:
            print("SPECIFIC APPEND FOR RANGED BOSS")
        if current_room == room_list[30]:
            print("SPECIFIC APPEND FOR EXEC")


        if action.lower().strip() == "n" or action.lower().strip() == "north":
            if current_room[1] != None:
                next_room = room_list[current_room[1]]
                break
            else:
                print("\nYou cannot go that way.")
        elif action.lower().strip() == "e" or action.lower().strip() == "east":
            try:
                next_room = room_list[current_room[2]]
                break
            except TypeError:
                print("\nYou cannot go that way.")
        elif action.lower().strip() == "s" or action.lower().strip() == "south":
            if current_room == room_list[10]:
                if stair_unlocked == False:
                    print("The door to the stairwell is locked.")
                    for obj in inventory:
                        if obj == "Key":
                            print("You used the key!")
                            stair_unlocked = True
                            next_room = room_list[current_room[3]]
                else:
                    next_room = room_list[current_room[3]]
                    break
            else:
                try:
                    next_room = room_list[current_room[3]]
                    break
                except TypeError:
                    print("\nYou cannot go that way.")
        elif action.lower().strip() == "w" or action.lower().strip() == "west":
            try:
                next_room = room_list[current_room[4]]
                break
            except TypeError:
                print("\nYou cannot go that way.")
        elif action.lower().strip() == "q" or action.lower().strip() == "q":
            done = True
            breaktest = True
            print("Thank you for playing.")
            break
        elif action.lower().strip() == "f":
            if current_room == room_list[0]:
                # misc item rooms
                if current_room[7] == False:
                    print(current_room[5])
                    try:
                        item = current_room[8]
                        inventory.append(item)
                        print("{} has been added to your inventory!".format(item))
                        current_room[7] = True
                    except TypeError:
                        print("")
                else:
                    print("\nNothing new since last inspection.")
            elif current_room == room_list[7]:
                print(current_room[5])
                print(current_room[6])
                current_health = base_health
            elif current_room == room_list[8]:
                # SHOP
                if first_time:
                    print("secret dialogue")
                    first_time = False
                if records_unlocked:
                    print("You can't look at him the same after what you read..")
                    print("shop options")
                    buy = int(input("What would you like to buy?"))
                else:
                    print(current_room[5])
                    print("shop options")
                    buy = int(input("What would you like to buy?"))
            elif current_room == room_list[2] or current_room == room_list[3] or current_room == room_list[19]:
                # weapon rooms
                if current_room[7] == False:
                    print(current_room[5])
                    current_room[7] = True
                    try:
                        weapon = current_room[8]
                        weapons.append(weapon)
                        print("{} has been added to your inventory!".format(weapon["name"]))
                        try:
                            print(weapon["image"])
                        except KeyError:
                            print("")
                        # if len(weapons) < 1:
                        #     equipped.pop(weapon)
                        #     print("'{}' has been automatically equipped.")
                    except TypeError:
                        print("")
                    if current_room == room_list[3]:
                        item = current_room[9]
                        inventory.append(item)
                        print("'{}' has been added to your inventory!".format(item))
                else:
                    print("\nNothing new since last inspection.")
            elif current_room == room_list[4]:
                # SPECIFIC SITUATION FOR ROOM THAT HAS ARMOR AND WEAPON
                if current_room[7] == False:
                    print(current_room[5])
                    weapon = current_room[9]
                    weapons.append(weapon)
                    print("{} has been added to your inventory!".format(weapon["name"]))
                    try:
                        print(weapon["image"])
                    except KeyError:
                        print("")
                    # if not weapons:
                    #     equipped[0] = weapon
                    #     print("'{}' has been automatically equipped.".format(weapon))
                    #     inventory.pop(weapon)
                    piece = current_room[8]
                    armor.append(piece)
                    print("{} has been added to your inventory!".format(piece["name"]))
                    try:
                        print(piece["image"])
                    except KeyError:
                        print("")
                    # if not armor:
                    #     equipped[1] = piece
                    #     print("'{}' has been automatically equipped.".format(piece))
                    #     inventory.pop(piece)
                    # tried to add an automatically equip feature but just couldnt get it to work :/
                    current_room[7] = True
                else:
                    print("\n Nothing new since last inspection.")
            elif current_room == room_list[16] or current_room == room_list[17]:
                # armor rooms
                if current_room[7] == False:
                    print(current_room[5])
                    piece = current_room[8]
                    armor.append(piece)
                    print("{} has been added to your inventory!".format(piece["name"]))
                    try:
                        print(piece["image"])
                    except KeyError:
                        print("")
                else:
                    print("Nothing new since last inspection.")
            elif current_room == room_list[13] or current_room == room_list[23]:
                print(current_room[5])
                if current_room == room_list[13]:
                    records_unlocked = True
                else:
                    library_unlocked = True
            elif current_room == room_list[28]:
                # BREWERY PUZZLE ROOM
                if current_room[7] == False:
                    print(current_room[5])
                    item = current_room[8]
                    inventory.append(item)
                    print("'{}' has been added to your inventory!".format(item))
                    current_room[7] = True
                if current_room[9] == False:
                    bottles = [5, 4, 3, 2, 1]
                    user_bottles = [1, 2, 3, 4, 5]
                    brewing = True
                    print("\nOn what seems like the main desk, there's a note along with 5 bottles.")
                    print("The note reads, 'Arrange the bottles in reverse order.'")
                    while brewing:
                        if user_bottles == bottles:
                            print("\nThat seems to have worked, the bottles disappeared and a pill has taken "
                                  "their place.")
                            print("You took the pill and feel yourself get stronger!\nBase attack has increased by 5.")
                            base_attack += 5
                            brewing = False
                            brewing_unlocked = True
                            break
                        print("\nYour bottles are in the order {}.".format(user_bottles))
                        move = int(input("\nWhich bottle would you like to swap? Type 0 to give up."))
                        replacement = int(input("Bottle to swap with?"))
                        moveindex = move - 1
                        replacementindex = replacement - 1
                        if move == 0:
                            brewing = False
                        try:
                            user_bottles[moveindex] = replacement
                            user_bottles[replacementindex] = move
                        except ValueError:
                            print("That is not a valid option, try again.")
                    current_room[9] = True
                else:
                    print(current_room[6])
                    print("You've already solved the puzzle, there's nothing left for you here.")
            elif current_room == room_list[5] or current_room == room_list[29]:
                print(current_room[6])
                print("\nYou saved the game!")
                print("If you die, you will respawn here.")
                save_data = [current_room, stats, inventory, weapons, armor, equipped, stair_unlocked, brewing_unlocked,
                             records_unlocked, first_time, library_unlocked, current_health]
            elif current_room == room_list[10]:
                if stair_unlocked == True:
                    print(current_room[5])
                else:
                    print("You need to unlock it to go further.")
            else:
                print(current_room[6])
        elif action.lower().strip() == "i":
            organizing = True
            while organizing:
                stats = [current_health, base_health, base_attack + weapon_attack + bonus_attack,
                         base_defense + armor_defense +
                         bonus_defense, gold]
                if current_health > 70:
                    color = "\033[1;32m"
                elif current_health > 40:
                    color = "\033[1;33m"
                else:
                    color = "\033[1:31m"
                print("\n{}'s Inventory\n".format(username))
                print("STATS:")
                print("\nHEALTH:", color, "{} /".format(current_health), "{}\033[0m".format(base_health))
                print("ATTACK: {}".format(stats[2]))
                print("DEF: {}".format(stats[3]))
                print("\nGOLD: \033[1;33m{}\033[0m".format(stats[4]))
                print("\nWEAPONS:")
                try:
                    for o in weapons:
                        print(o["name"])
                except TypeError:
                    print("")
                print("\nARMOR:")
                try:
                    for c in armor:
                        print(c["name"])
                except TypeError:
                    print("")
                print("\nMISC ITEMS:")
                print(inventory)
                print("\nEQUIPPED ITEMS:")
                try:
                    print("WEAPON: {}".format(equipped[0]["name"]))
                except TypeError:
                    print("WEAPON: ")
                try:
                    print("TOP ARMOR: {}".format(equipped[1]["name"]))
                except TypeError:
                    print("TOP ARMOR: ")
                try:
                    print("MID ARMOR: {}".format(equipped[2]["name"]))
                except TypeError:
                    print("MID ARMOR: ")
                try:
                    print("BOT ARMOR: {}".format(equipped[3]["name"]))
                except TypeError:
                    print("BOT ARMOR: ")
                equip = input("\nWould you like to equip or unequip anything?\n")
                if equip.lower().strip() == "y" or equip.lower().strip() == "yes":
                    print("1) WEAPON\n2) ARMOR")
                    piece = input("\nWhich of these would you like to change? Q to cancel.")
                    if piece.lower().strip() == "q" or piece.lower().strip() == "quit":
                        organizing = False
                        break
                    elif piece.strip() == "1":
                        organizing = False
                        counter = 1
                        try:
                            for i in range(len(weapons)):
                                print("{})".format(counter), "{}".format(weapons[counter-1]["name"]))
                                counter += 1
                        except TypeError:
                            print("goddamnit")
                        part = int(input("\nWhich weapon would you like to equip? 0 to cancel."))
                        try:
                            try:
                                weapon_inventory_adjust(part-1)
                                weapon_attack = equipped[0]["damage"]
                            except IndexError:
                                print("That is not a valid option, try again.")
                        except TypeError:
                            print("That is not a valid option, try again.")
                    elif piece.strip() == "2" or piece == "3" or piece == "4":
                        organizing = False
                        for i in armor:
                            pcounter = 0
                            counter = [1, 2, 3, 4, 5, 6, 7]
                            try:
                                print("{})".format(counter[pcounter]), "{}".format(i["name"]))
                            except TypeError:
                                print("")
                            pcounter += 1
                            if pcounter >= 1:
                                part = int(input("\nWhich piece of armor would you like to equip? 0 to cancel."))
                                part_shift = part-1
                                if armor[part_shift]["type"] == "Top":
                                    armor_id = 1
                                elif armor[part_shift]["type"] == "Mid":
                                    armor_id = 2
                                elif armor[part_shift]["type"] == "Bot":
                                    armor_id = 3
                                else:
                                    print("That is not a valid option, try again.")
                            else:
                                print("You have no armor to equip.")
                                organizing = False
                                break
                            try:
                                armor_inventory_adjust(int(part_shift))
                                armor_defense = armor[part - 1]["defense"]
                                # kept getting errors even though it was working so i just commented it out lol
                            except TypeError:
                                ""
                                # print("That is not a valid option, try again.")
                                # print("4")
                            else:
                                print("")
                else:
                    organizing = False
        else:
            print("That is not a valid option, try again.")
print("Thank you for playing!")
