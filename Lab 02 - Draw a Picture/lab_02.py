import arcade
arcade.open_window(800, 600, "USS Hannibal")
arcade.set_background_color(arcade.csscolor.BLACK)

arcade.start_render()

# The Water
arcade.draw_lrtb_rectangle_filled(0, 799, 300, 0, arcade.csscolor.DARK_BLUE)

# The hull
arcade.draw_polygon_filled(((200, 350), (600, 350), (500, 300), (300, 300)), arcade.csscolor.GRAY)

# Main Gun
arcade.draw_lrtb_rectangle_filled(520, 600, 370, 363, arcade.csscolor.DARK_CYAN)
arcade.draw_polygon_filled(((510, 375), (535, 375), (560, 350), (510, 350)), arcade.csscolor.CADET_BLUE)

# Cab
arcade.draw_lrtb_rectangle_filled(375, 475, 400, 350, arcade.csscolor.GRAY)

# Window
arcade.draw_circle_filled(400, 375, 7, arcade.csscolor.BLACK)

# Window 2
arcade.draw_lrtb_rectangle_filled(427, 465, 380, 370, arcade.csscolor.LIGHT_YELLOW)

# Spotlight
arcade.draw_lrtb_rectangle_filled(220, 255, 380, 355, arcade.csscolor.SLATE_GRAY)
arcade.draw_ellipse_filled(220, 368, 5, 20, arcade.csscolor.YELLOW)
arcade.draw_triangle_filled(240, 370, 220, 350, 260, 350, arcade.csscolor.CADET_BLUE)
arcade.draw_polygon_filled(((0, 450), (220, 375), (220, 360), (0, 330)), arcade.csscolor.LIGHT_GOLDENROD_YELLOW)

# Moon
arcade.draw_circle_filled(750, 550, 40, arcade.csscolor.LIGHT_GRAY)
arcade.draw_circle_filled(750, 575, 10, arcade.csscolor.GRAY)
arcade.draw_circle_filled(745, 565, 10, arcade.csscolor.GRAY)
arcade.draw_circle_filled(725, 555, 5, arcade.csscolor.GRAY)
arcade.draw_circle_filled(775, 570, 7, arcade.csscolor.GRAY)
arcade.draw_circle_filled(735, 525, 8, arcade.csscolor.GRAY)
arcade.draw_circle_filled(775, 545, 10, arcade.csscolor.GRAY)

# Stars
arcade.draw_circle_filled(100, 550, 2, arcade.csscolor.WHITE)
arcade.draw_circle_filled(175, 450, 2, arcade.csscolor.WHITE)
arcade.draw_circle_filled(195, 500, 2, arcade.csscolor.WHITE)
arcade.draw_circle_filled(165, 590, 2, arcade.csscolor.WHITE)
arcade.draw_circle_filled(300, 500, 2, arcade.csscolor.WHITE)
arcade.draw_circle_filled(600, 540, 2, arcade.csscolor.WHITE)
arcade.draw_circle_filled(500, 495, 2, arcade.csscolor.WHITE)


arcade.finish_render()

arcade.run()
