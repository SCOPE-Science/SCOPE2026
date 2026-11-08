"""Exact finite checks for minimum supports of quadratic polynomial functions.
Usage: python3 verify.py
"""
import itertools
from fractions import Fraction


def lower_fraction(m, n):
    def factors(a):
        p = 2
        out = []
        while p * p <= a:
            if a % p == 0:
                out.append(p)
                while a % p == 0:
                    a //= p
            p += 1
        if a > 1:
            out.append(a)
        return out
    return min((Fraction(1, 2) if n == 1 else Fraction(1, 4)) if p == 2 else Fraction(p-2, p) for p in factors(m))


def monomials(x):
    return (1,) + x + tuple(v * v for v in x) + tuple(
        x[i] * x[j] for i in range(len(x)) for j in range(i+1, len(x)))


def exhaustive(m, n):
    vectors = [monomials(x) for x in itertools.product(range(m), repeat=n)]
    d = len(vectors[0]); total = m ** n
    fractions = [(1, 2) if p == 2 and n == 1 else
                 (1, 4) if p == 2 else (p - 2, p)
                 for p in prime_divisors(m)]
    a, b = min(fractions, key=lambda ab: ab[0] / ab[1]); bound = total * a // b
    assert bound * b == total * a
    checked = 0
    observed = total
    for coefs in itertools.product(range(m), repeat=d):
        nonzero = 0
        for v in vectors:
            if sum(c * t for c, t in zip(coefs, v)) % m:
                nonzero += 1
                if nonzero > bound:
                    break
        if 0 < nonzero < observed:
            observed = nonzero
        assert nonzero == 0 or nonzero >= bound, (m, n, coefs, nonzero, bound)
        checked += 1
    assert observed == bound, (m, n, observed, bound)
    return checked, observed


def prime_divisors(m):
    ps = []
    for p in range(2, m+1):
        if m % p == 0:
            ps.append(p)
            while m % p == 0:
                m //= p
        if m == 1: break
    return ps


def witness(m, n):
    ps = prime_divisors(m)
    p = min(ps, key=lambda p: (1/2 if n == 1 else 1/4) if p == 2 else (p-2)/p)
    def q(x):
        if p == 2 and n >= 2:
            return (m//2) * x[0] * x[1]
        if p == 2:
            return (m//2)*x[0]
        return (m//p)*x[0]*(x[0]-1)
    hits = sum(q(x) % m != 0 for x in itertools.product(range(m),repeat=n))
    minratio = min((Fraction(1,2) if n==1 else Fraction(1,4)) if pp==2 else Fraction(pp-2,pp) for pp in ps)
    a,b = minratio.numerator,minratio.denominator
    assert hits*b==m**n*a, (m,n,p,hits,a,b)
    return hits


if __name__ == '__main__':
    total = 0
    for m,n in ((2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(4,2),
                (5,1),(5,2),(6,1),(6,2),(7,1),(7,2),(8,1),(8,2),(9,1)):
        trials,minimum=exhaustive(m,n)
        assert minimum==witness(m,n)
        total += trials
        print(f'modulus={m} variables={n} polynomials={trials} exact_minimum_support={minimum}')
    for m in range(2,101):
        for n in (1,2,3):
            assert witness(m,n)==m**n*min((1/2 if p==2 and n==1 else 1/4) if p==2 else (p-2)/p for p in prime_divisors(m))
    print('VERIFY_OK exhaustive_polynomials=',total,'CRT_witness_checks=',99*3)
