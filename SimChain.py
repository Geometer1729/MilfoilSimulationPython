

class Chain:
    def __init__(self,frame,sims):
        (sim , con), *future = sims
        self.sim = sim
        self.con = con
        self.future = future
        self.current = frame
    def __iter__(self):
        return self
    def __next__(self):
        if (self.con(self.current)):
            if(len(self.future)==0):
                raise ValueError("Chain End")
            (newSim , newCon) , *newFuture = self.future
            self.sim = newSim
            self.con = newCon
            self.future = newFuture
        self.current = self.sim(self.current).__next__().current
        return self




def runTill(frame,sim_,condition):
    sim = sim_(frame)
    frames = []
    while (not condition(sim.curent)):
        frames.append(sim.curent)
        sim = sim.__next__()
    return (sim.curent , frames)


def chainSims(start,sims):
    frame = start
    for sim,condition in sims:
        frame , data = runTill(frame,sim,condition)
        allData.append(data)
    return (frame,data)
