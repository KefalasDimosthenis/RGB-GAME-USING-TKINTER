from math import sqrt
import random


def color_diff(x, y):

    r1 = x[0]
    r2 = y[0]
    g1 = x[1]
    g2 = y[1]
    b1 = x[2]
    b2 = y[2]

    diff = abs(sqrt(((r2 - r1) ** 2) + ((g2 - g1) ** 2) + ((b2 - b1) ** 2)))
    max_diff = sqrt(255**2 + 255**2 + 255**2)
    x = (diff / max_diff) * 100
    return x


def rgb_to_Hex(rgb):
    return "#%02x%02x%02x" % rgb


def rand_color_picker():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    rgb = (r, g, b)
    return rgb
