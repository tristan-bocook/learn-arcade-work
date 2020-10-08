print(""" Welcome to prison. Your psycho brother framed you for mass murder so he could steal your wife and 
        kids. Your plan is to escape and take your wife and kids to mexico where a connection will hook you up
        with a taco truck business and a new home. Good Luck!""")


class Room:
    """
    This is a class that represents the room
    """
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():

    room_list = []

# Creating rooms
    room = Room(""" You're currently in your cell. To the North is the warden's office(a friend may have spiked his 
    drink). To the east is a hole leading to the next cell.""", 3, 1, None, None)
    room_list.append(room)

    room = Room(""" You're in cell 1. To the west is your cell. To the east is a hole leading to cell 2""", None, 2, None, 0)
    room_list.append(room)

    room = Room(""" You're in cell 2. To the east is cell 1. To the north is the chow hall (home to salmonella 
    and fights!)""", 5, None, None, 1)
    room_list.append(room)

    room = Room(""" You're in the warden's room with the warden fast asleep. To the north is A block which leads to 
    many different sections of the prison. To the south is the your cell.""", 7, None, 0, None)
    room_list.append(room)

    room = Room(""" You're in the guard's quarter's. To the north is B block. To the east is the guard's room. """,
                8, 5, None, None)
    room_list.append(room)

    room = Room(""" You're in the chow hall. To the north is c block. To the west is the guard's room, lucky for you all 
    the guards were deployed to stop a conveniently timed riot.""", 9, None, 2, 4)
    room_list.append(room)

    room = Room(""" You're in S block. To the north is the rec room which is outfitted with a broken arcade machine.
                To the east is A block which is the crossroads of the prison.""", 10, 7, None, None)
    room_list.append(room)

    room = Room(""" You're in A block. To the north is a hall leading to the worker's quarters. To the east is a hallway 
    leading to B block. To the south is a hallway leading to the warden's room. To the west is a hallway leading to 
    S block """, 11, 8, 3, 6)
    room_list.append(room)

    room = Room(""" You're in B block. To the east is hallway leading to c block. To the south is a door leading to the 
                guard's quarter's. To the west is a hallway leading to A block """, None, 9, 4, 7)
    room_list.append(room)

    room = Room(""" You're in C block. To the north is the equipment room which holds various tools and rec room tech. 
    To the south is the chow hall. To the west is a hallway that leads to B block. """, 12, None, 5, 8)
    room_list.append(room)

    room = Room(""" You're in the rec room. To the north is a doorway leading to the janitorial room, 
    you may have heard rumors of a great poster (*cough cough*) """, 13, None, 6, None)
    room_list.append(room)

    room = Room(""" You're in the worker's quarter's. To the north is a hall leading to the worker's yard, 
    lucky for you no guards occupy it due to a sudden riot. To the south is a hallway leading to A block. """, 14,
                None, 7, None)
    room_list.append(room)

    room = Room(""" You're in the equipment room. To the north is a door leading to Security which is very short 
    staffed. To the south is C block. """, 16, None, 12, None)
    room_list.append(room)

    room = Room(""" You're in the janitorial room. To the north you discover a poster of Emily Ratajkowski. She reminds 
    you of your sweet wife Maria, but upon closer inspection you feel a slight draft. Behind the poster is a secret 
    hole leading what you believe to be the exit. To the east is a door leading to the working yard""", 18, 14, 10, None)
    room_list.append(room)

    room = Room(""" You're in the working yard. To the east is a rec yard where you've met allies critical for your 
    escape. To the south is the worker's quarters. To the west is a door leading to the janitorial room. To the west is 
    the working yard.""", None, 15, 11, 13)
    room_list.append(room)

    room = Room(""" You're in the rec yard. To the north is the gate (a couple friends may have sabotaged it). To the 
    east is a door leading to security. To the west is the working yard.""", 19, 16, None, 14)
    room_list.append(room)

    room = Room(""" You're in security. To the east is the armory which holds equipment you may need in case your escape 
    goes FUBAR. To the south is a door leading to the equipment room. To the west is the rec yard. """, None, 17, 12, 15)
    room_list.append(room)

    room = Room(""" You're in the armory. To the north is a door leading to a second guard's quarters. 
    To the west is a door leading to security. """, 20, None, None, 16)
    room_list.append(room)

    room = Room(""" You're currently crawling through a secret exit which is really a sewer system. 
    To the north is freedom. To the south is the janitorial room (if you feel like chickening out at 
    least you can clean yourself).""", 22, None, 13, None)
    room_list.append(room)

    room = Room(""" You're at the gate. To the north is a break in the fencing which leads to freedom. To the south is 
    the rec yard, although you might get stabbed for chickening out.""", 21, None, 15, None)
    room_list.append(room)

    room = Room("You're at the second guard's quarter's. To the south is the armory (What did you expect?).", None, None, 17, None)
    room_list.append(room)

    room = Room("freedom", None, None, 17, None)
    room_list.append(room)

    room = Room("secret freedom", None, None, 18, None)
    room_list.append(room)
# Setting up game

    current_room = 0
    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        print()
        user_input = input("Which direction do you take? ")

        if user_input.lower() == "north" or user_input.lower() == "n":
            next_room = room_list[current_room].north

            if next_room == None:
                print("You can't go that way!")

            else:
                current_room = next_room

        elif user_input.lower() == "east" or user_input.lower() == "e":
            next_room = room_list[current_room].east

            if next_room == None:
                print("You can't go that way!")

            else:
                current_room = next_room

        elif user_input.lower() == "south" or user_input.lower() == "s":
            next_room = room_list[current_room].south

            if next_room == None:
                print("You can't go that way!")

            else:
                current_room = next_room

        elif user_input.lower() == "west" or user_input.lower() == "w":
            next_room = room_list[current_room].west

            if next_room == None:
                print("You can't go that way!")

            else:
                current_room = next_room

        else:
            print("Uh, uh, uh, that's not the magic word!")

        if current_room == 21 or current_room == 22:
            print("You have found your freedom (illegally). Congrats!")
            done = True

main()
