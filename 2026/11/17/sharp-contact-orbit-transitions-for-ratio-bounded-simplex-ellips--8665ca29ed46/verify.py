"""Numerical and exact-rational checks for the ratio-bounded simplex central polytope.

Run: python3 verify.py
The full-dimensional theorem follows from the analytical proof, not these tests.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, sqrt, isclose
import random

COUNT = 0

def ok(cond, message):
    global COUNT
    assert cond, message
    COUNT += 1


def vertices(m,c):
    for k in range(1,m):
        den=m+k*(c-1)
        for inds in combinations(range(m),k):
            S=set(inds)
            yield k,tuple((c if i in S else 1)/den for i in range(m))


def rin(m,c):
    return (c-1)/(m*sqrt(1+c*c-(c-1)**2/m))


def r_squared(k,m,c):
    return (c-1)**2*k*(m-k)/(m*(m+k*(c-1))**2)


def winning_ks(m,c):
    a=[r_squared(k,m,c) for k in range(1,m)]
    top=max(a)
    return [k for k,v in enumerate(a,1) if isclose(v,top,rel_tol=1e-10,abs_tol=1e-13)]

# Exact barycentric vertices and active inequalities, independent rational arithmetic.
for m in range(4,11):
    for c in [Fraction(7,6),Fraction(3,2),Fraction(2),Fraction(7,3),Fraction(5)]:
        v=list(vertices(m,c))
        ok(len(v)==2**m-2,(m,c,'vertex count'))
        for k,x in v:
            ok(sum(x)==1,(m,c,'normalization'))
            ok(all(x[i]<=c*x[j] for i in range(m) for j in range(m)),(m,c,'facets'))
            sq=sum((xi-Fraction(1,m))**2 for xi in x)
            ok(sq==Fraction((c-1)**2*k*(m-k),m*(m+k*(c-1))**2),(m,c,'radius'))

# Strictly ordered crossing thresholds, correct contact orbits between transitions.
for m in range(4,31):
    h=m//2
    cs=[sqrt((m-k)*(m-k-1)/(k*(k+1))) for k in range(1,h)]
    ok(all(cs[i]>cs[i+1]>1 for i in range(len(cs)-1)) or len(cs)<2,(m,'threshold order'))
    for k,ck in enumerate(cs,1):
        ok(isclose(r_squared(k,m,ck),r_squared(k+1,m,ck),rel_tol=1e-12),(m,k,'critical equality'))
        for j in range(1,m):
            ok(r_squared(j,m,ck) <= r_squared(k,m,ck)*(1+1e-10),(m,k,j,'contact dominance'))
    bounds=[1.0]+list(reversed(cs))+[max(2.0,cs[0]*2.0)]
    for i in range(len(bounds)-1):
        c=(bounds[i]+bounds[i+1])/2
        expect=h-i
        ok(winning_ks(m,c)==[expect],(m,c,expect,winning_ks(m,c)))

# Strict monotonicity of outer/inner radius and limiting values.
for m in range(4,31):
    cs=[1.00001,1.01,1.1,1.2,1.5,2.,3.,5.,10.,100.]
    v=[sqrt(max(r_squared(k,m,c) for k in range(1,m)))/rin(m,c) for c in cs]
    ok(all(a<b for a,b in zip(v,v[1:])),(m,'ratio monotonic'))
    low=sqrt(2*(m//2)*(m-m//2)/m)
    high=m-1
    ok(abs(v[0]-low)<1e-4,(m,'low limit'))
    ok(v[-1]<high,(m,'high bound'))

# Independent H-polytope vertex extraction, no pre-enumerated vertices supplied.
try:
    import numpy as np
    from scipy.spatial import HalfspaceIntersection
    for m in range(4,8):
        for c in (1.42,2.23,4.15):
            # Coordinates x_0,...,x_{m-2}; x_{m-1}=1-sum.
            half=[]
            for i in range(m):
                for j in range(m):
                    if i==j: continue
                    ci=np.zeros(m-1); cj=np.zeros(m-1)
                    vi=0.0; vj=0.0
                    if i==m-1: ci[:]=-1;vi=1
                    else: ci[i]=1
                    if j==m-1: cj[:]=-1;vj=1
                    else: cj[j]=1
                    half.append(list(ci-c*cj)+[vi-c*vj])
            hs=HalfspaceIntersection(np.array(half),np.full(m-1,1/m))
            ex=[]
            for x in hs.intersections:
                xx=np.append(x,1-np.sum(x))
                if not any(np.linalg.norm(xx-y)<1e-7 for y in ex): ex.append(xx)
            expected=[np.array(v) for _,v in vertices(m,c)]
            ok(len(ex)==len(expected),(m,c,'H polytope vertex count',len(ex)))
            for x in ex:
                ok(min(np.linalg.norm(x-y) for y in expected)<1e-7,(m,c,'H vertex equality'))
except ImportError:
    print('SciPy not installed: independent halfspace vertex extraction skipped')

print('PASS:',COUNT,'finite exact, scalar and halfspace checks')
