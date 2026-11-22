#!/usr/bin/env python3
"""Independent finite-state certificate verifier for Roman domination of P(n,2).
Requires Python 3 standard library only. Run from this file's directory.
"""
from itertools import product
from pathlib import Path

DIGITS = tuple(product(range(9), repeat=4))
assert len(DIGITS) == 6561
P = [int(x) for x in (Path(__file__).parent / 'potential.txt').read_text().split()]
assert len(P) == len(DIGITS)
assert min(P) == -26 and max(P) == 0

def outer(d): return d // 3
def inner(d): return d % 3

adj = [[] for _ in DIGITS]
rev = [[] for _ in DIGITS]
edge_count = 0
tight_count = 0
for i, (a, b, c, d) in enumerate(DIGITS):
    for e in range(9):
        v, u = outer(c), inner(c)
        if v == 0 and not (outer(b) == 2 or outer(d) == 2 or u == 2):
            continue
        if u == 0 and not (inner(a) == 2 or inner(e) == 2 or v == 2):
            continue
        j = ((i % 729) * 9) + e
        reduced = 7 * (v + u) - 8 + P[i] - P[j]
        assert reduced >= 0, (i, j, reduced)
        edge_count += 1
        if reduced == 0:
            tight_count += 1
            adj[i].append(j)
            rev[j].append(i)
assert edge_count == 48681, edge_count
assert tight_count == 6099, tight_count

# Kosaraju iterative SCC decomposition on the directed tight subgraph.
seen = [False] * 6561
order = []
for root in range(6561):
    if seen[root]:
        continue
    seen[root] = True
    dfs = [(root, 0)]
    while dfs:
        u, k = dfs[-1]
        if k == len(adj[u]):
            order.append(u)
            dfs.pop()
        else:
            dfs[-1] = (u, k + 1)
            w = adj[u][k]
            if not seen[w]:
                seen[w] = True
                dfs.append((w, 0))
seen = [False] * 6561
cycles = []
for root in reversed(order):
    if seen[root]:
        continue
    comp = []
    stack = [root]
    seen[root] = True
    while stack:
        u = stack.pop()
        comp.append(u)
        for w in rev[u]:
            if not seen[w]:
                seen[w] = True
                stack.append(w)
    if len(comp) > 1 or any(x in adj[x] for x in comp):
        cycles.append(comp)
assert len(cycles) == 1 and len(cycles[0]) == 7, list(map(len, cycles))
cyclic = set(cycles[0])
for x in cyclic:
    assert sum(w in cyclic for w in adj[x]) == 1
    assert sum(w in cyclic for w in rev[x]) == 1

# Independently witness admissibility and exact seven periods.
word = ((0,2),(0,2),(1,0),(0,0),(2,0),(0,0),(1,0))
assert sum(sum(row) for row in word) == 8
assert len(set(word[i:] + word[:i] for i in range(7))) == 7
for m in (1, 2, 3, 4, 5):
    n = 7 * m
    labels = word * m
    assert sum(sum(row) for row in labels) == 8*m
    for i in range(n):
        v,u = labels[i]
        if v == 0:
            assert 2 in (labels[(i-1)%n][0],labels[(i+1)%n][0],u)
        if u == 0:
            assert 2 in (labels[(i-2)%n][1],labels[(i+2)%n][1],v)

# One abstract cycle's labels must be the designated 7-symbol word up to rotation.
cycle = next(iter(cyclic))
seen_word = []
x = cycle
for _ in range(7):
    a,b,c,d = DIGITS[x]
    seen_word.append((outer(c),inner(c)))
    x = next(y for y in adj[x] if y in cyclic)
assert x == cycle
assert tuple(seen_word) in {word[i:]+word[:i] for i in range(7)}, seen_word
print('PASS: 6561 states; 48681 admissible transitions; 6099 tight edges; single critical directed 7-cycle; seven cyclic optimal words')
