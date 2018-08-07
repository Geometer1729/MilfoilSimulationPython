import interpilation     as interp
import RungeKuta         as rk4
import numpy             as np
import SimChain          as sc
import iteratedFunc      as iter
import matplotlib.pyplot as plt
from itertools import  cycle
tau = 2*np.pi



tol = 0.01
maxStep = 0.01

testFrame = (0,[(1,0),(0,1)])
testSystem1 = lambda t,x : [-1*x[1],x[0]] # simple circular orbit
testSystem2 = lambda t,xs : [-t*x for x in xs] # acelerating "nearly exponential" decay
testFunction1 = lambda f : (f[0]+0.1,[(1-f[1][0][0],0),(f[1][1][0],0)])
testPhase1 = sc.buildODEPhase(tol,maxStep,testSystem1,rk4.timeCon(tau))
testPhase2 = sc.buildODEPhase(tol,maxStep,testSystem2,rk4.timeCon(10))
testPhase3 = iter.buildIter(testFunction1)
testPhase4 = sc.buildODEPhase(tol,maxStep,testSystem1,rk4.timeCon(10+tau))
testChain = sc.Chain(testFrame,[testPhase1,testPhase2,testPhase3,testPhase4])
testTimes = np.arange(0,10+tau,0.05)
testData = interp.interpilate(testTimes,testChain)

plt.plot(testTimes,testData)
plt.show()
