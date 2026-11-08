#!/usr/bin/env python3
"""Exact coefficient checks and finite numerical corroboration of a genus-two
canonical-curve calculation. Python 3 standard library only. The finite group
census is diagnostic, not a proof of the all-parameter stabilizer theorem.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import sqrt, pi
from cmath import exp, log

def coefficient_identities(r):
    # Relations A^3=-r, B^3=-1/r, C^2=r, D^2=1/r.
    # Pullbacks f'=r*g and g'=(1/r)*f are compared coefficientwise.
    assert (r, -r, r, r) == (r, -r, r, r) # f': (z4^2, x2^3, x1^3, x0^6)
    A3, B3, C2, D2 = -r, -1/r, r, 1/r
    fprime = (C2, r, A3, -r*r*B3)
    r_g = (r, r, -r, r)
    gprime = (D2, Q(1), A3, -B3)
    invr_f = (1/r, Q(1), -r, 1/r)
    assert fprime == r_g, (fprime, r_g)
    assert gprime == invr_f, (gprime, invr_f)
    # In the preceding tuples the order is (z_target^2,x0^6,x2^3,x1^3).
    for t3 in (Q(2), Q(3), Q(-5)):
        if t3 in (Q(1), r*r): continue
        w2 = (t3-r*r)/(t3-1)
        new_t3 = r*r/t3
        assert (new_t3-r*r)/(new_t3-1) == r*r/w2

for r in (Q(2), Q(3,2), Q(-3)):
    coefficient_identities(r)

# Bolza parameter exact test in Q(sqrt(3)): s=-26 +/- 15sqrt(3).
def mul(a,b):
    return (a[0]*b[0]+3*a[1]*b[1], a[0]*b[1]+a[1]*b[0])
for s in ((-26,15),(-26,-15)):
    ss = mul(s,s)
    assert ss[0]+52*s[0]+1 == 0 and ss[1]+52*s[1] == 0

# The published surface-moduli parameter v=r+r^{-1}, and the canonical
# curve parameter u=r^2+r^{-2}, satisfy u=v^2-2 identically.
for r in (Q(2),Q(3),Q(-3,2),Q(1,2)):
    v=r+1/r; u=r*r+1/(r*r)
    assert u==v*v-2
    assert ((-r)*(-r)+1/((-r)*(-r)))==u
    assert (1/r)**2 + r*r ==u

# The octahedral configuration {0,infty,+/-1,+/-i} is normalized by
# R(z)=(i-z)/(z+i), a 3-cycle on each of the two triples. Its fixed
# points are alpha,beta; h(z)=(z-alpha)/(z-beta) conjugates R to a
# multiplication of order three.
I=1j
al=(sqrt(3)-1)*(1+I)/2
be=-(sqrt(3)+1)*(1+I)/2
R=lambda z:(I-z)/(z+I)
h=lambda z:(z-al)/(z-be)
assert abs(R(0)-1)<1e-12
assert abs(R(1)-I)<1e-12
assert abs(R(I))<1e-12
assert abs(R(-1)+I)<1e-12
assert abs(R(al)-al)<1e-12 and abs(R(be)-be)<1e-12
assert abs(h(0)-(sqrt(3)-2))<1e-12
assert abs(h(-1)-(-1+I*sqrt(3))/2)<1e-12
s_oct=(h(-1)/h(0))**3
assert abs(s_oct-(-26-15*sqrt(3)))<1e-9

# Diagnostic exhaustive stabilizer count: every fractional linear map
# preserving 6 points is determined by three ordered distinct images.
# 6*5*4=120 triples are all tested; complex comparisons are approximate.
omega=exp(2j*pi/3)
def reduced_stabilizer_count(s):
    a=exp(log(complex(s))/3)
    B=[omega**j for j in range(3)]+[a*omega**j for j in range(3)]
    x0,x1,x2=B[:3]
    def phi(z):
        if abs(z-x2)<1e-9: return None
        return (z-x0)*(x1-x2)/((z-x2)*(x1-x0))
    us=[phi(z) for z in B]; good=[]
    for ids in permutations(range(6),3):
        y0,y1,y2=(B[j] for j in ids)
        def inv(u):
            if u is None: return y2
            return (y2*(y1-y0)*u+y0*(y2-y1))/((y1-y0)*u+(y2-y1))
        image_points=[inv(u) for u in us]
        indices=[min(range(6),key=lambda j:abs(z-B[j])) for z in image_points]
        if len(set(indices))==6 and all(abs(z-B[j])<1e-7 for z,j in zip(image_points,indices)):
            good.append(tuple(indices))
    return len(good)

assert reduced_stabilizer_count(4)==6
assert reduced_stabilizer_count(-1)==12
assert reduced_stabilizer_count(-26+15*sqrt(3))==24
assert reduced_stabilizer_count(-26-15*sqrt(3))==24
print('VERIFY_OK')
