"""Independent re-verification of the I^(3) subset I^2 certificate + C5 data for DRAFT."""
import json, sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1804/output/artifacts')
from petersen_core import EDGES, all_minimal_covers
from itertools import combinations_with_replacement
covers = all_minimal_covers()
Cmat = [[(m >> v) & 1 for v in range(10)] for m in covers]
E = EDGES
# genuine 2-edge-product exponent set
G = set()
for i, j in combinations_with_replacement(range(len(E)), 2):
    g = [0]*10
    for e in (E[i], E[j]):
        g[e[0]] += 1; g[e[1]] += 1
    G.add(tuple(g))
cert = json.load(open('contain32_certificate.json'))
mins = [tuple(a) for a in cert['minimals']]
wit = {eval(k): tuple(v) for k, v in cert['witness'].items()}
assert cert['failures'] == [], "failures nonempty!"
assert len(mins) == 562, len(mins)
for a in mins:
    assert all(sum(Cmat[c][v]*a[v] for v in range(10)) >= 3 for c in range(15)), ("infeasible", a)
    # minimality
    for v in range(10):
        if a[v] == 0: continue
        assert any(sum(Cmat[c][w]*a[w] for w in range(10)) == 3 and Cmat[c][v] == 1 for c in range(15)), ("not minimal", a, v)
    w = wit[a]
    assert w in G, ("bad witness", a, w)
    assert all(w[v] <= a[v] for v in range(10)), ("no domination", a, w)
print("CERTIFICATE OK: 562/562 minimals feasible, minimal, dominated by genuine I^2 gens; 0 failures.")
# C5 monomial data
cyc = (1, 2, 4, 6, 9)
a = [1 if v in set(cyc) else 0 for v in range(10)]
sums = sorted(sum(Cmat[c][v]*a[v] for v in range(10)) for c in range(15))
print("C5 cover sums:", sums, "min:", min(sums), "deg:", sum(a))
json.dump({'cycle': list(cyc), 'exponent': a, 'cover_sums_sorted': sums},
          open('c5_monomial.json', 'w'))
# six-cover data for LP dual certificate
six = sorted([sorted(v for v in range(10) if (m >> v) & 1) for m in covers if bin(m).count('1') == 6])
json.dump({'six_covers': six}, open('covers6.json', 'w'))
print("six covers:", six)
inc = [sum(1 for S in six if v in S) for v in range(10)]
print("incidence per vertex:", inc)
print("sizes of all minimal covers:", sorted([bin(m).count('1') for m in covers]))
