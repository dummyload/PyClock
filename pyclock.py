#!/usr/bin/python


"""
Analogue clock using PyGTK2.
"""


from datetime import datetime
from gtk.gdk import Rectangle
from gobject import timeout_add
from math import cos, pi, sin
import gtk


class PyClock(gtk.Window):
    """
    Main class for PyClock.
    """

    @property
    def _TIME(self):
        """
        Time property.
        """
        return self._time

    @_TIME.setter
    def _TIME(self, the_time):
        self._time = the_time
        self.redraw_canvas()

    def __init__(self):
        """
        Instantiate an instance of PyClock.
        """
        super(PyClock, self).__init__()

        self.set_title("PyClock")
        self.resize(230, 230)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)

        self._time = None
        self._update()

        self._draw_area = gtk.DrawingArea()

        self._draw_area.connect("expose-event", self._expose)
        self.add(self._draw_area)

        timeout_add(1000, self._update)

        self.show_all()

    def _expose(self, *arg):
        """

        """
        self._context = self._draw_area.window.cairo_create()
        self._context.rectangle(0, 0, self.allocation.width,
                                self.allocation.height)
        self._context.clip()

        dimensions = self.get_allocation()

        # get the center point of the window.
        self._center_x = dimensions.x + dimensions.width / 2
        self._center_y = dimensions.y + dimensions.height / 2

        # ensure the circle remains a circle when resizing the window,
        # with about a 5 pixel padding from any edge.
        self._radius = min(dimensions.width /2,
                           dimensions.height / 2) - 5

        self._draw_clock_face()
        self._draw_hands()

        return False

    def _draw_clock_face(self):
        """
        Draw the clock face.
        """
        # clock background
        #
        self._context.arc(self._center_x, self._center_y, self._radius,
                          0, 2 * pi)
        # main circle
        self._context.set_source_rgb(1, 1, 1)
        self._context.fill_preserve()
        # circle outline
        self._context.set_source_rgb(0, 0, 0)
        self._context.stroke()

        # draw the hour ticks
        for tick in range(12):
            self._context.save()

            # if the tick falls on a quarter, extend the line slightly.
            if tick % 3 == 0:
                # accentuate the quarter lines by making them slightly
                # wider (thicker) than the others and changing the
                # colour of the line.
                self._context.set_line_width(4)
                self._context.set_source_rgb(0.7, 0.2, 0.0)
                inset = 0.2 * self._radius
            else:
                inset = 0.1 * self._radius

            self._context.move_to(self._center_x + (self._radius - inset) * cos(tick * pi / 6),
                                  self._center_y + (self._radius - inset) * sin(tick * pi / 6))
            self._context.line_to(self._center_x + self._radius * cos(tick * pi / 6),
                                  self._center_y + self._radius * sin(tick * pi / 6))
            self._context.stroke()
            self._context.restore()

    def _draw_hands(self):
        """
        Draw the hands of the clock.
        """
        # get the hour, minute and second from the time instance
        # variable.
        self._draw_hour_hand()
        self._draw_minute_hand()
        self._draw_second_hand()

    def _draw_hour_hand(self):
        """
        Draw the hour hand.
        """
        hour = self._time.hour
        minute = self._time.minute

        # the hour hand is rotated 30 degrees (pi/6 r) per hour + 1/2 a
        # degree (pi/360) per minute.
        self._context.save()
        self._context.set_line_width(2.5 * self._context.get_line_width())

        # move cursor to the center of the drawing area in preparation
        # to draw the hour hand.
        self._context.move_to(self._center_x, self._center_y)
        # draw the how hand.
        self._context.line_to(
            self._center_x + self._radius / 2 * sin(pi /6 * hour + pi / 360 * minute),
            self._center_y + self._radius / 2 * -cos(pi /6 * hour + pi / 360 * minute))
        self._context.stroke()
        self._context.restore()

    def _draw_minute_hand(self):
        """
        Draw the minute hand.
        """
        minute = self._time.minute

        # the minute hand is rotated 6 degrees (pi/30 r) per minute.
        self._context.save()
        self._context.move_to(self._center_x, self._center_y)

        self._context.line_to(self._center_x + self._radius * 0.75 * sin(pi / 30 * minute),
                              self._center_y + self._radius * 0.75 * -cos(pi / 30 * minute))

        self._context.stroke()
        self._context.restore()

    def _draw_second_hand(self):
        """
        Draw the second hand.
        """
        second = self._time.second

        # operates similar to the second hand:
        # rotated 6 degrees (pi/30 r) per minute.
        self._context.save()

        # differentiate the second hand from the minute hand by
        # changing the colour of the line.
        self._context.set_source_rgb(1.0, 0.0, 0.0)

        self._context.move_to(self._center_x, self._center_y)

        self._context.line_to(self._center_x + self._radius * 0.75 * sin(pi / 30 * second),
                              self._center_y + self._radius * 0.75 * -cos(pi / 30 * second))

        self._context.stroke()
        self._context.restore()

    def redraw_canvas(self):
        """
        Redraw the canvas to make it look as thought the hands are
        ticking.
        """
        if self.window:
            dimensions = self.get_allocation()
            rect = Rectangle(0, 0, dimensions.width, dimensions.height)
            self.window.invalidate_rect(rect, True)
            self.window.process_updates(True)

    def _update(self):
        """
        Get the current time of the machine.
        """
        self._TIME = datetime.now()

        # returning True ensures that the timer object will fire again.
        return True


if __name__ == "__main__":
    PyClock()

    gtk.main()
