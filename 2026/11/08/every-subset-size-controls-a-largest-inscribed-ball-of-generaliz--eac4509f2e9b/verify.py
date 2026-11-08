#!/usr/bin/env python3
"""Reproducibility checks for Euclidean inballs of parking-function polytopes.

Requires Python 3.10+.  For independent numerical linear-program checks,
install scipy; the exact-formula and phase checks use the standard library.
Finite checks support, but do not prove, the all-dimensional theorem.
"""
from decimal import Decimal, getcontext
from itertools import combinations
from math import sqrt
import random

getcontext().prec = 65
D = Decimal
checks = 0

def ranking(b):
    n = len(b)
    s = []
    v = 0
    for x in b:
        assert isinstance(x, int) and x > 0
        v += x
        s.append(v)
    r = [sum(s[n-k:])-k for k in range(1,n+1)]
    return r

def thresholds(b):
    return [D(r)/(D(k)+D(k).sqrt()) for k,r in enumerate(ranking(b),1)]

def witness_for_layer(n,m):
    """Construct integer parameters whose sole tight upper-facet size is m."""
    assert n>=2 and 1<=m<=n
    g = [D(k)+D(k).sqrt() for k in range(n+1)]
    gaps = [2*g[k]-g[k-1]-g[k+1] for k in range(1,n)]
    eps = min(gaps)/D(16)
    rr = [g[k]+eps*(abs(k-m)-m) for k in range(n+1)]
    scale = D(10)**24
    ranks = [int((x*scale).to_integral_value()) for x in rr]
    increments = [ranks[k]-ranks[k-1] for k in range(1,n+1)]
    assert all(increments[k]>increments[k+1] for k in range(n-1))
    assert increments[-1]>=1
    ascending = increments[::-1]
    b = [ascending[0]+1]+[ascending[i]-ascending[i-1] for i in range(1,n)]
    assert all(v>=1 for v in b)
    return b

def norm_check(b):
    global checks
    n=len(b); vals=thresholds(b); rr=min(vals)
    # The centered closed ball satisfies every subset halfspace.
    rank=ranking(b)
    for k, limit in enumerate(rank,1):
        assert D(k)*rr + D(k).sqrt()*rr <= D(limit)+D('1e-22')
        checks += 1
    # The lower facets are tangent, and at least one upper layer is tangent.
    assert min(abs(v-rr) for v in vals) < D('1e-22')
    checks+=1
    # Any other radius would violate an active upper layer and the lower caps.
    k0 = vals.index(rr)+1
    assert (D(k0)+D(k0).sqrt())*rr - D(rank[k0-1]) < D('1e-22')
    checks+=1

rng=random.Random(51763)
for n in range(2,8):
    for z in range(24):
        b=[rng.randint(1,25) for _ in range(n)]
        norm_check(b)
for n in range(2,8):
    for m in range(1,n+1):
        b=witness_for_layer(n,m)
        vals=thresholds(b)
        assert all(vals[m-1] < vals[j] for j in range(n) if j!=m-1), (n,m,b)
        checks+=n
        norm_check(b)

# A modest, explicit 3D intermediate-facet phase: vector (34,1,16).
b=(34,1,16)
v=thresholds(b)
assert v[1]<v[0] and v[1]<v[2]
assert ranking(b)==[50,84,117]
checks+=3

# Completely independent full halfspace Chebyshev linear programs in small n.
try:
    from scipy.optimize import linprog
except ImportError:
    print('scipy missing: numerical LP cross-checks skipped')
else:
    for n in range(2,6):
        for rep in range(20):
            b=[rng.randint(1,14) for _ in range(n)]
            prefix=[]; s=0
            for t in b:
                s+=t;prefix.append(s)
            rows=[];rhs=[]
            for i in range(n):
                row=[0.0]*(n+1);row[i]=-1.0;row[-1]=1.0
                rows.append(row);rhs.append(-1.0)
            for k in range(1,n+1):
                for I in combinations(range(n),k):
                    row=[0.0]*(n+1)
                    for i in I:row[i]=1.0
                    row[-1]=sqrt(k)
                    rows.append(row);rhs.append(float(sum(prefix[n-k:])))
            result=linprog([0.0]*n+[-1.0],A_ub=rows,b_ub=rhs,
                           bounds=[(None,None)]*n+[(0,None)],method='highs')
            assert result.success
            rad=float(min(thresholds(b)))
            assert abs(result.x[-1]-rad)<1e-7
            assert all(abs(result.x[i]-(1+rad))<1e-6 for i in range(n))
            checks+=n+2
print('VERIFY_OK', checks, 'checks')
