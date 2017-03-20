import numpy as np 
import matplotlib.pyplot as plt 
import time, sys

a = 149.62 # Major axis
b = 149.6 # Minor axis
e = 0.0167112299 # Eccentricity of Earth's orbit
c = 2.5 # Distance from center to foci

theta = 0
points = []

while theta < 2*np.pi: # Completes one orbit
        r = (a*(1-e**2))/(1+e*np.cos(theta))
#        print(np.c_[r,theta])
        points.append((theta, r))
        theta += np.pi/180

	x = a * np.cos(theta)
	y = b * np.sin(theta)
	print(np.c_[x, y]) # x = acos(t), y = bsin(t)


if __name__ == '__main__':
        if len(sys.argv) > 1 and sys.argv[1] == 'save':
                plt.savefig('plot.jpg', dpi=80, writer='imagemagick')
        else:
		plt.polar(*zip(*points))
                plt.show()
