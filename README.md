# PyClock

## Introduction
Simple project implementing various clock interfaces; analogue, binary and digital (7 segment).

## Usage
From the directory containing the source:

```bash
python pyclock.py {options}
```

### Options

 Short | Long | Info
 --- | --- | ---
  -i | --interface | Interface type. Valid options: _**analogue**_, *binary*, *digital*
  -l | --led-colour | Colour of the LEDs for the digital and binary clock interfaces.


#### Colours
It is possible to change the colour of the 'LEDs' on both the digital and binary clock interfaces by using the *-l* or *--led-colour* flags.

 Colours can be specified as either a hex RGB (#FF00FF) or a valid name from the [X11 Color Name Chart](https://en.wikipedia.org/wiki/X11_color_names#Color_name_chart).

#### Examples
```bash
# RGB values
python pyclock -i binary -l '#DAA520'
python pyclock -i digital -l \#4B0082

# X11 colour names.
python pyclock -i digital -l indigo
python pyclock -i binary -l 'dodger blue'
```
