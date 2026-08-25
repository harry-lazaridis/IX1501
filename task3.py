import numpy as np
from numpy import random

faces = np.array([4, 6, 8, 12, 20])

def simulation(n_trials):
    w = 0
    for _ in range(n_trials):
        S = 0 
        for n in faces:
            S += random.randint(1, n) 
        if S <= 10 or S >= 45:
            w += 1
    return w / n_trials

print(simulation(1000))

