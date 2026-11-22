#!/usr/bin/env python3
"""Exact finite corroboration for a quadratic binomial map; not an infinite proof."""
from collections import Counter
from math import comb

def F(x): return (x + 2) * (2*x + 3)
def valuation(n):
    assert n != 0
    return (abs(n)&-abs(n)).bit_length()-1

def periods(k):
    q=1<<k; seen=set(); cycles=[]
    for a in range(q):
        if a in seen: continue
        curr=a; visit=[]
        while curr not in seen:
            seen.add(curr);visit.append(curr)
            curr=F(curr)%q
        assert curr==a, (k,a,curr)
        cycles.append((a%2,len(visit)))
    assert len(seen)==q
    return Counter(cycles)

checks=0
for x in range(-100,101):
    assert F(x)==(2*x+4)*(2*x+3)//2
    fx=F(x)
    assert F(fx)-x == 8*(x*x+3*x+3)*(x*x+4*x+5)
    assert valuation(F(x)-x)==1
    assert valuation(F(fx)-x)==(3 if x%2==0 else 4)
    checks+=4
for k in range(1,13):
    q=1<<k
    for x in range(q):
        a=x; t=0; expected=(1 if k==1 else (1<< (1+max(k-(3 if x%2==0 else 4),0))))
        while True:
            a=F(a)%q;t+=1
            if a==x: break
            assert t<=expected
        assert t==expected,(k,x,t,expected)
        checks+=1
    c=periods(k)
    expected=Counter()
    for par in (0,1):
        L=1 if k==1 else 1<<(1+max(k-(3 if par==0 else 4),0))
        expected[(par,L)]=(q//2)//L
    assert c==expected,(k,c,expected)
    checks+=1
print('VERIFY_OK', checks)
