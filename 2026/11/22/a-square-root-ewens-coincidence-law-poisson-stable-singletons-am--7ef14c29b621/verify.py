#!/usr/bin/env python3
"""Exact arithmetic checks for independent Ewens block coincidences.
Only small finite instances are checked; the asymptotic argument is analytic.
"""
from fractions import Fraction
from math import factorial, comb

def partitions(n):
    blocks = []
    def rec(i):
        if i == n:
            yield tuple(tuple(x) for x in blocks)
            return
        for j in range(len(blocks)):
            blocks[j].append(i)
            yield from rec(i+1)
            blocks[j].pop()
        blocks.append([i])
        yield from rec(i+1)
        blocks.pop()
    yield from rec(0)

def rising(x, m):
    p=Fraction(1)
    for j in range(m): p*=x+j
    return p

def falling(n,k):
    p=1
    for j in range(k): p*=n-j
    return p

def weight(part, n, theta):
    w=theta**len(part)
    for b in part: w*=factorial(len(b)-1)
    return w/rising(theta,n)

def exact(n, theta):
    ps=list(partitions(n))
    ws=[weight(p,n,theta) for p in ps]
    assert sum(ws)==1
    s=[frozenset(b[0] for b in p if len(b)==1) for p in ps]
    bf=[frozenset(frozenset(b) for b in p) for p in ps]
    f1=Fraction(0); f2=Fraction(0); pairs=Fraction(0); large=Fraction(0)
    for i,p in enumerate(ps):
        for j,q in enumerate(ps):
            w=ws[i]*ws[j]
            k=len(s[i]&s[j]); f1+=w*k; f2+=w*k*(k-1)
            large+=w*int(any(len(b)>1 for b in (bf[i]&bf[j])))
            pairs+=w*sum(int(any(u in b and v in b for b in p) and any(u in b and v in b for b in q)) for u in range(n) for v in range(u+1,n))
    p1=theta/(theta+n-1)
    p2=theta**2/((theta+n-2)*(theta+n-1)) if n>=2 else Fraction(0)
    assert f1==n*p1**2,(n,theta,'mean')
    assert f2==n*(n-1)*p2**2,(n,theta,'factorial')
    assert pairs==Fraction(comb(n,2),1)/(theta+1)**2,(n,theta,'pairs')
    assert large>=0
    print('OK',n,theta,'common_singletons_mean=',f1,'meet_pairs_mean=',pairs,'full_nontrivial_probability=',large)

if __name__=='__main__':
    checks=0
    for n in range(2,7):
        for theta in (Fraction(1,2),Fraction(1),Fraction(3)):
            exact(n,theta);checks+=3
    print('PASS:',checks,'independent exact identities across 15 complete paired-partition enumerations.')
