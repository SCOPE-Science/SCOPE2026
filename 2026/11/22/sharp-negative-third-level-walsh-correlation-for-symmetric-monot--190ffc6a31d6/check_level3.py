#!/usr/bin/env python3
"""Exact finite checks of a sharp third Walsh-level correlation formula.

Standard library only.  Finite verification supplements, but does not
replace, the proof for arbitrary dimensions.
"""
from fractions import Fraction
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def peak_index(m):
    """Smallest k in the left half attaining the positive third-level peak."""
    k = 0
    while k < m // 2 and m - 2 * k - 1 > 0 and (m - 2 * k - 1)**2 > 3 * m + 1:
        k += 1
    return k


def verify():
    coefficient_checks = 0
    for n in range(3, 121):
        m = n - 1
        F = [comb(m, k) * ((m - 2*k)**2 - m) for k in range(m+1)]
        P, Q = max(F), -min(F)
        k = peak_index(m)
        assert F[k] == P
        assert -F[m//2] == Q
        optimal_positive = {k, m-k}
        j = m - 2*k
        if (j-1)**2 == 3*m+1:
            optimal_positive.update((k+1, m-k-1))
        assert optimal_positive == {i for i, x in enumerate(F) if x == P}
        assert {m//2, (m+1)//2} == {i for i, x in enumerate(F) if x == -Q}
        coefficients = []
        for t in range(1, n+1):
            direct = -choose(n-3,t-1) + 2*choose(n-3,t-2) - choose(n-3,t-3)
            assert direct * m * (m-1) == -F[t-1]
            coefficients.append(Fraction(direct, 2**n))
            coefficient_checks += 1
        bound = Fraction(comb(n,3)*P*Q, 2**(2*n)*m*m*(m-1)*(m-1))
        assert max((-comb(n,3)*a*b for a in coefficients for b in coefficients)) == bound
    # Independent direct Walsh expectation on every cube point for small n.
    for n in range(3, 9):
        for t in range(1, n+1):
            for order in (1,3):
                mask = (1 << order)-1
                total = sum(((-1)**((x&mask).bit_count())) for x in range(1 << n)
                            if x.bit_count() >= t)
                if order == 1:
                    expected = -choose(n-1,t-1)
                else:
                    expected = -choose(n-3,t-1)+2*choose(n-3,t-2)-choose(n-3,t-3)
                assert total == expected, (n,t,order,total,expected)
    print(f'PASS: 118 dimensions, {coefficient_checks} exact threshold coefficients; '
          'exhaustive pair maxima and full Walsh sums for dimensions 3 through 8.')


if __name__ == '__main__':
    verify()
