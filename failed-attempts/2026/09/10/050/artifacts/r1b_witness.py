"""Corroborating structural fact: D4(3) contains explicit Theta_{4,4,4} with BOTH
endpoints in L (162 such pairs found in R1). Extract one explicit witness:
endpoints + three pairwise internally-disjoint length-4 paths, all vertices
pairwise consistent with the D4(3) adjacency. This proves the only explicit
published algebraic candidate family is NOT fully F-free, so audit Step 3
(fix an F-free A_n) has no ready witness; the true VW graph is existence-only
(journal, no explicit adjacency usable in the hour).
stdlib only; writes r1b_witness.json.
"""
import itertools
import json
from r1_D4_freeness import build_D4, len4_paths

q = 3
adj, nP, nL = build_D4(q)
N = nP + nL

found = None
for i in range(nP, N):
    for j in range(i + 1, N):
        paths = len4_paths(adj, i, j)
        if len(paths) < 3:
            continue
        for combo in itertools.combinations(range(len(paths)), 3):
            used = set()
            ok = True
            for idx in combo:
                internal = set(paths[idx][1:-1])
                if internal & used:
                    ok = False
                    break
                used |= internal
            if ok:
                found = {
                    "endpoints": (i, j),
                    "paths": [list(paths[k]) for k in combo],
                }
                break
        if found:
            break
    if found:
        break

assert found is not None
# verify against adjacency
for p in found["paths"]:
    assert p[0] == found["endpoints"][0] and p[-1] == found["endpoints"][1]
    assert len(set(p)) == 5
    for a, b in zip(p, p[1:]):
        assert b in adj[a], (a, b)
internals = [set(p[1:-1]) for p in found["paths"]]
for a in range(3):
    for b in range(a + 1, 3):
        assert not (internals[a] & internals[b])
found["verified"] = True
print(json.dumps(found, indent=2))
with open("r1b_witness.json", "w") as f:
    json.dump(found, f, indent=2)
print("wrote r1b_witness.json")
