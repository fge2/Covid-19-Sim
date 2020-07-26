import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from person import Person
import stats
from Population import Population
import animate
import math

# implement quaratine policies by sectioning off a portion of the population
#
# methods: updatev3
#   modified update function to quaratine when certain % of population infected
#       args: 
#           *see update*
#           wall: percentage of area to section off
#           lag: frames before slowly removing quaratine
#
#    quaratine_update: helper function to update the quaratine wall

def updatev3(frame_number, pop, status, ax1, ax2, scat, restriction, colormap, time, wall = 0.25, lag = 500):
    quaratine_update(frame_number, pop, restriction, lag)
    animate.update(frame_number, pop, status, ax1, ax2, scat, colormap, time)


# slowly drop the quarantine and restrict movement on both sides of wall
def quaratine_update(frame_number, pop, restriction, lag):
    # change height
    height = 1
    if frame_number >= lag and len(pop.infected()) > 0 and (1-(frame_number - lag)/1000) > 0:    
        height = (1-(frame_number - lag)/1000)
        restriction.set_ydata([0, height])

    # only update active persons
    active = pop.active()
    right = [p for p in active if p.get_xpos() > 0.25 and 
        (p.get_xpos() + p.get_speed() * math.cos(math.radians(p.get_theta())) / 100) <= wall + 0.015 and 
        p.get_ypos() <= height]
    left = [p for p in active if p.get_xpos() < 0.25 and 
        (p.get_xpos() + p.get_speed() * math.cos(math.radians(p.get_theta())) / 100) >= wall - 0.015 and 
        p.get_ypos() <= height]

    # corner cases when hitting quaratine wall
    for p in right:
        if p.get_theta() < 180:
            p.set_theta(np.random.uniform(0, 90))
        else:
            p.set_theta(np.random.uniform(270, 360))

    for p in left:
        if p.get_theta() < 90:
            p.set_theta(np.random.uniform(90, 180))
        else:
            p.set_theta(np.random.uniform(180, 270))


# driver function for lockdown
if __name__ == "__main__":

    # set variables for frame
    fig, ax1, ax2 = animate.frame()
    status = [[],[],[],[]]
    n_size = 400
    pop = Population(n_size)
    wall = 0.25
    lag = 500

    # textbox to track frame number
    time = ax1.text(1, 1.05, "frame number: " + str(0), transform=ax1.transAxes, fontsize=8, verticalalignment='top', horizontalalignment='right')

    # declare colors for scatter plot
    color1='black'
    color2='red'
    color3='green'
    color4='gray'
    colormap = np.array([color1,color2,color3,color4])
    categories = pop.status()

    # create graphs
    scat = ax1.scatter(pop.xposition(), pop.yposition(), c=colormap[categories], s=2)
    line = ax2.plot()
    restriction, = ax1.plot([wall, wall], [0, 1], c='black', linewidth = 6)

    # Construct the animation, using the update function as the animation director.
    animation = FuncAnimation(fig, updatev3, fargs = [pop, status, ax1, ax2, scat, restriction, colormap, time, wall, lag], interval=10)
    fig.suptitle('Covid-19 Simulation: 25% of population quarantined')
    plt.show()