#!/usr/bin/env python

# config.py
#
# Copyright (C) 2013, 2014 Kano Computing Ltd.
# License:   http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

game_speed = {
    's': 0.2,
    'm': 0.12,
    'f': 0.07,
}

# ASCII hex values
keys = {
    'DOWN': 0x42,
    'LEFT': 0x44,
    'RIGHT': 0x43,
    'UP': 0x41,
    'q': 0x71,
    'Q': 0x51,
    'ENTER': 0x0a,
}

apple_domain = 1000

food_values = {
    'apple': 3,
}

# For resolution <= 1080(w)
game_sizes_small = {
    's': (20, 15),
    'm': (25, 20),
    'l': (30, 25),
}

# For resolution <= 1280(w)
game_sizes_medium = {
    's': (20, 15),
    'm': (25, 20),
    'l': (35, 30),
}

# For resolution > 1280(w)
game_sizes_big = {
    's': (25, 20),
    'm': (35, 30),
    'l': (46, 40),
}

initial_size = 4
