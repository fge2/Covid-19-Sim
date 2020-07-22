import matplotlib.pyplot as plt
import matplotlib.animation as animation
import population
from matplotlib.lines import Line2D


# line graph to show infections over time displayed on axis 2 of main figure
#
# args:
#   axes: ax2 of main figure
#   pop:  population data type
#   x1:   list of number of healthy persons over time
#   x2:   list of number of infected persons over time

def create_stats(axes, pop, x1, x2):
    # append next data point
    healthy = pop.healthy()
    infected = pop.infected()
    x1.append(len(healthy))
    x2.append(len(infected))

    # redraw grah
    axes.clear()
    axes.set_xlim(0, 1.3*len(x1)), axes.set_xticks([])
    axes.set_ylim(0, pop.pop_size())
    inf = axes.plot(x2, c='red')
    health = axes.plot(x1, c='black')

    # legend
    labels = [Line2D([0], [0], color='black'), Line2D([0], [0], color='red')]
    handles = [len(healthy), len(infected)]
    axes.legend(labels, handles, loc = 'upper right')

plt.show()