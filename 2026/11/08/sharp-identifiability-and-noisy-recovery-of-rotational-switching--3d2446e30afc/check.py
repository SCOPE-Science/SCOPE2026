#!/usr/bin/env python3
"""Standalone exact checker for cyclic rotational-word identities.

Execute with Python 3.10+: python check.py
All main results are proven analytically in RESULT.md; finite checks are corroboration.
"""
from math import gcd, floor
from fractions import Fraction


def word(p, ell, m):
    return tuple(int((i*m) % p < ell) for i in range(p))


def corr(w, t):
    p = len(w)
    return sum(w[i]*w[(i+t) % p] for i in range(p))


def canonical(w):
    p = len(w)
    return min(w[t:]+w[:t] for t in range(p))


def switch_count(w):
    p = len(w)
    return sum(w[i] != w[(i+1) % p] for i in range(p))


def g(p, ell, r):
    r %= p
    return max(ell-r, 0)+max(ell-(p-r), 0)


def tests():
    a = b = c = 0
    for p in range(5, 90):
        units = [m for m in range(1,p) if gcd(m,p)==1]
        for ell in range(2,p-1):
            L = min(ell,p-ell)
            for m in units:
                w = word(p,ell,m)
                assert sum(w)==ell
                assert switch_count(w)==2*min(L,m,p-m)
                assert canonical(w)==canonical(word(p,ell,p-m))
                assert corr(w,0)==ell
                assert corr(w,pow(m,-1,p))==ell-1
                for t in (1,2,3,p//2,p-1):
                    assert corr(w,t)==g(p,ell,(t*m)%p)
                a+=1
    for p in range(5,34):
        units = [m for m in range(1,p) if gcd(m,p)==1]
        for ell in range(2,p-1):
            classes = {}
            for m in units:
                w=word(p,ell,m)
                key=canonical(w)
                classes.setdefault(key,[]).append(m)
                peaks={t for t in range(1,p) if corr(w,t)==ell-1}
                assert peaks=={pow(m,-1,p),(-pow(m,-1,p))%p}
            assert len(classes)*2 == len(units)
            assert all(set(v)=={m,p-m} for v in classes.values() for m in v)
            b+=1
    for p in (7,11,13,17,19,23,29,31,37,41,43):
        for ell in ((p-1)//2,(p+1)//2):
            for e in (Fraction(0),Fraction(1,10),Fraction(1,3),Fraction(2,5),Fraction(1,2)):
                k=(1-2*e)**2
                eta=2*e*(1-e)
                for r in range(1,(p-1)//2+1):
                    q=Fraction(2*r,p)
                    Q=eta+k*q
                    assert Q==q*((1-e)**2+e**2)+(1-q)*2*e*(1-e)
                    if e==Fraction(1,2):assert Q==Fraction(1,2)
                    else:assert eta+k*Fraction(2*(r+1),p)-Q == k*Fraction(2,p)
                    c+=1
    print('PASS: exact word/switch identities:',a)
    print('PASS: cyclic uniqueness/autocorrelation cases:',b)
    print('PASS: rational observation-channel identities:',c)

if __name__=='__main__':
    tests()
