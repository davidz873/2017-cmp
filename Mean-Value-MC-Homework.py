import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/np.sqrt(x)/(np.exp(x)+1)
    
def w(x):
    return 1/np.sqrt(x)
    
    
    
X = np.linspace(0,1,10**6)

plt.plot(X,f(X))
plt.show()



def wxintegral(N):
    I = 0
    x = np.random.random(N)
    I = sum(w(x))
    print('factor', I)
    return I/N


def MC(N):
    xi = np.random.random(N)
    F = f(xi)
    W = w(xi)
    integ = wxintegral(N)
    FW = sum(F)/sum(W)
    I = FW*integ/N
    print('The area is',I)
    return I
    
MC(10**6)