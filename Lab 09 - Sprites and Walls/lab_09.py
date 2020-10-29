"""
Sprite move between different rooms.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_rooms
"""

import arcade
import random
import os

SPRITE_SCALING = 0.5
SPRITE_SCALING_OIL = 0.05
NUMBER_OF_OIL = 25
SPRITE_NATIVE_SIZE = 150
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)
WALL_SCALING = 1.2

SCREEN_WIDTH = SPRITE_SIZE * 14
SCREEN_HEIGHT = SPRITE_SIZE * 10
SCREEN_TITLE = "The Space Odyssey but it's a 4 room coin collecting game."

MOVEMENT_SPEED = 5


class Room:
    """
    This class holds all the information about the
    different rooms.
    """
    def __init__(self):
        # You may want many lists. Lists for coins, monsters, etc.
        self.wall_list = None

        # This holds the background images. If you don't want changing
        # background images, you can delete this part.
        self.background = None


def setup_room_1():
    """
    Create and return room 1.
    If your program gets large, you may want to separate this into different
    files.
    """

    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            if (x != SPRITE_SIZE * 6 and x != SPRITE_SIZE * 7) or y == 0:
                # Kenny.nl
                wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            # Kenny.nl
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    coordinate_list = [[2, 3],
                       [3.15, 4.15],
                       [4.25, 4.15],
                       [4.25, 5.3],
                       [5.39, 5.3]]
    for coordinate in coordinate_list:
        wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
        wall.left = coordinate[0] * SPRITE_SIZE
        wall.bottom = coordinate[1] * SPRITE_SIZE
        room.wall_list.append(wall)

    coordinate_list = [[6.5, 5.3],
                       [7.6, 5.3],
                       [7.6, 4.15],
                       [8.75, 4.15],
                       [9.9, 3]]
    for coordinate in coordinate_list:
        wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
        wall.left = coordinate[0] * SPRITE_SIZE
        wall.bottom = coordinate[1] * SPRITE_SIZE
        room.wall_list.append(wall)

    wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
    wall.left = 11 * SPRITE_SIZE
    wall.bottom = 7 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
    wall.left = 6 * SPRITE_SIZE
    wall.bottom = 1.5 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
    wall.left = 6 * SPRITE_SIZE
    wall.bottom = 2.7 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
    wall.left = 6 * SPRITE_SIZE
    wall.bottom = 3.9 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
    wall.left = 2 * SPRITE_SIZE
    wall.bottom = 7 * SPRITE_SIZE
    room.wall_list.append(wall)

    wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
    wall.left = 10 * SPRITE_SIZE
    wall.bottom = 6 * SPRITE_SIZE
    room.wall_list.append(wall)

    for y in range(7, 9):
        wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
        wall.left = 8 * SPRITE_SIZE
        wall.bottom = y * SPRITE_SIZE
        room.wall_list.append(wall)

    # If you want coins or monsters in a level, then add that code here.
    # Boolean variable if we successfully placed the coin
    for i in range(NUMBER_OF_OIL):
        # Create the coin instance
        # Coin image from kenney.nl
        oil = arcade.Sprite("oil.png", SPRITE_SCALING_OIL)

    oil_placed_successfully = False

    # Keep trying until success
    while not oil_placed_successfully:
        # Position the coin
        oil.center_x = random.randrange(SCREEN_WIDTH)
        oil.center_y = random.randrange(SCREEN_HEIGHT)

        # See if the coin is hitting a wall
        wall_hit_list = arcade.check_for_collision_with_list(oil, room.wall_list)

        # See if the coin is hitting another coin
        oil_hit_list = arcade.check_for_collision_with_list(oil, room.oil_list)

        if len(wall_hit_list) == 0 and len(oil_list) == 0:
            # It is!
            oil_placed_successfully = True

    # Add the coin to the lists
    room.oil_list.append(oil)

    # Load the background image for this level.
    # https: // www.needpix.com / about
    room.background = arcade.load_texture("nebula.png")

    return room


def setup_room_2():
    """
    Create and return room 2.
    """
    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        # Kenny.nl
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            if (x != SPRITE_SIZE * 6 and x != SPRITE_SIZE * 7) or y == 0:
                # Kenny.nl
                wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up
            # Kenny.nl
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x != 0:
                wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)
    # Kenny.nl

    for y in range(3, 9):
        wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
        wall.left = 3 * SPRITE_SIZE
        wall.bottom = y * SPRITE_SIZE
        room.wall_list.append(wall)

    for x in range(4, 11):
        wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
        wall.left = x * SPRITE_SIZE
        wall.bottom = 5 * SPRITE_SIZE
        room.wall_list.append(wall)

    wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
    wall.left = 10.5 * SPRITE_SIZE
    wall.bottom = 6.15 * SPRITE_SIZE
    room.wall_list.append(wall)

    for y in range(1, 4):
        wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
        wall.left = 5 * SPRITE_SIZE
        wall.bottom = y * SPRITE_SIZE
        room.wall_list.append(wall)

    for y in range(2, 5):
        wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
        wall.left = 10.5 * SPRITE_SIZE
        wall.bottom = y * SPRITE_SIZE
        room.wall_list.append(wall)

    wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
    wall.left = 7.5 * SPRITE_SIZE
    wall.bottom = 3 * SPRITE_SIZE
    room.wall_list.append(wall)

    # https: // pixabay.com / illustrations / search / nebula /
    room.background = arcade.load_texture("galaxy.png")

    return room


def setup_room_3():
    """
    Create and return room 1.
    If your program gets large, you may want to separate this into different
    files.
    """

    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            if (x != SPRITE_SIZE * 6 and x != SPRITE_SIZE * 7) or y == SCREEN_HEIGHT - SPRITE_SIZE:
                # Kenny.nl
                wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            # Kenny.nl
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == SCREEN_WIDTH - SPRITE_SIZE:
                wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)
    # Kenny.nl
    for x in range(1, 5):
        wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
        wall.left = x * SPRITE_SIZE
        wall.bottom = 7 * SPRITE_SIZE
        room.wall_list.append(wall)
    # Kenny.nl
    for y in range(1, 6):
        wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
        wall.left = 3 * SPRITE_SIZE
        wall.bottom = y * SPRITE_SIZE
        room.wall_list.append(wall)

    coordinate_list = [[8.35, 4.15],
                       [9.5, 4.15],
                       [10.6, 4.15],
                       [10.6, 5.3],
                       [11.74, 5.3]]
    for coordinate in coordinate_list:
        wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
        wall.left = coordinate[0] * SPRITE_SIZE
        wall.bottom = coordinate[1] * SPRITE_SIZE
        room.wall_list.append(wall)

    for x in range(4, 7):
        wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
        wall.left = x * SPRITE_SIZE
        wall.bottom = 3 * SPRITE_SIZE
        room.wall_list.append(wall)

    for y in range(7, 9):
        wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
        wall.left = 7 * SPRITE_SIZE
        wall.bottom = y * SPRITE_SIZE
        room.wall_list.append(wall)

    wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
    wall.left = 10 * SPRITE_SIZE
    wall.bottom = 1.15 * SPRITE_SIZE
    room.wall_list.append(wall)

    # If you want coins or monsters in a level, then add that code here.

    # Load the background image for this level.
    # https://www.astrobin.com/264452/?nc=all
    room.background = arcade.load_texture("nebula.jpg")

    return room


def setup_room_4():
    """
    Create and return room 1.
    If your program gets large, you may want to separate this into different
    files.
    """

    room = Room()

    """ Set up the game and initialize the variables. """
    # Sprite lists
    room.wall_list = arcade.SpriteList()

    # -- Set up the walls
    # Create bottom and top row of boxes
    # This y loops a list of two, the coordinate 0, and just under the top of window
    for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
        # Loop for each box going across
        for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
            if (x != SPRITE_SIZE * 6 and x != SPRITE_SIZE * 7) or y == SCREEN_HEIGHT - SPRITE_SIZE:
                # Kenny.nl
                wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

    # Create left and right column of boxes
    for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
        # Loop for each box going across
        for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
            # Skip making a block 4 and 5 blocks up on the right side
            # Kenny.nl
            if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)
    # Kenny.nl
    for x in range(3, 9):
        wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
        wall.left = x * SPRITE_SIZE
        wall.bottom = 6.5 * SPRITE_SIZE
        room.wall_list.append(wall)

    for x in range(3, 9):
        wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
        wall.left = x * SPRITE_SIZE
        wall.bottom = 2 * SPRITE_SIZE
        room.wall_list.append(wall)

    for y in range(1, 7):
        wall = arcade.Sprite("corridor_wall.png", WALL_SCALING)
        wall.left = 8 * SPRITE_SIZE
        wall.bottom = y * SPRITE_SIZE
        room.wall_list.append(wall)

    for x in range(1, 7):
        wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
        wall.left = x * SPRITE_SIZE
        wall.bottom = 4.4 * SPRITE_SIZE
        room.wall_list.append(wall)

    for y in range(3, 9):
        wall = arcade.Sprite("machine_barrel_NW.png", WALL_SCALING)
        wall.left = 10.5 * SPRITE_SIZE
        wall.bottom = y * SPRITE_SIZE
        room.wall_list.append(wall)

    # If you want coins or monsters in a level, then add that code here.

    # Load the background image for this level.
    # https://www.nytimes.com/2020/08/07/science/supernova-neutron-star-sn1987a.html
    room.background = arcade.load_texture("supernova.jpg")

    return room


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.current_room = 0

        # Set up the player
        self.rooms = None
        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        # Kenny.nl
        self.player_sprite = arcade.Sprite("character_robot_idle.png", SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 200
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

        # Our list of rooms
        self.rooms = []

        # Create the rooms. Extend the pattern for each room.
        room = setup_room_1()
        self.rooms.append(room)

        room = setup_room_2()
        self.rooms.append(room)

        room = setup_room_3()
        self.rooms.append(room)

        room = setup_room_4()
        self.rooms.append(room)

        # Our starting room number
        self.current_room = 0

        # Create a physics engine for this room
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the background texture
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.rooms[self.current_room].background)

        # Draw all the walls in this room
        self.rooms[self.current_room].wall_list.draw()

        # If you have coins or monsters, then copy and modify the line
        # above for each list.

        self.player_list.draw()
        self.oil_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > SCREEN_WIDTH:
            if self.current_room == 0:
                self.current_room = 1
            elif self.current_room == 3:
                self.current_room = 2
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0

        elif self.player_sprite.center_x < 0:
            if self.current_room == 1:
                self.current_room = 0
            elif self.current_room == 2:
                self.current_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = SCREEN_WIDTH

        elif self.player_sprite.center_y > SCREEN_HEIGHT:
            if self.current_room == 1:
                self.current_room = 2
            elif self.current_room == 0:
                self.current_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = 0

        elif self.player_sprite.center_y < 0:
            if self.current_room == 2:
                self.current_room = 1
            elif self.current_room == 3:
                self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_y = SCREEN_HEIGHT


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
