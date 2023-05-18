from config import *
from attractors import *
import numpy as np

# Set default xyz
def set_default(attractorName):
    x, y, z = get_default(attractorName)
    if NUM_PARTICLES > 1:
        for i in range(NUM_PARTICLES):
            x, y, z = x+np.random.rand()-0.5, y+np.random.rand()-0.5, z+np.random.rand()-0.5
            init_points[i] = np.array([[[x], [y], [z]]])
    elif NUM_PARTICLES == 1:
        init_points[0] = np.array([[[x], [y], [z]]])

# Get default xyz
def get_default(attractorName):
    match attractorName:
        case "LORENZ":
            return 1.1, 2, 7
        case "THOMAS":
            return 1.1, 1.1, -0.01
        case "AIZAWA":
            return 1, 1, 1
        case "DADRAS":
            return 1.1, 2.1, -2
        case "CHEN":
            return 5, 10, 10
        case "ROSSLER":
            return 1, 10, 0.50
        case "HALVORSEN":
            return -1.48, -1.51, 2.04
        case "RABINOVICH FABRIKANT":
            return -1, 0.00001, 0.5
        case "THREE SCROLL UNIFED":
            return -0.29, -0.25, -0.59
        case "SPROTT":
            return 0.65, 0.07, 0.01
        case "FOUR WING":
            return 1.3, -0.18, 0.01

# Different scale for attractors
def get_scale(attractorName):
    match attractorName:
        case "LORENZ":
            return LORENZ_SCALE
        case "THOMAS":
            return THOMAS_SCALE
        case "AIZAWA":
            return AIZAWA_SCALE
        case "DADRAS":
            return DADRAS_SCALE
        case "CHEN":
            return CHEN_SCALE
        case "ROSSLER":
            return ROSSLER_SCALE
        case "HALVORSEN":
            return HALVORSEN_SCALE
        case "RABINOVICH FABRIKANT":
            return RABINOVICH_FABRIKANT_SCALE
        case "THREE SCROLL UNIFED":
            return THREE_SCROLL_UNIFED_SCALE
        case "SPROTT":
            return SPROTT_SCALE
        case "FOUR WING":
            return FOUR_WING_SCALE

# Update xyz
def update_xyz(x, y, z, attractorName):
    match attractorName:
        case "LORENZ":
            return Lorenz(x, y, z)
        case "THOMAS":
            return Thomas(x, y, z)
        case "AIZAWA":
            return Aizawa(x, y, z)
        case "DADRAS":
            return Dadras(x, y, z)
        case "CHEN":
            return Chen(x, y, z)
        case "ROSSLER":
            return Rossler(x, y, z)
        case "HALVORSEN":
            return Halvorsen(x, y, z)
        case "RABINOVICH FABRIKANT":
            return Rabinovich_Fabrikant(x, y, z)
        case "THREE SCROLL UNIFED":
            return Three_Scroll_Unifed(x, y, z)
        case "SPROTT":
            return Sprott(x, y, z)
        case "FOUR WING":
            return Four_Wing(x, y, z)
        