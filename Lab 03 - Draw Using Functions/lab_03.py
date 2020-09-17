import arcade
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_luna(x, y):
    """ Draw a moon """

    # Moon
    arcade.draw_circle_filled(x, y, 40, arcade.csscolor.LIGHT_GRAY)
    arcade.draw_circle_filled(x, y + 25, 10, arcade.csscolor.GRAY)
    arcade.draw_circle_filled(x - 5, y + 15, 10, arcade.csscolor.GRAY)
    arcade.draw_circle_filled(x - 25, y + 5, 5, arcade.csscolor.GRAY)
    arcade.draw_circle_filled(x + 25, y + 20, 7, arcade.csscolor.GRAY)
    arcade.draw_circle_filled(x - 15, y - 25, 8, arcade.csscolor.GRAY)
    arcade.draw_circle_filled(x + 25, y - 5, 10, arcade.csscolor.GRAY)

def draw_stars():
    """ Draw the stars """

    # Stars
    arcade.draw_circle_filled(100, 550, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(175, 450, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(195, 500, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(165, 590, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(300, 500, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(600, 540, 2, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(500, 495, 2, arcade.csscolor.WHITE)

def draw_water():
    """ Draw the ground """

    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 2, 0, arcade.csscolor.DARK_BLUE)

def draw_buoy(x, y):
    """ Draw a buoy"""

    # The float
    arcade.draw_lrtb_rectangle_filled(540 + x, 610 + x, 220 + y, 200 + y, arcade.csscolor.ORANGE_RED)

    # The body
    arcade.draw_triangle_filled(550 + x, 220 + y, 600 + x, 220 + y, 575 + x, 260 + y, arcade.csscolor. ORANGE_RED)

    # The light
    arcade.draw_circle_filled(575 + x, 268 + y, 8, arcade.csscolor.GOLD)

def draw_destroyer(x, y):
    """ Draw a destroyer """

    # The hull
    arcade.draw_polygon_filled(((200 + x, 350 + y), (600 + x, 350 + y), (500 + x, 300 + y), (300 + x, 300 + y)), arcade.csscolor.GRAY)

    # Main gun
    arcade.draw_lrtb_rectangle_filled(520 + x, 600 + x, 370 + y, 363 + y, arcade.csscolor.DARK_CYAN)
    arcade.draw_polygon_filled(((510 + x, 375 + y), (535 + x, 375 + y), (560 + x, 350 + y), (510 + x, 350 + y)), arcade.csscolor.CADET_BLUE)

    # Cab
    arcade.draw_lrtb_rectangle_filled(375 + x, 475 + x, 400 + y, 350 + y, arcade.csscolor.GRAY)

    # Window
    arcade.draw_circle_filled(400 + x, 375 + y, 7, arcade.csscolor.BLACK)

    # Window 2
    arcade.draw_lrtb_rectangle_filled(427 + x, 465 + x, 380 + y, 370 + y, arcade.csscolor.LIGHT_YELLOW)

    # Spotlight
    arcade.draw_lrtb_rectangle_filled(220 + x, 255 + x, 380 + y, 355 + y, arcade.csscolor.SLATE_GRAY)
    arcade.draw_ellipse_filled(220 + x, 368 + y, 5, 20, arcade.csscolor.YELLOW)
    arcade.draw_triangle_filled(240 + x, 370 + y, 220 + x, 350 + y, 260 + x, 350 + y, arcade.csscolor.CADET_BLUE)
    arcade.draw_polygon_filled(((x, 450 + y), (220 + x, 375 + y), (220 + x, 360 + y), (x, 330 + y)), arcade.csscolor.LIGHT_GOLDENROD_YELLOW)

def main():

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "NAVAL ARMADA")
    arcade.set_background_color(arcade.color.BLACK)

    arcade.start_render()

    draw_water()
    draw_destroyer(0, 0)
    draw_destroyer(-200, -150)
    draw_destroyer(-50, -300)
    draw_luna(750, 550)
    draw_stars()
    draw_buoy(0, 0)
    draw_buoy(-450, 40)
    draw_buoy(75, -100)

    arcade.finish_render()

    arcade.run()

main()
