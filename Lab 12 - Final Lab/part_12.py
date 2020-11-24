import random
import arcade
import timeit

SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_enemy = 0.5
SPRITE_SCALING_LASER = 0.1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Blood and Iron"

BULLET_SPEED = 5
ENEMY_SPEED = 2

MAX_PLAYER_BULLETS = 3

# This margin controls how close the enemy gets to the left or right side
# before reversing direction.
ENEMY_VERTICAL_MARGIN = 15
RIGHT_ENEMY_BORDER = SCREEN_WIDTH - ENEMY_VERTICAL_MARGIN
LEFT_ENEMY_BORDER = ENEMY_VERTICAL_MARGIN

# How many pixels to move the enemy down when reversing
ENEMY_MOVE_DOWN_AMOUNT = 30

# Game state
GAME_OVER = 1
PLAY_GAME = 0


class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("BLOOD AND IRON", SCREEN_WIDTH/2, 540,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("HELP! It's the Second World War and the ruthless Nazi army is invading your home, Stalingrad.", SCREEN_WIDTH/2,
                         (SCREEN_HEIGHT / 2) + 75, arcade.color.BARN_RED, font_size=16, anchor_x="center")
        arcade.draw_text("You'll take on the role of famous, russian tank commander, Dmirty Fyodorovich Lavrinenko.", SCREEN_WIDTH/2,
                         (SCREEN_HEIGHT / 2) + 25, arcade.color.BARN_RED, font_size=16, anchor_x="center")
        arcade.draw_text("You're Stalingrad's last line of defense until reinforces show up. Put on your war face", SCREEN_WIDTH/2,
                         (SCREEN_HEIGHT / 2) - 25, arcade.color.BARN_RED, font_size=16, anchor_x="center")
        arcade.draw_text("commander and show those Nazis what happens when you invade the motherland.", SCREEN_WIDTH / 2,
                         (SCREEN_HEIGHT / 2) - 75, arcade.color.BARN_RED, font_size=16, anchor_x="center")

        arcade.draw_text("Click to advance", SCREEN_WIDTH/2, 100,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)


class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.RED_DEVIL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Instructions Screen", SCREEN_WIDTH/2, 540,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Comrade the plan is simple: Use the mouse to maneuver your tank from left to right. AVOID FIRE.",
                         SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) + 75, arcade.color.YELLOW, font_size=16, anchor_x="center")
        arcade.draw_text("The enemy will fire at you, but you have the power to fire back. Use the mouse buttons to shoot.",
                         SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) + 25, arcade.color.YELLOW, font_size=16, anchor_x="center")
        arcade.draw_text("Do what you must to eliminate all incoming hostiles. The army is large and will attack in waves!",
                         SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 25, arcade.color.YELLOW, font_size=16, anchor_x="center")
        arcade.draw_text("You will be provided cover but note that the cover will disappear as it gets shot. BE WISE.",
                         SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 75, arcade.color.YELLOW, font_size=16, anchor_x="center")
        arcade.draw_text("The nazis think you'll fear their numbers, but you are russian. you dont know defeat. DON'T QUIT!",
                         SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 125, arcade.color.YELLOW, font_size=16, anchor_x="center")

        arcade.draw_text("Click to advance", SCREEN_WIDTH/2, 100,
                         arcade.color.GRAY, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)


class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("game_over.png")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

        self.processing_time = 0
        self.draw_time = 0
        self.frame_count = 0
        self.fps_start_timer = None
        self.fps = None

    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                SCREEN_WIDTH, SCREEN_HEIGHT)

        if self.frame_count % 60 == 0:
            if self.fps_start_timer is not None:
                total_time = timeit.default_timer() - self.fps_start_timer
                self.fps = 60 / total_time
            self.fps_start_timer = timeit.default_timer()
        self.frame_count += 1

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = MyGame()
        game_view.setup()
        self.window.show_view(game_view)


class MyGame(arcade.View):
    """ Main application class. """

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__()

        self.background = None

        # Variables that will hold sprite lists
        self.player_list = None
        self.enemy_list = None
        self.player_bullet_list = None
        self.enemy_bullet_list = None
        self.shield_list = None

        # Textures for the enemy
        self.enemy_textures = None

        # State of the game
        self.game_state = PLAY_GAME

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        self.processing_time = 0
        self.draw_time = 0
        self.fps = 0

        # Enemy movement
        self.enemy_change_x = -ENEMY_SPEED

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)

        # Load sounds. Sounds from kenney.nl
        self.gun_sound = arcade.load_sound("tankshot.mp3")
        self.hit_sound = arcade.load_sound("hit3.wav")

        arcade.set_background_color(arcade.color.AMAZON)

        # arcade.configure_logging()

    def setup_level_one(self):

        self.background = arcade.load_texture("stalingrad.jpg")

        # Load the textures for the enemies, one facing left, one right
        self.enemy_textures = []
        texture = arcade.load_texture("nazisoldier.png", mirrored=True)
        self.enemy_textures.append(texture)
        texture = arcade.load_texture("nazisoldier.png")
        self.enemy_textures.append(texture)

        # Create rows and columns of enemies
        positions = [380, 580], \
                    [420, 580], \
                    [460, 580], \
                    [500, 580], \
                    [540, 580], \
                    [580, 580], \
                    [620, 580], \
                    [340, 580], \
                    [460, 530], \
                    [500, 530], \
                    [540, 530], \
                    [580, 530], \
                    [420, 530], \
                    [380, 530], \
                    [420, 480], \
                    [540, 480], \
                    [500, 480], \
                    [460, 480], \
                    [500, 430], \
                    [460, 430]

        for position in positions:

            # Create the enemy instance
            # enemy image from kenney.nl
            enemy = arcade.Sprite()
            enemy.scale = SPRITE_SCALING_enemy
            enemy.texture = self.enemy_textures[1]
            # Position the enemy
            enemy.position = position
            # Add the enemy to the lists
            self.enemy_list.append(enemy)

    def setup_level_two(self):
        print("bruh")
        self.background = arcade.load_texture("battleground1.png")

        # Load the textures for the enemies, one facing left, one right
        self.enemy_textures = []
        texture = arcade.load_texture("naziSS.png", mirrored=True)
        self.enemy_textures.append(texture)
        texture = arcade.load_texture("naziSS.png")
        self.enemy_textures.append(texture)

        # Create rows and columns of enemies
        positions = [380, 580], \
                    [420, 580], \
                    [460, 580], \
                    [500, 580], \
                    [540, 580], \
                    [580, 580], \
                    [620, 580], \
                    [340, 580], \
                    [460, 530], \
                    [500, 530], \
                    [540, 530], \
                    [580, 530], \
                    [420, 530], \
                    [380, 530], \
                    [420, 480], \
                    [540, 480], \
                    [500, 480], \
                    [460, 480], \
                    [500, 430], \
                    [460, 430]

        for position in positions:
            # Create the enemy instance
            # enemy image from kenney.nl
            enemy = arcade.Sprite()
            enemy.scale = SPRITE_SCALING_enemy
            enemy.texture = self.enemy_textures[1]
            # Position the enemy
            enemy.position = position
            # Add the enemy to the lists
            self.enemy_list.append(enemy)

    def make_shield(self, x_start):
        """
        Make a shield, which is just a 2D grid of solid color sprites
        stuck together with no margin so you can't tell them apart.
        """
        shield_block_width = 5
        shield_block_height = 10
        shield_width_count = 20
        shield_height_count = 5
        y_start = 150
        for x in range(x_start, x_start + shield_width_count * shield_block_width, shield_block_width):
            for y in range(y_start, y_start + shield_height_count * shield_block_height, shield_block_height):
                shield_sprite = arcade.SpriteSolidColor(shield_block_width, shield_block_height, arcade.color.BLACK)
                shield_sprite.center_x = x
                shield_sprite.center_y = y
                self.shield_list.append(shield_sprite)

    def setup(self):
        """
        Set up the game and initialize the variables.
        Call this method if you implement a 'play again' feature.
        """

        self.game_state = PLAY_GAME

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.shield_list = arcade.SpriteList(is_static=True)

        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = arcade.Sprite("tank.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 40
        self.player_list.append(self.player_sprite)

        # Make each of the shields
        for x in range(75, 800, 190):
            self.make_shield(x)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        self.setup_level_one()

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        arcade.start_render()

        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

        draw_start_time = timeit.default_timer()

        # Draw all the sprites.
        self.enemy_list.draw()
        self.player_bullet_list.draw()
        self.enemy_bullet_list.draw()
        self.shield_list.draw()
        self.player_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.BLACK, 14)

        # Display timings
        output = f"Processing time: {self.processing_time:.3f}"
        arcade.draw_text(output, 20, SCREEN_HEIGHT - 20, arcade.color.BLACK, 16)

        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 20, SCREEN_HEIGHT - 40, arcade.color.BLACK, 16)

        if self.fps is not None:
            output = f"FPS: {self.fps:.0f}"
            arcade.draw_text(output, 20, SCREEN_HEIGHT - 60, arcade.color.BLACK, 16)

        self.draw_time = timeit.default_timer() - draw_start_time

        # Draw game over if the game state is such
        if self.game_state == GAME_OVER:
            arcade.draw_text(f"GAME OVER", 250, 300, arcade.color.BLACK, 55)
            self.window.set_mouse_visible(True)

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """

        # Don't move the player if the game is over
        if self.game_state == GAME_OVER:
            return

        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """

        # Only allow the user so many bullets on screen at a time to prevent
        # them from spamming bullets.
        if len(self.player_bullet_list) < MAX_PLAYER_BULLETS:

            # Gunshot sound
            arcade.play_sound(self.gun_sound)

            # Create a bullet
            bullet = arcade.Sprite("tankshell.png", SPRITE_SCALING_LASER)

            # The image points to the right, and we want it to point up. So
            # rotate it.
            bullet.angle = 90

            # Give the bullet a speed
            bullet.change_y = BULLET_SPEED

            # Position the bullet
            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top

            # Add the bullet to the appropriate lists
            self.player_bullet_list.append(bullet)

    def update_enemies(self):

        # Move the enemy vertically
        for enemy in self.enemy_list:
            enemy.center_x += self.enemy_change_x

        # Check every enemy to see if any hit the edge. If so, reverse the
        # direction and flag to move down.
        move_down = False
        for enemy in self.enemy_list:
            if enemy.right > RIGHT_ENEMY_BORDER and self.enemy_change_x > 0:
                self.enemy_change_x *= -1
                move_down = True
            if enemy.left < LEFT_ENEMY_BORDER and self.enemy_change_x < 0:
                self.enemy_change_x *= -1
                move_down = True

        # Did we hit the edge above, and need to move t he enemy down?
        if move_down:
            # Yes
            for enemy in self.enemy_list:
                # Move enemy down
                enemy.center_y -= ENEMY_MOVE_DOWN_AMOUNT
                # Flip texture on enemy so it faces the other way
                if self.enemy_change_x > 0:
                    enemy.texture = self.enemy_textures[0]
                else:
                    enemy.texture = self.enemy_textures[1]

    def allow_enemies_to_fire(self):
        """
        See if any enemies will fire this frame.
        """
        # Track which x values have had a chance to fire a bullet.
        # Since enemy list is build from the bottom up, we can use
        # this to only allow the bottom row to fire.
        x_spawn = []
        for enemy in self.enemy_list:
            # Adjust the chance depending on the number of enemies. Fewer
            # enemies, more likely to fire.
            chance = 4 + len(self.enemy_list) * 4

            # Fire if we roll a zero, and no one else in this column has had
            # a chance to fire.
            if random.randrange(chance) == 0 and enemy.center_x not in x_spawn:
                # Create a bullet
                bullet = arcade.Sprite("bullet2.png", SPRITE_SCALING_LASER * 1.5)

                # Angle down.
                bullet.angle = 180

                # Give the bullet a speed
                bullet.change_y = -BULLET_SPEED

                # Position the bullet so its top id right below the enemy
                bullet.center_x = enemy.center_x
                bullet.top = enemy.bottom

                # Add the bullet to the appropriate list
                self.enemy_bullet_list.append(bullet)

            # Ok, this column has had a chance to fire. Add to list so we don't
            # try it again this frame.
            x_spawn.append(enemy.center_x)

    def process_enemy_bullets(self):

        # Move the bullets
        self.enemy_bullet_list.update()

        # Loop through each bullet
        for bullet in self.enemy_bullet_list:
            # Check this bullet to see if it hit a shield
            hit_list = arcade.check_for_collision_with_list(bullet, self.shield_list)

            # If it did, get rid of the bullet and shield blocks
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                for shield in hit_list:
                    shield.remove_from_sprite_lists()
                continue

            # See if the player got hit with a bullet
            if arcade.check_for_collision_with_list(self.player_sprite, self.enemy_bullet_list):
                self.game_state = GAME_OVER

            # If the bullet falls off the screen get rid of it
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

    def process_player_bullets(self):

        # Move the bullets
        self.player_bullet_list.update()

        # Loop through each bullet
        for bullet in self.player_bullet_list:

            # Check this bullet to see if it hit a enemy
            hit_list = arcade.check_for_collision_with_list(bullet, self.shield_list)
            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                for shield in hit_list:
                    shield.remove_from_sprite_lists()
                continue

            # Check this bullet to see if it hit a enemy
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every enemy we hit, add to the score and remove the enemy
            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                self.score += 1

                # Hit Sound
                arcade.play_sound(self.hit_sound)

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

    def on_update(self, delta_time):
        """ Movement and game logic """

        if self.game_state == GAME_OVER:
            return

        self.update_enemies()
        self.allow_enemies_to_fire()
        self.process_enemy_bullets()
        self.process_player_bullets()

        if len(self.enemy_list) == 0:
            self.setup_level_two()


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
