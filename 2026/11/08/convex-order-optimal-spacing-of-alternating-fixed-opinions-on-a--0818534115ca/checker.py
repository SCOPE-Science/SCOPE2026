#!/usr/bin/env python3
"""Exact finite checks for cyclic voter systems with alternating frozen opinions."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import prod

checks = 0

def assert_eq(left, right):
    global checks
    checks += 1
    assert left == right, (left, right)

def law(gaps):
    """Exact stationary opinion-count distribution from independent uniform walls."""
    masses = {len(gaps)//2: F(1)}
    for length in gaps:
        nxt = {}
        for x, px in masses.items():
            for j in range(length):
                nxt[x+j] = nxt.get(x+j, F(0)) + px / length
        masses = nxt
    return masses

def call(dist, t):
    return sum((x-t)*p for x,p in dist.items() if x > t)

def moments(dist):
    ex = sum(x*p for x,p in dist.items())
    var = sum((x-ex)**2*p for x,p in dist.items())
    return ex,var

def comps(n,m):
    for cuts in combinations(range(1,n),m-1):
        points=(0,)+cuts+(n,)
        yield tuple(points[i+1]-points[i] for i in range(m))

def is_majorizing(a,b):
    a=sorted(a,reverse=True)
    b=sorted(b,reverse=True)
    return sum(a)==sum(b) and all(sum(a[:k])>=sum(b[:k]) for k in range(1,len(a)))

def generator_law(n, pins):
    """Stationary law obtained independently from the full exact configuration generator."""
    import sympy as sp
    flexible = [v for v in range(n) if v not in pins]
    N=1<<len(flexible)
    Q=sp.zeros(N,N)
    states=[]
    for b in range(N):
        state=dict(pins)
        for j,v in enumerate(flexible):
            state[v]=(b>>j)&1
        states.append(state)
        for j,v in enumerate(flexible):
            rate=sp.Rational(sum(state[w]!=state[v] for w in ((v-1)%n,(v+1)%n)),2)
            if rate:
                Q[b,b]-=rate
                Q[b,b^(1<<j)]+=rate
    A=Q.T
    A[N-1,:]=sp.ones(1,N)
    v=sp.zeros(N,1)
    v[N-1]=1
    pi=A.inv()*v
    assert all(x>=0 for x in pi)
    out={}
    for k,p in enumerate(pi):
        x=sum(states[k].values())
        out[x]=out.get(x,F(0))+F(int(p.p),int(p.q))
    return out

# All elementary balancing moves, including the convex-call inequality at every strike.
for total in range(4,28):
    for a in range(1,total//2):
        b=total-a
        if b<a+2:
            continue
        old=law((a,b)); new=law((a+1,b-1))
        assert_eq(moments(old)[0],moments(new)[0])
        for strike in range(-1,total+1):
            assert_eq(call(new,strike)<=call(old,strike), True)
        assert_eq(moments(new)[1]<moments(old)[1],True)

# For every positive-gap composition in the stated small finite range,
# balanced spacing is convex-order minimal and maximal concentration is maximal.
for m in (2,4,6):
    for n in range(max(4,m),min(m+8,15)):
        q,r=divmod(n,m)
        low=(q,)*(m-r)+(q+1,)*r
        high=(n-m+1,)+(1,)*(m-1)
        lo,hi=law(low),law(high)
        for g in comps(n,m):
            dist=law(g)
            assert_eq(moments(dist)[0],F(n,2))
            assert_eq(moments(dist)[1],F(sum(k*k-1 for k in g),12))
            for strike in range(-1,n+1):
                assert_eq(call(lo,strike)<=call(dist,strike)<=call(hi,strike),True)
            if sorted(g)!=sorted(low):
                assert_eq(moments(lo)[1]<moments(dist)[1],True)
            if sorted(g)!=sorted(high):
                assert_eq(moments(dist)[1]<moments(hi)[1],True)

# Independently solve state generators on small rings, not relying on the wall formula.
for n in range(4,8):
    for sep in range(1,n):
        pins={0:1,sep:0}
        g=(sep,n-sep)
        assert_eq(generator_law(n,pins),law(g))
for n in range(4,8):
    for pins_vertices in combinations(range(1,n),3):
        vertices=(0,)+pins_vertices
        g=tuple((vertices[(i+1)%4]-vertices[i])%n for i in range(4))
        pins={v:(1 if i%2==0 else 0) for i,v in enumerate(vertices)}
        assert_eq(generator_law(n,pins),law(g))

assert_eq(moments(law((3,3,3,3))),(F(6),F(8,3)))
assert_eq(moments(law((9,1,1,1))),(F(6),F(20,3)))
print(f'PASS {checks} exact assertions')
