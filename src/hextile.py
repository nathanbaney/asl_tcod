# individual hexagon on the map, basically a tdl Window with
# troop information, terrain, etc that gets drawn to consoles
from enum import Enum
import tcod

class TerrainType(Enum):
    FIELDS = 1
    FOREST = 2

class Hex:
    units = []
    terrain = TerrainType.FIELDS

    
