#!/usr/bin/python


from math import cos, pi, sin
import gtk


class PyClock(gtk.Window):
    """

    """

    def __init__(self):
        """
        Instantiate an instance of PyClock.
        """
        super(PyClock, self).__init__()

        self.set_title("PyClock")
        self.resize(230, 230)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)

        self._draw_area = gtk.DrawingArea()

        self._draw_area.connect("expose-event", self._expose)
        self.add(self._draw_area)

        self.show_all()

    def _expose(self, *arg):
        """

        """
        self._context = self._draw_area.window.cairo_create()
        self._context.rectangle(0, 0, self.allocation.width, self.allocation.height)
        self._context.clip()

        self._draw_clock_face()

        return False

    def _draw_clock_face(self):
        """
        Draw the clock face.
        """
        dimensions = self.get_allocation()

        # get the centre point of the window.
        center_x = dimensions.x + dimensions.width / 2
        center_y = dimensions.y + dimensions.height / 2

        # ensure the circle stays, well, a circle!
        radius = min(dimensions.width / 2,
                     dimensions.height / 2) - 5

        # clock back
        self._context.arc(center_x, center_y, radius, 0, 2 * pi)
        # main circle
        self._context.set_source_rgb(1, 1, 1)
        self._context.fill_preserve()
        # circle outline
        self._context.set_source_rgb(0, 0, 0)
        self._context.stroke()

        # draw the hour ticks
        for tick in range(12):
            self._context.save()

            if tick % 3 == 0:
                inset = 0.2 * radius
            else:
                inset = 0.1 * radius

            self._context.move_to(center_x + (radius - inset) * cos(tick * pi / 6),
                                  center_y + (radius - inset) * sin(tick * pi / 6))
            self._context.line_to(center_x + radius * cos(tick * pi / 6),
                                  center_y + radius * sin(tick * pi / 6))
            self._context.stroke()
            self._context.restore()


if __name__ == "__main__":
    PyClock()

    gtk.main()
