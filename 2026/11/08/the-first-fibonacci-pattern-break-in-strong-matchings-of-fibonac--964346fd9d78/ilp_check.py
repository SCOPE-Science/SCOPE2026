"""Independent exact integer-program cross-check (SciPy/HiGHS required).

Run: python ilp_check.py
Pairwise conflicts are recomputed directly from binary Hamming distances.
"""
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix

for n in range(1, 9):
    verts = [x for x in range(1 << n) if (x & (x << 1)) == 0]
    edges = [(a, b) for a in verts for b in verts
             if a < b and (a ^ b).bit_count() == 1]
    conflicts = []
    for i, (a, b) in enumerate(edges):
        for j in range(i + 1, len(edges)):
            c, d = edges[j]
            if min((a ^ c).bit_count(), (a ^ d).bit_count(),
                   (b ^ c).bit_count(), (b ^ d).bit_count()) <= 1:
                conflicts.append((i, j))
    A = lil_matrix((len(conflicts), len(edges)), dtype=float)
    for row, (i, j) in enumerate(conflicts):
        A[row, i] = A[row, j] = 1.0
    result = milp(c=-np.ones(len(edges)),
                  integrality=np.ones(len(edges)),
                  bounds=Bounds(np.zeros(len(edges)), np.ones(len(edges))),
                  constraints=LinearConstraint(A.tocsr(),
                                               np.zeros(len(conflicts)),
                                               np.ones(len(conflicts))),
                  options={'time_limit': 60, 'mip_rel_gap': 0})
    assert result.status == 0, (n, result.message)
    optimum = int(round(-result.fun))
    assert abs(-result.fun - optimum) < 1.e-7
    print(f'n={n} vertices={len(verts)} edges={len(edges)} '
          f'conflicts={len(conflicts)} maximum={optimum}')
    assert optimum == [0, 1, 1, 1, 2, 3, 5, 8, 12][n]
