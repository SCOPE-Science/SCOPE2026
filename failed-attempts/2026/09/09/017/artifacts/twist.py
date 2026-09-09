"""Twist-region analysis of KATLAS 8_19 PD + local twist insertion. Bounded step."""
import sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-314/output/artifacts')
from pdcal import build_from_X, bracket_X

RAW = [(4, 2, 5, 1), (8, 4, 9, 3), (9, 15, 10, 14), (5, 13, 6, 12),
       (13, 7, 14, 6), (11, 1, 12, 16), (15, 11, 16, 10), (2, 8, 3, 7)]
P0 = lambda a, b, c, d: [(a, c), (b, d)]
P1 = lambda a, b, c, d: [(a, d), (b, c)]

# Edge->crossings incidence (computed): bigon pairs share 2 edges.
X = {i + 1: RAW[i] for i in range(8)}
edge_at = {}
for c, (a, b, cc, d) in X.items():
    for x in (a, b, cc, d):
        edge_at.setdefault(x, []).append(c)
print('bigon pairs:', [(c1, c2) for c1 in X for c2 in X if c1 < c2 and
      len(set(X[c1]) & set(X[c2])) == 2])
