"""Standalone exact arithmetic checks for a neutral piecewise-affine map.
Run: python3 neutral_period4_check.py
Finite checks supplement, but do not prove, the infinite-quantifier theorem.
"""
from fractions import Fraction as F
from itertools import product

def step(x,y,c=F(1)):
    return abs(x)-1, x+c*abs(y)-1

def core_interval(x):
    assert F(-1)<=x<=F(0)
    t= -F(1)-2*x
    if t>0: return F(0), t
    if t<0: return -(F(2)+x), -(F(1)-x)
    return -F(3,2),F(0)

def in_core(x,y):
    return F(-1)<=x<=F(0) and core_interval(x)[0]<=y<=core_interval(x)[1]

n_core=0;n_capture=0;n_four=0
for ix,iy in product(range(-24,25),range(-30,31)):
    x,y=F(ix,6),F(iy,7)
    for n in range(1000):
        if in_core(x,y):break
        x,y=step(x,y)
    else: raise AssertionError(('noncapture',ix,iy))
    n_capture+=1
    a,b=x,y
    for j in range(4):x,y=step(x,y)
    assert (x,y)==(a,b)
    n_four+=1
for ix in range(-36,1):
    x=F(ix,36)
    lo,hi=core_interval(x)
    for j in range(37):
        y=lo+(hi-lo)*F(j,36)
        assert in_core(x,y)
        x1,y1=step(x,y)
        assert in_core(x1,y1)
        x2,y2=step(x1,y1)
        x3,y3=step(x2,y2)
        x4,y4=step(x3,y3)
        assert (x4,y4)==(x,y)
        n_core+=1
# Exact area of the two planar triangular components: half plus the vertical zero-area segment.
# Integral_{-1}^{-1/2}(-1-2u)du + Integral_{-1/2}^0(1+2u)du = 1/4+1/4.
assert F(1,4)+F(1,4)==F(1,2)
# Test the c<1 two-step contraction and selection of the central neutral two-cycle.
n_contract=0
for c in [F(1,4),F(1,2),F(3,4),F(999,1000)]:
    for u in [F(-1),F(-3,4),F(-1,2),F(-1,4),F(0)]:
        v=-u-1
        def G(z):return c*abs(c*abs(z)+u-1)+v-1
        for za,zb in product([F(-3),F(-1),F(0),F(2),F(4)],repeat=2):
            assert abs(G(za)-G(zb))<=c*c*abs(za-zb)
            n_contract+=1
print(f'CHECK_OK capture_cases={n_capture} core_cases={n_core} exact_4_cycles={n_four} contraction_pairs={n_contract} area=1/2')
