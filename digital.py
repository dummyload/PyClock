#!/usr/bin/python

"""
Digital clock implemented in GTK2.
"""


# STDLIB IMPORTS
from math import pi

# THIRD PARTY IMPORTS
from gtk import main
from gtk.gdk import color_parse
import gtk

# LOCAL IMPORTS
from _BasePyClock import BasePyClock


# TUPLE CONTAING DICTIONARIES DETAILING WHICH SEGMENTS WILL NEED TO BE
# 'ON' TO DISPLAY A NUMBER.
SEGMENTS = (
    # Number 0:
    {"a": True, "b": True, "c": True, "d": True, "e": True, "f": True,
     "g": False},
    # Number 1:
    {"a": False, "b": True, "c": True, "d": False, "e": False, "f": False,
     "g": False},
    # Number 2:
    {"a": True, "b": True, "c": False, "d": True, "e": True, "f": False,
     "g": True},
    # Number 3:
    {"a": True, "b": True, "c": True, "d": True, "e": False, "f": False,
     "g": True},
    # Number 4:
    {"a": False, "b": True, "c": True, "d": False, "e": False, "f": True,
     "g": True},
    # Number 5:
    {"a": True, "b": False, "c": True, "d": True, "e": False, "f": True,
     "g": True},
    # Number 6:
    {"a": True, "b": False, "c": True, "d": True, "e": True, "f": True,
     "g": True},
    # Number 7:
    {"a": True, "b": True, "c": True, "d": False, "e": False, "f": False,
     "g": False},
    # Number 8:
    {"a": True, "b": True, "c": True, "d": True, "e": True, "f": True,
     "g": True},
    # Number 9:
    {"a": True, "b": True, "c": True, "d": False, "e": False, "f": True,
     "g": True})


class DigitalPyClock(BasePyClock):
    """
    Class implementing the DigitalPyClock.
    """

    _SEGMENT_ORIENTATION = {"a": 'h',
                            "b": 'v',
                            "c": 'v',
                            "d": 'h',
                            "e": 'v',
                            "f": 'v',
                            "g": 'h'}

    # segement offsets for drawing the seven segment display.
    _SEGMENT_OFFSETS = {"a": (5, 0),
                        "b": (60, 5),
                        "c": (60, 65),
                        "d": (5, 120),
                        "e": (0, 65),
                        "f": (0, 5),
                        "g": (5, 60)}

    def __init__(self, led_colour="red"):
        """
        Instantiate an instance of DigitalPyClock.
        """
        super(DigitalPyClock, self).__init__(title="Digital PyClock",
                                             init_width=640, init_height=160)

        self._colour_obj = color_parse(spec=led_colour)
        self._led_red = self._colour_obj.red / 65535.0
        self._led_green = self._colour_obj.green / 65535.0
        self._led_blue = self._colour_obj.blue / 65535.0

    def _draw_clock(self):
        """
        Draw the clock.
        """
        self._draw_hour_segments()
        self._draw_double_dots(x_pos=210, y_pos=50, y_pos2=110, radius=10)
        self._draw_minute_segments()
        self._draw_double_dots(x_pos=425, y_pos=50, y_pos2=110, radius=10)
        self._draw_second_segments()

    def _draw_hour_segments(self):
        """
        Draw the segments to display the hour.
        """
        tens = self._time.hour / 10
        units = self._time.hour % 10

        self._draw_seven_segment(number=tens, start_x=20, start_y=20)
        self._draw_seven_segment(number=units, start_x=115, start_y=20)

    def _draw_minute_segments(self):
        """
        Draw the segments to display the minutes.
        """
        tens = self._time.minute / 10
        units = self._time.minute % 10

        self._draw_seven_segment(number=tens, start_x=240, start_y=20)
        self._draw_seven_segment(number=units, start_x=335, start_y=20)

    def _draw_second_segments(self):
        """
        Draw the segments to display the seconds.
        """
        tens = self._time.second / 10
        units = self._time.second % 10

        self._draw_seven_segment(number=tens, start_x=460, start_y=20)
        self._draw_seven_segment(number=units, start_x=555, start_y=20)

    def _draw_seven_segment(self, number, start_x, start_y):
        """
        Draw the seven segment display.

          a
        f   b
          g
        e   c
          d

        @type number: int
        @param number: Number to display on the seven segment.

        @type start_x: int
        @param start_x: Point on the X axis to start drawing the
            display from.

        @type start_y: int
        @param start_y: Point on the Y axis to start drawing the
            display from.
        """
        num_segment = SEGMENTS[number]
        segments = num_segment.keys()

        for segment in segments:
            on = num_segment.get(segment, False)
            offset = self._SEGMENT_OFFSETS.get(segment)
            x_offset = offset[0]
            y_offset = offset[1]

            if self._SEGMENT_ORIENTATION.get(segment) == 'h':
                self._draw_h_led(start_x=(start_x + x_offset),
                                 start_y=(start_y + y_offset),
                                 fill=on)
            else:
                self._draw_v_led(start_x=(start_x + x_offset),
                                 start_y=(start_y + y_offset),
                                 fill=on)

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
        points = ((start_x + 10, start_y + 10), (start_x + 40, start_y + 10),
                  (start_x + 50, start_y), (start_x + 40, start_y - 10),
                  (start_x + 10, start_y - 10), (start_x, start_y))

        self._draw_segment(start_x=start_x, start_y=start_y, fill=fill,
                       points=points)

    def _draw_v_led(self, start_x, start_y, fill=True):
        """
        Draw a vertical LED:
        /\
        ||
        \/

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
        points = ((start_x + 10, start_y + 10), (start_x + 10, start_y + 40),
                  (start_x, start_y + 50), (start_x - 10, start_y + 40),
                  (start_x - 10, start_y + 10), (start_x, start_y))

        self._draw_segment(start_x=start_x, start_y=start_y, fill=fill,
                       points=points)

    def _draw_segment(self, start_x, start_y, points, fill=True):
        """
        Draw the LED.

        @type start_x: int
        @param start_x: Point on the X axis to start drawing the LED
            from.

        @type start_y: int
        @param start_y: Point on the Y axis to start drawing the LED
            from.

        @type points: ( (int, int) )
        @param points: Tuple containg tuples of X and Y coordinates
            which will be used to draw the polygon.

        @type fill: bool
        @param fill: If True, set the colour of the LED to the
            colour_obj instance variable, else set the colour to black.

        """
        self._context.save()
        # self._context.set_line_width(2.5 * self._context.get_line_width())

        self._context.move_to(start_x, start_y)

        for point in points:
            self._context.line_to(point[0], point[1])

        if fill:
            self._context.set_source_rgb(self._led_red,
                                         self._led_green,
                                         self._led_blue)
        else:
            self._context.set_source_rgb(self._led_red * 0.4,
                                         self._led_green * 0.4,
                                         self._led_blue * 0.4)

        # LED background
        self._context.fill_preserve()

        # LED outline.
        self._context.set_source_rgb(0.0, 0.0, 0.0)
        self._context.stroke()
        self._context.restore()

    def _draw_double_dots(self, x_pos, y_pos, y_pos2, radius):
        """
        Draw the double dots (:) which separate the hour, minute and
        seconds.

        @type x_pos: int
        @param x_pos: Center point along the X axis of the circle.

        @type y_pos: int
        @param y_pos: Center point along the Y axis to draw the first
            circle.

        @type y_pos2: int
        @param y_pos2: Center point along the Y axis to draw the second
            circle.

        @type radius: int
        @param radius: Radius of the dots to draw.
        """
        self._context.save()

        self._context.arc(x_pos, y_pos, radius, 0, 2 * pi)

        self._context.set_source_rgb(self._led_red, self._led_green,
                                     self._led_blue)
        self._context.fill_preserve()

        self._context.set_source_rgb(0.0, 0.0, 0.0)
        self._context.stroke()

        self._context.arc(x_pos, y_pos2, radius, 0, 2 * pi)

        self._context.set_source_rgb(self._led_red, self._led_green,
                                     self._led_blue)
        self._context.fill_preserve()

        self._context.set_source_rgb(0.0, 0.0, 0.0)
        self._context.stroke()

        self._context.restore()


if __name__ == "__main__":
    DigitalPyClock()

    main()
