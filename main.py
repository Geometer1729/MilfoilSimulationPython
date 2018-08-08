from interpilation import interpilate
from SimChain import Chain

from RungeKuta import buildODEPhase , timeCon
from iteratedFunc      import buildIter
import matplotlib.pyplot as plt
import numpy             as np

tau = 2*np.pi



tol = 0.01
maxStep = 0.01

testFrame = (0,[(1,0),(0,1)])
testSystem1 = lambda t,x : [-1*x[1],x[0]] # simple circular orbit
testSystem2 = lambda t,xs : [-t*x for x in xs] # acelerating "nearly exponential" decay
testFunction1 = lambda t,xs: (x+t/10 for x in xs)
testPhase1 = buildODEPhase(tol,maxStep,testSystem1,timeCon(tau))
testPhase2 = buildODEPhase(tol,maxStep,testSystem2,timeCon(10))
testPhase3 = buildIter(0.1,testFunction1)
testPhase4 = buildODEPhase(tol,maxStep,testSystem1,timeCon(10+tau))
testChain = Chain(testFrame,[testPhase1,testPhase2,testPhase3,testPhase4])
testTimes = np.arange(0,10+tau,0.05)
testData = interpilate(testTimes,testChain)

plt.plot(testTimes,testData)
plt.show()
