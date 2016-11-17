#!/usr/bin/python

"""
Digital clock implemented in GTK2.
"""


# STDLIB IMPORTS
from math import pi

# THIRD PARTY IMPORTS
from gtk import main
from gtk.gdk import Color, color_parse
import gtk

# LOCAL IMPORTS
from _BasePyClock import BasePyClock


class DigitalPyClock(BasePyClock):
    """
    Class implementing the DigitalPyClock.
    """

    def __init__(self, led_colour="red"):
        """
        Instantiate an instance of DigitalPyClock.
        """
        super(DigitalPyClock, self).__init__(title="Digital PyClock")

        self._colour_obj = color_parse(spec=led_colour)
        self._led_red = self._colour_obj.red / 65535.0
        self._led_green = self._colour_obj.green / 65535.0
        self._led_blue = self._colour_obj.blue / 65535.0

    def _expose(self, *args):
        """
        Method used to draw on to the canvas.

        Overrides the base class: Uses a different method to draw.
        """
        self._context = self._draw_area.window.new_gc()

        # self._context.set_rgb_fg_color(self._colour_obj)
        # self._draw_area.window.draw_arc(gc=self._context, filled=True,
        #                                 x=100, y=100, width=20, height=20,
        #                                 angle1=0, angle2=360*64)

        self._draw_h_led(start_x=100, start_y=100)

    def _draw_h_led(self, start_x, start_y, fill=True):
        """
        Draw a horizontal LED: <=>

        @type start_x: int
        @param start_x: Point on the X axis to start drawing the LED
            from.

        @type start_y: int
        @param start_y: Point on the Y axis to start drawing the LED
            from.

        @type fill: bool
        @param fill: If True, set the colour of the LED to the
            colour_obj instance variable, else set the colour to black.
        """
        if fill:
            self._context.set_rgb_fg_color(self._colour_obj)
        else:
            _colour_obj = Color(red=self._led_red * 0.325,
                                green=self._led_green * 0.325,
                                blue=self._led_blue * 0.325)
            self._context.set_rgb_fg_color(_colour_obj)

            self._context.line_width = 6
            points = [(start_x, start_y), (start_x + 20, start_y + 20),
                      (start_x + 40, start_y + 20), (start_x + 60, start_y),
                      (start_x + 40, start_y - 20), (start_x + 20, start_y - 20),
                      (start_x, start_y)]

            self._draw_area.window.draw_polygon(gc=self._context,
                                                filled=True,
                                                points=points)

    def _draw_clock(self):
        """
        Draw the clock.
        """




if __name__ == "__main__":
    DigitalPyClock()

    main()
