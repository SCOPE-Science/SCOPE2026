#!/usr/bin/env python3
"""Exact finite-state check for a three-zone market map."""
from fractions import Fraction
from itertools import product
S=(-1,0,1)

def phi(pair,r):
    p,q=pair
    delta=q-p
    return (q, 1 if delta>r else (-1 if delta < -r else 0))

SIX=((-1,-1),(-1,0),(0,1),(1,1),(1,0),(0,-1))
assert len(set(SIX))==6
for r, maximum, target in [
    (Fraction(1,2),1,set(SIX)|{(0,0)}),
    (Fraction(1),3,{(0,0)}),
    (Fraction(3,2),3,{(0,0)}),
    (Fraction(2),2,{(0,0)}),
    (Fraction(5),2,{(0,0)}),
]:
    for pair in product(S,repeat=2):
        current=pair
        for _ in range(maximum):
            if current in target:break
            current=phi(current,r)
        assert current in target,(r,pair,current)
    if r<1:
        assert all(phi(SIX[i],r)==SIX[(i+1)%6] for i in range(6))
        assert phi((0,0),r)==(0,0)
    else:
        assert phi((0,0),r)==(0,0)
# With unscaled data, the first two iterates always have first coordinate
# among {-d,0,d}, irrespective of the input real amplitude.
for d,h in [(Fraction(1,3),Fraction(1,2)),(Fraction(2),Fraction(1)),
            (Fraction(2),Fraction(2)),(Fraction(2),Fraction(4))]:
    def f(x,y):
        z=x-y
        return (d if z>h else (-d if z < -h else Fraction(0)), x)
    for initial in [(Fraction(17),Fraction(-11)),(h,Fraction(0)),
                    (-h,Fraction(0)),(Fraction(0),Fraction(0)),
                    (Fraction(1,17),Fraction(2,19))]:
        p=initial
        states=[]
        for n in range(6):
            states.append(p)
            p=f(*p)
        assert states[2][0] in (-d,0,d) and states[2][1] in (-d,0,d)
        if d<=h: assert states[5]==(0,0)
        else:
            pts={(d*x,d*y) for x,y in SIX}
            assert states[3] in pts|{(0,0)}
print('PASS: exhaustive nine-state transition graph, all regime boundaries, and off-grid checks')
