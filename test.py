
five = 5

class Count:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num == 5:
            raise ValueError(5)
        self.num += 1
        return self

c=Count()
while True:
    n=c.num
    try:
        c.__next__()
    except ValueError as e:
        print (n)
        break
