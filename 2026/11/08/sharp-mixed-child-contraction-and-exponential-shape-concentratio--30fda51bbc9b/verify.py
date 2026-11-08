#!/usr/bin/env python3
"""Exact polyhedral proof checker for the largest-angle bisection mixed-block bound.
Uses only Python's standard library and rational arithmetic.
All possible ordering regions and their vertices are exhausted symbolically.
"""
from fractions import Fraction as Q
from itertools import combinations

Z = (Q(0), Q(0), Q(0))
a = (Q(1, 2), Q(0), Q(0))
b = (Q(0), Q(1), Q(0))
c = (Q(0), Q(0), Q(1))

def add(u, v):
    return tuple(p + q for p, q in zip(u, v))

def neg(u):
    return tuple(-p for p in u)

def sub(u, v):
    return add(u, neg(v))

def mul(q, u):
    return tuple(q * p for p in u)

def val(u, x, y):
    return u[0] + u[1]*x + u[2]*y

# Branch cases are sorted raw child angle triples (a,b,a+c) and (a,c,a+b).
# Each returned triple is half of its largest angle, followed by middle and least.
def L(t, j):
    A, B, C = t
    if j == 0:  # B>=A+C>=A
        return (mul(Q(1,2), B), add(A,C), A), [sub(B,add(A,C))]
    if j == 1:  # A+C>=B>=A
        return (mul(Q(1,2), add(A,C)), B, A), [sub(add(A,C),B),sub(B,A)]
    if j == 2:  # A+C>=A>=B
        return (mul(Q(1,2), add(A,C)), A, B), [sub(A,B)]
    raise ValueError(j)

def R(t, j):
    A, B, C = t
    if j == 0:  # A>=C
        return (mul(Q(1,2),add(A,B)), A, C), [sub(A,C)]
    if j == 1:  # C>=A
        return (mul(Q(1,2),add(A,B)), C, A), [sub(C,A)]
    raise ValueError(j)

# A compact convex polygon is specified by linear half-planes g(x,y)>=0.
# Any linear inequality on such a polygon is decided at the exact vertices.
def vertices(halfplanes):
    pts = set()
    for u, v in combinations(halfplanes, 2):
        a0,a1,a2 = u
        b0,b1,b2 = v
        det = a1*b2-a2*b1
        if det == 0:
            continue
        x = (-a0*b2+a2*b0)/det
        y = (-a1*b0+a0*b1)/det
        if all(val(g,x,y)>=0 for g in halfplanes):
            pts.add((x,y))
    return sorted(pts)

original = (a,b,c)
base = [sub(b,c), c, sub((Q(1),Q(0),Q(0)),b)] # x>=y>=0, x<=1.
# In each cell, M-m is this linear function.
spread_cases = [
    (sub(b,a), [sub(b,a),sub(c,a)]),
    (sub(b,c), [sub(b,a),sub(a,c)]),
    (sub(a,c), [sub(a,b)]),
]
nonempty = 0
vertex_checks = 0
one_step_checks = 0
one_step_width_checks = 0
max_gap = None
worst = None

for direction in 'LR', 'RL':
    first, second = direction
    first_fn = L if first == 'L' else R
    second_fn = L if second == 'L' else R
    for i in range(3 if first == 'L' else 2):
        t1, c1 = first_fn(original, i)
        for j in range(3 if second == 'L' else 2):
            t2, c2 = second_fn(t1, j)
            for spread, cs in spread_cases:
                poly = vertices(base + c1 + c2 + cs)
                if not poly:
                    continue
                nonempty += 1
                for px, py in poly:
                    vertex_checks += 1
                    m0 = min(val(z,px,py) for z in original)
                    m1 = min(val(z,px,py) for z in t1)
                    m2 = min(val(z,px,py) for z in t2)
                    assert m1 >= m0 and m2 >= m1, (direction,i,j,px,py,'minimum decrease')
                    one_step_checks += 2
                    v0 = val(spread,px,py)
                    v1 = max(val(z,px,py) for z in t1)-m1
                    assert v1 <= v0, (direction,i,j,px,py,"one_step_spread")
                    one_step_width_checks += 1
                    v2 = max(val(z,px,py) for z in t2)-m2
                    gap = v2 - Q(3,4)*v0
                    if max_gap is None or gap > max_gap:
                        max_gap = gap
                        worst = (direction,i,j,px,py)
                    assert gap <= 0, (direction,i,j,px,py,gap)

assert nonempty == 31, nonempty
assert max_gap == 0, (max_gap,worst)
# Exact sharpness: normalized isosceles inputs x=y=t, 0<t<1/2.
# RL maps (t,t) to ((t+1/2)/(t+3/2), 2t/(t+3/2)),
# and (H(RL(t,t))-1)/(H(t,t)-1)=3/4.
for t in (Q(1,100),Q(1,8),Q(1,4),Q(2,5),Q(49,100)):
    x,y = (t+Q(1,2))/(t+Q(3,2)), 2*t/(t+Q(3,2))
    h0 = Q(1,2)/t
    h2 = Q(1,2)/y
    assert (h2-1) == Q(3,4)*(h0-1)
    assert x <= Q(1,2) and y <= x
print('VERIFY_OK rational_cells=%d vertex_checks=%d minimum_checks=%d one_step_width_checks=%d maximal_linear_gap=%s sharp_isosceles_cases=5' %
      (nonempty,vertex_checks,one_step_checks,one_step_width_checks,max_gap))
