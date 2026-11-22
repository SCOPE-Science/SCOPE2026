"""Numerical consistency checks for an idealized dual-target detection model."""
import math
import random
from scipy.optimize import brentq


def R(t):
    return t / math.expm1(t) if t < 700 else 0.0


def deriv_scaled(y, u, v):
    return (1-y)*R(u*y*math.exp(-y)) + R(v*y)


def joint(y,u,v):
    return -math.expm1(-u*y*math.exp(-y)) * -math.expm1(-v*y)


def opt(u,v):
    hi=max(2.0,math.log1p(u/v)+5)
    while deriv_scaled(hi,u,v)>0:
        hi*=2
    return brentq(lambda y: deriv_scaled(y,u,v),1,hi,xtol=1e-13)

checks=0
cases=[(10.0,0.5),(10.,1.),(10.,2.),(10.,10*math.exp(-2)),(.1,.1),(.001,5.)]
rng=random.Random(4406)
cases += [(10**rng.uniform(-2,1),10**rng.uniform(-2,1)) for _ in range(2000)]
for u,v in cases:
    y=opt(u,v)
    assert y>1 and deriv_scaled(y*.999999,u,v)>0 and deriv_scaled(y*1.000001,u,v)<0
    checks+=3
    signed=math.log(u/v)-2
    if abs(signed)>1e-10:
        assert (y>2)==(signed>0)
        checks+=1
    for scale in (.01,.1,.5,.9,1.1,2,10,100):
        z=y*scale
        assert joint(z,u,v)<=joint(y,u,v)+1e-12
        checks+=1
for u,v in [(10,.5),(10,1),(10,2),(10,10*math.exp(-2))]:
    y=opt(u,v)
    print('PARAMETERS',u,v,'OPTIMUM',repr(y),'VALUE',repr(joint(y,u,v)))
for u in (1e3,1e5,1e8):
    y=opt(u,1.0)
    print('ASYMPT',u,y,'DIFF',y-math.log(u))
    assert y>2 and y<math.log(u)
    checks+=2
print('PASS',checks,'assertions')
