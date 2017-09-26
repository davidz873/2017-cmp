import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from scipy.optimize import curve_fit

f = lambda x,a,b: a*x+b # current and resistance should be linear
i12 = np.loadtxt("Downloads\\i12mean.txt",float)
v34 = np.loadtxt("Downloads\\v34mean.txt",float)
i34 = np.loadtxt("Downloads\\i34mean.txt",float)
v12 = np.loadtxt("Downloads\\v12mean.txt",float)# imported data
i14 = np.loadtxt("Downloads\\i14mean.txt",float)
v23 = np.loadtxt("Downloads\\v23mean.txt",float)
i23 = np.loadtxt("Downloads\\i23mean.txt",float)
v14 = np.loadtxt("Downloads\\v14mean.txt",float)

R1234, cov1 = curve_fit(f, i12, v34)
R3412, cov2 = curve_fit(f, i34, v12)
R1423, cov3 = curve_fit(f, i14, v23)
R2314, cov4 = curve_fit(f, i23, v14)

v34p = R1234[0]*i12 + R1234[1]  # predicted values
v12p = R3412[0]*i34 + R3412[1]  
v23p = R1423[0]*i14 + R1423[1]
v14p = R2314[0]*i23 + R2314[1]

RH = (R1234[0]+R3412[0])/2
RV = (R1423[0]+R2314[0])/2
RS = 0.00001
VDP = 0

while VDP <= 1:
    VDP = np.exp((-1*np.pi*RH)/RS) + np.exp((-1*np.pi*RV)/RS)
    RS += 0.00001

print('The Sheet Resistance of the 94.5 wt% Bi2Te3 SWCNT sample is \n',RS,' Ohms')

plt.plot(i34, v12, 'o', label='experimental values')
plt.plot(i34, v12p, '-s', label='model values')
plt.legend()

plt.xlabel('Current across terminals 34')
plt.ylabel('Voltage across terminals 12')
plt.show()