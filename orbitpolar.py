import numpy as np 
import matplotlib.pyplot as plt 
import time, sys

a = 149.62 # Major axis
b = 149.6 # Minor axis
e = 0.0167112299 # Eccentricity of Earth's orbit
c = 2.5 # Distance from center to foci

theta = 0
points = []
xypoints = []

fig = plt.figure()
ax = plt.subplot(111, projection='polar')

while theta < 2*np.pi: # Completes one orbit
        r = (a*(1-e**2))/(1+e*np.cos(theta))
#        print(np.c_[r,theta])
        points.append((theta, r))
        theta += np.pi/180

	x = a * np.cos(theta)
	y = b * np.sin(theta)
	xypoints.append((x, y))
	print(np.c_[x, y]) # x = acos(t), y = bsin(t)

plt.polar(*zip(*points))
ax.scatter(theta, c, cmap='hsv', alpha=0.75)
ax.annotate('Sun (2.5, 0)',
            xy=(0, c),  # theta, radius
            xytext=(0.525, 0.47),    # fraction, fraction
            textcoords='figure fraction',
            horizontalalignment='left',
            verticalalignment='bottom')

ax.annotate('Eccentricity: 0.0167',
            xy=(0, c),  # theta, radius
            xytext=(0.05, 0.05),    # fraction, fraction
            textcoords='figure fraction',
            horizontalalignment='left',
            verticalalignment='bottom')

velocity = np.sqrt(()


#earth = ax.scatter(points[0], cmap='hsv', alpha = 0.75, color='green')

#for coordinate in points:
	# points[0] is (0, 147.11966578236201). I need to split the string to get each point, then apply that to the scatter function
	

if __name__ == '__main__':
        if len(sys.argv) > 1 and sys.argv[1] == 'save':
                plt.savefig('plot.jpg', dpi=80, writer='imagemagick')
        else:
                plt.show()
