#!/usr/bin/python

"""
Binary clock using PyGTK2.
"""


# STDLIB IMPORTS
from math import pi

# THIRD PARTY IMPORTS
from gtk.gdk import Color
import gtk

# LOCAL IMPORTS
from _BasePyClock import _BasePyClock


class BinaryPyClock(_BasePyClock):
    """
    Class implementing a clock with a binary interface.
    """

    _LED_RADIUS = 10

    def __init__(self, led_colour="#EE0000"):
        """
        Instantiate an instance of BinaryPyClock.

        @type led_colour: str
        @param led_colour: Colour of the LED's.
            DEFAULT: #FF0000
        """
        super(BinaryPyClock, self).__init__(title="Binary PyClock")

        color_obj = Color(led_colour)
        self._led_red = color_obj.red / 65535.0
        self._led_green = color_obj.green / 65535.0
        self._led_blue = color_obj.blue / 65535.0

    def _expose(self, *args):
        """
        Method used to draw on to the canvas.
        """
        self._context = self._draw_area.window.cairo_create()
        content_area = gtk.gdk.Rectangle(width=self.allocation.width,
                                         height=self.allocation.height)
        self._context.rectangle(content_area)
        self._context.clip()

        self._draw_clock()

    def _draw_clock(self):
        """
        Draw the clock, i.e. the LEDs
        """
        self._draw_year_leds()
        self._draw_hour_leds()
        self._draw_minute_leds()
        self._draw_second_leds()

    def _draw_leds(self, binary, y_pos):
        """
        Draw the LEDs to display the binary for a particular time
        component.

        @type binary: str
        @param binary: Binary representation of the time component.

        @type y_pos: int
        @param y_pos: Center point of LED along the Y axis.
        """
        # iterate of the bits to draw the LEDs.
        for bit in range(len(binary)):

            # work out the X position of the LED
            led_x_center = self._get_led_x_pos(led_pos=bit)

            self._context.arc(led_x_center, y_pos, self._LED_RADIUS, 0, 2 * pi)

            # LED on
            if binary[bit] == "1":
                self._context.set_source_rgb(self._led_red, self._led_green,
                                             self._led_blue)

            # LED off
            else:
                self._context.set_source_rgb(0.0, 0.0, 0.0)

            self._context.fill_preserve()
            self._context.set_source_rgb(0.0, 0.0, 0.0)

            self._context.stroke()

    def _get_led_x_pos(self, led_pos):
        """
        Return the X position of an LED.

        @type led_pos: int
        @param led_pos: LED position

        @rtype: int
        @return: Center point of the LED along the X axis.
        """
        return (led_pos * self._LED_RADIUS * 4) + (self._LED_RADIUS * 2)

    def _draw_year_leds(self):
        """
        Draw the year
        @return:
        """
        year = self._time.year

    def _draw_hour_leds(self):
        """
        Draw the LEDs to display the hours.
        """
        hour = self._time.hour

        # convert the string hours to a binary string. Remove the
        # '0b' from the beginning of the string and ensure that the
        # number of binary bits equals 5.
        bin_hour = bin(int(hour))[2:].zfill(5)

        self._draw_leds(binary=bin_hour, y_pos=140)

    def _draw_minute_leds(self):
        """
        Draw the LEDs to display the minutes.
        """
        minute = self._time.minute

        # convert the string minutes to a binary string. Remove the
        # '0b' from the beginning of the string and ensure that the
        # number of binary bits equals 6.
        bin_min = bin(int(minute))[2:].zfill(6)

        self._draw_leds(binary=bin_min, y_pos=180)

    def _draw_second_leds(self):
        """
        Draw the LEDs to display the seconds.
        """
        seconds = self._time.second

        # convert the string seconds to a binary string. Remove the
        # '0b' from the beginning of the string and ensure that the
        # number of binary bits equals 6.
        bin_sec = bin(int(seconds))[2:].zfill(6)

        self._draw_leds(binary=bin_sec, y_pos=220)


if __name__ == "__main__":
    BinaryPyClock()

    gtk.main()
