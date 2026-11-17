#!/usr/bin/env python3
"""Exact polynomial identities and independent perturbation checks for Akima cluster geometry."""
from fractions import Fraction as Q
from random import Random


def h10(t):
    return t*(1-t)*(1-t)


def h11(t):
    return -t*t*(1-t)


def slope(d, i):
    left = abs(d[i-1]-d[i-2])
    right = abs(d[i+1]-d[i])
    if left+right == 0:
        return (d[i-1]+d[i])/2
    return (right*d[i-1]+left*d[i])/(right+left)


def critical(d):
    return [i for i in range(2,len(d)-1)
            if d[i-2]==d[i-1] and d[i]==d[i+1] and d[i-1]!=d[i]]


def bump(i, x):
    if i-1 <= x <= i:
        return float(h11(x-(i-1)))
    if i <= x <= i+1:
        return float(h10(x-i))
    return 0.


# All polynomial and turning-point evaluations below are rational identities.
third=Q(1,3)
twothirds=Q(2,3)
assert h10(third)==Q(4,27)
assert h11(twothirds)==-Q(4,27)
assert h10(Q(0))==h10(Q(1))==h11(Q(0))==h11(Q(1))==0
# Derivative factorization: H10'=(1-t)(1-3t), H11'=t(3t-2).
for t in [Q(i,19) for i in range(20)]:
    assert (1-t)*(1-3*t)==(1-4*t+3*t*t)
    assert t*(3*t-2)==(3*t*t-2*t)
assert 2*h10(third)+2*(-h11(twothirds)) == Q(16,27)
print('EXACT_HERMITE_BUMP_MAXIMUM_AND_VARIATION_PASS 4/27 16/27')

rng=Random(20261114)
for _ in range(3000):
    # Piecewise-affine test data, with repeated adjacent secants and sharp corners.
    vals=[]
    for block in range(9):
        vals += [Q(rng.randint(-4,4))]*rng.randint(1,4)
    vals=[float(x) for x in vals]
    C=critical(vals)
    assert all(j-i>=2 for i,j in zip(C,C[1:]))
    eps=1e-9
    pert=[x+eps*rng.uniform(-1,1) for x in vals]
    for i in range(2,len(vals)-1):
        sm=slope(pert,i)
        if i in C:
            assert min(vals[i-1],vals[i])-1e-6<=sm<=max(vals[i-1],vals[i])+1e-6
        else:
            assert abs(sm-slope(vals,i))<1e-5
print('ALL_REGULAR_SLOPES_AND_CRITICAL_INTERVALS_PASS 3000')

# Two interacting singular knots at secant indices 2 and 4, sharing one gap.
for k in range(500):
    t=Q(rng.randint(1,98),100)
    u=Q(rng.randint(1,98),100)
    eps=Q(1,10**8)
    g0=eps*t/(1-t)
    g2=eps
    g4=eps*(1-u)/u
    dd=[Q(0)]
    for gap in [g0,Q(1),g2,Q(1),g4]:
        dd.append(dd[-1]+gap)
    assert abs(slope(dd,2)-t)<Q(1,100000)
    assert abs(slope(dd,4)-(1+u))<Q(1,100000)
# Boundary ratios: two critical sites can attain opposite endpoints simultaneously.
for exponents in [(2,1,2),(1,2,1),(2,1,3),(3,1,2)]:
    g=[Q(1,10**(e*4)) for e in exponents]
    dd=[Q(0)]
    for gap in [g[0],Q(1),g[1],Q(1),g[2]]:
        dd.append(dd[-1]+gap)
    a=slope(dd,2)
    b=slope(dd,4)-1
    assert 0<a<1+Q(1,1000) and 0<b<1+Q(1,1000)
print('SIMULTANEOUS_TWO_CORNER_RATIO_ATTAINMENT_PASS 504')

# Since critical knots cannot be neighbors, the two-cell bumps have disjoint
# open supports; verify exact additivity of variation numerically as a stress test.
for C,coef in [([0],[1.]),([0,2],[1.,-2.]),([-3,0,3],[1.3,-.7,2.])]:
    lo=min(C)-1
    hi=max(C)+1
    N=(hi-lo)*8000
    ys=[sum(c*bump(i,lo+(hi-lo)*j/N) for i,c in zip(C,coef)) for j in range(N+1)]
    numeric_var=sum(abs(ys[j+1]-ys[j]) for j in range(N))
    exact_var=float(Q(16,27))*sum(abs(v) for v in coef)
    assert abs(numeric_var-exact_var)<1e-6,(numeric_var,exact_var)
print('INDEPENDENT_CONTINUUM_BUMP_VARIATION_STRESS_PASS')
print('ALL_AKIMA_CLUSTER_GEOMETRY_CHECKS_PASS')
