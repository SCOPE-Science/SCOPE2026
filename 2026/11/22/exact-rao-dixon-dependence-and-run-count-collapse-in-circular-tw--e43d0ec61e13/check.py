"""Exact independent weak-composition checks for two circular spacing-frequency statistics.
Run: python3 check.py (only Python standard library required).
"""
from fractions import Fraction
from math import comb


def compositions(total, slots):
    if slots == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for tail in compositions(total - first, slots - 1):
                yield (first,) + tail


def theoretical_moments(m, n):
    assert m >= 2 and n >= 2
    var_z = Fraction(m*n*(m-1)*(n-1), (m+n-2)*(m+n-1)**2)
    var_q = Fraction(4*n*(m-1)*(m+n)*(n-1)*(m+n+1),
                     (m+1)**2*(m+2)*(m+3))
    cov = Fraction(2*n*(m-1)*(n-1), (m+1)*(m+n-1))
    rho_sq = Fraction((m+2)*(m+3)*(m+n-2), m*(m+n)*(m+n+1))
    return var_z, var_q, cov, rho_sq


def empirical_exact(m, n):
    data = list(compositions(n, m))
    assert len(data) == comb(n+m-1, m-1)
    zs = [sum(v == 0 for v in row) for row in data]
    qs = [sum(v*v for v in row) for row in data]
    count = len(data)
    mean_z = Fraction(sum(zs), count)
    mean_q = Fraction(sum(qs), count)
    var_z = Fraction(sum(v*v for v in zs), count) - mean_z**2
    var_q = Fraction(sum(v*v for v in qs), count) - mean_q**2
    cov = Fraction(sum(z*q for z, q in zip(zs, qs)), count) - mean_z*mean_q
    return data, zs, qs, var_z, var_q, cov


def main():
    checks = 0
    for m in range(2, 8):
        for n in range(2, 8):
            data, zs, qs, vz, vq, cov = empirical_exact(m, n)
            evz, evq, ecov, erho = theoretical_moments(m, n)
            assert (vz, vq, cov) == (evz, evq, ecov), (m,n)
            checks += 1
            if n <= m:
                for row, z in zip(data, zs):
                    r = sum(abs(Fraction(v) - Fraction(n,m)) for v in row)
                    c = 2*sum(v > 0 for v in row)
                    assert r == Fraction(2*n, m)*z
                    assert r == 2*n - Fraction(n, m)*c
                    checks += 2
                assert cov**2/(vz*vq) == erho
                checks += 1
                for z in range(max(0,m-n), m):
                    observed = sum(v == z for v in zs)
                    predicted = comb(m,z)*comb(n-1, m-z-1)
                    assert observed == predicted, (m,n,z)
                    checks += 1
    for s in range(2, 30):
        expected = Fraction((s-1)*(s+2)*(s+3), s*s*(2*s+1))
        assert theoretical_moments(s,s)[3] == expected
        assert expected > Fraction(1,2)
        if s >= 3:
            prior = Fraction((s-2)*(s+1)*(s+2), (s-1)**2*(2*s-1))
            assert expected < prior
        checks += 3
    print('PASS:',checks,'exact-rational assertions')

if __name__ == '__main__':
    main()
