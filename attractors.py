import numpy as np
# Lorenz
def Lorenz(x, y, z):
    sigma = 10
    beta = 8/3
    rho = 28
    dt = 0.02

    dx = (sigma*(y-x))*dt
    dy = (x*(rho-z)-y)*dt
    dz = (x*y - beta*z)*dt

    return x+dx,y+dy,z+dz

# Thomas
def Thomas(x, y, z):
    b = 0.208186
    dt = 1

    dx = (np.sin(y)-b*x)*dt
    dy = (np.sin(z)-b*y)*dt
    dz = (np.sin(x)-b*z)*dt

    return x+dx,y+dy,z+dz