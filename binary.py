#!/usr/bin/python

"""
Binary clock using PyGTK2.
"""


# STDLIB IMPORTS

# THIRD PARTY IMPORTS
import gtk

# LOCAL IMPORTS
from _BasePyClock import _BasePyClock


class BinaryPyClock(_BasePyClock):
    """
    Class implementing a clock with a binary interface.
    """

    def __init__(self, led_colour="red"):
        """
        Instantiate an instance of BinaryPyClock.

        @type led_colour: str
        @param led_colour: Colour of the LED's.
            DEFAULT: red
        """
        super(BinaryPyClock, self).__init__(title="Binary PyClock")

        self._led_colour = led_colour

    def _expose(self, *args):
        """
        Method used to draw on to the canvas.
        """

if __name__ == "__main__":
    BinaryPyClock()

    gtk.main()
