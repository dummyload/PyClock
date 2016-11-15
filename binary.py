#!/usr/bin/python

"""
Binary clock using PyGTK2.
"""


# STDLIB IMPORTS


# THIRD PARTY IMPORTS
import gtk


class BinaryPyClock(gtk.Window):
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
        super(BinaryPyClock, self).__init__()

        self.set_title("Binary PyClock")
        self.resize(width=300, height=200)
        self.connect("destroy", gtk.main_quit)

        self.show_all()

if __name__ == "__main__":
    BinaryPyClock()

    gtk.main()
