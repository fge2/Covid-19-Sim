import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation
from person import Person
import quarantine
import stats
import population
from population import Population
from matplotlib.lines import Line2D

# module to provide animation functions
#
# methods: 
#   update: update the frame
#       args:
#           frame_number: default parameter for funcAnimation update func
#           pop:        population list
#           x1, x2:     lists of healthy/infected numbers over time 
#           ax1:        axis to display scatterplot of persons
#           ax2:        axis to display x1,x2 below simulation frame
#           scat:       scatter plot to display and update individual positions/status
#           colormap:   colormap for persons in scat
#           rate:       rate of infection
#           time:       frame counter
#
#   status_update: helper function to update infections
#   position_update: helper function to update positions


def update(frame_number, pop, x1, x2, ax1, ax2, scat, colormap, rate, time):
    # update population data and infection data
    position_update(pop)
    status_update(pop, rate)
    stats.create_stats(ax2, pop, x1, x2)
    
    # update scatter plot with new data
    newx = pop.xposition()
    newy = pop.yposition()
    categories = pop.status()
    scat.set_offsets(np.stack((newx, newy), axis = 1))
    scat.set_color(colormap[categories])

    # update frame counter
    time.set_text("frame number: " + str(frame_number))

    # stop at 100% infection
    if len(pop.infected()) == pop.pop_size():
        animation.event_source.stop()


def status_update(pop, rate):
    healthy = pop.healthy()
    infected = pop.infected()

    # loop through healthy if less ppl are healthy to reduce iterations and infect with chance = rate
    if len(healthy) > len(infected):
        for j in infected:
            for i in healthy:
                if i.distance(j) < 0.005:
                    i.infect(rate)
                    if i.status == 1:
                        break
    # vice versa
    else:
        for i in healthy:
            for j in infected:
                if i.distance(j) < 0.005:
                    i.infect(0.3)
                    if i.status == 1:
                        break


def position_update(pop):
    # only update active persons
    active = pop.active()

    # corner cases when hitting boundaries of region
    for p in active:
        if p.xpos < 0.005:
            if p.theta < 180:
                p.set_theta(np.random.uniform(0, 90))
            else:
                p.set_theta(np.random.uniform(270, 360))

        if p.xpos > 0.995:
            if p.theta < 90:
                p.set_theta(np.random.uniform(90, 180))
            else:
                p.set_theta(np.random.uniform(180, 270))

        if p.ypos < 0.005:
            if p.theta < 270:
                p.set_theta(np.random.uniform(90, 180))
            else:
                p.set_theta(np.random.uniform(0, 90))

        if p.ypos > 0.995:
            if p.theta < 90:
                p.set_theta(np.random.uniform(270, 360))
            else:
                p.set_theta(np.random.uniform(180, 270))

        # scale position update
        p.xpos = p.xpos + p.vel * math.cos(math.radians(p.theta)) / 100
        p.ypos = p.ypos + p.vel * math.sin(math.radians(p.theta)) / 100


# create new Figure and an Axes
# returns figure and axes for scatter and line plots
def frame():
    fig = plt.figure()
    ax1 = plt.subplot2grid((4,1),(0,0), rowspan=3)
    ax2 = plt.subplot2grid((4,1),(3,0), rowspan=1)
    ax1.set_xlim(0, 1), ax1.set_xticks([])
    ax1.set_ylim(0, 1), ax1.set_yticks([])

    # scatter legend   
    labels = [Line2D([0], [0], marker='.', color='white', markerfacecolor='black', markersize=8), Line2D([0], [0], marker='.', color='white', markerfacecolor='red', markersize=8)]
    handles = ['healthy','infected']
    ax1.legend(labels, handles, loc = 'upper right')

    return fig, ax1, ax2


# driver function for base simulation with no policy implementations
if __name__ == "__main__":
    
    # set variables for frame
    x1 = []
    x2 = []
    n_size = 400
    rate = 1
    fig, ax1, ax2 = frame()
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
    animation = FuncAnimation(fig, update, fargs = [pop, x1, x2, ax1, ax2, scat, colormap, rate, time], interval=10)
    fig.suptitle('Covid-19 Simulation')
    plt.show()