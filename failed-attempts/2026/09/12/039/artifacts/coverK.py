"""Exhaustive UNSAT for 10-partition via maximal-matching set cover + symmetry breaking.
Fix: first class = canonical max matching containing block 0 (try each orbit rep);
then branch-and-bound cover of the rest in 9 classes. Also used for 11-cover of A4."""
import sys, time, math

A = [
    ((0, 1, 4), (0, 2, 9), (0, 5, 11)),
    ((0, 1, 4), (0, 2, 12), (0, 5, 13)),
    ((0, 1, 8), (0, 2, 5), (0, 4, 10)),
    ((0, 1, 8), (0, 2, 5), (0, 4, 13)),
]
V = 19
which = int(sys.argv[1]) if len(sys.argv) > 1 else 0
K = int(sys.argv[2]) if len(sys.argv) > 2 else 10
TIME = float(sys.argv[3]) if len(sys.argv) > 3 else 1500


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
contain = [[] for _ in range(m)]
for mi, mt in enumerate(mm):
    for i in mt:
        contain[i].append(mi)
for i in range(m):
    contain[i].sort(key=lambda mi: -len(mm[mi]))

sys.setrecursionlimit(10000)
t0 = time.time()
nodes = [0]
timed_out = [False]


def cover(remaining, depth, Kloc):
    nodes[0] += 1
    if not remaining:
        return []
    if depth == Kloc:
        return None
    if time.time() - t0 > TIME:
        timed_out[0] = True
        return None
    if depth + math.ceil(len(remaining) / 6) > Kloc:
        return None
    rem = set(remaining)
    v = min(remaining, key=lambda i: sum(1 for mi in contain[i] if set(mm[mi]) <= rem))
    for mi in contain[v]:
        s = set(mm[mi])
        if s <= rem:
            out = cover(remaining - s, depth + 1, Kloc)
            if timed_out[0]:
                return None
            if out is not None:
                return [mi] + out
    return None


# symmetry break: first class must be a maximal matching containing block 0,
# considered up to stabilizer of block 0 — here just dedupe by sorted block-tuple
# under the cyclic group action on matchings (cheap canonical filter).
def cyc_canon(mt):
    imgs = []
    for s in range(V):
        imgs.append(tuple(sorted(tuple(sorted((x + s) % V for x in blocks[i])) for i in mt)))
    return min(imgs)


seen = set()
firsts = []
for mi in contain[0]:
    c = cyc_canon(mm[mi])
    if c not in seen:
        seen.add(c)
        firsts.append(mi)
print(f"distinct first classes (cyc-canonical): {len(firsts)}", flush=True)

full = set(range(m))
sols = []
for fi, mi in enumerate(firsts):
    s = set(mm[mi])
    out = cover(full - s, 1, K)
    if timed_out[0]:
        print(f"TIMEOUT after first {fi+1}/{len(firsts)} nodes={nodes[0]}", flush=True)
        break
    if out is not None:
        sols = [mi] + out
        print(f"SOLUTION with first {fi+1}/{len(firsts)} nodes={nodes[0]}", flush=True)
        break
    if (fi + 1) % 20 == 0:
        print(f"  tried {fi+1}/{len(firsts)} nodes={nodes[0]} t={time.time()-t0:.0f}", flush=True)
print(f"done t={time.time()-t0:.1f} nodes={nodes[0]} solved={bool(sols)} timeout={timed_out[0]}", flush=True)
if sols:
    with open(f"partition{K}_A{which+1}.txt", "w") as fh:
        for ci, mi in enumerate(sols):
            fh.write(f"class {ci} ({len(mm[mi])} blocks):\n")
            for i in sorted(mm[mi]):
                fh.write("  " + repr(sorted(blocks[i])) + "\n")
    seen2 = set()
    for mi in sols:
        pts = set()
        for i in mm[mi]:
            assert not (set(blocks[i]) & pts)
            pts |= set(blocks[i])
            assert i not in seen2
            seen2.add(i)
    assert len(seen2) == 57
    print(f"VERIFIED {K}-partition")
else:
    if not timed_out[0]:
        print(f"CERTIFIED: no {K}-partition (exhaustive, symmetry-broken)")
