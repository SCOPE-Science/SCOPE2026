"""Enumerate unlabeled posets n=0..6.
Universe: naturally labeled posets = upper-triangular transitive masks (every iso class
contains one, via any linear extension). Isomorphism key: min over S_n of the FULL n*n
relation bitmask (relabeled posets need not be naturally labeled, so the key must use
the full relation). Numpy-vectorized with uint64 keys.
Writes posets.json: [{n, idx, le (reflexive comparability rows), canon}] + counts.
"""
import itertools, json
import numpy as np

def trans_masks(n):
    if n == 0:
        return np.zeros(1, dtype=np.uint32)
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    K = len(pairs)
    pidx = {p: k for k, p in enumerate(pairs)}
    M = np.arange(1 << K, dtype=np.uint32)
    ok = np.ones(len(M), dtype=bool)
    for i in range(n):
        for j in range(i + 1, n):
            for l in range(j + 1, n):
                a, b, c = pidx[(i, j)], pidx[(j, l)], pidx[(i, l)]
                bad = (((M >> np.uint32(a)) & np.uint32(1)) &
                       ((M >> np.uint32(b)) & np.uint32(1)) &
                       (~(M >> np.uint32(c)) & np.uint32(1))).astype(bool)
                ok &= ~bad
    return M[ok]

def full_keys(T, n):
    """Full-relation bitmask F (bit i*n+j) for each upper-triangular mask."""
    N = len(T)
    F = np.zeros(N, dtype=np.uint64)
    for i in range(n):
        F |= np.uint64(1) << np.uint64(i * n + i)
    for i in range(n):
        for j in range(i + 1, n):
            b = (j - i - 1) + sum(n - 1 - r for r in range(i))  # index of (i,j) in pairs order
            F |= ((T.astype(np.uint64) >> np.uint64(b)) & np.uint64(1)) << np.uint64(i * n + j)
    return F

def canonical(T, n):
    F = full_keys(T, n)
    best = np.full(len(T), np.uint64(0xFFFFFFFFFFFFFFFF), dtype=np.uint64)
    for s in itertools.permutations(range(n)):
        inv = np.array([s.index(a) for a in range(n)])  # inv[a] = s^{-1}(a)
        P = np.zeros(len(T), dtype=np.uint64)
        for a in range(n):
            for b in range(n):
                old = inv[a] * n + inv[b]
                P |= ((F >> np.uint64(old)) & np.uint64(1)) << np.uint64(a * n + b)
        if np.any(P < best):
            best = np.minimum(best, P)
    return best

def le_rows(n, mask):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    le = [1 << i for i in range(n)]
    for k, (i, j) in enumerate(pairs):
        if (mask >> k) & 1:
            le[i] |= (1 << j)
    return le

out, counts = [], {}
for n in range(0, 7):
    T = trans_masks(n)
    C = canonical(T, n)
    order = np.argsort(C, kind="stable")
    T, C = T[order], C[order]
    _, first = np.unique(C, return_index=True)
    reps = np.sort(first)
    U = T[reps]
    counts[n] = len(U)
    for t, m in enumerate(U):
        out.append({"n": n, "idx": t, "le": le_rows(n, int(m)), "canon": int(m)})
print("counts:", counts)
assert counts == {0: 1, 1: 1, 2: 2, 3: 5, 4: 16, 5: 63, 6: 318}, counts
with open("posets.json", "w") as f:
    json.dump({"counts": {str(k): v for k, v in counts.items()}, "types": out}, f)
print("wrote posets.json with", len(out), "types")
