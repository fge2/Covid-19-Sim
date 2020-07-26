import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation
from person import Person
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
#           status:     2d list of current number of healthy/infected/recovered/dead people
#           ax1:        axis to display scatterplot of persons
#           ax2:        axis to display x1,x2 below simulation frame
#           scat:       scatter plot to display and update individual positions/status
#           colormap:   colormap for persons in scat
#           time:       frame counter
#   status_update: helper function to update infections
#   position_update: helper function to update positions


def update(frame_number, pop, status, ax1, ax2, scat, colormap, time):
    # stop at 100% infection
    if len(pop.infected()) > 0:
        # update population data and infection data
        position_update(pop)
        status_update(frame_number, pop)
        stats.create_stats(ax2, pop, status)
        
        # update scatter plot with new data
        newx = pop.xposition()
        newy = pop.yposition()
        categories = pop.status()
        scat.set_offsets(np.stack((newx, newy), axis = 1))
        scat.set_color(colormap[categories])

        # update frame counter
        time.set_text("frame number: " + str(frame_number))

    
def status_update(curr_frame, pop):
    healthy = pop.healthy()
    infected = pop.infected()

    # loop through healthy if less ppl are healthy to reduce iterations and allow infections 
    if len(healthy) > len(infected):
        for j in infected:
            for i in healthy:
                if i.distance(j) < 0.008:
                    i.infect()
                    if i.status == 1:
                        i.set_recover(curr_frame)
                        break
    # vice versa
    else:
        for i in healthy:
            for j in infected:
                if i.distance(j) < 0.008:
                    i.infect()
                    if i.status == 1:
                        i.set_recover(curr_frame)
                        break
    
    # update recover if on recovery frame
    for p in infected: 
        p.death()
        if curr_frame == p.recovery:
           p.recover()


def position_update(pop):
    # only update active persons
    active = pop.active()

    # corner cases when hitting boundaries of region
    for p in active:
        if p.get_xpos() < 0.005:
            if p.get_theta() < 180:
                p.set_theta(np.random.uniform(0, 90))
            else:
                p.set_theta(np.random.uniform(270, 360))

        if p.get_xpos() > 0.995:
            if p.get_theta() < 90:
                p.set_theta(np.random.uniform(90, 180))
            else:
                p.set_theta(np.random.uniform(180, 270))

        if p.get_ypos() < 0.005:
            if p.get_theta() < 270:
                p.set_theta(np.random.uniform(90, 180))
            else:
                p.set_theta(np.random.uniform(0, 90))

        if p.get_ypos() > 0.995:
            if p.get_theta() < 90:
                p.set_theta(np.random.uniform(270, 360))
            else:
                p.set_theta(np.random.uniform(180, 270))

        # scale position update
        p.set_xpos(p.get_xpos() + p.get_speed() * math.cos(math.radians(p.get_theta())) / 100)
        p.set_ypos(p.get_ypos() + p.get_speed() * math.sin(math.radians(p.get_theta())) / 100)


# create new Figure and an Axes
# returns figure and axes for scatter and line plots
def frame():
    fig = plt.figure()
    ax1 = plt.subplot2grid((6,1),(0,0), rowspan=4)
    ax2 = plt.subplot2grid((6,1),(4,0), rowspan=2)
    ax1.set_xlim(0, 1), ax1.set_xticks([])
    ax1.set_ylim(0, 1), ax1.set_yticks([])

    # scatter legend   
    labels = [Line2D([0], [0], marker='.', color='white', markerfacecolor='black', markersize=8), 
                Line2D([0], [0], marker='.', color='white', markerfacecolor='red', markersize=8),
                Line2D([0], [0], marker='.', color='white', markerfacecolor='green', markersize=8),
                Line2D([0], [0], marker='.', color='white', markerfacecolor='gray', markersize=8)]
    handles = ['healthy','infected', 'recovered', 'deceased']
    ax1.legend(labels, handles, loc = 'upper right')

    return fig, ax1, ax2


# driver function for base simulation with no policy implementations
if __name__ == "__main__":
    
    # set variables for frame
    status = [[],[],[],[]]
    n_size = 400
    fig, ax1, ax2 = frame()
    pop = Population(n_size)

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
    
    # Construct the animation, using the update function as the animation director.
    animation = FuncAnimation(fig, update, fargs = [pop, status, ax1, ax2, scat, colormap, time], interval=10)
    fig.suptitle('Covid-19 Simulation')
    plt.show()