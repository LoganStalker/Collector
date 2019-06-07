from collections import namedtuple

# display settings
WIN_WIDTH = 640
WIN_HEIGHT = 480

# colors
Colors = namedtuple('Colors', ['background_fill', 'hero1'])
COLORS = Colors(
    background_fill=(80, 80, 190),
    hero1=(200, 100, 0),
)