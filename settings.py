# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024      # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 736  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 35
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
BOARD = [[]]
print(f"height{GRIDHEIGHT}")
print(f"width{GRIDWIDTH}")
for y in range(0, int(GRIDWIDTH)):
    if y > 0:
        BOARD.append([])
    for x in range(0, int(GRIDHEIGHT)):
        BOARD[y].append(0)
