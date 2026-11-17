#!/usr/bin/env python3
"""Exact finite checks for labelled recursive-tree leaf/offspring covariance."""
from fractions import Fraction as Q
from itertools import product
from math import factorial, log

COUNT=0

def check(condition, message):
    global COUNT
    assert condition, message
    COUNT += 1

def harmonic(m):
    return sum((Q(1, r) for r in range(1, m+1)), Q(0))

def formula(n, i):
    assert 3 <= n and 2 <= i <= n
    return (Q(n-i, 2) - (i-1)*(harmonic(n-2)-harmonic(i-2)))/(n-1)

def local_formula(n, i, j):
    assert 2 <= i < j <= n
    return (Q(1, 2)-Q(i-1, j-2))/(n-1)

for n in range(3, 9):
    possibilities = factorial(n-1)
    leaves_total=Q(0)
    leaves_square=Q(0)
    kids_sum = {i:Q(0) for i in range(1,n+1)}
    kids_leaves = {i:Q(0) for i in range(1,n+1)}
    attach_count = {(i,j):Q(0) for j in range(3,n+1) for i in range(2,j)}
    attach_leaves = {key:Q(0) for key in attach_count}
    for choices in product(*(range(1,j) for j in range(2,n+1))):
        children=[0]*(n+1)
        for parent in choices:
            children[parent] += 1
        leaves = sum(children[i]==0 for i in range(1,n+1))
        leaves_total += leaves
        leaves_square += leaves*leaves
        for i in range(1,n+1):
            kids_sum[i] += children[i]
            kids_leaves[i] += children[i]*leaves
        for j in range(3,n+1):
            i=choices[j-2]
            if i>=2:
                attach_count[i,j]+=1
                attach_leaves[i,j]+=leaves
    EL=leaves_total/possibilities
    VL=leaves_square/possibilities-EL*EL
    check(EL==Q(n,2),f'leaves mean n={n}')
    check(VL==Q(n,12),f'leaves variance n={n}')
    for i in range(2,n+1):
        cov=kids_leaves[i]/possibilities-(kids_sum[i]/possibilities)*EL
        check(cov==formula(n,i),f'global covariance n={n},i={i}: {cov} vs {formula(n,i)}')
    for (i,j),count in attach_count.items():
        cov=attach_leaves[i,j]/possibilities-(count/possibilities)*EL
        check(cov==local_formula(n,i,j),f'local covariance n={n},i={i},j={j}')
    # The prior root case is included only as a consistency check.
    rootcov=kids_leaves[1]/possibilities-(kids_sum[1]/possibilities)*EL
    check(rootcov==Q(n-2,2*(n-1)),f'root consistency n={n}')

for n in range(3, 151):
    fs={i:formula(n,i)*(n-1) for i in range(2,n+1)}
    check(fs[n-1]==Q(-1,2) and fs[n]==0, f'endpoint n={n}')
    for i in range(2,n-1):
        check(fs[i+2]-2*fs[i+1]+fs[i]==Q(1,i),f'convex n={n},i={i}')
    signs=[(fs[i]>0)-(fs[i]<0) for i in range(2,n)]
    allowed=sorted(signs,reverse=True)
    check(signs==allowed, f'sign order n={n}: {signs}')
    check((fs[2]>0)==(n>=7),f'first onset n={n}')

rho=0.28466813704083843
check(abs((1-rho)/2+rho*log(rho))<1e-13,'asymptotic cutoff')
for t in [0.12,0.25,0.4,0.6,0.9]:
    n=200000
    i=int(t*n)
    # Fast harmonic-number approximations with certified deterministic error O(n^-2)
    H=lambda m: log(m)+0.5772156649015328606+1/(2*m)-1/(12*m*m)
    cv=((n-i)/2-(i-1)*(H(n-2)-H(i-2)))/(n-1)
    limit=(1-t)/2+t*log(t)
    check(abs(cv-limit)<6e-5,f'asymptotic profile t={t}: {cv} vs {limit}')
print(f'VERIFY_OK {COUNT} exact finite or profile assertions')
