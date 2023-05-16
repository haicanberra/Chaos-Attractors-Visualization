from config import *
from attractors import *

# Different scale for attractors
def get_scale(attractorName):
    match attractorName:
        case "LORENZ":
            return LORENZ_SCALE
        case "THOMAS":
            return THOMAS_SCALE

# Update xyz
def update_xyz(x, y, z, attractorName):
    match attractorName:
        case "LORENZ":
            return Lorenz(x, y, z)
        case "THOMAS":
            return Thomas(x, y, z)
        
