import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import sys
from matplotlib.patches import Ellipse

# Initilize the graph and stuff
fig = plt.figure()
fig.set_dpi(100)
ax = plt.subplot(xlim=(0,10), ylim=(0,10))

# Fancy geometry stuff to scale the width and height of the ellipse
x0, y0 = ax.transAxes.transform((0, 0)) # lower left in pixels
x1, y1 = ax.transAxes.transform((10, 10)) # upper right in pixes
dx = x1 - x0
dy = y1 - y0
maxd = max(dx, dy)
width = 1 * maxd / dx
height = 1 * maxd / dy

# Two ellipses to demonstrate alpa
ax.add_artist(Ellipse((1, 7), width, height, 1, color='green', alpha=0.75))
ax.add_artist(Ellipse((1, 8), width, height, 1, color='green', alpha=0.75))


def update(i):
	# Label axis with time and print new ellipse
	label = 'time: {0}s'.format(i)
	ax.set_xlabel(label)
	ax.add_artist(Ellipse((i + 1, 2), width, height, 1, color='green', alpha=0.55))

if __name__ == '__main__':
	# Call animation function at an interval of 1 second for 10 frames
	ani = animation.FuncAnimation(fig, update, frames = np.arange(0,10), interval = 1000)
	if len(sys.argv) > 1 and sys.argv[1] == 'save':
		ani.save('plot.gif', dpi=80, writer='imagemagick')
	else:
		plt.show()


