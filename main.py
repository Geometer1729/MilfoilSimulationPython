import interpilation     as interp
import RungeKuta         as rk4
import numpy             as np
import SimChain          as sc
import matplotlib.pyplot as plt
tau = 2*np.pi


testFrame = (0,[(1,0),(0,1)])
testSystem1 = lambda t,x : [-1*x[1],x[0]] # simple circular orbit
testSystem2 = lambda t,xs : [-t*x for x in xs] # acelerating "exponential" decay
testPrep1 = rk4.prepSim(0.01,0.01,testSystem1)
testPrep2 = rk4.prepSim(0.01,0.01,testSystem2)
#testSim = testPrep(testFrame)
testTimes = np.arange(0,10,0.001) 
testPhase1 = (testPrep1,rk4.timeCon(tau))
testPhase2 = (testPrep2,rk4.timeCon(10))
testPhases = [testPhase1,testPhase2]
testChain = sc.Chain(testFrame,testPhases)
testData = interp.interpilate(testTimes,testChain)

plt.plot(testTimes,testData)
plt.show()
