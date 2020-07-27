# Covid19-Sim

A small project to simulate the spread of Covid-19 in different scenarios using python animation and matplotlib.

Default simulation where each individual is allowed to move freely. Person status is color coded. Almost all persons are infected.

```
python animate.py
```

![](unrestrained.gif)

## Lockdown
Simulation where 90% population lockdown is enforced at 10% infections. Both percentages are parameters that can be altered within the code. Lockdown appears effective in limiting infections and the virus quickly dies out. A majority of the population is never infected.

```
python lockdown.py
```

![](lockdown.gif)

## Quarantine
Simulation where 25% of the environment area is quarantined. Quarantine is slowly fazed out after a set number of frames. Patient zero is placed in quarantined area. Parameters include the area of the quarantine zone as well as when to end the quarantine. Virus propagates in 2 waves: within the quarantined group and then the rest of the population as quarantine is dropped. Most of the population is infected, yet the quarantine proves to be effective in flattening the curve. In some iterations of the simulation, the virus is completely eliminated within quarantine walls when the entire subgroup recovers before quarantine is ended.
```
python quarantine.py
```

![](quarantine.gif)
