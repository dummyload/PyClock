"""
Module containing the base class for the PyClock and its various
interfaces.
"""


# STDLIB IMPORTS
from datetime import datetime

# THIRD PARTY IMPORTS
from gobject import timeout_add
from gtk import DrawingArea, main_quit, WIN_POS_CENTER, Window
from gtk.gdk import Rectangle


class _BasePyClock(Window):
    """
    Base class for PyClock.
    """

    def __init__(self, title):
        """
        Instantiate an instance of _BasePyClock.
        """
        super(_BasePyClock, self).__init__()

        self.set_title(title=title)
        self.resize(width=230, height=230)
        self.set_position(position=WIN_POS_CENTER)
        self.connect("destroy", main_quit)

        self._time = datetime.now()

        self._draw_area = DrawingArea()
        self._draw_area.connect("expose-event", self._expose)
        self.add(self._draw_area)

        timeout_add(1000, self._update)

        self.show_all()

    def _expose(self, *arg):
        """
        Method used to draw on to the canvas.
        """
        print "'_expose()' needs implementing"

    def _redraw_canvas(self):
        """
        Redraw the canvas to make it look as thought the hands are
        ticking.
        """
        if self.window:
            dimensions = self.get_allocation()
            rect = Rectangle(width=dimensions.width,
                             height=dimensions.height)
            self.window.invalidate_rect(rect, True)
            self.window.process_updates(True)

    def _update(self):
        """
        Get the current time of the machine and set the class _TIME
        property so that the canvas willbe updated.

        @rtype: bool
        @return: Return True to ensure that the timer object will fire
            again.
        """
        self._time = datetime.now()
        self._redraw_canvas()

        # returning True ensures that the timer object will fire again.
        return True
