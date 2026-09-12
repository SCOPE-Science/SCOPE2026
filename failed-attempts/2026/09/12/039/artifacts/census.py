"""Greedy K-partition + maximal-matching census for each cyclic STS(19)."""
import sys

A = [
    ((0, 1, 4), (0, 2, 9), (0, 5, 11)),
    ((0, 1, 4), (0, 2, 12), (0, 5, 13)),
    ((0, 1, 8), (0, 2, 5), (0, 4, 10)),
    ((0, 1, 8), (0, 2, 5), (0, 4, 13)),
]
V = 19


def develop(fam):
    blocks = set()
    for t in fam:
        for s in range(V):
            blocks.add(frozenset((x + s) % V for x in t))
    return sorted(blocks)


def greedy(blocks, K):
    m = len(blocks)
    adj = [set() for _ in range(m)]
    for i in range(m):
        for j in range(i + 1, m):
            if blocks[i] & blocks[j]:
                adj[i].add(j)
                adj[j].add(i)
    order = sorted(range(m), key=lambda i: -len(adj[i]))
    color = [-1] * m
    for v in order:
        used = {color[j] for j in adj[v] if color[j] >= 0}
        for c in range(K):
            if c not in used:
                color[v] = c
                break
        if color[v] < 0:
            return None
    return color


def enum_maximal_matchings(blocks):
    """Backtracking enumeration of all maximal matchings (as block-index tuples)."""
    m = len(blocks)
    pt2blocks = {}
    for i, b in enumerate(blocks):
        for x in b:
            pt2blocks.setdefault(x, []).append(i)
    res = []

    def rec(chosen, usedpts, cand):
        # cand: blocks disjoint from usedpts
        if not cand:
            res.append(tuple(chosen))
            return
        # branch: take first candidate or exclude it
        v = cand[0]
        rest = cand[1:]
        # include v
        bv = blocks[v]
        rest2 = [u for u in rest if not (blocks[u] & bv)]
        rec(chosen + [v], usedpts | set(bv), rest2)
        # exclude v: only if v still has a disjoint partner available later or
        # v conflicts... standard maximal enumeration: exclude v, continue
        rec(chosen, usedpts, rest)

    rec([], set(), list(range(m)))
    return res


for w in range(4):
    blocks = develop(A[w])
    c11 = greedy(blocks, 11)
    print(f"A{w+1}: greedy-11 {'OK' if c11 else 'FAIL'}", flush=True)
    t0 = __import__("time").time()
    mm = enum_maximal_matchings(blocks)
    from collections import Counter
    print(f"A{w+1}: maximal matchings={len(mm)} sizes={sorted(Counter(len(x) for x in mm).items())} t={__import__('time').time()-t0:.1f}s", flush=True)
