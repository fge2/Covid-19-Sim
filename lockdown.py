import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation
from person import Person
import stats
import population
from population import Population
import animate

# implement socialdistancing/lockdown policies by freezing movement
#
# methods: updatev2
#   modified update function to quaratine when certain % of population infected
#       args: 
#           *see update*
#           lockdown: percentage to initiate lockdown
#           inactive: percentage of population to lockdown


def updatev2(frame_number, pop, x1, x2, ax1, ax2, scat, colormap, rate, time, lockdown = 0.1, inactive = 0.9):
    animate.update(frame_number, pop, x1, x2, ax1, ax2, scat, colormap, rate, time)
    if len(pop.infected()) > lockdown * pop.pop_size():
        pop.lockdown(math.floor(inactive * pop.pop_size()))


# driver function for lockdown
if __name__ == "__main__":

    # set variables for frame
    fig, ax1, ax2 = animate.frame()
    x1 = []
    x2 = []
    n_size = 400
    rate = 1
    pop = Population(n_size)

    # textbox to track frame number
    time = ax1.text(1, 1.05, "frame number: " + str(0), transform=ax1.transAxes, fontsize=8, verticalalignment='top', horizontalalignment='right')

    # declare colors for scatter plot
    color1='black'
    color2='red'
    colormap = np.array([color1,color2])
    categories = pop.status()

    # create graphs
    scat = ax1.scatter(pop.xposition(), pop.yposition(), c=colormap[categories], s=2)
    line = ax2.plot()

    # Construct the animation, using the update function as the animation director.
    animation = FuncAnimation(fig, updatev2, fargs = [pop, x1, x2, ax1, ax2, scat, colormap, rate, time], interval=10)
    fig.suptitle('Covid-19 Simulation: Lockdown at 10% infections')
    plt.show()