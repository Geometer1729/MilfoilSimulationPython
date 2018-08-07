import RungeKuta as rk4

class Chain:
    def __init__(self,frame,sims):
        sim , *self.future = sims
        self.sim = sim(frame)
        self.frame = frame
    def __iter__(self):
        return self
    def __next__(self):
        try:
            self.sim.__next__()
            self.frame=self.sim.frame
        except StopIteration:
            if len(self.future) == 0:
                raise StopIteration
            sim , *self.future = self.future
            self.sim = sim(self.frame)
            self.__next__() # reatempt step in new system
        return self


class Condition:
    def __init__(self,sim,con,frame):
        self.sim = sim
        self.con = con
        self.frame = frame
    def __iter__(self):
        return self
    def __next__(self):
        if (self.con(self.frame)):
            raise StopIteration
        self.frame = self.sim(self.frame).__next__().frame
        return self

def prepCon(sim,con):
    return lambda frame : Condition(sim,con,frame)

def buildODEPhase(maxStep,tolerance,system,con):
    prep = rk4.prepSim(0.01,0.01,system)
    return lambda frame: Condition(prep,con,frame)
