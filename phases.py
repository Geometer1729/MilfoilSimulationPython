from numpy import log , exp , sin
from params import *
# frames stored as
# [milfoil , carbohydrates (sometimes)]

def clearWatter(t,xs):
        m , *_ = xs
        i0 = iradiance(t)
        ird = i0 * exp(-(kwt*d+ km*m))
        im = i0 * exp(kwt*(d-m/ps))
        tmp = temp(t)
        mewt = mew0 * thetag**(tmp - tb)
        dm =(mewt / km)*log((k1+im)/(k1 +ird))-m*(lambdafunc(tmp)+delta)
        return [dm]

def uniformSun(t,xs):
    m , *_ = xs
    tmp = temp(t)
    mewt = mew0 * thetag**(tmp-tb)
    i0 = iradiance(t)
    dm = (mewt*m*i0)/(k1+i0)-m*(lambdafunc(tmp)+delta)
    return [dm]

def uniformBiomass(t,xs):
    m , c , *_ = xs
    i0 = iradiance(t)
    tmp = temp(t)
    mewt =mew0*thetag**(tmp-tb)
    dc = -mew1*c
    im = i0 * exp(kwt*(d-m/ps))
    ird = i0 * exp(-(kwt*d+ km*m))
    dm = mewt/(kwt/ps+km)*log((k1+im)/(k1+ird))-m*(lambdafunc(tmp)+delta)-dc

def temp(t):
    return tempAmp*sin((1/2)*tau*(input+tempPhase)/360)**2 #frequency is 2 cyles per year

def lambdafunc(temp):
    return lambda0*(thetar**(temp-tb))
