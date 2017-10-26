import numpy as np
import matplotlib.pyplot as plt

x_min, x_max = -2, 2                          # range of x
y_min, y_max = -2, 2                          # range of x

def f(x,y):
    return 1/2*x**2 + 1/4*y**2

def f1(x):
    return 1/2*x**2 

def f2(y):
    return 1/4*y**2



def MC(N):
    nx = np.linspace(x_min,x_max,N)
    ny = np.linspace(y_min,y_max,N)

    F1 = f1(nx)
    F2 = f2(ny)
    
    xz = 2*np.random.random(N)
    yz = np.random.random(N)
    Xz = np.delete(xz,xz!=f1)
    Yz = np.delete(yz,yz!=f2)
    xmin = np.amin(Xz)
    ymin = np.amin(Yz)
    local_min = f(xmin,ymin)
    print('The local minumum is ',local_min, 'which occurs at ', '(',np.abs(xmin),',',np.abs(ymin),')')
MC(10**6)