"""Exact and independent finite checks for common labelled cherries in binary Patricia tries.

Requires only Python 3 standard library. No randomness or external resources.
Run: python check.py
"""
from fractions import Fraction
from math import comb, exp, log, pi


def rational_probabilities(nmax=16):
    p = {2: Fraction(1)}
    z = {}
    for n in range(3, nmax + 1):
        den = 2 ** n - 2
        p[n] = Fraction(2, den) * (
            1 + sum(comb(n - 2, k - 2) * p[k] for k in range(3, n))
        )
        if n >= 4:
            z[n] = Fraction(2, den) * (
                sum(comb(n - 4, k) * p[k + 2] * p[n - k - 2]
                    for k in range(n - 3))
                + sum(comb(n - 4, k - 4) * z[k] for k in range(4, n))
            )
    return p, z


def exact_pair_binomial(n):
    # Fully independent of split recursion: summing geometric prefix lengths.
    return sum(((-1) ** j) * comb(n - 2, j) * Fraction(2 ** j, 2 ** (j + 1) - 1)
               for j in range(n - 1))


def truncated_pair(n, L):
    return sum(2.0 ** (-l - 1) * (1.0 - 2.0 ** -l) ** (n - 2)
               for l in range(L + 1))


def truncated_two_pairs(n, L):
    # Exact joint two-pair prefix formula truncated at depth L.
    ans = 0.0
    for a in range(1, L + 1):
        x = 2.0 ** -a
        for b in range(1, L + 1):
            y = 2.0 ** -b
            incompatible = 1.0 - 2.0 ** (-min(a, b))
            ans += (x * y / 4.0) * incompatible * max(0.0, 1.0 - x - y) ** (n - 4)
    return ans


def periodic_F(s):
    return sum(0.5 * (2.0 ** (s + j)) * exp(-(2.0 ** (s + j)))
               for j in range(-60, 35))


def main():
    p, z = rational_probabilities(16)
    count = 0
    # The geometric-word formula and a structurally different recursive split
    # formula agree exactly; an identity of distinct algorithms.
    for n in range(2, 17):
        assert p[n] == exact_pair_binomial(n), (n, p[n], exact_pair_binomial(n))
        count += 1
        # A finite truncation has a deterministic geometric upper bound.
        value = truncated_pair(n, 48)
        assert abs(value - float(p[n])) <= 2.0 ** -48
        count += 1
    for n in range(4, 17):
        value = truncated_two_pairs(n, 48)
        assert abs(value - float(z[n])) <= 2.0 ** -47
        count += 1
    assert p[3] == Fraction(1, 3)
    assert p[4] == Fraction(5, 21)
    assert z[4] == Fraction(1, 7)
    count += 3
    # Independent n=4 shape decomposition: balanced split with probability 3/7;
    # the 1+3 split otherwise. The common-cherry law follows by label symmetry.
    h2 = Fraction(3, 49)
    h1 = Fraction(32, 147)
    h0 = Fraction(106, 147)
    assert h0 + h1 + h2 == 1
    assert h1 + 2 * h2 == comb(4, 2) * p[4] ** 2
    assert 2 * h2 == (4 * 3 * 2 * 1 // 4) * z[4] ** 2
    count += 3
    for n in (40, 80, 160, 320, 640):
        pn = truncated_pair(n, 56)
        zn = truncated_two_pairs(n, 56)
        f = periodic_F(log(n, 2) % 1.0)
        assert abs(n * pn - f) < 4.0 / n
        assert abs(zn / pn ** 2 - 1.0) < 3.0 / n ** .5
        count += 2
    period = [periodic_F(k / 10) ** 2 / 2.0 for k in range(10)]
    assert max(period) - min(period) > 9e-6
    count += 1
    print('PASS:', count, 'exact/controlled numerical assertions')
    print('p3=', p[3], 'p4=', p[4], 'q4=', z[4])
    print('n=4 H law:', [h0, h1, h2])
    print('periodic Poisson means (grid):', [round(v, 12) for v in period])
    print('minimum, maximum on grid:', min(period), max(period))


if __name__ == '__main__':
    main()
