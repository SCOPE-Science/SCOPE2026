#!/usr/bin/env python3
"""Exact finite-state checks for triangular-book sandpile avalanche polynomial.

Uses independent burning recurrence tests and queue-based legal stabilization,
compares the full multivariate count rather than only avalanche size.
"""
from collections import Counter, deque
from itertools import product
from math import comb
from fractions import Fraction

def stabilize(h, leaf, n):
    x=[h]+list(leaf)
    q=deque(i for i in range(n+1) if x[i]>=(n+1 if i==0 else 2))
    fires=[0]*(n+1)
    while q:
        i=q.popleft(); d=n+1 if i==0 else 2
        if x[i]<d: continue
        x[i]-=d; fires[i]+=1
        js=range(1,n+1) if i==0 else (0,)
        for j in js:
            x[j]+=1
            if x[j]>=(n+1 if j==0 else 2): q.append(j)
        if x[i]>=d: q.append(i)
    return tuple(x),tuple(fires)

def recurrent_by_burning(h,leaf,n):
    stable,fire=stabilize(h+1,[a+1 for a in leaf],n)
    return stable==(h,)+leaf and all(k==1 for k in fire)

def predicted_monomials(n):
    counts=Counter()
    zero=(0,)*(n+1)
    counts[zero]+=n*2**(n-1)
    # source = common non-sink spine vertex
    for leaf in product((0,1),repeat=n):
        counts[(1,)+leaf]+=1
    # source at a page tip
    for j in range(n):
        x=[0]*(n+1);x[j+1]=1
        counts[zero]+=(n+1)*2**(n-2) if n>=2 else 1
        counts[tuple(x)]+=(n+1)*2**(n-2) if n>=2 else 1
        for leaf in product((0,1),repeat=n-1):
            y=[1]+[0]*n;y[j+1]=1
            for i,k in zip((i for i in range(n) if i!=j),leaf): y[i+1]=k
            counts[tuple(y)]+=1
    return counts

def main():
    checks=0
    for n in range(1,10):
        actual=Counter(); states=0
        for h in range(n+1):
            for leaf in product((0,1),repeat=n):
                pred_rec=(h >= sum(a==0 for a in leaf))
                from_burning=recurrent_by_burning(h,leaf,n)
                assert from_burning==pred_rec,(n,h,leaf)
                checks+=1
                if not from_burning: continue
                states+=1
                for source in range(n+1):
                    x=[h,*leaf];x[source]+=1
                    _,odometer=stabilize(x[0],x[1:],n)
                    actual[odometer]+=1
                    assert all(k<=1 for k in odometer)
                    checks+=1
        predicted=predicted_monomials(n)
        assert actual==predicted,(n,actual-predicted,predicted-actual)
        assert states==2**(n-1)*(n+2)
        assert sum(actual.values())==(n+1)*states
        # Source-conditioned means and variance:
        for source in range(n+1):
            mean=sum(sum(fire)*count for fire,count in actual.items() if False)
            # source-resolved distribution obtained independently below
            source_counter=Counter()
            for h in range(n+1):
                for leaf in product((0,1),repeat=n):
                    if h<sum(a==0 for a in leaf): continue
                    x=[h,*leaf];x[source]+=1
                    _,odometer=stabilize(x[0],x[1:],n)
                    source_counter[sum(odometer)]+=1
            assert sum(t*k for t,k in source_counter.items())==states
            if source==0:
                expected={0:n*2**(n-1)}
                for k in range(n+1):expected[k+1]=expected.get(k+1,0)+comb(n,k)
            else:
                c=(n+1)*2**(n-2) if n>=2 else 1
                expected={0:c,1:c}
                for k in range(n): expected[k+2]=expected.get(k+2,0)+comb(n-1,k)
            assert source_counter==expected
            checks+=2
        checks+=3
        print('n',n,'recurrent',states,'monomial_types',len(actual))
    print('PASS',checks,'exact checks')
if __name__=='__main__':main()
