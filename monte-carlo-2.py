#Calculate the Area between the two curves using Monte Carlo methods
import matplotlib.pyplot as plt
from random import random
import numpy as np




def f(x):                 # def upper function
    return np.sqrt(1-(x-1)**2)
        
def F(x):                 # def lower function
    return x**2

xarray = np.linspace(0,1.7,10000)   #x array for plot 

y1 = f(xarray)                      #y arrays for plot
y2 = F(xarray)

def MC(N):                           #1x1 monte carlo for area between curves
    y = np.random.random(N)
    x = np.linspace(0,1,N)
    yf = f(x)
    yF = F(x)
    condition = (yf >= y) & (yF <=y)
    count = np.sum(condition)
    I = count/N
    return I

area = MC(10**7)

print(area)