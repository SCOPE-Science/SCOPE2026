#!/usr/bin/env python3
"""Exact Mobius inversion and orbit-population integrity over F_2 and F_4."""
from math import gcd


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    if n == 1:
        return 1
    count = 0
    p = 2
    while p*p <= n:
        if n%p == 0:
            n//=p
            if n%p == 0:
                return 0
            count += 1
        while n%p == 0:
            n//=p
        p += 1
    if n>1:
        count+=1
    return -1 if count%2 else 1


def fixed(n, t, q):
    return q ** (2*gcd(n,t) - (n%2==1 and t%2==1))


def primitive(n, d, q):
    return sum(mobius(d//e)*fixed(n,e,q) for e in divisors(d))


def run():
    checks=0
    for q in (2,4):
        for n in range(3,61):
            order = n if n%2==0 else 2*n
            p = {d:primitive(n,d,q) for d in divisors(order)}
            assert all(v>=0 and v%d==0 for d,v in p.items())
            assert sum(p.values())==q**(2*n)
            assert p[order]>0
            for t in divisors(order):
                assert sum(v for d,v in p.items() if t%d==0)==fixed(n,t,q)
                checks+=1
    print('divisor and primitive-orbit census comparisons:', checks)
    print('n range: 3..60; q in {2,4}')
    print('all nonnegative integral orbits, full population, sharp order: PASS')


if __name__=='__main__':
    run()
