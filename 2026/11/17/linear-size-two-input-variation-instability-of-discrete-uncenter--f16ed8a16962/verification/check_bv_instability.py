#!/usr/bin/env python3
"""Exact rational diagnostics for interval-maximal variation instability.

Run with Python 3.8+ and no third-party packages.
"""
from fractions import Fraction as Q


def variation(x):
    return sum((abs(v - u) for u, v in zip(x, x[1:])), Q(0))


def interval_maximum(x):
    n = len(x)
    prefix = [Q(0)]
    for value in x:
        prefix.append(prefix[-1] + value)
    out = []
    for i in range(n):
        best = Q(-1)
        for a in range(i + 1):
            for b in range(i + 1, n + 1):
                avg = (prefix[b] - prefix[a]) / Q(b - a)
                if avg > best:
                    best = avg
        out.append(best)
    return out


def witness(q, extra=0):
    m = 12 * q
    epsilon = Q(1, 100 * m)
    f = [Q(1)] * m + [Q(3, 4) if d % 2 else Q(0)
                         for d in range(1, m + 1)] + [Q(0)] * extra
    h = [Q(1)] * m + [Q(0)] * (m + extra)
    g = [a + epsilon * b for a, b in zip(f, h)]
    return m, epsilon, f, g, h


def main():
    exact = 0
    for q in range(1, 6):
        for extra in (0, 3) if q <= 3 else (0,):
            m, epsilon, f, g, h = witness(q, extra)
            delta = [v - u for u, v in zip(interval_maximum(f), interval_maximum(g))]
            assert variation([epsilon * a for a in h]) == epsilon
            for d in range(8 * q + 3, m + 1):
                value = delta[m + d - 1]
                if d % 2:
                    assert value == 0, (q, extra, d, value)
                else:
                    assert value >= epsilon / 2, (q, extra, d, value)
                exact += 1
            ratio = variation(delta) / epsilon
            assert ratio >= Q(4 * q - 3, 2), (q, extra, ratio)
    symbolic = 0
    for q in range(1, 2001):
        m = 12 * q
        eps = Q(1, 100 * m)
        for d in (8 * q + 3, 8 * q + 4, m - 1, m):
            if d % 2:
                assert m * (Q(1, 4) + eps) < Q(3, 4) * (d // 2)
            else:
                assert Q(m) + Q(3, 4) * (d // 2) > Q(m + d, 2)
            symbolic += 1
    print('EXACT_ODD_EVEN_BRANCH_COMPARISONS_PASSED', exact)
    print('EXACT_INTEGER_BRANCH_INEQUALITIES_PASSED', symbolic)
    print('ZERO_PADDING_AND_TOTAL_VARIATION_RATIOS_PASSED')
    print('ALL_UNCENTERED_INTERVAL_VARIATION_DIAGNOSTICS_PASSED')


if __name__ == '__main__':
    main()
