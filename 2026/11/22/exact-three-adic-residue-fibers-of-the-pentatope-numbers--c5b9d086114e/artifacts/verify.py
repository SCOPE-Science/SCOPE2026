#!/usr/bin/env python3
"""Exact finite checks for the 3-adic residue fibers of pentatope numbers.

No external dependencies. Run with python3 check.py.
These checks corroborate, but do not replace, the proof in RESULT.md.
"""
from math import comb
from collections import Counter

def poly(x):
    return x*(x-1)*(x-2)*(x-3)//24

def invmod8(k):
    return pow(8,-1,3**k)

def H(u,m):
    return (u*(9*u+2)*pow(8,-1,m))%m

def predicted_counts(k):
    """Full residue fibers from two isometric branches plus square roots."""
    q=3**k
    out={r:2 for r in range(q)}
    if k==1:
        out[0]+=3
        return out
    e=k-1
    m=3**e
    inv128=pow(128,-1,m)
    squares=Counter((w*w)%m for w in range(m))
    for a in range(m):
        v=(a-inv128)%m
        out[3*a]+=3*squares[v]
    return out

def predicted_histogram(k):
    e=k-1
    out=Counter()
    out[2]=3**k-1-sum(3**(e-2*j-1) for j in range((e+1)//2))
    for j in range((e+1)//2):
        out[2+6*3**j]+=3**(e-2*j-1)
    out[2+3**(1+e//2)]+=1
    return +out

def check():
    total=0
    for k in range(1,8):
        q=3**k
        P=3*q
        actual=Counter(comb(n,4)%q if n>=4 else 0 for n in range(P))
        predicted=predicted_counts(k)
        assert actual==predicted, (k,actual,predicted)
        assert Counter(actual.values())==predicted_histogram(k),k
        assert sum(actual.values())==P
        # A lower candidate power 3^k fails on the 1(mod 3) branch.
        assert (poly(3*q//3+1)-poly(1))%q !=0 if k>=2 else (poly(4)-poly(1))%3!=0
        # The least-period assertion itself follows from the isometry proof;
        # finite sampling checks the claimed period over several blocks.
        for n in range(0,min(P,1000)):
            assert (poly(n+P)-poly(n))%q==0
        total+=P+min(P,1000)
        print('k=',k,'modulus=',q,'period=',P,'fiber_histogram=',sorted(predicted_histogram(k).items()))
    print('PASS:',total,'exact finite index/period checks, all target fiber spectra reproduced')

if __name__=='__main__':
    check()
