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


class BasePyClock(Window):
    """
    Base class for PyClock.
    """

    def __init__(self, title, init_width=230, init_height=230):
        """
        Instantiate an instance of _BasePyClock.

        @type title: str
        @param title: String to be used for the window title.

        @type init_width: int
        @param init_width: Initial width of the window.
            DEFAULT: 230

        @type init_height: int
        @param init_height: Initial heigh of the window.
            DEFAULT: 230
        """
        super(BasePyClock, self).__init__()

        self.set_title(title=title)
        self.resize(width=init_width, height=init_height)
        self.set_position(position=WIN_POS_CENTER)
        self.connect("destroy", main_quit)

        self._time = datetime.now()

        self._draw_area = DrawingArea()
        self._draw_area.connect("expose-event", self._expose)
        self.add(self._draw_area)

        timeout_add(1000, self._update)

        self.show_all()

    def _expose(self, *args):
        """
        Method used to draw on to the canvas.
        """
        self._context = self._draw_area.window.cairo_create()
        content_area = Rectangle(width=self.allocation.width,
                                 height=self.allocation.height)
        self._context.rectangle(content_area)
        self._context.clip()

        self._draw_clock()

    def _draw_clock(self):
        """
        Draw the clock.

        NEEDS IMPLEMENTING IN THE INHERITING CLASS.
        """
        raise NotImplementedError

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
