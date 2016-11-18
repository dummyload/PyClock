#!/usr/bin/python


"""

"""


# STDLIB IMPORTS
from argparse import ArgumentParser

# THIRD PARTY IMPORTS
from gtk import main

# LOCAL IMPORTS
from analogue import AnaloguePyClock
from binary import BinaryPyClock
from digital import DigitalPyClock


def _parse_arguments():
    """
    Parse the command line arguments.

    @rtype: dict[str, str]
    @return: Dictionary containing key/value pairs.
    """
    description = "Variety of clocks interfaces implemented in Python."
    parser = ArgumentParser(description=description)

    clock_interfaces = ['analogue', 'binary', 'digital']

    parser.add_argument("-i", "--interface", choices=clock_interfaces,
                        default='analogue')

    parser.add_argument("-l", "--led-colour", default='red', type=str)

    _args = parser.parse_args()

    return {'interface': _args.interface,
            'led_colour': _args.led_colour}


if __name__ == "__main__":
    args = _parse_arguments()

    interface = args.get("interface")

    if interface == "binary":
        clock = BinaryPyClock(led_colour=args.get("led_colour"))
    elif interface == "digital":
        clock = DigitalPyClock(led_colour=args.get("led_colour"))
    else:
        clock = AnaloguePyClock()

    try:
        main()
    except KeyboardInterrupt:
        pass
