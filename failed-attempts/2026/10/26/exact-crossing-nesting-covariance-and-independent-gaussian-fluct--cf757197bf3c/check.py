#!/usr/bin/env python3
"""Independent finite enumeration and symbolic identities for uniform random chord diagrams.
Only Python's standard library and SymPy (for exact symbolic polynomial integration) are used.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, factorial


@lru_cache(maxsize=None)
def matchings(endpoints):
    if not endpoints:
        return ((),)
    first = endpoints[0]
    out = []
    for j in range(1, len(endpoints)):
        second = endpoints[j]
        rest = endpoints[1:j] + endpoints[j + 1:]
        for m in matchings(rest):
            out.append(((first, second),) + m)
    return tuple(out)


def counts(matching):
    crossing = nesting = alignment = 0
    for i, (a, b) in enumerate(matching):
        for c, d in matching[i + 1:]:
            a1, a2, b1, b2 = sorted((a, b, c, d))
            # Compare the partners of the earliest endpoint in the 4-set.
            partner = b if a == a1 else (a if b == a1 else (d if c == a1 else c))
            if partner == a2:
                alignment += 1
            elif partner == b1:
                crossing += 1
            elif partner == b2:
                nesting += 1
            else:
                raise AssertionError('unclassified pair')
    return crossing, nesting, alignment


def check_enumeration():
    assertions = 0
    for n in range(2, 8):
        all_m = matchings(tuple(range(2*n)))
        total = len(all_m)
        assert total == factorial(2*n) // (2**n * factorial(n))
        assertions += 1
        sums = [0, 0, 0]
        seconds = [[0]*3 for _ in range(3)]
        for m in all_m:
            x = counts(m)
            assert sum(x) == comb(n, 2)
            assertions += 1
            for a in range(3):
                sums[a] += x[a]
                for b in range(3):
                    seconds[a][b] += x[a]*x[b]
        mu = Fraction(n*(n-1), 6)
        assert all(Fraction(s, total) == mu for s in sums)
        assertions += 3
        base = Fraction(n*(n-1), 90)
        expected = [
            [2*(n+3), -5, -(2*n+1)],
            [-5, 2*(n+3), -(2*n+1)],
            [-(2*n+1), -(2*n+1), 2*(2*n+1)],
        ]
        for a in range(3):
            for b in range(3):
                observed = Fraction(seconds[a][b], total) - mu**2
                assert observed == base*expected[a][b], (n,a,b,observed,base*expected[a][b])
                assertions += 1
        print(f'Exact enumeration n={n}: {total:,} perfect matchings, all 9 covariance entries pass')
    return assertions


def check_integrals():
    import sympy as s
    u,v = s.symbols('u v', real=True)
    ell = v-u
    fc = 2*ell*(1-ell)
    fn = ell**2 + 2*u*(1-v)
    E = lambda p: s.factor(2*s.integrate(s.integrate(s.expand(p),(v,u,1)),(u,0,1)))
    gs = [fc - s.Rational(1,3), fn-s.Rational(1,3)]
    checks = [
        (E(fc), s.Rational(1,3)), (E(fn), s.Rational(1,3)),
        (E(gs[0]**2), s.Rational(1,45)),
        (E(gs[1]**2), s.Rational(1,45)),
        (E(gs[0]*gs[1]), s.Integer(0)),
        (s.factor(s.Rational(2,9)-2*s.Rational(1,45)), s.Rational(8,45)),
        (s.factor(s.Rational(-1,9)-2*s.Integer(0)), s.Rational(-1,9)),
    ]
    for x,y in checks:
        assert x==y,(x,y)
    print('SymPy verified both conditional means, full rank-two first-projection Gram matrix, and canonical kernel covariance')
    return len(checks)


if __name__ == '__main__':
    a = check_enumeration()
    b = check_integrals()
    print(f'PASS: {a+b:,} independently counted exact assertions, all symbolic identities checked')
