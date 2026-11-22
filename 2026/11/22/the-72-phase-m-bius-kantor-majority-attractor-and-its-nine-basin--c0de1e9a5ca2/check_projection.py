#!/usr/bin/env python3
"""Exact two-shore majority projection for the Möbius–Kantor incidence graph."""
from collections import Counter
from itertools import product

N = 8
adj = [set() for _ in range(16)]
for i in range(N):
    for a, b in ((i, (i + 1) % N), (i, i + N), (i + N, (i + 3) % N + N)):
        adj[a].add(b)
        adj[b].add(a)
assert len({(min(i,j), max(i,j)) for i in range(16) for j in adj[i]}) == 24
assert all(len(a) == 3 for a in adj)
U = [0, 2, 4, 6, 9, 11, 13, 15]
V = [1, 3, 5, 7, 8, 10, 12, 14]
assert all(set(adj[i]).issubset(V) for i in U)
assert all(set(adj[i]).issubset(U) for i in V)

def morph(source, target, x):
    idx = {vertex: i for i,vertex in enumerate(source)}
    return sum((sum((x >> idx[j]) & 1 for j in adj[i]) >= 2) << k
               for k, i in enumerate(target))

h = [morph(U, V, x) for x in range(256)]
g = [morph(V, U, x) for x in range(256)]
P = [g[h[x]] for x in range(256)]
Q = [h[g[x]] for x in range(256)]
P2 = [P[P[x]] for x in range(256)]
Q2 = [Q[Q[x]] for x in range(256)]
assert len(set(h)) == len(set(g)) == 136
assert len(set(P)) == len(set(Q)) == 88
assert len(set(P2)) == len(set(Q2)) == 72
assert all(P[P2[x]] == P2[x] and Q[Q2[x]] == Q2[x] for x in range(256))
assert all(P[P[g[x]]] == P[g[x]] and Q[Q[h[x]]] == Q[h[x]] for x in range(256))
assert any(P[x] != P2[x] for x in range(256))
assert sum(P[x] == x for x in range(256)) == 72
assert sum(Q[x] == x for x in range(256)) == 72
R = Counter(P2)
S = Counter(Q2)
assert Counter(R.values()) == Counter({1:22, 2:48, 69:2})
assert Counter(S.values()) == Counter({1:22, 2:48, 69:2})
assert len({h[u] for u in R}) == 72
assert all(g[h[u]] == u and R[u] == S[h[u]] for u in R)

C = Counter()
for u, v in product(R, S):
    other = (g[v], h[u])
    assert other[0] in R and other[1] in S
    assert (g[other[1]], h[other[0]]) == (u, v)
    if (u, v) > other:
        continue
    if (u, v) == other:
        C['fixed', R[u]*S[v]] += 1
    else:
        C['period_two',R[u]*S[v]+R[other[0]]*S[other[1]]] += 1
expected = {
    ('fixed',1):22, ('fixed',4):48, ('fixed',4761):2,
    ('period_two',2):231, ('period_two',4):1056,
    ('period_two',8):1128, ('period_two',138):44,
    ('period_two',276):96, ('period_two',9522):1,
}
assert C == Counter(expected), (C, Counter(expected))
assert sum(k[1]*n for k,n in C.items()) == 65536
assert sum(n for (kind,s),n in C.items() if kind=='fixed')==72
assert sum(n for (kind,s),n in C.items() if kind=='period_two')==2556

def step(a):
    u,v=a
    return (g[v],h[u])
def is_periodic(a):
    return step(step(a)) == a
entry = Counter()
for a in product(range(256),repeat=2):
    p = a
    for t in range(4):
        if is_periodic(p):
            entry[t] += 1
            break
        p = step(p)
    else:
        raise AssertionError((a,p))
assert entry == Counter({0:5184,1:15552,2:22528,3:22272})
print('PROJECTION_CERTIFICATE_OK')
print('one_shore_image_136 fixed_P_72 fiber_spectrum',sorted(Counter(R.values()).items()))
print('basin_classes',sorted(C.items()))
print('entry_times',sorted(entry.items()))
