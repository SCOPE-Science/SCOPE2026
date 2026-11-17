#!/usr/bin/env python3
"""Exact finite-profile verification for sequential (1,3) hysteresis on double stars.
The graph has two adjacent hubs (u,v), a leaves at u, b leaves at v.
One sweep updates u, v, then all leaves. This script checks representative
periodicity and closed census formulas for a,b up to 40; it is not the proof
for unbounded parameters (given separately in RESULT.md).
"""
from math import comb
from collections import Counter

def next_profile(s,a,b):
    h,j,k,l=s
    H=int(h+j+k >= (3 if h else 1))
    J=int(j+H+l >= (3 if j else 1))
    return (H,J,a-k if H else 0,b-l if J else 0)

def next_full(s,a,b):
    h,j,A,B=s
    H=int(h+j+A.bit_count()>=(3 if h else 1))
    J=int(j+H+B.bit_count()>=(3 if j else 1))
    return (H,J,((1<<a)-1)^A if H else 0, ((1<<b)-1)^B if J else 0)

def exact_counts(a,b):
    universe=[(h,j,k,l) for h in range(2) for j in range(2)
             for k in range(a+1) for l in range(b+1)]
    successor={s:next_profile(s,a,b) for s in universe}
    indegree={s:0 for s in universe}
    for t in successor.values(): indegree[t]+=1
    todo=[s for s in universe if indegree[s]==0]
    for s in todo:
        t=successor[s]
        indegree[t]-=1
        if indegree[t]==0: todo.append(t)
    recurrent={s for s in universe if indegree[s]>0}
    counts=Counter()
    for h,j,k,l in recurrent:
        s=(h,j,(1<<k)-1,(1<<l)-1)
        t=next_full(s,a,b);period=1
        while t!=s:
            period+=1
            if period>12: raise AssertionError((a,b,s,period))
            t=next_full(t,a,b)
        counts[period]+=comb(a,k)*comb(b,l)
    return counts

def predicted(a,b):
    t=lambda m:sum(comb(m,k) for k in range(2,m-1))
    return {1:1, 2:(2**a-2)*(2**b-2),
            3:3 if a>=2 and b>=2 else 0,
            6:3*(t(a)+t(b))}

def uniform_cycles(a,b):
    states=[(h,j,u,v) for h in range(2) for j in range(2)
           for u in range(2) for v in range(2)]
    def f(s):
        h,j,u,v=s
        H=int(h+j+a*u >=(3 if h else 1))
        J=int(j+H+b*v >=(3 if j else 1))
        return (H,J, 1-u if H else 0, 1-v if J else 0)
    successors={s:f(s) for s in states}
    seen=set();periodic=[]
    for s in states:
        if s in seen:continue
        seq=[];ix={};x=s
        while x not in ix and x not in seen:
            ix[x]=len(seq);seq.append(x);x=successors[x]
        if x in ix:periodic.append(seq[ix[x]:])
        seen.update(seq)
    return periodic

if __name__=='__main__':
    for a in (1,2):
        for b in (1,2):
            cs=uniform_cycles(a,b)
            expected=[1,3] if a==b==2 else [1]
            assert sorted(map(len,cs))==expected,(a,b,cs)
            print(f'uniform a={a} b={b}: periods '+str(sorted(map(len,cs))))
    checked=0
    for a in range(1,41):
        for b in range(1,41):
            result=exact_counts(a,b);expected=predicted(a,b)
            assert all(result.get(p,0)==expected.get(p,0) for p in result.keys()|expected.keys()),(a,b,result,expected)
            assert set(result)<= {1,2,3,6},(a,b,result)
            checked+=1
    print(f'PASS: {checked} pairs of sizes 1..40, exact period-state counts all agree.')
    for a,b in [(1,3),(1,4),(2,2),(2,5),(4,4),(5,7),(10,10),(40,40)]:
        print(f'D_({a},{b}) primitive periodic STATES: {dict(sorted(exact_counts(a,b).items()))}')
