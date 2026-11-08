#!/usr/bin/env python3
"""Exact finite checks for the paired uniform-attachment leaf law.
Run: python3 verify.py.  Uses only Python's standard library.
"""
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict

checks=0

def eq(x,y,description):
    global checks
    assert x==y,(description,x,y)
    checks+=1

def step(d,m):
    ans=defaultdict(Q)
    for k,a in d.items():
        ans[k]+=a*Q(k,m)
        ans[k+1]+=a*Q(m-k,m)
    return dict(ans)

def marginal(n):
    d={1:Q(1)}
    for m in range(2,n): d=step(d,m)
    return d

def conditional(start,end,k):
    d={k:Q(1)}
    for m in range(start,end): d=step(d,m)
    return d

def pair_dynamic(n,t):
    d=defaultdict(Q)
    for k,q in marginal(t).items():
        c=conditional(t,n,k)
        for a,qa in c.items():
            for b,qb in c.items(): d[a,b]+=q*qa*qb
    return dict(d)

def histories(start,end):
    return product(*(range(1,j) for j in range(start,end+1)))

def leaf_count(n,parents):
    child=[0]*(n+1)
    for parent in parents: child[parent]+=1
    return sum(x==0 for x in child[1:])

def pair_exhaustive(n,t):
    counts=defaultdict(int)
    total=0
    tails=list(histories(t+1,n))
    for early in histories(2,t):
        for a in tails:
            v=leaf_count(n,early+a)
            for b in tails:
                w=leaf_count(n,early+b)
                counts[v,w]+=1
                total+=1
    return {k:Q(v,total) for k,v in counts.items()}

for n in range(2,11):
    d=marginal(n)
    eq(sum(d.values()),Q(1),('sum',n))
    eq(sum(k*q for k,q in d.items()),Q(n,2),('mean',n))
    v=sum((Q(k)-Q(n,2))**2*q for k,q in d.items())
    eq(v,Q(n,12) if n>=3 else Q(0),('variance',n))

for n in range(3,11):
    for t in range(2,n+1):
        d=pair_dynamic(n,t)
        eq(sum(d.values()),Q(1),('pair sum',n,t))
        eq(sum(a*q for (a,b),q in d.items()),Q(n,2),('first mean',n,t))
        eq(sum(b*q for (a,b),q in d.items()),Q(n,2),('second mean',n,t))
        cov=sum((Q(a)-Q(n,2))*(Q(b)-Q(n,2))*q for (a,b),q in d.items())
        exact=Q(0) if t==2 else Q(t,12)*Q((t-1)**2,(n-1)**2)
        eq(cov,exact,('pair cov',n,t))
        eq(sum(abs(d.get((a,b),Q(0))-d.get((b,a),Q(0))) for a,b in d),Q(0),('symmetry',n,t))
        if t>=3:
            eq(cov / Q(n,12),Q(t*(t-1)**2,n*(n-1)**2),('correlation',n,t))

for n in range(2,7):
    for t in range(2,n+1):
        direct=pair_exhaustive(n,t)
        via_dp=pair_dynamic(n,t)
        for a in range(1,n+1):
            for b in range(1,n+1):
                eq(direct.get((a,b),Q(0)),via_dp.get((a,b),Q(0)),('direct paired enumeration',n,t,a,b))

for t in range(2,10):
    for n in range(t,13):
        for k in marginal(t):
            cd=conditional(t,n,k)
            m=sum(a*q for a,q in cd.items())
            eq(m,Q(n,2)+Q(t-1,n-1)*(Q(k)-Q(t,2)),('conditional regression',t,n,k))

print(f'VERIFY_OK {checks} exact assertions')

# Cross-time rank-one kernel, and increasing upper-tail event association.
for t in range(2,9):
    for s in range(t,11):
        for u in range(t,11):
            mixture=defaultdict(Q)
            for k,pk in marginal(t).items():
                ps=conditional(t,s,k)
                pu=conditional(t,u,k)
                for a,pa in ps.items():
                    for b,pb in pu.items():
                        mixture[a,b]+=pk*pa*pb
            cross=sum((Q(a)-Q(s,2))*(Q(b)-Q(u,2))*v for (a,b),v in mixture.items())
            expected=Q(0) if t==2 else Q(t*(t-1)**2,12*(s-1)*(u-1))
            eq(cross,expected,('rank-one cross-time',t,s,u))
            if s<=8 and u<=8:
                for a0 in range(1,s+1):
                    for b0 in range(1,u+1):
                        pab=sum(p for (a,b),p in mixture.items() if a>=a0 and b>=b0)
                        pa=sum(p for (a,b),p in mixture.items() if a>=a0)
                        pb=sum(p for (a,b),p in mixture.items() if b>=b0)
                        assert pab>=pa*pb,('nonnegative tail association',t,s,u,a0,b0)
                        checks+=1
print(f'VERIFY_OK_EXTENDED {checks} exact assertions')
