#!/usr/bin/env python3
"""Exact, finite, reproducible checks of a real octagonal projection formula.

These checks confirm sharp witnesses on a rational grid; the mathematical
proof, not the finite grid, covers all real parameter values.
"""
from fractions import Fraction as F
from itertools import product

def determinant(matrix):
    """Gaussian elimination over exact Fractions."""
    rows = [[F(v) for v in row] for row in matrix]
    n = len(rows)
    det = F(1)
    for j in range(n):
        pivot = next((i for i in range(j,n) if rows[i][j]), None)
        if pivot is None: return F(0)
        if pivot != j:
            rows[j], rows[pivot] = rows[pivot], rows[j]
            det = -det
        z = rows[j][j]
        det *= z
        for i in range(j+1,n):
            t = rows[i][j]/z
            for k in range(j,n):
                rows[i][k] -= t*rows[j][k]
    return det

norming_pairs = [
 ((-1,-1,-1,-1),(-1,0)),
 ((-1,-1,-1,-1),('B-','B-')),
 ((-1,-1,-1,1),(0,-1)),
 ((-1,-1,-1,1),('B-','B-')),
 ((-1,1,-1,-1),(-1,0)),
 ((-1,1,-1,-1),('B-','B+')),
 ((-1,1,1,-1),(0,1)),
 ((-1,1,1,-1),('B-','B+')),
]
count = 0

def check(test):
    global count
    count += 1
    if not test:
        raise AssertionError('exact rational assertion %d' % count)

for beta in (F(1,2), F(51,100), F(3,5), F(2,3), F(3,4), F(1,1)):
    q = 2*beta*beta - 2*beta + 1
    a = (1-beta)/q
    b = (2*beta-1)/(2*q)
    value = beta/q
    theta = beta*(2*beta-1)/q
    pairs=[]
    for e, f in norming_pairs:
        fx = -beta if f[0]=='B-' else f[0]
        fy = -beta if f[1]=='B-' else (beta if f[1]=='B+' else f[1])
        pairs.append(([fx*v for v in e]+[fy*v for v in e]))
        x=a*e[0]+b*(e[2]+e[3])
        y=a*e[1]+b*(e[2]-e[3])
        check(fx*x+fy*y==value)
    check(determinant(pairs)==64*beta**4)
    check(q > 0)
    check(a >= 0 and b >= 0)
    check(0 <= theta <= 1)
    check(a + 2*beta*b == 1)
    check(a + 2*b == value)
    check(2*beta*(a+b) == value)
    # The two coefficient identities prove the dual inequality for all u,v.
    check(theta + (1-theta)*2*beta == value)
    check(2*theta + (1-theta)*2*beta == 2*beta*value)
    observed = F(0)
    for p in product((-1, 1), repeat=4):
        x = a*p[0]+b*(p[2]+p[3])
        y = a*p[1]+b*(p[2]-p[3])
        # Check each individual support, not just the combined maximum.
        for v in (abs(x), abs(y), beta*abs(x+y), beta*abs(x-y)):
            check(v <= value)
        observed = max(observed, abs(x), abs(y), beta*abs(x+y), beta*abs(x-y))
    check(observed == value)
    # Exact endpoint and interior behavior follows by factoring lambda - 1.
    check(value-1 == ((2*beta-1)*(1-beta))/q)
print('OCTAGONAL_ABSOLUTE_PROJECTION_EXACT_OK',count)
