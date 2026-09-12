"""Exhaustive 11-colouring via maximal-matching set cover (branch and bound).
Finds an explicit 11-partition of each cyclic STS(19)."""
import sys, time

A = [
    ((0, 1, 4), (0, 2, 9), (0, 5, 11)),
    ((0, 1, 4), (0, 2, 12), (0, 5, 13)),
    ((0, 1, 8), (0, 2, 5), (0, 4, 10)),
    ((0, 1, 8), (0, 2, 5), (0, 4, 13)),
]
V = 19
which = int(sys.argv[1]) if len(sys.argv) > 1 else 0
K = int(sys.argv[2]) if len(sys.argv) > 2 else 11


def develop(fam):
    blocks = set()
    for t in fam:
        for s in range(V):
            blocks.add(frozenset((x + s) % V for x in t))
    return sorted(blocks)


blocks = develop(A[which])
m = len(blocks)
bsets = [set(b) for b in blocks]

mm = []


def rec(chosen, usedpts, cand):
    if not cand:
        mm.append(tuple(chosen))
        return
    v = cand[0]
    rest = cand[1:]
    bv = bsets[v]
    rec(chosen + [v], usedpts | bv, [u for u in rest if not (bsets[u] & bv)])
    rec(chosen, usedpts, rest)


rec([], set(), list(range(m)))
print(f"A{which+1}: maximal matchings={len(mm)}", flush=True)
# index: matchings containing block i
contain = [[] for _ in range(m)]
for mi, mt in enumerate(mm):
    for i in mt:
        contain[i].append(mi)
for i in range(m):
    contain[i].sort(key=lambda mi: -len(mm[mi]))

from functools import lru_cache
sys.setrecursionlimit(10000)
t0 = time.time()
nodes = [0]
TIME = 240


def cover(remaining, depth, chosen):
    nodes[0] += 1
    if nodes[0] % 200000 == 0:
        print(f"  depth={depth} rem={len(remaining)} nodes={nodes[0]} t={time.time()-t0:.0f}", flush=True)
    if not remaining:
        return list(chosen)
    if depth == K or time.time() - t0 > TIME:
        return None
    # lower bound: remaining blocks / max matching size 6
    import math
    if depth + math.ceil(len(remaining) / 6) > K:
        return None
    # pick uncovered block with fewest covering options (restricted to remaining)
    rem = set(remaining)
    v = min(remaining, key=lambda i: sum(1 for mi in contain[i] if set(mm[mi]) <= rem))
    for mi in contain[v]:
        s = set(mm[mi])
        if s <= rem:
            r = chosen + [mi]
            out = cover(remaining - s, depth + 1, r)
            if out is not None:
                return out
    return None


sol = cover(set(range(m)), 0, [])
print(f"nodes={nodes[0]} t={time.time()-t0:.1f} solved={sol is not None}", flush=True)
if sol is not None:
    with open(f"partition11_A{which+1}.txt", "w") as fh:
        for ci, mi in enumerate(sol):
            fh.write(f"class {ci} ({len(mm[mi])} blocks):\n")
            for i in sorted(mm[mi]):
                fh.write("  " + repr(sorted(blocks[i])) + "\n")
    # verify
    seen = set()
    for mi in sol:
        pts = set()
        for i in mm[mi]:
            assert not (set(blocks[i]) & pts)
            pts |= set(blocks[i])
            assert i not in seen
            seen.add(i)
    assert len(seen) == 57
    print("VERIFIED 11-partition")
