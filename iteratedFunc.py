
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

def buildIter(func,times=1):
    return lambda frame: Iter(func,times,frame)
