from interpilation import interpilate
from SimChain import Chain
from phases import Growth , Winter
from RungeKuta import buildODEPhase , timeCon
from iteratedFunc import buildIter
import matplotlib.pyplot as plt
import numpy as np
from itertools import chain
from ipywidgets import interactive, fixed
import ipywidgets as widgets
from matplotlib.pyplot import figure

tol = 0.001
maxStep = 0.05
winterTime=0.1

def plotFrom(growthTime,seasons,startC):
    testFrame = (0,[(0,0),(startC,0)])
    testTimes = np.arange(0,seasons*(growthTime+winterTime),maxStep)
    GrowthPhase = lambda n: buildODEPhase(tol,maxStep,Growth,timeCon(n*growthTime+(n-1)*winterTime))
    WinterPhase = buildIter(winterTime,Winter)
    Phases= list(chain.from_iterable((GrowthPhase(x), WinterPhase) for x in range(1,seasons+1) ))
    Env = Chain(testFrame,Phases)
    testData = interpilate(testTimes,Env)
    t,s=Env.frame
    ms,cs = s
    m,dm = ms
    c,dc = cs
    plt.plot(testTimes,testData)
    plt.show()
    print("end carbs :",c)

interactive(plotFrom,growthTime=(0.01,10),seasons=(0,10),startC=widgets.FloatSlider(value=0.5,min=0.001,max=1,step=0.001))
