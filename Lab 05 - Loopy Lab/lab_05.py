import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            # row is 0 when and column is 0 x and y is 5x5
            x = 10 * column + 5  # Instead of zero, calculate the proper x location using 'column'
            y = 10 * row + 5  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    # Below, replace "pass" with your code for the loop.
    # Use the modulus operator and an if statement to select the color
    # Don't loop from 30 to 60 to shift everything over, just add 300 to x.
    for row in range(30):
        for column in range(30):
            # row is 0 when and column is 0 x and y is 5x5
            x = 10 * column + 305  # Instead of zero, calculate the proper x location using 'column'
            y = 10 * row + 5  # Instead of zero, calculate the proper y location using 'row'
            if column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.CHINESE_RED)


def draw_section_3():
    # Use the modulus operator and an if/else statement to select the color.
    # Don't use multiple 'if' statements.
    for row in range(30):
        for column in range(30):
            # row is 0 when and column is 0 x and y is 5x5
            x = 10 * column + 605  # Instead of zero, calculate the proper x location using 'column'
            y = 10 * row + 5  # Instead of zero, calculate the proper y location using 'row'
            if row % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.CHINESE_RED)


def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
    for row in range(30):
        for column in range(30):
            # row is 0 when and column is 0 x and y is 5x5
            x = 10 * column + 905  # Instead of zero, calculate the proper x location using 'column'
            y = 10 * row + 5  # Instead of zero, calculate the proper y location using 'row'
            if row % 2 == 0 or column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.CHINESE_RED)


def draw_section_5():
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
    for row in range(30):
        for column in range(row + 1):
            # row is 0 when and column is 0 x and y is 5x5
            x = 10 * (30 - column) + 5  # Instead of zero, calculate the proper x location using 'column'
            y = 10 * (29 - row) + 305  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.MAGENTA_HAZE)


def draw_section_6():
    for row in range(30):
        for column in range(row + 1):
            # row is 0 when and column is 0 x and y is 5x5
            x = 10 * column + 305  # Instead of zero, calculate the proper x location using 'column'
            y = 10 * (29 - row) + 305  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.MAGENTA_HAZE)


def draw_section_7():
    for row in range(30):
        for column in range(row + 1):
            # row is 0 when and column is 0 x and y is 5x5
            x = 10 * column + 605  # Instead of zero, calculate the proper x location using 'column'
            y = 10 * row + 305  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.COCOA_BROWN)


def draw_section_8():
    for row in range(30):
        for column in range(row + 1):
            # row is 0 when and column is 0 x and y is 5x5
            x = 10 * (29 - column) + 905  # Instead of zero, calculate the proper x location using 'column'
            y = 10 * row + 305  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.ARMY_GREEN)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()
