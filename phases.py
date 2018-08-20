from numpy import log , exp , sin

# frames stored as
# [milfoil , carbohydrates (sometimes)]

def Growth(t,x):
    m , c = x
    return [m*(1-m)+c,-c]

def Winter(t,x):
    m , c = x
    return [0,m/10]
