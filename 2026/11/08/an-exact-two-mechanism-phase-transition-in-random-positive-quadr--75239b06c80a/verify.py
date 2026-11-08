"""Standalone cross-checks for exact degree-two random-node quadrature formulas.
Runs with standard Python 3. This is supporting finite evidence, not a proof.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import log, sqrt, pi
import random

GRID = tuple(map(F, ['-5/6','-1/2','-1/6','1/6','1/2','5/6']))
TARGETS = tuple(map(F, ['1/9','1/5','1/3','1/2','4/5']))

def geometry(nodes, q):
    neg = [-z for z in nodes if z < 0]
    pos = [z for z in nodes if z > 0]
    return bool(neg and pos and min(neg) * min(pos) <= q <= max(neg) * max(pos))

def direct(nodes, q):
    # Caratheodory: target (0,q) lies in the convex hull iff some <=3 nodes suffice.
    for a,b in combinations(sorted(set(nodes)), 2):
        if a < 0 < b and -a*b == q: return True
    for a,b,c in combinations(sorted(set(nodes)), 3):
        weights = [(q + y*z) / ((x-y)*(x-z)) for x,y,z in ((a,b,c),(b,a,c),(c,a,b))]
        if all(w >= 0 for w in weights): return True
    return False

checks=0
for m in (3,4,5):
    for tup in product(GRID, repeat=m):
        for q in TARGETS:
            assert geometry(tup,q) == direct(tup,q),(tup,q)
            checks+=1

# Independent high-precision-ish composite midpoint quadrature for finite-m laws.
def midint(fn, lo, hi, count=50000):
    step=(hi-lo)/count
    return step*sum(fn(lo+(i+.5)*step) for i in range(count))

def fail_parts(m,q):
    h=(1+q)/2
    PA=h**m + m/2*midint(lambda x: ((x+q/x)/2)**(m-1),q,1)
    PB=m/2*midint(lambda s: ((2-s-q/s)/2)**(m-1)-((1-s)/2)**(m-1),q,1)
    return PA,PB

for q in (.05,3-2*sqrt(2),1/3,.7):
    pa2,pb2=fail_parts(2,q)
    assert abs(pa2+pb2-1)<1e-9
    pa3,pb3=fail_parts(3,q)
    p3=1-pa3-pb3
    exact=1.5*q*(log(1/q)-1+q)
    assert abs(p3-exact)<1e-9,(q,p3,exact)
    pa4,pb4=fail_parts(4,q)
    assert abs((1-pa4-pb4)-2*exact)<1e-9

# Checks of large-m prefactors, at fixed parameters away from endpoint degeneracies.
for q in (.05,3-2*sqrt(2),1/3):
    h=(1+q)/2
    b=1-sqrt(q)
    m=200
    pa,pb=fail_parts(m,q)
    assert abs(pa/(2/(1-q)*h**m)-1)<.04
    assert abs(pb/(sqrt(pi*m*sqrt(q)/(2*b))*b**m)-1)<.04

# Deterministic seeded Monte Carlo comparisons for the three-node closed law.
rng=random.Random(2602326)
for q in (.08,1/3,.65):
    total=90000
    hits=sum(geometry([rng.uniform(-1,1) for _ in range(3)],q) for _ in range(total))
    expected=1.5*q*(log(1/q)-1+q)
    assert abs(hits/total-expected)<.012

print('VERIFY_OK',checks,'exact-rational configuration checks; integral/moment/asymptotic/MC cross-checks passed')
