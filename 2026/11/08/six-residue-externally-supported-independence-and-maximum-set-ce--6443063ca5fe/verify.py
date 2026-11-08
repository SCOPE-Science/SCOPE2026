#!/usr/bin/env python3
"""Exact integer verification of ESI sets on circular ladders.

Only the Python standard library is used.  Run: python3 verify.py
"""
from collections import Counter
from itertools import product
import sys

ALPHABET = (-1, 0, 1)


def local_ok(word):
    """Seven consecutive column symbols; test the two central vertices."""
    assert len(word) == 7
    if any(word[i] == word[i + 1] != -1 for i in range(6)):
        return False
    chosen = {(i, a) for i, a in enumerate(word) if a != -1}
    for r in (0, 1):
        neighbors = ((3, 1 - r), (2, r), (4, r))
        if not any(u in chosen for u in neighbors):
            continue
        def is_exterior(v):
            j, s = v
            adjacent = ((j, 1 - s), (j - 1, s), (j + 1, s))
            return v not in chosen and not any(t in chosen for t in adjacent)
        if not any(is_exterior(u) for u in neighbors):
            return False
    return True


def essential_automaton():
    states = list(product(ALPHABET, repeat=6))
    index = {s: i for i, s in enumerate(states)}
    edges = []
    adj = [[] for _ in states]
    for s in states:
        for a in ALPHABET:
            if local_ok(s + (a,)):
                v, w = index[s], index[s[1:] + (a,)]
                edges.append((v, w, int(a != -1)))
                adj[v].append(w)
    assert len(states) == 729 and len(edges) == 429
    # Tarjan SCC; only a nontrivial component or a loop can contain a closed walk.
    sys.setrecursionlimit(5000)
    ids = [-1] * len(states)
    low = [0] * len(states)
    stack = []
    instack = [False] * len(states)
    sccs = []
    tick = 0
    def visit(v):
        nonlocal tick
        ids[v] = low[v] = tick
        tick += 1
        stack.append(v)
        instack[v] = True
        for w in adj[v]:
            if ids[w] < 0:
                visit(w)
                low[v] = min(low[v], low[w])
            elif instack[w]:
                low[v] = min(low[v], ids[w])
        if low[v] == ids[v]:
            block = set()
            while True:
                w = stack.pop()
                instack[w] = False
                block.add(w)
                if v == w:
                    break
            sccs.append(block)
    for v in range(len(states)):
        if ids[v] < 0:
            visit(v)
    cyclic = [s for s in sccs if len(s) > 1 or any(v in adj[v] for v in s)]
    assert len(cyclic) == 1 and len(cyclic[0]) == 117
    vertices = sorted(cyclic[0])
    remap = {v: i for i, v in enumerate(vertices)}
    arcs = [(remap[v], remap[w], wt) for v, w, wt in edges
            if v in remap and w in remap]
    assert len(arcs) == 241
    return [states[v] for v in vertices], arcs


def potential_and_cost_arcs(size, arcs):
    h = [0] * size
    for _ in range(size + 1):
        changed = False
        for a, b, w in arcs:
            new = h[a] + 3 * w - 2
            if h[b] < new:
                h[b] = new
                changed = True
        if not changed:
            break
    else:
        raise AssertionError('Positive-weight directed circuit')
    assert Counter(h) == {0: 57, 1: 40, 2: 20}
    costs = [(a, b, 2 - 3 * w + h[b] - h[a]) for a, b, w in arcs]
    assert min(c for _, _, c in costs) == 0
    assert Counter(c for _, _, c in costs) == {0: 144, 1: 40, 2: 57}
    return costs


def low_cost_determinant(size, edges, bound=4):
    # Exactly compute p_n(t)=tr(C(t)^n) mod t^(bound+1), 1<=n<=size.
    # All entries are arbitrary-precision Python integers, not machine words.
    a = [[[0] * size for _ in range(size)] for _ in range(bound + 1)]
    for i in range(size):
        a[0][i][i] = 1
    powers = [[0] * (bound + 1)]
    for n in range(1, size + 1):
        b = [[[0] * size for _ in range(size)] for _ in range(bound + 1)]
        for src, dst, cost in edges:
            for d in range(bound + 1 - cost):
                target = b[d + cost]
                origin = a[d]
                for start in range(size):
                    target[start][dst] += origin[start][src]
        a = b
        powers.append([sum(a[d][i][i] for i in range(size))
                       for d in range(bound + 1)])
    # Newton identities exactly determine every coefficient of det(I-x*C(t)),
    # because the determinant has degree at most size in x.
    det = [[0] * (bound + 1) for _ in range(size + 1)]
    det[0][0] = 1
    for k in range(1, size + 1):
        rhs = [0] * (bound + 1)
        for j in range(1, k + 1):
            pj = powers[j]
            prev = det[k - j]
            for d1 in range(bound + 1):
                if pj[d1]:
                    for d2 in range(bound + 1 - d1):
                        rhs[d1 + d2] += pj[d1] * prev[d2]
        for d in range(bound + 1):
            assert rhs[d] % k == 0
            det[k][d] = -rhs[d] // k
    expected = {(0, 0): 1, (6, 0): -1, (2, 1): -2,
                (1, 2): -1, (4, 2): -1, (7, 2): -1,
                (5, 4): 1}
    nonzero = {(k, d): det[k][d]
               for k in range(size + 1) for d in range(bound + 1)
               if det[k][d]}
    assert nonzero == expected, nonzero
    print('EXACT_NEWTON_DETERMINANT_OK',size, len(edges), nonzero)
    return powers


def independent_brute_histogram(n):
    # Independent implementation, directly on the 2*n-vertex graph.
    full = (1 << (2 * n)) - 1
    adj = []
    for i in range(n):
        for r in (0, 1):
            ids = (2 * i + 1 - r, 2 * ((i - 1) % n) + r,
                   2 * ((i + 1) % n) + r)
            adj.append(sum(1 << j for j in set(ids)))
    hist = Counter()
    for word in product(ALPHABET, repeat=n):
        chosen = 0
        for i, a in enumerate(word):
            if a >= 0:
                chosen |= 1 << (2 * i + a)
        touched = 0
        independent = True
        for v in range(2 * n):
            if chosen >> v & 1:
                if adj[v] & chosen:
                    independent = False
                    break
                touched |= adj[v]
        if not independent:
            continue
        exterior = full & ~(chosen | touched)
        if any((touched >> v & 1) and not (adj[v] & exterior)
               for v in range(2 * n)):
            continue
        hist[chosen.bit_count()] += 1
    return hist


def claimed_values(n):
    q, r = divmod(n, 6)
    a = (4 * q, 4 * q, 4 * q + 1, 4 * q + 1,
         4 * q + 2, 4 * q + 2)[r]
    m = (6, 2 * n, 2 * n, 2 * n * n // 3,
         n * (n + 5) // 3, n * (n - 2) * (n + 7) // 9)[r]
    return a, m


def run():
    states, edges = essential_automaton()
    costs = potential_and_cost_arcs(len(states), edges)
    powers = low_cost_determinant(len(states), costs)
    for n in range(3, 12):
        hist = independent_brute_histogram(n)
        expect_a, expect_m = claimed_values(n)
        assert max(hist) == expect_a
        assert hist[expect_a] == expect_m
        if n >= 7:
            for k, count in hist.items():
                deficit = 2 * n - 3 * k
                if 0 <= deficit <= 4:
                    assert powers[n][deficit] == count, (n, k, deficit)
        print('DIRECT_GRAPH_OK',n,'alpha',expect_a,'maximizers',expect_m,'total',sum(hist.values()))
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
