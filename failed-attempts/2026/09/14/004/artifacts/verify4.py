import json, sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1804/output/artifacts')
from petersen_core import EDGES, all_minimal_covers
from itertools import combinations_with_replacement
covers = all_minimal_covers()
Cmat = [[(m >> v) & 1 for v in range(10)] for m in covers]
E = EDGES
def gens(r):
    G = set()
    for combo in combinations_with_replacement(range(len(E)), r):
        g = [0]*10
        for e in combo:
            g[E[e][0]] += 1; g[E[e][1]] += 1
        G.add(tuple(g))
    return G
G2, G3 = gens(2), gens(3)
cert = json.load(open('contain4_certificate.json'))
mins = [tuple(a) for a in cert['minimals']]
assert cert['fail_vs_I2'] == [] and cert['fail_vs_I3'] == [], "failures!"
print("num minimals:", len(mins))
from collections import Counter
print("degree dist:", sorted(Counter(sum(a) for a in mins).items()))
print("max coord:", max(max(a) for a in mins))
for a in mins:
    assert all(sum(Cmat[c][v]*a[v] for v in range(10)) >= 4 for c in range(15))
    for v in range(10):
        if a[v] == 0: continue
        assert any(sum(Cmat[c][w]*a[w] for w in range(10)) == 4 and Cmat[c][v]==1 for c in range(15)), (a, v)
    assert any(all(g[v] <= a[v] for v in range(10)) for g in G2), ("not in I2", a)
    assert any(all(g[v] <= a[v] for v in range(10)) for g in G3), ("not in I3", a)
print("VERIFY4 OK: all minimals feasible, minimal, in I^2 and I^3.")
