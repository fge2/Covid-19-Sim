import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Population
from matplotlib.lines import Line2D


# line graph to show infections over time displayed on axis 2 of main figure
#
# args:
#   axes: ax2 of main figure
#   pop:  population data type
#   status: 2d list of current number of healthy/infected/recovered/dead people


def create_stats(axes, pop, status):
    # append next data point
    healthy = pop.healthy()
    infected = pop.infected()
    recovered = pop.recovered()
    dead = pop.dead()
    status[0].append(len(healthy))
    status[1].append(len(infected))
    status[2].append(len(recovered))
    status[3].append(len(dead))

    # redraw grah
    axes.clear()
    axes.set_xlim(0, 1.25*len(status[0]))
    # axes.set_xticks([])
    axes.set_ylim(0, pop.pop_size())
    axes.plot(status[0], c='black')
    axes.plot(status[1], c='red')
    axes.plot(status[2], c='green')
    axes.plot(status[3], c='gray')


    # legend
    labels = [Line2D([0], [0], color='black'), Line2D([0], [0], color='red'), Line2D([0], [0], color='green'), Line2D([0], [0], color='gray')]
    handles = [len(healthy), len(infected) , len(recovered), len(dead)]
    axes.legend(labels, handles, loc = 'upper right')

plt.show()