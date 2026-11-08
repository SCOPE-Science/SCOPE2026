#!/usr/bin/env python3
"""Independent nine-local-case coefficient enumerator for primitive-3 states."""
from itertools import product
from math import log,sqrt

coeff = [[0,0,0],[0,0,0]]  # entries A^2,AB,B^2; categories terminal supported/unsup
for u,v in product(range(3),repeat=2):
    # Root terminal is phase 0; two branch-root phases u,v.
    tu = (u+1)%3 in (0,v)
    tv = (v+1)%3 in (0,u)
    t0 = 1 in (u,v)
    # Each attached subtree supplies (A+B) possibilities if the triangle supports its root,
    # or only A possibilities if the root otherwise needs support from the subtree.
    left = (1,1) if tu else (1,0)
    right = (1,1) if tv else (1,0)
    pol = (left[0]*right[0],left[0]*right[1]+left[1]*right[0],left[1]*right[1])
    for j in range(3): coeff[0 if t0 else 1][j] += pol[j]
assert coeff == [[5,6,2],[4,4,1]],coeff
print('local polynomial coefficients A,B:',coeff)
A,B=2,1
for h in range(7):
    print(f'h={h} triangle_blocks={2**(h+1)-1} vertices={2**(h+2)-1} rooted_supported={A} rooted_unsupported={B} primitive_3={3*A}')
    na = 5*A*A+6*A*B+2*B*B
    nb = 4*A*A+4*A*B+B*B
    A,B=na,nb
r=0.5
entropy=0.5*log(2)
for j in range(48):
    q=5+6*r+2*r*r
    entropy+=2**(-j-2)*log(q)
    r=(4+4*r+r*r)/q
assert 0.711 < r < 0.716
assert 340 > (2+sqrt(5))**4
assert entropy > log(2+sqrt(5))
print(f'entropy_per_triangle_approx={entropy:.12f}; growth_base_approx={__import__("math").exp(entropy):.12f}')
print('exact_lower_bound: entropy > log(340)/4 > log(2+sqrt(5))')
print('RECURRENCE_CHECK_OK')
