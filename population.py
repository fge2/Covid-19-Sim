from person import Person

# Population class to simulate a group of individuals of size n_size
# last individual initialized to be infected
#
# fields:
#   pop:    list of persons
#   size:   number of persons in list   
#   vel:    speed of individual
#   theta:  trajectory
#   status: health/infected
#   locked: movement restricted/free
#
# methods:
#   quarantine: lockdown movement of a given number of persons
#       args: 
#           qty: quantity
#   other: various methods to return subsets of population

class Population:
    def __init__(self, n_size):
        self.pop = [Person() for i in range(n_size)]
        self.size = n_size

        # initialize patient 0
        self.pop[n_size - 1].status = 1
        
    def lockdown(self, qty):
        for i in range(qty):
            self.pop[i].set_speed(0)

    def pop_size(self):
        return self.size

    def infected(self):
        return [p for p in self.pop if p.status == 1]

    def healthy(self):
        return [p for p in self.pop if p.status == 0]

    def active(self):
        return [p for p in self.pop if p.locked == 0]

    def status(self):
        return [p.status for p in self.pop]

    def xposition(self):
        return [p.xpos for p in self.pop]

    def yposition(self):
        return [p.ypos for p in self.pop]