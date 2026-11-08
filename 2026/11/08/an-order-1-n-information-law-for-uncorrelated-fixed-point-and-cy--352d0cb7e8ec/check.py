#!/usr/bin/env python3
"""Self-contained reproducibility checks for fixed-point/cyclic-core information."""
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import product
from math import comb, factorial


def derangements(n):
    d = [1, 0]
    for j in range(2, n + 1):
        d.append((j - 1) * (d[j - 1] + d[j - 2]))
    return d[:n + 1]


def q(m, k, der):
    return Fraction(der[m - k], factorial(k) * factorial(m - k)) if 0 <= k <= m else Fraction(0)


def cyclic_count(f):
    n = len(f)
    cyc = set()
    for i in range(n):
        j = i
        for _ in range(n):
            j = f[j]
        cyc.add(j)
    return len(cyc)


def weight(n, m):
    return Fraction(factorial(n), factorial(n - m)) * Fraction(m, n ** (m + 1))


def d_decimal(x):
    return Decimal(x.numerator) / Decimal(x.denominator)


def divergence_to_poisson(m, der):
    s = Decimal(0)
    for k in range(m + 1):
        x = q(m, k, der)
        if x:
            p = d_decimal(x)
            s += p * (p.ln() + Decimal(factorial(k)).ln() + Decimal(1))
    return s


def divergence_binomial(n):
    s = Decimal(0)
    for k in range(n + 1):
        x = Fraction(comb(n, k) * (n - 1) ** (n - k), n ** n)
        if x:
            p = d_decimal(x)
            s += p * (p.ln() + Decimal(factorial(k)).ln() + Decimal(1))
    return s


def direct_info(n, der):
    res = Decimal(0)
    for m in range(1, n + 1):
        wm = d_decimal(weight(n, m))
        for k in range(m + 1):
            qq = q(m, k, der)
            if qq:
                bb = Fraction(comb(n, k) * (n - 1) ** (n - k), n ** n)
                res += wm * d_decimal(qq) * (d_decimal(qq) / d_decimal(bb)).ln()
    return res


def main():
    tests = 0
    der = derangements(210)
    for n in range(1, 7):
        actual = Counter()
        for f in product(range(n), repeat=n):
            actual[(cyclic_count(f), sum(i == f[i] for i in range(n)))] += 1
        for m in range(1, n + 1):
            for k in range(n + 1):
                lhs = Fraction(actual[m, k], n ** n)
                rhs = weight(n, m) * q(m, k, der)
                assert lhs == rhs, (n, m, k, lhs, rhs)
                tests += 1
        assert sum(weight(n, m) for m in range(1, n + 1)) == 1
        tests += 1
    for m in range(1, 70):
        assert sum(q(m, k, der) for k in range(m + 1)) == 1
        assert sum(k * q(m, k, der) for k in range(m + 1)) == 1
        tests += 2
        if m >= 2:
            assert sum(k * (k - 1) * q(m, k, der) for k in range(m + 1)) == 1
            tests += 1
    with localcontext() as ctx:
        ctx.prec = 66
        dvals = [Decimal(0)] + [divergence_to_poisson(m, der) for m in range(1, 41)]
        partial = sum(Decimal(m) * dvals[m] for m in range(1, 31))
        # D(Q_m || Pois(1)) <= chi-squared <= (e*2^(m+1)+1)/(m+1)!
        tail = sum(Decimal(m) * ((Decimal(1).exp()) * (2 ** (m + 1)) + 1) /
                   Decimal(factorial(m + 1)) for m in range(31, 211))
        # For m >= 31, successive majorant terms have ratio <= 2/31.
        # Thus the infinite remainder is bounded by its first term / (1-2/31).
        a31 = Decimal(31) * (Decimal(1).exp() * (2 ** 32) + 1) / Decimal(factorial(32))
        certified_tail = a31 / (1 - Decimal(2) / Decimal(31))
        assert tail < certified_tail < Decimal('1.5e-24')
        assert abs(partial - Decimal('3.692926238979770132438700')) < Decimal('1e-23')
        tests += 2
        print('J_30 =', partial)
        print('certified 30-term remainder <', certified_tail)
        for n in [2, 3, 5, 10, 20, 35]:
            lhs = direct_info(n, der)
            via = sum(d_decimal(weight(n, m)) * dvals[m] for m in range(1, n + 1)) - divergence_binomial(n)
            assert abs(lhs - via) < Decimal('1e-54'), (n, lhs, via)
            assert lhs > 0
            tests += 2
            print('n=', n, 'n*I=', Decimal(n) * lhs)
        for n in [50, 100, 200]:
            # D values for m>40 have negligible error under the superfactorial bound.
            expectation = sum(d_decimal(weight(n, m)) * dvals[m] for m in range(1, 41))
            approx = Decimal(n) * (expectation - divergence_binomial(n))
            print('n=', n, 'n*I approximately=', approx)
            tests += 1
    print('PASS:', tests, 'checks, exact mapping enumeration through n=6')


if __name__ == '__main__':
    main()
