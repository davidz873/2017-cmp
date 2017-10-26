## Decay process
import numpy as np
import matplotlib.pyplot as plt


# Initial parameters
NTl = 1000
NPb = 0
tau = 3.053*60
dt = 1 
p = 1 - 2**(-dt/tau)
tmax = 1000
mu = np.log(2)/tau
t_points = np.arange(0.0, tmax, dt)
Tl = []
Pb = []

for t in t_points:
    Tl.append(NTl)
    Pb.append(NPb)
    
    
    # Calculate the decayed atoms
    decay = 0
    for i in range(NTl):
        z0 = np.random.random()
        x = (-np.log(1-z0)/mu)
        if x<p:
            decay += 1
    NTl -= decay
    NPb += decay

plt.plot(t_points, Tl, label='Tl')
plt.plot(t_points, Pb, label='Pb')
plt.xlabel("Time")
plt.ylabel("Number of atoms")
plt.legend()
plt.show()