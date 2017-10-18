import numpy as np


# two dice

def dice(N):
    a = np.random.randint(1,7,N)
    b = np.random.randint(1,7,N)
    two_sixes = (a == 6) & (b == 6)
    count = sum(two_sixes)
    print('Two sixes were rolled ',count,' out of',N,' times.')
    

dice(10**6)