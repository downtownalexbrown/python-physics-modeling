import matplotlib.pyplot as plt
import matplotlib.animation as animation
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

# Add the ball object
ax.add_artist(Ellipse((2, 2), width, height, 1))

#def animate():
ball = plt.Circle((7, 7), 1, alpha=0.55, color='blue')	
ax.add_artist(ball)
#ani = animation.FuncAnimation(fig, animate, interval = 2)

plt.show()


