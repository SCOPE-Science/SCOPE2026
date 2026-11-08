#!/usr/bin/env python3
"""Exact certificate for a five-cycle two-probe trace-coupling problem.
Uses only the Python standard library; all arithmetic is rational/integer.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter

# Affine value p+q*t of the Rademacher quadratic edge sum.
LEVELS = {'A': (4, 1, 1), 'B': (2, -1, 4),
          'C': (0, 1, 6), 'D': (-2, -1, 4),
          'E': (-4, 1, 1)}
ORDERS = [('E', 'D', 'C', 'B', 'A'),
          ('D', 'E', 'B', 'C', 'A'),
          ('D', 'B', 'E', 'C', 'A')]
INTERVALS = [(F(0), F(1)), (F(1), F(3)), (F(3), None)]
EXPECTED = [(F(0), F(0), F(4)), (F(7), F(-4), F(1)),
            (F(4), F(0), F(0))]
checks = 0

def check(test, info):
    global checks
    assert test, info
    checks += 1

def polynomial(pair):
    p, q = pair
    return F(p), F(q)

def groups(t):
    vals=[]
    for z in product((-1, 1), repeat=5):
        sig=[z[i]*z[(i+1)%5] for i in range(5)]
        vals.append(sum(sig[:4])+t*sig[4])
    return vals

def from_order(order):
    out=[]
    for name in order:
        p,q,k = LEVELS[name]
        out.extend([(p,q)]*k)
    check(len(out)==16, 'level multiplicities')
    return out

def sym_variance(order):
    seq=from_order(order)
    coeff=[F(0),F(0),F(0)]
    for a,b in zip(seq,reversed(seq)):
        p=F(a[0]+b[0]);q=F(a[1]+b[1])
        for i,v in enumerate([p*p,2*p*q,q*q]):coeff[i]+=v/F(16)
    return tuple(coeff)

def value(c,t): return c[0]+c[1]*t+c[2]*t*t

def coupling_variance(t):
    sorted_values=sorted(groups(t))
    return sum((a+b)**2 for a,b in zip(sorted_values,reversed(sorted_values)))/32

def best_fixed_flip(t):
    # z'=s*z for fixed s; exactly 32 possible choices.
    wins=[]
    for sign in product((-1,1), repeat=5):
        edge=[sign[i]*sign[(i+1)%5] for i in range(5)]
        winners=sum((F(1) if i<4 else t)**2 for i,e in enumerate(edge) if e==1)
        wins.append(4*winners)
    return min(wins)

# Invariants: the product of edge-signs is one; each of the 16 patterns
# appears exactly twice among the 32 vertex-sign assignments.
patterns=Counter()
for z in product((-1,1), repeat=5):
    e=tuple(z[i]*z[(i+1)%5] for i in range(5))
    check(__import__('math').prod(e)==1,'cycle parity')
    patterns[e]+=1
check(len(patterns)==16, '16 parity patterns')
for n in patterns.values():check(n==2,'uniform fibers')

# The affine level ordering is verified at interval endpoints and one interior
# test, sufficient because every pairwise difference is affine.
for idx,(order,interval,coeff) in enumerate(zip(ORDERS,INTERVALS,EXPECTED)):
    lo,hi=interval
    for pair_name in zip(order,order[1:]):
        p1,q1,_=LEVELS[pair_name[0]]; p2,q2,_=LEVELS[pair_name[1]]
        for t in ([lo,hi] if hi is not None else [lo,lo+1]):
            check(p1+q1*t<=p2+q2*t, (idx,'ordering',pair_name,t))
        if hi is None:check(q1<=q2,(idx,'order at infinity',pair_name))
    check(sym_variance(order)==coeff, (idx,'polynomial',sym_variance(order),coeff))

# Full exact 32-state cross-check on a dense rational parameter grid including
# all order boundaries, plus optimality among all fixed sign-flip probes.
samples={F(0),F(1),F(2),F(3),F(4),F(10)}
for denominator in range(1,32):
    for numerator in range(1,10*denominator+1):
        samples.add(F(numerator,denominator))
for t in sorted(samples):
    expected=(4*t*t if t<=1 else ((t-2)**2+3 if t<=3 else F(4)))
    check(coupling_variance(t)==expected, ('coupling variance',t))
    flip=4*min(F(1),t*t)
    check(best_fixed_flip(t)==flip, ('fixed flip variance',t))
    check(expected<=flip,('global vs flip',t))
    check(expected>=0,('variance nonnegative',t))
    check(2*(4+t*t)>=expected,('iid benchmark',t))

# Independent small-cycle minimality checks (analytic proof is in RESULT.md):
# On positive triangles antitone coupling preserves one smallest edge, whereas
# every even cycle has a fixed alternating vertex sign flip with zero error.
for a,b,c in [(F(1),F(1),F(1)), (F(3,2),F(1),F(1,4)),
              (F(3),F(2),F(1)), (F(7,3),F(13,9),F(2,5))]:
    triangle=[]
    for z in product((-1,1),repeat=3):
        triangle.append(a*z[0]*z[1]+b*z[1]*z[2]+c*z[2]*z[0])
    triangle.sort()
    v=sum((x+y)**2 for x,y in zip(triangle,reversed(triangle)))/8
    check(v==4*min(a*a,b*b,c*c),('triangle',a,b,c,v))
for n in (4,6,8):
    for z in product((-1,1),repeat=n):
        z_alt=[((-1)**i)*z[i] for i in range(n)]
        for i in range(n):
            check(z[i]*z[(i+1)%n]+z_alt[i]*z_alt[(i+1)%n]==0,
                  ('even cycle',n,z,i))

check(coupling_variance(F(2))==3,'sharp t=2 value')
check(best_fixed_flip(F(2))==4,'sharp t=2 fixed flip')
check(2*(4+F(2)**2)==16,'sharp t=2 independent')
print('PASS',checks,'exact assertions')
print('Optimal variances: t in (0,1): 4t^2; [1,3]: (t-2)^2+3; [3,infinity): 4')
print('Optimal fixed sign-flip variance: 4 min(1,t^2)')
print('At t=2: global 3, fixed sign-flip 4, independent 16; relative extra improvement 1/4')
