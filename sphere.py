import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

ball = plt.Circle((5, 5), 1, alpha=0.55, color='blue')

# Initilize the graph and stuff
ax = plt.subplot(aspect='equal')
ax.add_artist(ball)

# Change size of graph
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))

def animate():
	ball = plt.Circle((5, 5), 1, alpha=0.55, color='blue')	

ani = animation.FuncAnimation(fig, animate, interval = 2)

plt.show()


