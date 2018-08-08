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
