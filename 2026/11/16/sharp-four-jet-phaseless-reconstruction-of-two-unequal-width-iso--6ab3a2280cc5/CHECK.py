#!/usr/bin/env python3
"""Exact-rational test of fourth-order Gaussian Fourier-intensity formulas."""
from fractions import Fraction as F

def conv(a,b,maxdeg=4):
    out=[F(0)]*(maxdeg+1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<=maxdeg: out[i+j]+=x*y
    return out

def independent_expansion(s,q,h_direction):
    # 2 exp(-s*t^2) (cosh(q*t^2)+cos(h_direction*t))
    E=[F(1),F(0),-s,F(0),s*s/2]
    H=[F(2),F(0),-h_direction*h_direction/2,F(0),
       q*q/2+h_direction**4/F(24)]
    return [2*x for x in conv(E,H)]

def formula(s,q,h_direction,magnitude2):
    return [F(4),F(0),-4*s*magnitude2-h_direction*h_direction,
            F(0),(2*s*s+q*q)*magnitude2**2
            +s*magnitude2*h_direction**2+h_direction**4/F(12)]

checks=0
for s,q in [(F(3,2),F(1,4)),(F(2),F(1,2)),(F(4,3),F(1,3))]:
    for a,b in [(F(1),F(0)),(F(0),F(1)),(F(2),F(3)),(F(-1,2),F(3,4))]:
        # xi=t*(a,b); displacement=(1,2), so v=t*(a+2b)
        u=a*a+b*b; v=a+2*b
        actual=independent_expansion(s*u,q*u,v)
        assert actual==formula(s,q,v,u),(actual,formula(s,q,v,u))
        checks+=1

examples=[(F(2),F(1,4),F(1)),(F(41,20),F(47,200),F(4,5))]
def coeffs(s,z,r): return F(4)*s+r,2*s*s+z+s*r+r*r/F(12)
for s,z,r in examples:
    assert s>0 and 0<=z<s*s and r>0
    assert coeffs(s,z,r)==(F(9),F(31,3))
    checks+=1
assert examples[0][2]!=examples[1][2]
assert examples[0][0]!=examples[1][0]
print(f'CHECK_OK exact_rational_taylor_directions=12 one_dim_collisions=2 checks={checks}')
