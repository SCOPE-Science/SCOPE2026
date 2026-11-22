#!/usr/bin/env python3
"""Finite independent checks of terminal counts in a binary composition tree."""
from collections import defaultdict
from fractions import Fraction as Q
from math import factorial

def beta(a,b):
    return Q(factorial(a-1)*factorial(b-1),factorial(a+b-1))

# Integral of (1-t)^2(8t+50t^2)+8t^2(1-t)^4.
assert 8*beta(2,3)+50*beta(3,3)+8*beta(3,5)==Q(253,105)
laws={1:{(1,0):Q(1)}}
assertions=1
for n in range(2,45):
    d=defaultdict(Q)
    d[(0,0)]+=Q(2,n+1)
    for i in range(1,n):
        for (x,y),a in laws[i].items():
            for (z,w),b in laws[n-i].items():
                d[(x+z,y+w)]+=a*b/Q(n+1)
    if n==2:
        d={(0,1):Q(2,3),(2,0):Q(1,3)}
    laws[n]=dict(d)
    assert sum(d.values())==1; assertions+=1
    ex=sum(x*p for (x,y),p in d.items())
    ey=sum(y*p for (x,y),p in d.items())
    ed=2*ex-5*ey
    vd=sum((2*x-5*y-ed)**2*p for (x,y),p in d.items())
    if n>=4:
        assert ex==Q(n+2,6); assert ey==Q(n+2,15)
        assertions+=2
    if n>=6:
        assert ed==0
        assert vd==Q(253,105)*(n+2)
        assertions+=2
    # cross-check exact finite second-moment relation
    vx=sum((x-ex)**2*p for (x,y),p in d.items())
    vy=sum((y-ey)**2*p for (x,y),p in d.items())
    co=sum((x-ex)*(y-ey)*p for (x,y),p in d.items())
    assert vd==4*vx+25*vy-20*co; assertions+=1
print(f'PASS: {assertions} rational checks; sizes 2..44; balanced contrast exact for sizes 6..44')
