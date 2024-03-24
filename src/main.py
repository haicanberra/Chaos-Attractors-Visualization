import pygame, os, sys, numpy as np
from config import *
from attractors import *
from utils import *

if __name__ == "__main__":
    os.environ["SDL_VIDEO_CENTERED"]='1'

    pygame.init()
    
    pygame.display.set_caption(ATTRACTOR[CURRENT_INDEX] + " Attractor")
    canvas = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock() 

    if os.path.exists('font.ttf'):
        font = pygame.font.Font('font.ttf', 32)
    else:
        font = pygame.font.SysFont('arial', 32)

    running = True
    maxed = False
    set_default(ATTRACTOR[CURRENT_INDEX])
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
                    set_default(ATTRACTOR[CURRENT_INDEX])
                if event.key == pygame.K_d:
                    temp = CURRENT_INDEX
                    from config import *
                    CURRENT_INDEX = temp
                    maxed = False
                    if CURRENT_INDEX == MAX_INDEX-1:
                        CURRENT_INDEX = 0
                    else:
                        CURRENT_INDEX = CURRENT_INDEX + 1
                    set_default(ATTRACTOR[CURRENT_INDEX])
        title = ATTRACTOR[CURRENT_INDEX].swapcase()
        title = title.title()
        pygame.display.set_caption(title + " Attractor")
        text = font.render(title, True, PARTICLE)
        canvas.fill(BACKGROUND)
        canvas.blit(text, (50, HEIGHT//2-32))
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
            init_points_copy = init_points.copy()
            for i in range(len(init_points_copy)):
                x, y, z = update_xyz(init_points_copy[i][-1][0][0], init_points_copy[i][-1][1][0], init_points_copy[i][-1][2][0], ATTRACTOR[CURRENT_INDEX])
                init_points[i] = np.append(init_points[i], np.array([[[x], [y], [z]]]), axis=0)

        for ip in init_points:
            for p in init_points[ip]:
                rot2d = np.dot(rotX, np.dot(rotY, np.dot(rotZ, p)))
                proj2d = np.dot(projMat, rot2d)
                scale = get_scale(ATTRACTOR[CURRENT_INDEX])
                x_ = int(proj2d[0][0] * scale) + WIDTH//2
                y_ = int(proj2d[1][0] * scale) + HEIGHT//2
                pygame.draw.circle(canvas, PARTICLE, (x_, y_), SIZE)

        pygame.display.update()

        if THROTTLE:
            if init_points[0].shape[0] >= THRESHOLD:
                maxed = True

    pygame.quit()
    sys.exit()
