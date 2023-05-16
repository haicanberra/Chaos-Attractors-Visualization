import pygame, os, numpy as np
from config import *
from attractors import *
from utils import *

if __name__ == "__main__":
    os.environ["SDL_VIDEO_CENTERED"]='1'

    pygame.init()
    
    pygame.display.set_caption(ATTRACTOR[CURRENT_INDEX] + " Attractor")
    canvas = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock() 

    running = True
    maxed = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_a:
                    temp = CURRENT_INDEX
                    from config import *
                    CURRENT_INDEX = temp
                    maxed = False
                    if CURRENT_INDEX == 0:
                        CURRENT_INDEX = MAX_INDEX-1
                    else:
                        CURRENT_INDEX = CURRENT_INDEX - 1
                if event.key == pygame.K_d:
                    temp = CURRENT_INDEX
                    from config import *
                    CURRENT_INDEX = temp
                    maxed = False
                    if CURRENT_INDEX == MAX_INDEX-1:
                        CURRENT_INDEX = 0
                    else:
                        CURRENT_INDEX = CURRENT_INDEX + 1

        canvas.fill(BACKGROUND)
        clock.tick(FPS)

        rotX = np.array([[1, 0, 0],
                [0, np.cos(ANGLE), -np.sin(ANGLE)],
                [0, np.sin(ANGLE), np.cos(ANGLE)]])

        rotY = np.array([[np.cos(ANGLE), 0, np.sin(ANGLE)],
                    [0, 1, 0],
                    [-np.sin(ANGLE), 0, np.cos(ANGLE)]])

        rotZ = np.array([[np.cos(ANGLE), -np.sin(ANGLE), 0],
                    [np.sin(ANGLE), np.cos(ANGLE), 0 ],
                    [0, 0, 1]])
        ANGLE = ANGLE + dANGLE
        
        if not maxed:
            points_copy = np.copy(points)
            if NUM_PARTICLES == 1:
                x, y, z = update_xyz(x, y, z, ATTRACTOR[CURRENT_INDEX])
                points = np.append(points, np.array([[[x], [y], [z]]]), axis=0)
            else:
                for i in range(NUM_PARTICLES):
                    [[x], [y], [z]] = points_copy[-i]
                    x, y, z = update_xyz(x, y, z, ATTRACTOR[CURRENT_INDEX])
                    points = np.append(points, np.array([[[x], [y], [z]]]), axis=0)

        for point in points:
            rot2d = np.dot(rotX, np.dot(rotY, np.dot(rotZ, point)))
            proj2d = np.dot(projMat, rot2d)
            scale = get_scale(ATTRACTOR[CURRENT_INDEX])
            x_ = int(proj2d[0][0] * scale) + WIDTH//2
            y_ = int(proj2d[1][0] * scale) + HEIGHT//2
            pygame.draw.circle(canvas, PARTICLE, (x_, y_), SIZE)

        pygame.display.update()

        if THROTTLE:
            if points.shape[0] >= THRESHOLD:
                maxed = True

    pygame.quit()
    quit()
