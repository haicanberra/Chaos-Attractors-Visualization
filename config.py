import numpy as np
# Limit max iterations
THROTTLE = True
THRESHOLD = 100000

# Colors
BACKGROUND = (10,10,0)
PARTICLE = (np.random.randint(100,255), np.random.randint(100,255), np.random.randint(100,255))

# Canvas
WIDTH, HEIGHT = 1366, 768
FPS = 144

# Camera Rotation
DEFAULT_ANGLE = 90
ANGLE = DEFAULT_ANGLE
dANGLE = 0.001

# Attractor settings
CURRENT_INDEX = 0
LORENZ_SCALE = 10
THOMAS_SCALE = 80
AIZAWA_SCALE = 160
DADRAS_SCALE = 30
CHEN_SCALE = 30
ROSSLER_SCALE = 10
HALVORSEN_SCALE = 30
RABINOVICH_FABRIKANT_SCALE = 100
THREE_SCROLL_UNIFED_SCALE = 3
SPROTT_SCALE = 160
FOUR_WING_SCALE = 160
ATTRACTOR = ["LORENZ", "THOMAS", "AIZAWA", "DADRAS", "CHEN", "ROSSLER", "HALVORSEN", "RABINOVICH FABRIKANT", "THREE SCROLL UNIFED", "SPROTT", "FOUR WING"]
MAX_INDEX = len(ATTRACTOR)

# Particles
SIZE = 1
NUM_PARTICLES = 5

# Matrices
projMat = np.array([[1, 0, 0],
                    [0, 1, 0]])
init_points = {}
for i in range(NUM_PARTICLES):
    init_points[i] = np.empty((1,3,1))


