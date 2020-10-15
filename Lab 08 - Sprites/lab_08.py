""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_OIL = 0.05
SPRITE_SCALING_ASTEROID = 0.05
OIL_COUNT = 50
ASTEROID_COUNT = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Asteroid(arcade.Sprite):

    def reset_pos(self):

        if self.top < 0:
            # Reset the coin to a random spot above the screen
            self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                             SCREEN_HEIGHT + 100)
            self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the Asteroid
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class Oil(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.oil_list = None
        self.asteroid_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Sounds
        self.good_sound = arcade.load_sound("coin4.wav")
        self.bad_sound = arcade.load_sound("error4.wav")

        arcade.set_background_color(arcade.color.ROYAL_AZURE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.oil_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character_robot_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(OIL_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            oil = Oil("oil.png", SPRITE_SCALING_OIL)

            # Position the coin
            oil.center_x = random.randrange(SCREEN_WIDTH)
            oil.center_y = random.randrange(SCREEN_HEIGHT)
            oil.change_x = random.randrange(-3, 4)
            oil.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.oil_list.append(oil)

        for i in range(ASTEROID_COUNT):

            # Create asteroid
            asteroid = Asteroid("asteroid.png", SPRITE_SCALING_ASTEROID)

            # positioning the asteroid
            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(SCREEN_HEIGHT)

            # Adding asteroid to the lists
            self.asteroid_list.append(asteroid)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.oil_list.draw()
        self.player_list.draw()
        self.asteroid_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.oil_list) == 0:
            output = "Game Over!"
            arcade.draw_text(output, 310, 300, arcade.color.WHITE, 30)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        # Move the center of the player sprite to match the mouse x, y
        if len(self.oil_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        if len(self.oil_list) > 0:
            self.oil_list.update()
            self.asteroid_list.update()

        # Generate a list of all sprites that collided with the player.
        oil_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.oil_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for oil in oil_hit_list:
            oil.remove_from_sprite_lists()
            arcade.play_sound(self.good_sound, volume=0.01)
            self.score += 1

        asteroid_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.asteroid_list)

        for asteroid in asteroid_hit_list:
            asteroid.remove_from_sprite_lists()
            asteroid.reset_pos()
            arcade.play_sound(self.bad_sound, volume=0.01)
            self.score -= 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
