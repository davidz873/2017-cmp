#Calculate the Area between the two curves using Monte Carlo methods
import matplotlib.pyplot as plt
from random import random
import numpy as np




def f(x):                 # def upper function
    return np.sqrt(1-(x-1)**2)
        
def F(x):                 # def lower function
    return 2-np.sqrt(4-x**2)


def MC(N):                           #2x2 monte carlo for area between curves
    y = 2*np.random.random(N)
    x = np.linspace(0,2,N)
    yf = f(x)
    yF = F(x)
    condition = (yf >= y) & (yF <=y)
    count = np.sum(condition)
    I = 4*count/N    #area*count/attempts
    return I

area = MC(10**8)

print(area)