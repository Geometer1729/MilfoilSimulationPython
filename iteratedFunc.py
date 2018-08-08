from itertools import  cycle

class Iter:
    def __init__(self,func,times,frame):
        self.func=func
        self.times = times
        self.frame = frame
    def __iter__(self):
        return self
    def __next__(self):
        if self.times > 0:
            self.frame = self.func(self.frame)
            self.times-=1
        else:
            raise StopIteration

def buildIter(duration,func,times=1):
    frameFunc = lambda frame : appFunc(duration,func,frame)
    return lambda frame: Iter(frameFunc,times,frame)

def appFunc(duration,func,frame):
    t, pts = frame
    vals = [ x for x,_ in pts]
    return (t+duration,list(zip(func(t,vals),cycle([0]))))
