#!/usr/bin/env python3
"""Exact finite enumeration for a paired cubic irreducibility theorem.

Uses only Python's standard library; every prime up to 850 is checked by a
sieve and exact arithmetic. No probabilistic prime tests or numerical
approximation certify the finite exception list.
"""
from math import isqrt

def primes_through(n):
    sieve = bytearray(b'\x01') * (n+1)
    sieve[0:2] = b'\x00\x00'
    for k in range(2, isqrt(n)+1):
        if sieve[k]:
            sieve[k*k:n+1:k] = b'\x00'*(((n-k*k)//k)+1)
    return [k for k in range(2,n+1) if sieve[k]]

def count_pair(p):
    # f_c(X)=X^3+c(X^2+X+1) is reducible iff c=-x^3/(x^2+x+1)
    reducible = set()
    for x in range(p):
        d=(x*x+x+1)%p
        if d:
            c=(-pow(x,3,p)*pow(d,-1,p))%p
            reducible.add(c)
    return p-len(reducible.union({(-t)%p for t in reducible}))

def cubic_has_root(c,sign,p):
    # sign=1: f_{+,c}; sign=-1: f_{-,c}
    return any((x*x*x+c*(x*x+sign*x+1))%p == 0 for x in range(p))

def main():
    primes=primes_through(850)
    exception=[]
    for p in primes:
        n=count_pair(p)
        if n==0:
            exception.append(p)
        if p<=101:
            direct=sum((not cubic_has_root(c,1,p)) and (not cubic_has_root(c,-1,p)) for c in range(p))
            assert n==direct, (p,n,direct)
        if p>=11 and p!=7:
            # integer-only check of derived Weil bound
            assert (abs(9*n-(p+1))-93)**2 <= 26**2*p if abs(9*n-(p+1))>93 else True
    assert exception==[2,3,5,13], exception
    assert count_pair(7)==2 and count_pair(11)==2 and count_pair(13)==0
    print('FINITE_CERTIFICATE_OK', 'primes_checked=',len(primes), 'exceptions=',exception)
    print('sample_counts=',{p:count_pair(p) for p in (2,3,5,7,11,13,17,19,23,29,31,37,41)})
if __name__=='__main__':
    main()
