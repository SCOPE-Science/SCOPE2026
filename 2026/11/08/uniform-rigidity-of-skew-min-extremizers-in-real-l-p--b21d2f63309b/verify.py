"""Finite reproducibility diagnostics for a skew minimax stability theorem.

The general theorem is established analytically. These tests independently probe
normalization, extremal witnesses, and the quartic defect identity.
"""
import math
import random
from fractions import Fraction

SEED = 2611031
rnd = random.Random(SEED)
assertions = 0

def check(condition):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError('diagnostic failed at assertion %d' % assertions)

def norm(x, p):
    return sum(abs(a)**p for a in x)**(1/p)

# General sharp inequality on finite counting-measure spaces.
for p in (1.15, 1.5, 1.9, 2., 2.5, 4., 7., 12.):
    K = 2**abs(1/p-0.5)
    for _ in range(350):
        d = rnd.randint(2, 19)
        u = [rnd.uniform(-1,1) for _ in range(d)]
        v = [rnd.uniform(-1,1) for _ in range(d)]
        un, vn = norm(u,p),norm(v,p)
        u = [a/un for a in u]
        v = [a/vn for a in v]
        theta=rnd.uniform(0,math.pi/2)
        r,s = math.cos(theta),math.sin(theta)
        a=norm([r*x+s*y for x,y in zip(u,v)],p)
        b=norm([s*x-r*y for x,y in zip(u,v)],p)
        check(min(a,b)<=K+2e-12)

# Extremizers for subquadratic and superquadratic exponents.
for p in (1.13, 1.6, 1.99, 2.01, 3.1, 4., 10.):
    K=2**abs(1/p-.5)
    if p<2:
        u=[1.,0.]
        v=[0.,1.]
    else:
        z=2**(-1/p)
        u=[z,z]
        v=[z,-z]
    r=s=2**(-.5)
    a=norm([r*x+s*y for x,y in zip(u,v)],p)
    b=norm([s*x-r*y for x,y in zip(u,v)],p)
    check(abs(a-K)<2e-12)
    check(abs(b-K)<2e-12)

# Exact rational quartic defect identity, for exactly normalized pairs
# with rational fourth-power norm: use arbitrary rational nonunit vectors
# and normalize with their positive fourth roots in the identity below.
# Instead test the homogeneous identity including both fourth moments.
for _ in range(900):
    d=rnd.randrange(2,12)
    x=[Fraction(rnd.randint(-4,4),rnd.randint(1,7)) for _ in range(d)]
    y=[Fraction(rnd.randint(-4,4),rnd.randint(1,7)) for _ in range(d)]
    u4=sum(z**4 for z in x)
    v4=sum(z**4 for z in y)
    P=sum(xi*xi*yi*yi for xi,yi in zip(x,y))
    Q=sum(xi**3*yi+xi*yi**3 for xi,yi in zip(x,y))
    plus=sum((xi+yi)**4 for xi,yi in zip(x,y))/4
    minus=sum((xi-yi)**4 for xi,yi in zip(x,y))/4
    check(plus+minus == (u4+v4+6*P)/2)
    check(plus-minus==2*Q)
    check(min(plus,minus) == (u4+v4+6*P)/4-abs(Q))

print('VERIFY_OK',assertions,'finite assertions; analytic proof required')
