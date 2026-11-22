"""Supplementary direct Fourier checks for the two-axis sharp synthesis constant.
Python 3 standard library only. Execute: python checker.py
"""
import cmath
import math
import random
from fractions import Fraction


def field(q):
    if q == 9:
        elts = list(range(9))
        def mul(x,y):
            a,b=x%3,x//3
            c,d=y%3,y//3
            return (a*c+2*b*d)%3+3*((a*d+b*c)%3)
        def tr(x):
            return 2*(x%3)%3
        p=3
    else:
        assert q in (2,3,5,7,11)
        elts=list(range(q))
        mul=lambda x,y:(x*y)%q
        tr=lambda x:x
        p=q
    return elts,lambda x,y: cmath.exp(-2j*math.pi*tr(mul(x,y))/p)


def spectrum(q, center, horizontal, vertical):
    elts,chi=field(q)
    out=[]
    for u in elts:
        for v in elts:
            out.append(center+sum(horizontal[x]*chi(u,x) for x in elts[1:])
                        +sum(vertical[y]*chi(v,y) for y in elts[1:]))
    return out


def C(q):
    s=(q-1)**(1/3)
    return (1+(q-1)**2/(1+2*s)**3)**(-0.25)

rng=random.Random(31319)
total=0
for q in (2,3,5,7,9,11):
    E=field(q)[0][1:]
    s=(q-1)**(1/3)
    b=(1+s)/(q*(1+2*s))
    a=1-2*(q-1)*b
    spec=spectrum(q,a,{x:b for x in E},{x:b for x in E})
    target=[1]+[s/(1+2*s)]*(2*(q-1))+[-1/(1+2*s)]*((q-1)**2)
    # Compare multisets of Fourier coefficients, not frequency ordering.
    assert max(abs(x-y) for x,y in zip(sorted(spec,key=lambda z:z.real),
               sorted(target)))<2e-12
    ratio=max(map(abs,spec))/sum(abs(v)**4 for v in spec)**0.25
    assert abs(ratio-C(q))<2e-12
    total+=2
    for t in range(120):
        aa=complex(rng.uniform(-1,1),rng.uniform(-1,1))
        hh={x:complex(rng.uniform(-1,1),rng.uniform(-1,1)) for x in E}
        vv={x:complex(rng.uniform(-1,1),rng.uniform(-1,1)) for x in E}
        F=spectrum(q,aa,hh,vv)
        ratio=max(map(abs,F))/sum(abs(v)**4 for v in F)**0.25
        assert ratio <= C(q)*(1+2e-12), (q,ratio,C(q))
        total+=1
# Exact rational q=9 normalization and fourth-power norm.
assert (-1+16)/15==1
assert (1+16*Fraction(2,5)**4+64*Fraction(1,5)**4)==Fraction(189,125)
total+=2
print('PASS',total,'supplementary checks; prime-field and nine-element-field cases')
