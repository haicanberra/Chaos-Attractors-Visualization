import numpy as np
# Limit max iterations
THROTTLE = True
THRESHOLD = 100000

# Colors
BACKGROUND = (10,10,0)
PARTICLE = (np.random.randint(255), np.random.randint(255), np.random.randint(255))

# Canvas
WIDTH, HEIGHT = 1280, 720
FPS = 144

# Camera Rotation
DEFAULT_ANGLE = 90
ANGLE = DEFAULT_ANGLE
dANGLE = 0.001

# Attractor settings
ATTRACTOR = ["LORENZ", "THOMAS"]
CURRENT_INDEX = 0
MAX_INDEX = len(ATTRACTOR)

# Attractor scales
LORENZ_SCALE = 10
THOMAS_SCALE = 50

# Particles
SIZE = 1
NUM_PARTICLES = 1
RANDOM_LOCATION = True

# Matrices
projMat = np.array([[1, 0, 0],
                    [0, 1, 0]])
DEFAULT_X, DEFAULT_Y, DEFAULT_Z = 0.01, 0, 0
x, y, z = DEFAULT_X, DEFAULT_Y, DEFAULT_Z
points = np.array([[[x], [y], [z]]])
if NUM_PARTICLES > 1 and RANDOM_LOCATION:
    for _ in range(NUM_PARTICLES-1):
        x, y, z = 10*(np.random.rand()-0.5), 10*(np.random.rand()-0.5), 10*(np.random.rand()-0.5)
        points = np.append(points, np.array([[[x], [y], [z]]]), axis=0)
    

