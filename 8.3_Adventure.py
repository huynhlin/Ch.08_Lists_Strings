'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
done = False
room_list = []
room = ["SPAWN ROOM", None, None, 1, None]  # 0
room_list.append(room)
room = ["HALL 1", 0, 2, 5, 3]  # 1
room_list.append(room)
room = ["CHAPEL", None, None, None, 1]  # 2
room_list.append(room)
room = ["GARDEN", None, 1, None, 4]  # 3
room_list.append(room)
room = ["SHED", None, 3, None, None]  # 4
room_list.append(room)
room = ["HALL 2", 1, None, 6, None]  # 5
room_list.append(room)
room = ["HALL 3", 5, 8, 9, 7]  # 6
room_list.append(room)
room = ["APOTHECARY", None, 6, None, None]  # 7
room_list.append(room)
room = ["SHOP", None, None, None, 6]  # 8
room_list.append(room)
room = ["HALL 4", 6, None, 10, None]  # 9
room_list.append(room)
room = ["STAIRWELL (FLOOR ONE)", 9, None, 11, None]  # 10
room_list.append(room)
room = ["STAIRWELL EXIT (FLOOR TWO", 10, 16, 12, None]  # 11
room_list.append(room)
room = ["BLACKSMITH", 11, 15, 13, None]  # 12
room_list.append(room)
room = ["RECORD ROOM", 12, 14, None, None]  # 13
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
room = ["LIBRARY", 20, 31, 24, 18]  # 23
room_list.append(room)
room = ["HALL 7", 23, None, 25, 19]  # 24
room_list.append(room)
room = ["HALL 8", 24, None, 26, None]  # 25
room_list.append(room)
room = ["HALL 9", 25, None, 27, None]  # 26
room_list.append(room)
room = ["HALL 10", 26, 29, None, 28]  # 27
room_list.append(room)
room = ["BREWERY", None, 27, None, None]  # 28
room_list.append(room)
room = ["HALL 11", None, 30, None, 27]  # 29
room_list.append(room)
room = ["MAZE", None, None, None, 29]  # 30
room_list.append(room)
room = ["THRONE ROOM", None, None, None, 23]  # 31
room_list.append(room)

current_room = 0
#  room config done


