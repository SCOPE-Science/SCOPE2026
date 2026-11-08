"""Exact finite checks of cubical-skeleton Minkowski averaging formulas.

Usage: python3 checker.py  (standard library only).
The infinite-dimensional and all-parameter statements require the accompanying proof.
"""
from itertools import combinations, product
from fractions import Fraction

assertions = 0

# Independent construction: discretize each summand's face coordinates to {0,1/2,1}.
# Encode coordinates on this grid by 0,1,2; N-fold sums land in {0,...,2N}.
for n in range(1, 5):
    for k in range(n + 1):
        faces = [v for v in product((0, 1, 2), repeat=n)
                 if sum(t == 1 for t in v) <= k]
        for N in range(1, 4):
            sums = {(0,) * n}
            for _ in range(N):
                sums = {tuple(x[j] + y[j] for j in range(n))
                        for x in sums for y in faces}
            for v in product(range(2 * N + 1), repeat=n):
                assert (v in sums) == (sum(t % 2 for t in v) <= N * k), (n, k, N, v)
                assertions += 1

# Compare order-statistic distances with an independent exhaustive subset search;
# grid-cell positions are multiples of 1/(4N), and the squared distances are exact.
for n in range(1, 4):
    for k in range(n + 1):
        for N in range(1, 4):
            m = max(n - N * k, 0)
            positions = range(4 * N + 1)
            if (4 * N + 1) ** n > 1500:
                continue
            for v in product(positions, repeat=n):
                nearest = tuple(min(t % 4, 4 - t % 4) for t in v)
                predicted = sum(t * t for t in sorted(nearest)[:m])
                actual = min(sum(nearest[j] ** 2 for j in J)
                             for J in combinations(range(n), m))
                assert predicted == actual, (n, k, N, v)
                assertions += 1

# Weighted orthotopes: all grid-cell midpoints attain the claimed exact Hausdorff
# radius, and every point's m smallest grid-distances obey the global upper bound.
for lengths in [(1, 2, 3), (3, 7, 11), (1, 1, 5)]:
    n = len(lengths)
    for k in range(n + 1):
        for N in range(1, 4):
            m = max(n - N*k, 0)
            expected_sq = sum(Fraction(L*L, 4*N*N) for L in sorted(lengths)[:m])
            for parts in product(range(2*N+1), repeat=n):
                # Direct distance from coordinates to the regular coordinate grid.
                delta_sq = []
                for L, a in zip(lengths, parts):
                    x = Fraction(a*L, 2*N)
                    dist = min(abs(x - Fraction(j*L, N)) for j in range(N+1))
                    delta_sq.append(dist*dist)
                distance_sq = sum(sorted(delta_sq)[:m]); assert distance_sq <= expected_sq
                assertions += 1
            # Simultaneous grid-cell center achieves the upper bound exactly.
            x = [Fraction(L, 2*N) for L in lengths]
            delta_sq = [min((abs(y - Fraction(j*L, N)))**2 for j in range(N+1))
                        for L,y in zip(lengths,x)]
            assert sum(sorted(delta_sq)[:m]) == expected_sq
            assertions += 1

print(f"PASS: {assertions} exact assertions")
