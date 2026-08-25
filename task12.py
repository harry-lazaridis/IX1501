import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt

faces = np.array([4, 6, 8, 12, 20]) #Amount of sides for all 5 dices

def p(n):
    return np.ones(n) / n #The dices all have probability of 1/n of the sides of each dice

pf = p(faces[0]) #First dices probability functin
for n in faces[1:]: #Ad
    pf = np.convolve(pf, p(n))

s_values = np.arange(5, 5 + len(pf))
 #Task 1
table = pd.DataFrame({"s": s_values, "P(S = s)": pf})
print(table.to_string(index=False))

 #Task 2   
p_low = pf[(s_values <= 10)].sum()
p_high = pf[(s_values >= 45)].sum()
print(p_low)
print(p_high)
p_win = p_low + p_high
print(p_win)

#Task 3
def simulation(n_trials):
    w = 0
    for _ in range(n_trials):
        S = 0 
        for n in faces:
            S += random.randint(1, n + 1) 
        if S <= 10 or S >= 45:
            w += 1
    return w / n_trials


print("Simulation: ", simulation(1000))
print("Discrete: ", p_win)

#Task 4
trials_amount = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]
sim = [simulation(n) for n in trials_amount]

results = pd.DataFrame({
    "number_of_trials": trials_amount,
    "results": sim
})

print(results.to_string(index=False))

#task 5

def successes(n, reps=50):
    success = 0
    for _ in range(reps):
        P = simulation(n)
        relative_error = abs(P - p_win) / p_win
        if (relative_error <= 0.1):
            success += 1
    return success / reps

for i in range(1, 10):
    m = successes(i * 1000)
    print(m)
