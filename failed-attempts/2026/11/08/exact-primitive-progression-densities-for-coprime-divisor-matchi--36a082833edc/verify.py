#!/usr/bin/env python3
"""Exact finite checks for densities of primitive coprime-matching progressions."""
from fractions import Fraction
from math import gcd, prod
from itertools import product

def factor(n):
    a = {}
    d = 2
    while d*d <= n:
        while n%d == 0:
            a[d] = a.get(d,0)+1
            n //= d
        d += 1
    if n > 1:
        a[n] = 1
    return a

def density(n):
    exps = factor(n)
    result = Fraction(1)
    N = prod(e+1 for e in exps.values())
    for p,e in exps.items():
        if e >= p:
            t = N//(e+1)
            result *= Fraction(p+1-min(p,(e+1-p)*t),p+1)
    return result

def matches_source(n,a,b):
    N = prod(e+1 for e in factor(n).values())
    return all(sum((a+b*j)%p==0 for j in range(N)) <= N//(e+1)
               for p,e in factor(n).items())

def brute_matching(n,a,b):
    D = [d for d in range(1,n+1) if n%d == 0]
    N = len(D)
    reachable = {0}
    for j in range(N):
        new = set()
        for mask in reachable:
            for i,d in enumerate(D):
                if not mask & (1<<i) and gcd(d,a+b*j)==1:
                    new.add(mask | 1<<i)
        reachable = new
        if not reachable: return False
    return (1<<N)-1 in reachable

def matches_bad_prime_criterion(n,a,b):
    E = factor(n)
    N=prod(e+1 for e in E.values())
    return all(sum((a+b*j)%p==0 for j in range(N)) <= N//(e+1)
               for p,e in E.items() if e >= p)

def residue_density(n):
    E = factor(n)
    primes = [p for p,e in E.items() if e >= p]
    M = prod(primes)
    if M == 1: return Fraction(1),1
    good,primitive=0,0
    for a in range(M):
        for b in range(M):
            if gcd(gcd(a,b),M) != 1:
                continue
            primitive+=1
            if matches_bad_prime_criterion(n,a,b):
                good+=1
    return Fraction(good,primitive), primitive

def main():
    cases = [1,2,3,4,6,8,9,12,16,18,20,27,36,48,54,64,81,108,125,162,225,243,250,256,270,500,729,875,1600]
    residue = 0
    for n in cases:
        got,m = residue_density(n)
        assert got == density(n), (n,got,density(n))
        residue += m
    comparisons = 0
    for n in [1,2,3,4,6,8,9,12,16,18,27,36,48,81,108,125,225]:
        N=prod(e+1 for e in factor(n).values())
        if N>12: continue
        for a,b in product(range(1,17),repeat=2):
            if gcd(a,b) != 1: continue
            assert brute_matching(n,a,b)==matches_source(n,a,b),(n,a,b)
            comparisons+=1
    for p in [2,3,5,7,11]:
        for e in range(1,4*p+1):
            x=p**e
            if e < p:
                expected=Fraction(1)
            elif e<=2*p-2:
                expected=Fraction(2*p-e,p+1)
            else:
                expected=Fraction(1,p+1)
            assert density(x)==expected,(p,e)
    for n in range(1,181):
        for k in range(1,6):
            assert density(n*k)<=density(n),(n,k)
    print('VERIFY_OK residue_cases=%d primitive_residue_pairs=%d perfect_matching_comparisons=%d prime_power_cases=%d divisibility_checks=%d exact_rational=yes' %
          (len(cases),residue,comparisons,sum(4*p for p in [2,3,5,7,11]),180*5))
    for n in [4,8,27,81,108,243]:
        print('DENSITY n=%d value=%s'%(n,density(n)))

if __name__ == '__main__': main()
