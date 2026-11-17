"""Exact rational checks for a three-branch focus-return map.

Python 3 standard library only. Finite checks support, but do not replace,
analytic statements about all real initial conditions and all iterates.
"""
from fractions import Fraction as Q
from math import log


def F(x, y):
    return ((x + y + 1, Q(0)) if x <= 0 else (y + 1, -2*x))


def section_return(u):
    x, y = u, Q(0)
    for n in range(1, 20):
        x, y = F(x, y)
        if y == 0 and 0 <= x <= 1:
            return n, x
    raise AssertionError('no return in 20 steps')


def predicted(u):
    if 0 < u < Q(1,4):
        return 6, 4*u
    if Q(1,4) < u < Q(1,2):
        return 5, 4*u-1
    if Q(1,2) < u < 1:
        return 5, 2-2*u
    raise ValueError('exclude endpoint histories')


checks = 0
for denominator in [13,17,29,31,43,47,53,101,257,509]:
    for numerator in range(1, denominator):
        u = Q(numerator, denominator)
        if u in (Q(1,4), Q(1,2)):
            continue
        assert section_return(u) == predicted(u), (u, section_return(u), predicted(u))
        checks += 1

# Three full-branch linear maps, with exact reciprocal-slope branch weights.
slopes = (Q(4), Q(4), Q(-2))
lengths = (Q(1,4), Q(1,4), Q(1,2))
roofs = (6,5,5)
assert sum(lengths) == 1
assert all(abs(1/slopes[j]) == lengths[j] for j in range(3))
assert sum(lengths[j]*roofs[j] for j in range(3)) == Q(21,4)
assert sum(lengths[j]*roofs[j]**2 for j in range(3)) == Q(111,4)
# Var(R)=E(R^2)-E(R)^2=3/16.
assert Q(111,4)-Q(21,4)**2 == Q(3,16)
assert (Q(3,16) / (Q(21,4)**3)) == Q(4,3087)

# F_R(z)-X is multiplication by A_R, and A_R^2=-2I.
X = (Q(1,3),Q(-2,3))
assert F(*X) == X
for x,y in [(Q(1),Q(-1)),(Q(2,3),Q(0)),(Q(5,2),Q(-3)),(Q(4),Q(7))]:
    xr,yr = (y+1,-2*x)
    xrr,yrr = (yr+1,-2*xr)
    assert (xrr-X[0],yrr-X[1]) == (-2*(x-X[0]),-2*(y-X[1]))

# The proposed finite metric graph is invariant; test each affine segment
# at all partition vertices and rational interior points.
vertices = [(Q(-2),Q(0)),(Q(-1),Q(0)),(Q(0),Q(0)),(Q(1),Q(0)),
            (Q(-1),Q(-2)),(Q(1),Q(-2))]
segments = [(vertices[0],vertices[3]),(vertices[3],vertices[5]),
            (vertices[5],vertices[4]),(vertices[4],vertices[1])]
def in_graph(x,y):
    return ((y==0 and -2<=x<=1) or
            (x==1 and -2<=y<=0) or
            (y==-2 and -1<=x<=1) or
            (x==-1 and -2<=y<=0))
for A,B in segments:
    for den in (2,3,7,11):
        for i in range(den+1):
            t=Q(i,den)
            z=(A[0]*(1-t)+B[0]*t,A[1]*(1-t)+B[1]*t)
            assert in_graph(*z)
            assert in_graph(*F(*z)), (z,F(*z))
            checks += 1

# Numerical checks only for the entropy root/strict separation.
a,b=1.0,2.0
for _ in range(120):
    c=(a+b)/2
    if c**6-2*c-1>0: b=c
    else: a=c
lam=(a+b)/2
h_top=log(lam)
h_phys=2*log(2)/7
assert abs(lam**6-2*lam-1)<5e-14
assert h_top>h_phys
assert abs(lam**-6+2*lam**-5-1)<1e-13
print('PASS: rational branch and graph checks',checks)
print('PASS: branch probabilities = 1/4,1/4,1/2; roof = 6,5,5; mean roof = 21/4')
print('PASS: i.i.d. renewal variance = 3/16 and counting CLT variance = 4/3087')
print('PASS: isolated fixed focus and A_R^2 = -2 I')
print('topological entropy',repr(h_top),'physical entropy',repr(h_phys))
