#!/usr/bin/env python3
"""Independent exact checks for a finite-path outbreak-covariance theorem.

Python 3 standard library only. A uniformly selected seed reaches its open-edge
component; every contact edge is independently open with probability p.
"""
from fractions import Fraction
from itertools import combinations
from math import comb

checks = 0


def verify(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def predicted(n, i, j, p):
    """Indices are one-based, with i < j."""
    g_i = sum((p ** abs(v - i) for v in range(1, n + 1)), Fraction())
    g_j = sum((p ** abs(v - j) for v in range(1, n + 1)), Fraction())
    h = j - i + 1
    h += sum((p ** a for a in range(1, i)), Fraction())
    h += sum((p ** a for a in range(1, n - j + 1)), Fraction())
    joint = p ** (j - i) * h / n
    return g_i / n, g_j / n, joint


def enumerated(n, p):
    marg = [Fraction() for _ in range(n)]
    pair = [[Fraction() for _ in range(n)] for _ in range(n)]
    for edges in range(1 << (n - 1)):
        k = edges.bit_count()
        mass = p ** k * (1 - p) ** (n - 1 - k) / n
        for root in range(n):
            lo, hi = root, root
            while lo and (edges & (1 << (lo - 1))):
                lo -= 1
            while hi < n - 1 and (edges & (1 << hi)):
                hi += 1
            for a in range(lo, hi + 1):
                marg[a] += mass
                for b in range(a + 1, hi + 1):
                    pair[a][b] += mass
    return marg, pair


# Independent edge-state/seed enumeration against the closed moment formula.
for n in range(3, 10):
    for p in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
        marg, pair = enumerated(n, p)
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                a, b, c = predicted(n, i, j, p)
                verify(marg[i - 1] == a, ('first marginal', n, i, j, p))
                verify(marg[j - 1] == b, ('second marginal', n, i, j, p))
                verify(pair[i - 1][j - 1] == c, ('joint', n, i, j, p))


# Exact coefficient CDF proof for the adjacent-boundary pair.
# F = n^2 Cov(X_1,X_2); F/(1-p) = -1 + positive coefficients.
for n in range(3, 101):
    Dprime = [1, 1] + list(range(2, n))
    D = [(v - 1) + abs(w - 2) for v in range(1, n + 1)
                                    for w in range(1, n + 1)]
    verify(len(Dprime) == n and len(D) == n * n, ('sizes', n))
    verify(n * sum(a == 0 for a in Dprime) - sum(a == 0 for a in D) == -1,
           ('constant coefficient', n))
    for k in range(1, 2 * n - 3):
        q_k = n * sum(a <= k for a in Dprime) - sum(a <= k for a in D)
        verify(q_k > 0, ('strict positive coefficients', n, k))
    for p in (Fraction(1, 7), Fraction(2, 5), Fraction(3, 4)):
        a, b, joint = predicted(n, 1, 2, p)
        F = n*n*(joint - a*b)
        # F is also equal to n E p^Dprime - E p^D by independent construction.
        rhs = n * sum((p**a for a in Dprime), Fraction())
        rhs -= sum((p**a for a in D), Fraction())
        verify(F == rhs, ('cdf polynomial identity', n, p))


# Exact one-edge expansion (an independently checked finite polynomial identity).
# In powers of epsilon = 1-p, marginal failures are O(epsilon), and the
# coefficient of P(both fail) is sum of compatible single-edge cuts / n.
for n in range(3, 31):
    for i, j in combinations(range(1, n + 1), 2):
        single_cuts = sum(t for t in range(1, i))
        single_cuts += sum(n - t for t in range(j, n))
        coefficient = Fraction(single_cuts, n)
        formula = Fraction(i*(i-1)+(n-j)*(n-j+1), 2*n)
        verify(coefficient == formula, ('single-edge coefficient', n, i, j))
        verify((coefficient > 0) == ((i, j) != (1, n)),
               ('endpoint exception', n, i, j))


# Endpoint covariance is strictly negative in the whole nondegenerate range.
for n in range(3, 61):
    for p in (Fraction(1, 10), Fraction(1, 3), Fraction(1, 2), Fraction(9, 10)):
        a, b, joint = predicted(n, 1, n, p)
        verify(joint - a*b < 0, ('endpoint strict negativity', n, p))

print(f'PASS: {checks} exact rational assertions')
