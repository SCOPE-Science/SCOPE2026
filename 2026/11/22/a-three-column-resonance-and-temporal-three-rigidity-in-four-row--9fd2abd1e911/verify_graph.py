#!/usr/bin/env python3
"""Exact finite-state certificate for period-three Toom dynamics on four-row tori.

Uses standard-library integer operations and Kosaraju strongly connected components.
The theorem covers all horizontal circumferences, not just those enumerated here.
"""
from collections import Counter
from hashlib import sha256

H, K, N = 4, 16, 16**3

def majority(a, b, c):
    return (a & b) | (a & c) | (b & c)

def column_update(u, v):
    # The second bit at row r of the same column comes from its north neighbor.
    # The four-bit rotation below puts old bit r+1 at new bit r.
    north = (u >> 1) | ((u & 1) << 3)
    return majority(u, north, v)

def next2(a, b, c):
    return column_update(column_update(a, b), column_update(b, c))

def next3(a, b, c, d):
    return column_update(next2(a, b, c), next2(b, c, d))

def encode(a, b, c):
    return (a << 8) | (b << 4) | c

def decode(p):
    return p >> 8, (p >> 4) & 15, p & 15

out = [[] for _ in range(N)]
rev = [[] for _ in range(N)]
edge_hash = sha256()
for a in range(K):
    for b in range(K):
        for c in range(K):
            p = encode(a, b, c)
            for d in range(K):
                if next3(a, b, c, d) == a:
                    q = encode(b, c, d)
                    out[p].append(q)
                    rev[q].append(p)
                    edge_hash.update(f'{p}:{q}\n'.encode('ascii'))
assert sum(map(len, out)) == 10824

# Postorder by iterative depth-first search.
seen = bytearray(N)
order = []
for start in range(N):
    if seen[start]:
        continue
    seen[start] = 1
    stack = [(start, 0)]
    while stack:
        p, i = stack[-1]
        if i == len(out[p]):
            order.append(p)
            stack.pop()
        else:
            stack[-1] = (p, i + 1)
            q = out[p][i]
            if not seen[q]:
                seen[q] = 1
                stack.append((q, 0))

# Reverse traversal yields strongly connected components exactly.
comp = [-1] * N
components = []
for root in reversed(order):
    if comp[root] != -1:
        continue
    j = len(components)
    comp[root] = j
    component = []
    stack = [root]
    while stack:
        p = stack.pop()
        component.append(p)
        for q in rev[p]:
            if comp[q] == -1:
                comp[q] = j
                stack.append(q)
    components.append(component)

cyclic = []
for j, C in enumerate(components):
    if len(C) > 1 or any(p in out[p] for p in C):
        cyclic.append((j, C))
assert sorted(map(lambda t: len(t[1]), cyclic)) == [1, 1, 3, 3, 8, 136]

# Critical structural verification: every cyclic component other than the
# two isolated directed 3-cycles carries only one-step-fixed column pairs.
nonfixed = []
for j, C in cyclic:
    internal = [(p, q) for p in C for q in out[p] if comp[q] == j]
    bad = [p for p in C if column_update(*decode(p)[:2]) != decode(p)[0]]
    if bad:
        nonfixed.append(C)
        assert len(C) == 3 and len(internal) == 3
        assert Counter(p for p, q in internal) == Counter(C)
        assert Counter(q for p, q in internal) == Counter(C)
    else:
        assert all(column_update(*decode(p)[:2]) == decode(p)[0] for p in C)
assert len(nonfixed) == 2

# The unordered columns of the two 3-components are the two orientations
# of 2:1 mixtures of the alternating vertical words 5 and 10.
signatures = sorted(tuple(sorted(tuple(decode(p)) for p in C)) for C in nonfixed)
expected = sorted([
    tuple(sorted(((5, 5, 10), (5, 10, 5), (10, 5, 5)))),
    tuple(sorted(((5, 10, 10), (10, 10, 5), (10, 5, 10)))),
])
assert signatures == expected

# Explicit temporal orbit test on each representative of the two classes.
def global_update(cols):
    return tuple(column_update(cols[i], cols[(i + 1) % len(cols)])
                 for i in range(len(cols)))
for seed in ((5, 5, 10), (5, 10, 10)):
    x = seed
    temporal = set()
    for _ in range(3):
        assert x not in temporal
        temporal.add(x)
        x = global_update(x)
    assert x == seed
assert len(set().union(*map(set, signatures))) == 6

print('period-three transfer graph: vertices =', N,
      ', edges =', sum(map(len, out)))
print('SHA256 of sorted (source:target) edge stream:', edge_hash.hexdigest())
print('all nontrivial cyclic SCC sizes:', sorted((len(C) for _, C in cyclic), reverse=True))
print('non-one-step-fixed cyclic SCCs:', len(nonfixed), 'each a simple directed 3-cycle')
print('their column triples:', signatures)
print('CONCLUSION: two least-temporal-period-three orbits iff 3 divides circumference; otherwise zero.')
print('CHECKS PASSED')
