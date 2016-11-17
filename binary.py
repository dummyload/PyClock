#!/usr/bin/python

"""
Binary clock using PyGTK2.
"""


# STDLIB IMPORTS
from math import pi

# THIRD PARTY IMPORTS
from gtk.gdk import Color, color_parse
import gtk

# LOCAL IMPORTS
from _BasePyClock import BasePyClock


class BinaryPyClock(BasePyClock):
    """
    Class implementing a clock with a binary interface.
    """

    _LED_RADIUS = 10
    _NUM_LEDS = 11

    def __init__(self, led_colour="red"):
        """
        Instantiate an instance of BinaryPyClock.

        @type led_colour: str
        @param led_colour: Colour of the LED's.
            DEFAULT: red
        """
        super(BinaryPyClock, self).__init__(title="Binary PyClock",
                                            init_width=440,
                                            init_height=240)

        color_obj = color_parse(spec=led_colour)
        self._led_red = color_obj.red / 65535.0
        self._led_green = color_obj.green / 65535.0
        self._led_blue = color_obj.blue / 65535.0

    def _draw_clock(self):
        """
        Draw the clock, i.e. the LEDs
        """
        self._draw_year_leds()
        self._draw_month_leds()
        self._draw_day_leds()
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
                self._context.set_source_rgb(self._led_red * 0.325,
                                             self._led_green * 0.325,
                                             self._led_blue * 0.325)

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
        Draw the LEDs to display the year.
        """
        year = self._time.year

        # convert the string years to a binary string. Remove the
        # '0b' from the beginning of the string.
        bin_year = bin(int(year))[2:]

        self._draw_leds(binary=bin_year, y_pos=20)

    def _draw_month_leds(self):
        """
        Draw the LEDs to display the month.
        """
        month = self._time.month

        # convert the string months to a binary string. Remove the
        # '0b' from the beginning of the string and ensure that the
        # number of binary bits eqauls 4.
        bin_month = bin(int(month))[2:].zfill(self._NUM_LEDS)

        self._draw_leds(binary=bin_month, y_pos=60)

    def _draw_day_leds(self):
        """
        Draw the LEDs to display the day.
        """
        day = self._time.day

        # convert the string months to a binary string. Remove the
        # '0b' from the beginning of the string and ensure that the
        # number of binary bits equals 5.
        bin_day = bin(int(day))[2:].zfill(self._NUM_LEDS)

        self._draw_leds(binary=bin_day, y_pos=100)

    def _draw_hour_leds(self):
        """
        Draw the LEDs to display the hour.
        """
        hour = self._time.hour

        # convert the string hours to a binary string. Remove the
        # '0b' from the beginning of the string and ensure that the
        # number of binary bits equals 5.
        bin_hour = bin(int(hour))[2:].zfill(self._NUM_LEDS)

        self._draw_leds(binary=bin_hour, y_pos=140)

    def _draw_minute_leds(self):
        """
        Draw the LEDs to display the minute.
        """
        minute = self._time.minute

        # convert the string minutes to a binary string. Remove the
        # '0b' from the beginning of the string and ensure that the
        # number of binary bits equals 6.
        bin_min = bin(int(minute))[2:].zfill(self._NUM_LEDS)

        self._draw_leds(binary=bin_min, y_pos=180)

    def _draw_second_leds(self):
        """
        Draw the LEDs to display the second.
        """
        seconds = self._time.second

        # convert the string seconds to a binary string. Remove the
        # '0b' from the beginning of the string and ensure that the
        # number of binary bits equals 6.
        bin_sec = bin(int(seconds))[2:].zfill(self._NUM_LEDS)

        self._draw_leds(binary=bin_sec, y_pos=220)


if __name__ == "__main__":
    BinaryPyClock()

    gtk.main()
