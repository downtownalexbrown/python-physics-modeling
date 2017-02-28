import matplotlib.pyplot as plt
import time

ball = plt.Circle((5, 5), 1, alpha=0.55, color='blue')

# Initilize the graph and stuff
ax = plt.subplot(aspect='equal')
ax.add_artist(ball)

# Change size of graph
ax.set_xlim((0, 10))
ax.set_ylim((0, 10))

plt.show()

i = 0
while i < 10:
	plt.text(2, 8, r'slope= %i' % i, fontsize=15)
	i += 1
	time.sleep(1)


