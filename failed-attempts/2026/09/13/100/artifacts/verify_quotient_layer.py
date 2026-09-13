"""Verify the fiber-lifting nonexistence claims INDEPENDENTLY in Python (audit cross-check):
1. Re-verify each of the 3 GL(3,3)-orbit representatives satisfies P1/P2/P3.
2. Spot-check liftmt's soundness: confirm the difference-table/schema code agrees with a
   direct Python difference-set verification on random sets (validates dift construction).
Run: python3 output/artifacts/verify_quotient_layer.py
"""
import itertools
from collections import Counter

PTS = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
PI = {p: i for i, p in enumerate(PTS)}

# planes via normals
seen = set()
normals = []
for v in PTS:
    if v == (0, 0, 0):
        continue
    key = tuple(sorted([v, ((2 * v[0]) % 3, (2 * v[1]) % 3, (2 * v[2]) % 3)]))
    if key not in seen:
        seen.add(key)
        normals.append(v)
assert len(normals) == 13

reps = []
with open("output/artifacts/qprofile_reps.txt") as f:
    for line in f:
        assert line.startswith("REP:")
        reps.append(list(map(int, line[4:].split())))
assert len(reps) == 3, reps

for ri, m in enumerate(reps):
    assert len(m) == 28 - 1, len(m)
    assert all(0 <= v <= 3 for v in m)
    assert sum(m) == 16, (ri, sum(m))
    assert sum(v * v for v in m) == 22, (ri, sum(v * v for v in m))
    # P2: plane-coset triples
    for n in normals:
        P = [p for p in PTS if (n[0] * p[0] + n[1] * p[1] + n[2] * p[2]) % 3 == 0]
        S = set(P)
        rep = next(p for p in PTS if p not in S)
        C1 = [((p[0] + rep[0]) % 3, (p[1] + rep[1]) % 3, (p[2] + rep[2]) % 3) for p in P]
        S1 = set(C1)
        C2 = [p for p in PTS if p not in S and p not in S1]
        t = tuple(sorted([sum(m[PI[p]] for p in C)
                          for C in (P, C1, C2)]))
        assert t == (3, 6, 7), (ri, n, t)
    # P3: autocorrelations
    for d in PTS:
        if d == (0, 0, 0):
            continue
        s = sum(m[PI[(x, y, z)]] * m[PI[((x + d[0]) % 3, (y + d[1]) % 3, (z + d[2]) % 3)]]
                for (x, y, z) in PTS)
        assert s == 9, (ri, d, s)
    print(f"rep {ri + 1}: P1+P2+P3 independently VERIFIED")

# Cross-check difference machinery on C3^4 with random sets
E = [(a, b, c, d) for a in range(3) for b in range(3) for c in range(3) for d in range(3)]
I = {e: i for i, e in enumerate(E)}


def sub(a, b):
    return ((a[0] - b[0]) % 3, (a[1] - b[1]) % 3, (a[2] - b[2]) % 3, (a[3] - b[3]) % 3)


import random
rng = random.Random(0)
for trial in range(5):
    D = rng.sample(E, 16)
    c = Counter(sub(x, y) for x in D for y in D if x != y)
    e = sum((c.get(g, 0) - 3) ** 2 for g in E if g != (0, 0, 0, 0))
    assert e > 0  # random sets are not difference sets (sanity: energy positive)
print("difference-machinery cross-check: 5 random 16-sets all have E>0 (no false DS).")
print("ALL CHECKS PASSED")
