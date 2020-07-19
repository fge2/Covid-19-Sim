import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation
from Person import Person


def update(frame_number):
    for i in range(n_size):
        if pop[i].xpos < 0.005:
            if pop[i].theta < 180:
                pop[i].set_theta(np.random.uniform(0, 90))
            else:
                pop[i].set_theta(np.random.uniform(270, 360))

        if pop[i].xpos > 0.995:
            if pop[i].theta < 90:
                pop[i].set_theta(np.random.uniform(90, 180))
            else:
                pop[i].set_theta(np.random.uniform(180, 270))

        if pop[i].ypos < 0.005:
            if pop[i].theta < 270:
                pop[i].set_theta(np.random.uniform(90, 180))
            else:
                pop[i].set_theta(np.random.uniform(0, 90))

        if pop[i].ypos > 0.995:
            if pop[i].theta < 90:
                pop[i].set_theta(np.random.uniform(270, 360))
            else:
                pop[i].set_theta(np.random.uniform(180, 270))

        pop[i].xpos = pop[i].xpos + pop[i].vel * math.cos(math.radians(pop[i].theta)) / 100
        pop[i].ypos = pop[i].ypos + pop[i].vel * math.sin(math.radians(pop[i].theta)) / 100

    healthy = [p for p in pop if p.status == 0]
    infected = [p for p in pop if p.status == 1]
    if len(healthy) > len(infected):
        for j in infected:
            for i in healthy:
                if i.distance(j) < 0.005:
                    i.infect(0.3)
                    if i.status == 1:
                        break
    else:
        for i in healthy:
            for j in infected:
                if i.distance(j) < 0.005:
                    i.infect(0.3)
                    if i.status == 1:
                        break
        


    newx = [p.xpos for p in pop]
    newy = [p.ypos for p in pop]
    categories = [p.status for p in pop]

    scat.set_offsets(np.stack((newx, newy), axis = 1))
    scat.set_color(colormap[categories])


if __name__ == "__main__":
    # Create new Figure and an Axes which fills it.
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    ax.set_xlim(0, 1), ax.set_xticks([])
    ax.set_ylim(0, 1), ax.set_yticks([])

    n_size = 500
    pop = [Person() for i in range(n_size)]
    pop[1].status = 1

    color1='black'
    color2='red'
    colormap = np.array([color1,color2])
    categories = [p.status for p in pop]

    scat = ax.scatter([p.xpos for p in pop], [p.ypos for p in pop], c=colormap[categories], s=1)

    # Construct the animation, using the update function as the animation director.
    animation = FuncAnimation(fig, update, interval=10)
    plt.show()