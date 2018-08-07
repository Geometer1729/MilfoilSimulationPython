#simulation frames are stored as (time, [(value,derivitive)] )
#time dependent systems are stored as f: time , [value] -> system

import numpy as np

def scale(scaleBy,list):
    return [scaleBy * elem for elem in list]
def listSum(xs,ys):
     return [x+y for x,y in zip(xs,ys)]
def getVals(frame):
    return [val for val,_ in frame[1] ]

def weightedListSum(weights,lists):
    scaled = [scale(weight,list) for weight , list in zip(weights,lists) ]
    return [ sum(layer) for layer in np.transpose(scaled) ]

def RK4Step(h,tSystem,frame): # h is the step size
    t , ic = frame # time , initial stopConditionditions
    iv = getVals(frame) # initial values
    k1 = scale(h,tSystem(t,iv))
    k2 = scale(h,tSystem(t+h/2,listSum(iv,scale(1/2,k1))))
    k3 = scale(h,tSystem(t+h/2,listSum(iv,scale(1/2,k1))))
    k4 = scale(h,tSystem(t+h,listSum(iv,k3)))
    res = weightedListSum([1,1/6,2/6,2/6,1/6],[iv,k1,k2,k3,k4]) # result values
    return (t+h, list(zip(res,tSystem(t+h,res)))) # build next frame

def frameNorm(a,b): # norm for frames
    return (sum([ (val1-val2)**2 for val1 , val2 in zip(getVals(a),getVals(b))]))**0.5 # apply the l2 norm to the values

def smartRK4Step(tolerance,h,tSystem,frame):
    firstHalfStep = RK4Step(h/2,tSystem,frame)
    byHalfStep = RK4Step(h/2,tSystem,firstHalfStep)
    direct = RK4Step(h,tSystem,frame)
    if(frameNorm(direct,byHalfStep) < tolerance):
        return byHalfStep # it's more acurate and we already had to compute it
    return smartRK4Step(tolerance,h/4,tSystem,frame) # reduce step size and try again

class Simulate:
    def __init__(self,tolerance,h,tSystem,frame):
        self.maxStep = h
        self.tSystem = tSystem
        self.tolerance = tolerance
        self.frame = frame
    def __iter__(self):
        return self
    def __next__(self):
        self.frame = smartRK4Step(self.tolerance,self.maxStep,self.tSystem,self.frame)
        return self

timeCon = lambda stopTime: lambda frame: frame[0] > stopTime #creates a stop condition for a given stop time

def prepSim(tolerance,h,tSystem):
    return lambda frame: Simulate(tolerance,h,tSystem,frame)
