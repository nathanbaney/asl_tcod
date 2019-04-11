# Make sure 'arial10x10.png' is in the same directory as this script.
import tcod
import tcod.event
import hextile

#Global Stuff
WINDOW_WIDTH = 80
WINDOW_HEIGHT = 60

# Setup the font.
tcod.console_set_custom_font(
    "arial10x10.png",
    tcod.FONT_LAYOUT_TCOD | tcod.FONT_TYPE_GREYSCALE,
)
# Initialize the root console in a context.
with tcod.console_init_root(WINDOW_WIDTH, WINDOW_HEIGHT, order="F") as root_console:
    root_console.print_(x=0, y=0, string='Hello World!')
    while True:
        tcod.console_flush()  # Show the console.
        for event in tcod.event.wait():
            if event.type == "QUIT":
                raise SystemExit()
    # The libtcod window will be closed at the end of this with-block.
