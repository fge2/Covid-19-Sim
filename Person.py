import random
import math
import numpy as np

# Person class to simulate an individual
#
# fields:
#   xpos:   xcoordinate
#   ypos:   ycoordinate   
#   vel:    speed of individual
#   theta:  trajectory
#   status: health/infected/recovered/dead == 0/1/2/3
#   locked: movement restricted/free
#
# methods:
#   distance: returns distance to another person
#       args: p = another person
#   other: various methods to change field values

infect_rate = 0.3
recov_u = 200
recov_sigma = 50
death_rate = 0.0001

class Person:
    def __init__(self):
        self.xpos = np.random.uniform(0, 1)
        self.ypos = np.random.uniform(0, 1)
        self.vel = abs(np.random.normal(0, 1))
        self.theta = np.random.uniform(0, 360)
        self.status = 0
        self.locked = 0
        self.recovery = 0

    ######################## changing status ##################################
    def infect(self):
        if (random.uniform(0, 1) < infect_rate):
            self.status = 1
            self.recovery = math.floor(abs(np.random.normal(recov_u, recov_sigma)))
    
    def set_recover(self, curr_frame):
        self.recovery = self.recovery + curr_frame

    def recover(self):
        self.status = 2

    def death(self):
        if (random.uniform(0, 1) < death_rate):
            self.status = 3
            self.set_speed(0)
    ###########################################################################

    ######################## change/get attributes ############################
    def random_speed(self):
        self.vel = np.random.uniform(0, 1)

    def set_speed(self, speed):
        self.vel = speed

    def set_theta(self, theta):
        self.theta = theta

    def set_xpos(self, x):
        self.xpos = x

    def set_ypos(self, y):
        self.ypos = y

    def get_speed(self):
        return self.vel

    def get_theta(self):
        return self.theta

    def get_xpos(self):
        return self.xpos
    
    def get_ypos(self):
        return self.ypos
    ###########################################################################

    # distance to another person
    def distance(self, p):
        return math.sqrt((self.xpos - p.xpos)**2 + (self.ypos - p.ypos)**2)


if __name__ == "__main__":
    p = Person()
    print(p.theta)
    