#!/usr/bin/env python3
"""Exact finite diagnostics for rational quadratic-floor coprimality."""
from fractions import Fraction
from math import gcd, isqrt, lcm


def distinct_primes(n):
    out = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out.append(n)
    return out


def data(a,b):
    assert b >= 1 and gcd(a,b) == 1 and a >= 1
    weights = []
    modulus = 1
    for r in range(1,b):
        c,t = divmod(a*r*r,b)
        if not t or gcd(b,gcd(r,c)) != 1:
            weights.append((r,c,t,0,1))
            continue
        pset = [p for p in distinct_primes(t) if b % p]
        q = 1
        w = Fraction(1)
        for p in pset:
            q *= p
            w *= Fraction(p-1,p)
        weights.append((r,c,t,w,q))
        modulus = lcm(modulus,q)
    return sum((x[3] for x in weights),Fraction(0))/b, b*modulus, weights


def raw(a,b,n):
    return int(gcd(n,(a*n*n)//b)==1)


def model(a,b,n):
    if n % b == 0:
        return 0
    r=n%b
    q=n//b
    c,t=divmod(a*r*r,b)
    if not t or gcd(b,gcd(r,c)) > 1:
        return 0
    for p in distinct_primes(t):
        if b%p and (b*q+r)%p==0:
            return 0
    return 1


def main():
    triples = checks = pairs = spikes = 0
    for b in range(1,61):
        unit_a = [a for a in range(1, max(2,b)) if gcd(a,b)==1]
        for a in unit_a:
            delta, period, weights = data(a,b)
            # The per-residue CRT average is checked without assuming the formula.
            count = 0
            for r,c,t,w,q in weights:
                if t == 0 or gcd(b,gcd(r,c)) > 1:
                    assert w == 0
                    continue
                successes = sum(model(a,b,b*j+r) for j in range(q))
                assert Fraction(successes,q) == w
                count += 1
            for n in range(1, 6*b+41):
                got = raw(a,b,n)
                expected = model(a,b,n)
                if isqrt(b)**2 == b and n == isqrt(b):
                    expected += 1
                    spikes += 1
                assert got == expected, (a,b,n,got,expected)
                checks += 1
            assert sum((x[3] for x in weights),Fraction(0))/b == delta
            for r,c,t,w,q in weights:
                # Each nontrivial CRT fibre is periodic from its first point.
                for j in range(q+1):
                    assert model(a,b,b*j+r) == model(a,b,b*(j+q)+r)
                    pairs += 1
            triples += 1
        if b > 1:
            cache={a:data(a,b)[0] for a in unit_a}
            for a in unit_a:
                for u in unit_a:
                    assert cache[a]==cache[(a*u*u)%b]
    assert data(1,6)[0] == Fraction(1,2)
    assert data(5,6)[0] == Fraction(23,30)
    assert data(1,4)[0] == Fraction(1,2)
    assert raw(1,36,6) and not model(1,36,6)
    print('RATIONAL_QUADRATIC_COMPOSITE_OK',triples,'parameter_cases',checks,'raw_comparisons',pairs,'fibre_shift_tests',spikes,'spike_tests')

if __name__ == '__main__':
    main()
