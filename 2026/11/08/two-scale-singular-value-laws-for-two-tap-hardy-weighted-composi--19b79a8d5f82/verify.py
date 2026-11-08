#!/usr/bin/env python3
"""Exact rational checks for a two-scale Hardy weighted-composition theorem.
No external dependencies; finite checks corroborate rather than prove the infinite theorem.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import comb

checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

def path_polynomial(k, c):
    """Independently enumerate nonnegative closed nearest-neighbor cyclic paths."""
    coeff = defaultdict(F)
    def grow(path):
        if len(path) == k:
            if abs(path[-1] - path[0]) > 1 or min(path) != 0:
                return
            stays = sum(path[i] == path[(i+1)%k] for i in range(k))
            coeff[sum(path)] += (1+c*c)**stays * c**(k-stays)
            return
        for b in range(max(0,path[-1]-1),path[-1]+2):
            if b <= k:
                grow(path+[b])
    for start in range(k//2+1):
        grow([start])
    return dict(coeff)

def gram(n,r,m,c):
    a = 1+c*c
    mat = [[F(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        mat[j][j] = a*r**(2*j)
        if j+m<n:
            mat[j][j+m] = mat[j+m][j] = c*r**(2*j+m)
    return mat

def mul(x,y):
    n=len(x)
    z=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for t, v in enumerate(x[i]):
            if not v:continue
            for j, w in enumerate(y[t]):
                if w:z[i][j]+=v*w
    return z

def trace_power(x,k):
    p=x
    for _ in range(k-1):p=mul(p,x)
    return sum(p[i][i] for i in range(len(p)))

for c in (F(1),F(2,3),F(3,2)):
    a=1+c*c
    for k in range(1,7):
        pp=path_polynomial(k,c)
        check(len(pp)>0,('nonempty',c,k))
        check(pp.get(0)==a**k,('constant',c,k))
        check(all(v>0 for v in pp.values()),('positivity',c,k))
        check(sum(pp.values())==sum(F(comb(k,j)**2)*c**(2*j) for j in range(k+1)),('circle',c,k))
        if k>1:check(any(i>0 for i in pp),('strict',c,k))
        if k==2:check(pp=={0:a*a,1:2*c*c},('fourth',c))
        if k==3:check(pp=={0:a**3,1:3*a*c*c,2:3*a*c*c},('sixth',c))
        check(max(pp)<k*k,('finite',c,k))

# Direct finite Gram powers are bounded strictly below the exact full trace;
# a closed path absent from an N x N compression starts within m*k of the edge.
# Its minimal vertex is at least N-2*m*k, and a row has at most 3 choices per step.
for r,m,c,n in [(F(1,2),1,F(1),24), (F(2,3),2,F(2,3),36),
                (F(3,5),3,F(3,2),42)]:
    g=gram(n,r,m,c)
    for k in (1,2,3):
        p=path_polynomial(k,c)
        exact=sum(v*r**(2*m*degree) for degree,v in p.items())/(1-r**(2*k))
        low=trace_power(g,k)
        error=exact-low
        upper=F(3**k)*(1+c*c)**k*r**(2*k*(n-2*m*k))/(1-r**(2*k))
        check(error>0,('finite-lower',r,m,c,k))
        check(error<upper,('finite-tail',r,m,c,k))

print('TWO_TAP_EXACT_CHECK_OK',checks,'rational assertions; infinite spectral limits require the written proof')
