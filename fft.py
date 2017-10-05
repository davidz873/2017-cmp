import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from mpl_toolkits.mplot3d import Axes3D


sem = io.imread('bite.jpg')
s = np.fft.fft2(sem)
sshift = np.fft.fftshift(s)
magnitude = 20*np.log(np.abs(sshift))
phase = np.angle(sshift)
plt.imshow(phase, cmap = 'gray')
plt.grid()
plt.show()

plt.imshow(sem, cmap = 'gray')
plt.grid()


plt.subplot(3, 1, 1)
plt.imshow(sem, cmap = 'gray')
plt.xlabel('sem image')

plt.subplot(3, 1, 2)
plt.imshow(phase, cmap = 'gray')
plt.xlabel('phase')


plt.subplot(3, 1, 3)
plt.imshow(magnitude, cmap = 'gray')
plt.xlabel('magnitude')

