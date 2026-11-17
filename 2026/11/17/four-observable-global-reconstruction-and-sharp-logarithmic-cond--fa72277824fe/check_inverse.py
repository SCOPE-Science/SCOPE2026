#!/usr/bin/env python3
"""Reproduce exact time/area inverse identities for a piecewise quadratic center."""
from math import gamma, isclose, sqrt
from random import Random

B=lambda a,b:gamma(a)*gamma(b)/gamma(a+b)
P=(1.5)**(1.0/3.0)*B(0.5,4.0/3.0)
Q=(2.0/3.0)**(2.0/3.0)*B(0.5,1.0/3.0)
assert isclose(P/Q,3/5,rel_tol=2e-14)

def measure(a,b,c,r):
    assert min(a,b,c,r)>0
    return (P*(b/a)**(1/3)*r**(5/3), P*c**(-1/3)*r**(5/3),
            Q*a**(-1/3)*b**(-2/3)*r**(-1/3), Q*c**(-1/3)*r**(-1/3))

def invert(gp,gm,tp,tm):
    assert min(gp,gm,tp,tm)>0
    r=sqrt(5*gm/(3*tm))
    b=gp*tm/(gm*tp)
    c=P**3*r**5/gm**3
    a=b*P**3*r**5/gp**3
    return a,b,c,r

rng=Random(298133)
for k in range(1000):
    true=tuple(10**rng.uniform(-2,2) for i in range(4))
    data=measure(*true)
    recovered=invert(*data)
    for s,t in zip(true,recovered):
        assert isclose(s,t,rel_tol=1e-12), (k,true,data,recovered)
    assert isclose(data[0]/data[2], 0.6*true[1]*true[3]**2,rel_tol=1e-12)
    assert isclose(data[1]/data[3], 0.6*true[3]**2,rel_tol=1e-12)
for k in range(1000):
    data=tuple(10**rng.uniform(-2,2) for i in range(4))
    params=invert(*data)
    restored=measure(*params)
    for s,t in zip(data,restored):
        assert isclose(s,t,rel_tol=1e-12)
print('PIECEWISE_CENTER_FOUR_MEASUREMENT_INVERSE_OK')
