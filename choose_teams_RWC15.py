#/usr/bin/python

import numpy as np
import sys

list_names = np.genfromtxt(sys.argv[1],dtype="S20")
list_teams = np.genfromtxt(sys.argv[2],dtype="S20")

np.random.shuffle(list_names)
np.random.shuffle(list_teams)

for i in range(0,20):
    print list_names[i], list_teams[i]




