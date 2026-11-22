"""Exact-rational checks for erasure-robust integrated-process sampling.

Only Python standard-library fractions/combinatorics are needed. These checks
supplement, rather than replace, the analytic all-n proof in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def condrisk(ts):
    times = [Q(0), *ts]
    return sum((b-a)**3/Q(12) for a,b in zip(times,times[1:]))+(Q(1)-times[-1])**3/Q(3)


def risk(x,p):
    n=len(x)
    return sum((p**len(I)*(1-p)**(n-len(I)))*condrisk([x[i] for i in I])
               for k in range(n+1) for I in combinations(range(n),k))


def add(a,b):
    out=[Q(0)]*max(len(a),len(b))
    for i,v in enumerate(a): out[i]+=v
    for i,v in enumerate(b): out[i]+=v
    return out


def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): out[i+j]+=u*v
    return out


def power(a,k):
    out=[Q(1)]
    for _ in range(k): out=mul(out,a)
    return out


def sub(a,b):
    return add(a,[-v for v in b])


def crisk_poly(nodes):
    ts=[[Q(0)],*nodes]
    out=[Q(0)]
    for a,b in zip(ts,ts[1:]):
        out=add(out,[c/Q(12) for c in power(sub(b,a),3)])
    out=add(out,[c/Q(3) for c in power(sub([Q(1)],ts[-1]),3)])
    return out


def risk_poly(nodes):
    n=len(nodes)
    out=[Q(0)]
    for k in range(n+1):
        for I in combinations(range(n),k):
            weight=mul(power([Q(0),Q(1)],k),power([Q(1),Q(-1)],n-k))
            out=add(out,mul(weight,crisk_poly([nodes[i] for i in I])))
    return out


def coeff(a,k): return a[k] if k<len(a) else Q(0)


tests=0
for n in range(1,7):
    t=[Q(2*i,2*n+1) for i in range(1,n+1)]
    assert risk(t,Q(1))==Q(1,3*(2*n+1)**2)
    tests+=1
    for i in range(n):
        # Moving a point to a neighbouring (interior) rational value cannot
        # improve the exactly optimized all-delivered design.
        for q in [Q(-1,1000),Q(1,1000)]:
            z=t.copy();z[i]+=q
            assert 0<=z[0] and z[-1]<=1 and all(z[k]<=z[k+1] for k in range(n-1))
            assert risk(z,Q(1))>risk(t,Q(1))
            tests+=1
for n in range(1,7):
    ys=[Q(2*i-n-1,9) for i in range(1,n+1)]
    nodes=[[Q(2,3),y] for y in ys]
    flat=[[Q(2,3)] for _ in range(n)]
    deficit=sub(risk_poly(flat),risk_poly(nodes))
    assert all(coeff(deficit,j)==0 for j in range(3))
    assert coeff(deficit,3)==Q(n*(n*n-1),486)
    tests+=4
    # Polynomial coefficient for a second ordered perturbation, including a
    # nonoptimal asymmetric configuration, equals the exact limit energy.
    z=[Q(2*i-n-1,7)+Q(1,13) for i in range(1,n+1)]
    nodes2=[[Q(2,3),y] for y in z]
    predicted =sum(y*y/Q(2) for y in z)-sum((z[j]-z[i])/Q(9)
                                                   for i in range(n) for j in range(i+1,n))
    observed=coeff(sub(risk_poly(nodes2),risk_poly(flat)),3)
    assert observed==predicted
    tests+=1
    for p in [Q(1,100),Q(1,200)]:
        x=[Q(2,3)+p*y for y in ys]
        base=[Q(2,3)]*n
        assert all(x[i]<x[i+1] for i in range(n-1))
        if n>1: assert risk(x,p)<risk(base,p)
        else: assert risk(x,p)==risk(base,p)
        tests+=2
print(f'PASS: {tests} exact-rational assertions; polynomial order-3 identities for n=1..6;')
print('      exact p=1 optima and perturbations; exact small-p improvement checks.')
