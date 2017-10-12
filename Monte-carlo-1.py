import numpy as np
from random import random

def f(x):
    return np.sin(1/x/(2-x))**2 






def MC(N):                           #2x1 monte carlo for area between curves
    y = np.random.random(N)
    x = np.linspace(0,2,N)
    yf = f(x)
    condition = (yf >= y)
    count = np.sum(condition)
    I = 2*count/N
    return I

area = MC(10**7)

print(area)

area = np.empty([4,100])

for j in range(2,6):                     #area computation by monte carlo
    for k in range(100):
        area[j-2,k] = MC(10**j)

print('The area of the space between the two curves is\n',np.mean(area[3]),'\n')


standard_variance = np.empty(4)       #standard variance computation
for l in range(4):
    standard_variance[l] = (np.std(area[l,:]))**2
    
print('The standard variance for 100 area computations of 100 points is \n',standard_variance[0],'\nfor 1000 points\n',standard_variance[1],'\nfor 10000 points\n',standard_variance[2],'\nfor 100000 points\n',standard_variance[3])

