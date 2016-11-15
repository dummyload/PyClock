#!/usr/bin/python


"""

"""


# STDLIB IMPORTS
from argparse import ArgumentParser

# THIRD PARTY IMPORTS
from gtk import main

# LOCAL IMPORTS
from analogue import AnaloguePyClock


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

    _args = parser.parse_args()

    return {'interface': _args.interface}


if __name__ == "__main__":
    args = _parse_arguments()

    interface = args.get("interface")

    if interface == "binary":
        pass
    elif interface == "digital":
        pass
    else:
        clock = AnaloguePyClock()

    main()
