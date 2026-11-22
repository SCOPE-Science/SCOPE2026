"""Exact finite verification of the rectangular random rook-local-maximum law.

No randomized tests: all rank arrays for each listed board are enumerated.
Run: python3 verify_rook_maxima.py
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb, factorial

BOARDS = [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3)]
checks = 0
for r, c in BOARDS:
    count_hist = Counter()
    matching_hist = Counter()
    sample_count = factorial(r * c)
    for a in permutations(range(r * c)):
        row_max = [max(range(c), key=lambda j: a[i * c + j]) for i in range(r)]
        col_max = [max(range(r), key=lambda i: a[i * c + j]) for j in range(c)]
        matching = tuple((i, j) for i, j in enumerate(row_max) if col_max[j] == i)
        assert len(matching) >= 1
        count_hist[len(matching)] += 1
        matching_hist[matching] += 1
    N = r + c - 1
    for k in range(1, min(r, c) + 1):
        predicted = Fraction(comb(r, k) * comb(c-1, k-1), comb(N, c))
        observed = Fraction(count_hist[k], sample_count)
        assert observed == predicted, (r, c, k, observed, predicted)
        checks += 1
        predicted_fm = Fraction(factorial(r) * factorial(c) * factorial(N-k),
                                factorial(r-k) * factorial(c-k) * factorial(N))
        actual_fm = sum(
            Fraction(count_hist[s] * factorial(s), sample_count * factorial(s-k))
            for s in range(k, min(r, c) + 1)
        )
        assert actual_fm == predicted_fm, (r, c, k, actual_fm, predicted_fm)
        checks += 1
        values = [v for matching, v in matching_hist.items() if len(matching) == k]
        assert len(set(values)) == 1, (r, c, k, values)
        assert len(values) == comb(r, k) * comb(c, k) * factorial(k)
        checks += 2
    mean = Fraction(r*c, N)
    actual_mean = sum(Fraction(k*v, sample_count) for k,v in count_hist.items())
    assert actual_mean == mean
    checks += 1
    var = (Fraction(r*c*(r-1)*(c-1), N*N*(N-1)) if N > 1
           else Fraction(0))
    actual_var = sum(Fraction(v, sample_count) * (k-mean)**2
                     for k,v in count_hist.items())
    assert actual_var == var, (r,c,actual_var,var)
    checks += 1
    print(f"{r}x{c}: {sample_count} rank arrays, P(K=k) = " +
          ", ".join(f"{k}:{Fraction(count_hist[k],sample_count)}"
                    for k in sorted(count_hist)))
print(f"PASS: {checks} exact identities and matching-symmetry checks")
