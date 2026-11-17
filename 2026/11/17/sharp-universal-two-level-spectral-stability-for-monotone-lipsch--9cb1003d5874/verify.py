#!/usr/bin/env python3
"""Numerical corroboration for sharp two-level spectral functional calculus; standard library only."""
from fractions import Fraction
import itertools, math, random

def norm(a,z,c):
    return (math.hypot(a-c,2*z)+abs(a+c))/2

def positive_part(a,z,c):
    m=(a+c)/2; d=(a-c)/2; r=math.hypot(d,z)
    if m>=r: return (a,z,c)
    if m<=-r: return (0.,0.,0.)
    t=(m+r)/2
    return (t*(1+d/r),t*z/r,t*(1-d/r))

def normdiff(X,Y):
    return norm(*(x-y for x,y in zip(X,Y)))

# Rational parametrizations of real Hermitian unitaries, including both scalar unitaries.
maskcounts=0
for u,v,w in itertools.product((0,1),repeat=3):
    for k in range(-300,301):
        t=k/300; h=math.sqrt(max(0,1-t*t))
        assert norm(u*t,v*h,-w*t)<=2/math.sqrt(3)+1e-12
        maskcounts+=1
    assert max(u,w)<=2/math.sqrt(3)
print('ALL_EIGHT_SCHUR_VERTEX_MASKS_PASS',maskcounts)

# Exact critical algebra: a^2=1/3 solves 4-3 a^2=9 a^2, and value 2/sqrt(3).
a=1/math.sqrt(3); b=math.sqrt(2/3)
assert abs(a*a+b*b-1)<1e-14
assert abs((a+math.sqrt(4-3*a*a))/2-2/math.sqrt(3))<1e-14
assert abs(norm(a,b,0)-2/math.sqrt(3))<1e-14
print('EXACT_CRITICAL_UNITARY_FORMULA_PASS')

# Perturb an indefinite diagonal input; positive clipping differentiates to the mask (1,w,0).
H=(a,b,-a)
for eps,delt in ((1e-2,1e-6),(1e-3,1e-7),(1e-4,1e-8)):
    X=(1.,0.,-eps); Y=tuple(x+delt*y for x,y in zip(X,H))
    ratio=normdiff(positive_part(*Y),positive_part(*X))/delt
    assert ratio<=2/math.sqrt(3)+2e-7
    assert 2/math.sqrt(3)-ratio<5*eps+1e-6
    print('SHARP_POSITIVE_PART_APPROACH',eps,format(ratio,'.10f'))

rng=random.Random(60473)
for j in range(1500):
    X=tuple(rng.uniform(-2,2) for _ in range(3))
    Y=tuple(rng.uniform(-2,2) for _ in range(3))
    gain=normdiff(positive_part(*X),positive_part(*Y))/normdiff(X,Y)
    assert gain<=2/math.sqrt(3)+1e-12
print('RANDOM_REAL_SYMMETRIC_PAIRS_PASS_1500')
print('ALL_TWO_LEVEL_FUNCTIONAL_CALCULUS_CHECKS_PASS')
