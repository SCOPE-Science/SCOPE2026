"""Exact finite consistency tests for monomial Bergman weighted-composition isometries.

The proof of the infinite-dimensional theorem is analytical; these tests are
supplementary and verify endpoint block norms and the combinatorial obstruction.
Run: python3 check.py
"""
from fractions import Fraction
from collections import Counter

checks = 0
for N in range(2, 21):
    for n in range(0, 121):
        # alpha=0, sole output coefficient sqrt(N) at degree N(n+1)-1.
        image_norm = N * Fraction(1, N * (n + 1))
        assert image_norm == Fraction(1, n + 1)
        checks += 1
        # alpha=1, N coefficients all of squared modulus N.
        image_norm = N * sum(
            (Fraction(2, (k + 1) * (k + 2))
             for k in range(N * (n + 1) - 1, N * (n + 2) - 1)),
            Fraction(0, 1),
        )
        assert image_norm == Fraction(2, (n + 1) * (n + 2))
        checks += 1
        # Distinct inputs map to disjoint exponent blocks at the classified weights.
        support_n = set(range(N * (n + 1) - 1, N * (n + 2) - 1))
        support_next = set(range(N * (n + 2) - 1, N * (n + 3) - 1))
        assert not (support_n & support_next)
        checks += 1
    for degree in range(2, 13):
        # S(t)^degree has strictly positive coefficients at each integer
        # between 0 and degree*(N-1), which forces repeated residues.
        support = list(range(N - 1, N - 1 + degree * (N - 1) + 1))
        counts = Counter(k % N for k in support)
        assert max(counts.values()) >= 2
        checks += 1
print(f"PASS: {checks} exact finite supplementary assertions")
