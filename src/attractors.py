import numpy as np

def Thomas(x, y, z):
    b = 0.208186
    dt = 0.1

    dx = (np.sin(y)-b*x)*dt
    dy = (np.sin(z)-b*y)*dt
    dz = (np.sin(x)-b*z)*dt

    return x+dx,y+dy,z+dz

def Aizawa(x, y, z):

    a = 0.95
    b = 0.7
    c = 0.6
    d = 3.5
    e = 0.25
    f = 0.1
    dt = 0.01

    dx = ((z-b)*x-d*y)*dt
    dy = (d*x+(z-b)*y)*dt
    dz = (c+a*z-z**3/3-(x**2+y**2)*(1+e*z)+f*z*x**3)*dt

    return x+dx,y+dy,z+dz

def Lorenz(x, y, z):
    sigma = 10
    beta = 8/3
    rho = 28
    dt = 0.01

    dx = (sigma*(y-x))*dt
    dy = (x*(rho-z)-y)*dt
    dz = (x*y - beta*z)*dt

    return x+dx,y+dy,z+dz

def Dadras(x, y, z):
    a = 3
    b = 2.7
    c = 1.7
    d = 2
    e = 9
    dt = 0.01

    dx = (y-a*x+b*y*z)*dt
    dy = (c*y-x*z+z)*dt
    dz = (d*x*y-e*z)*dt

    return x+dx,y+dy,z+dz

def Chen(x, y, z):

    a = 5
    b = -10
    d = -0.38
    dt = 0.01

    dx = (a*x-y*z)*dt
    dy = (b*y + x*z)*dt
    dz = (d*z + x*y/3)*dt

    return x+dx,y+dy,z+dz

def Rossler(x, y, z):
    a = 0.2
    b = 0.2
    c = 5.7
    dt = 0.02

    dx = (-y-z)*dt
    dy = (x+a*y)*dt
    dz = (b+z*(x-c))*dt

    return x+dx,y+dy,z+dz

def Halvorsen(x, y, z):
    a = 1.89
    dt = 0.01

    dx = (-a*x-4*y-4*z-y**2)*dt
    dy = (-a*y-4*z-4*x-z**2)*dt
    dz = (-a*z-4*x-4*y-x**2)*dt

    return x+dx,y+dy,z+dz

def Rabinovich_Fabrikant(x, y, z):
    a = 0.14
    v = 0.10
    dt = 0.01

    dx = (y*(z-1+x**2)+v*x)*dt
    dy = (x*(3*z+1-x**2)+v*y)*dt
    dz = (-2*z*(a+x*y))*dt

    return x+dx,y+dy,z+dz

def Three_Scroll_Unifed(x, y, z):
    a = 32.48
    b = 45.84
    c = 1.18
    d = 0.13
    e = 0.57
    f = 14.7
    dt = 0.001

    dx = (a*(y-x)+d*x*z)*dt
    dy = (b*x-x*z+f*y)*dt
    dz = (c*z + x*y - e*x**2)*dt

    return x+dx,y+dy,z+dz

def Sprott(x, y, z):
    a = 2.07
    b = 1.79
    dt = 0.05

    dx = (y+a*x*y+x*z)*dt
    dy = (1-b*x**2+y*z)*dt
    dz = (x-x**2-y**2)*dt

    return x+dx,y+dy,z+dz

def Four_Wing(x, y, z):
    a = 0.2
    b = 0.01
    c = -0.4
    dt = 0.05

    dx = (a*x+y*z)*dt
    dy = (b*x+c*y-x*z)*dt
    dz = (-z -x*y)*dt

    return x+dx,y+dy,z+dz