#!/usr/bin/env python3
"""Independent finite checks for the reflective-semigroup Wilf limit law.

Uses only the Python standard library. Finite checks corroborate, but do not
replace, the analytic proof of the limiting distribution.
"""
import math


def predicted(g, a):
    q, r = divmod(g, a)
    assert 1 <= g and 2 <= a <= g + 1 and 1 <= r < a
    e = a if r == a - 1 else a - 1
    c = 2 * g - r + 1
    W = e * (c - g) - c
    if r == a - 1:
        assert W == q * a * (a - 2)
    else:
        assert W == q * a * (a - 3) + a - r - 2
    return W, e, c


def independently_enumerated(g, a):
    q, r = divmod(g, a)
    generating = [a, 2 * g + a - r] + list(range(g + 1, g + a))
    end = 2 * g + a + 2
    belongs = [False] * (end + 1)
    belongs[0] = True
    for n in range(1, end + 1):
        belongs[n] = any(n >= x and belongs[n - x] for x in generating)
    gaps = [n for n in range(end + 1) if not belongs[n]]
    assert len(gaps) == g
    assert len({gap % g for gap in gaps}) == g
    conductor = max(gaps) + 1
    left = sum(belongs[:conductor])
    minimal_generators = [n for n in range(1, conductor + a + 1)
                          if n <= end and belongs[n]
                          and not any(n - j > 0 and belongs[j] and belongs[n - j]
                                      for j in range(1, n))]
    return len(minimal_generators) * left - conductor, len(minimal_generators), conductor


def check():
    count = 0
    for g in range(1, 95):
        for a in range(2, g + 2):
            if g % a:
                assert predicted(g, a) == independently_enumerated(g, a), (g, a)
                count += 1
    assert count == 4116, count

    # Independently evaluate the integral on each interval (1/(q+1), 1/q]
    # and compare with the zeta expression, using ordinary floating arithmetic.
    for m in (1, 2, 3):
        zeta_expression = sum(
            (-1) ** (j + 1) * math.comb(m, j)
            * sum(1.0 / (n ** (m + j + 1)) for n in range(1, 50001))
            for j in range(1, m + 1)
        ) / (2 * m + 1)
        interval_integral = sum(
            (q ** m) * (q ** (-2 * m - 1) - (q + 1) ** (-2 * m - 1))
            / (2 * m + 1)
            for q in range(1, 50000)
        )
        assert abs(interval_integral - zeta_expression) < 1e-8, m

    means = {}
    for g in (37, 101, 251, 601, 1201, 5001, 15001):
        data = [predicted(g, a)[0] / g ** 2
                for a in range(2, g + 2) if g % a]
        assert len(data) == g + 1 - sum(g % d == 0 for d in range(1, g + 1))
        means[g] = sum(data) / len(data)
    # A coarse convergence check, not an asserted monotonicity theorem.
    target = sum(1.0 / n ** 3 for n in range(1, 50001)) / 3
    assert abs(means[15001] - target) < 0.0003
    print('PASS: 4116 independent semigroup genus/multiplicity checks')
    print('PASS: first three zeta-moment integral identities (truncated corroboration)')
    print('PASS: exact admissible counts and large-genus mean check')


if __name__ == '__main__':
    check()
