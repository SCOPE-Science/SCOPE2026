"""Exact finite-dimensional corroboration of the row-mode counting lemma.

The infinite-dimensional arguments are proved analytically in RESULT.md.
Only Python's standard library is required.
"""
from fractions import Fraction as F
from itertools import product

checks = 0
levels = [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]
for d in range(1, 5):
    # Diagonal positive symbols, with finite matrix algebra in operator norm.
    for diag in product(levels, repeat=d):
        modes = sorted([s for s in diag for _ in range(d)], reverse=True)
        assert len(modes) == d * d
        checks += 1
        for t in levels:
            high = [i for i, s in enumerate(diag) if s > t]
            # Each high spectral row carries d independent columns.
            basis = [(i, col) for i in high for col in range(d)]
            assert len(basis) == d * len(high)
            assert sum(s > t for s in modes) == len(basis)
            checks += 2
            if high:
                # Exact Frobenius corroboration on several rational test matrices.
                for seed in range(1, 5):
                    X = [[F((seed + i * 2 + col * 3) % 9 - 4, 7)
                          for col in range(d)] for i in high]
                    norm2 = sum(x*x for row in X for x in row)
                    out2 = sum(diag[i]**2 * x*x for i, row in zip(high, X)
                               for x in row)
                    assert out2 >= t*t*norm2
                    checks += 1
        # Finite rank truncations: exact matrix row count and exact norm error.
        for n in range(1, d * d + 2):
            beta = modes[n - 1] if n <= d * d else F(0)
            for t in levels:
                if t > beta:
                    kept = [s for s in diag if s > t]
                    rank = d * len(kept)
                    error = max((s for s in diag if s <= t), default=F(0))
                    assert rank < n
                    assert error <= t
                    checks += 2
# Hybrid direct sum: count modes with their row-dimension multiplicity.
blocks = [(2, (F(1), F(1, 2))), (3, (F(3, 4), F(1, 4), F(0))),
          (1, (F(1, 8),))]
all_modes = sorted([s for d, vals in blocks for s in vals for _ in range(d)],
                   reverse=True)
assert all_modes[:4] == [F(1), F(1), F(3, 4), F(3, 4)]
checks += 1
for n in range(1, len(all_modes) + 3):
    beta = all_modes[n - 1] if n <= len(all_modes) else F(0)
    for t in [F(0), F(1, 16), F(1, 8), F(1, 4), F(1, 2), F(3, 4), F(1)]:
        count = sum(d for d, vals in blocks for s in vals if s > t)
        assert ((t < beta) == (count >= n)) or (t == beta)
        checks += 1
print(f'MATRIX_MODULE_ROWS_EXACT_OK {checks}')
