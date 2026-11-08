#!/usr/bin/env python3
"""Exact finite checks for the split-polynomial coprimality theorem.

This is not a proof of the infinite density or published large-prime theorem.
"""
from math import gcd, isqrt, prod
from fractions import Fraction


def primes_to(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * ((n-p*p)//p+1)
    return [p for p in range(2,n+1) if sieve[p]]


def rho(shifts,p):
    return len({-h % p for h in shifts})


def local_crt(shifts,s,prime_set):
    D=prod(prime_set)
    rcount=0
    for u in range(D):
        def count_coords(coords):
            if len(coords)==s-1:
                return int(all(not (prod(u+h for h in shifts) % p==0 and all(v%p==0 for v in coords)) for p in prime_set))
            return sum(count_coords(coords+[a]) for a in range(D))
        rcount+=count_coords([])
    theory=Fraction(1)
    for p in prime_set:
        theory *= 1-Fraction(rho(shifts,p),p**s)
    assert Fraction(rcount,D**s)==theory,(shifts,s,prime_set)
    return theory


def test():
    for shifts in [(0,), (0,1), (0,1,2), (0,2,4), (-3,0,6)]:
        for s in [2,3]:
            for prime_set in [(2,3),(2,5)]:
                local_crt(shifts,s,prime_set)
    E=1.
    for p in primes_to(100000):
        E *= 1.-2./(p*p)
    assert 0.322 < E < 0.324
    ratios=[]
    count=0
    for n in range(1,300001):
        # isqrt(2*n*n) = floor(sqrt(2)*n) exactly.
        count += (gcd(n*(n+1),isqrt(2*n*n)) == 1)
        if n in (20000,100000,300000):
            ratios.append((n,count,round(count/n,8)))
    assert ratios[0][1]==6437 and ratios[1][1]==32254 and ratios[2][1]==96753
    print('VERIFY_OK exact_CRT_cases=20 Euler_truncation_100000=%.10f samples=%s' % (E,ratios))
    print('PROOF_STATUS finite_checks_only; infinite_theorem_uses_published_large_prime_bound')

if __name__=='__main__':
    test()
