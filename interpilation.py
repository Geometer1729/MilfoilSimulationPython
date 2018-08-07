
import numpy as np

def interpilate(times,sim_):
    sim = sim_ # prevents interp from altering the sim
    matches = [] # will be a list of the closest frames
    for t in times:
        stepTo(sim,t) # advance simulation to t
        matches.append(sim.current) #append frame coresponding to t
    result = []
    for t,match in zip(times,matches):
        matchTime , matchData = match
        jump = t - matchTime # the signed distance from the time in the closest frame to the interpilation target
        subRes = []
        for val , deriv in matchData:
            subRes.append(val+deriv*jump)
        result.append(subRes)
    return result

def stepTo(sim,t):
    simT , _ = sim.current
    if simT < t:
        try:
             sim.__next__()
        except ValueError as _:
            return #stop advancing if the simulation completes
        stepTo(sim,t)
