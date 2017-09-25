import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from scipy.optimize import curve_fit

f = lambda x,a,b: a*x+b # current and resistance should be linear
i34mean = np.loadtxt("Downloads\\i34mean.txt",float)
v12mean = np.loadtxt("Downloads\\v12mean.txt",float)# imported data


R3412, cov2 = curve_fit(f, i34mean, v12mean)


 # predicted values
v12pmean = R3412[0]*i34mean + R3412[1]  


plt.plot(i34mean, v12mean, 's', label='raw data v12')
plt.plot(i34mean, v12pmean, '-x', label='fitted data v12')
plt.legend()

plt.xlabel('Current')
plt.ylabel('Volts')
plt.show()