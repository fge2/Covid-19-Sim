import random
import math
import numpy as np

# Healthy
H = 0
# Infected
I = 0
# Dead
D = 0
# Recovered
R = 0

class Person:
    def __init__(self):
        self.xpos = np.random.uniform(0, 1)
        self.ypos = np.random.uniform(0, 1)
        self.vel = abs(np.random.normal(0, 1))
        self.theta = np.random.uniform(0, 360)
        self.status = 0

    def infect(self, prob):
        if (random.uniform(0, 1) < prob):
            self.status = 1
    
    def change_speed(self):
        self.vel = np.random.uniform(0, 1)

    def set_theta(self, theta):
        self.theta = theta

    def distance(self, p):
        return math.sqrt((self.xpos - p.xpos)**2 + (self.ypos - p.ypos)**2)


if __name__ == "__main__":
    p = Person()
    print(p.theta)
