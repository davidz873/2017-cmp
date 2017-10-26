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

nx = np.linspace(x_min,x_max,10**6)
ny = np.linspace(y_min,y_max,10**6)

F1 = f1(nx)
F2 = f2(ny)

def MC(N):
    nx = np.linspace(x_min,x_max,N)
    ny = np.linspace(y_min,y_max,N)

    F1 = f1(nx)
    F2 = f2(ny)
    
    x = 4*np.random.random(N)-2
    y = 4*np.random.random(N)-2
    where_x = F1 == x
    where_y = F2 == y
    X = x * where_x
    Y = y * where_y
    xmin = np.amin(X)
    ymin = np.amin(Y)
    local_min = f(xmin,ymin)
    print('The local minumum is ',local_min, 'which occurs at ', '(',np.abs(xmin),',',np.abs(ymin),')')
MC(10**6)