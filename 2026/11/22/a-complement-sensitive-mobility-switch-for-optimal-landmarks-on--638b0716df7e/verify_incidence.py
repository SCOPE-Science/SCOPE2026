#!/usr/bin/env python3
"""Independent Clebsch graph model from incidence and disjointness of pairs of five labels."""
from itertools import combinations
from collections import Counter, deque

labels = tuple(range(5))
V = [('center',)] + [('single', i) for i in labels] + [('pair', i, j) for i, j in combinations(labels, 2)]
n = len(V)
assert n == 16

# This incidence construction does not use a binary-vector/Cayley graph representation.
def adjacent(u, v):
    if u[0] == 'center': return v[0] == 'single'
    if v[0] == 'center': return u[0] == 'single'
    if u[0] == 'single' and v[0] == 'pair': return u[1] in v[1:]
    if v[0] == 'single' and u[0] == 'pair': return v[1] in u[1:]
    if u[0] == 'pair' and v[0] == 'pair': return set(u[1:]).isdisjoint(v[1:])
    return False

A = [set(j for j in range(n) if j != i and adjacent(V[i], V[j])) for i in range(n)]
assert all(len(x) == 5 for x in A)
assert all((j in A[i]) == (i in A[j]) for i in range(n) for j in range(n))

def Dmat(graph):
    d = [[-1]*n for _ in range(n)]
    for s in range(n):
        d[s][s] = 0
        todo = deque([s])
        while todo:
            u = todo.popleft()
            for v in graph[u]:
                if d[s][v] == -1:
                    d[s][v] = d[s][u] + 1
                    todo.append(v)
    return d

D = Dmat(A)
Ac = [set(range(n)) - {i} - A[i] for i in range(n)]
Dc = Dmat(Ac)

def resolves(S, M):
    return len({tuple(M[x][y] for y in S) for x in range(n)}) == n

count_per_size = {}
for k in range(1, 5):
    count_per_size[k] = sum(resolves(S, D) for S in combinations(range(n), k))
assert count_per_size == {1:0, 2:0, 3:0, 4:80}
B = {frozenset(S) for S in combinations(range(n), 4) if resolves(S, D)}
T = {frozenset(A[c] - {p}) for c in range(n) for p in A[c]}
assert B == T and len(T) == 80
assert {frozenset(S) for S in combinations(range(n), 4) if resolves(S, Dc)} == B

E = set()
slide = set()
slide_c = set()
for b, t in combinations(sorted(B, key=lambda b:tuple(sorted(b))), 2):
    if len(b & t) == 3:
        pair = tuple(sorted((tuple(sorted(b)),tuple(sorted(t)))))
        E.add(pair)
        u = next(iter(b - t))
        v = next(iter(t - b))
        if v in A[u]: slide.add(pair)
        if v in Ac[u]: slide_c.add(pair)
assert len(E) == 160
assert len(slide) == 0
assert slide_c == E
assert all(len(A[c] & A[d]) <= 2 for c in range(n) for d in range(c+1,n))

# The 5 local 4-subsets at each center have all ten exchanges, with no cross-center exchanges.
centers = [[frozenset(A[c] - {p}) for p in A[c]] for c in range(n)]
assert len({tuple(sorted(group, key=lambda s:tuple(sorted(s)))) for group in centers}) == n
assert all(len(group)==5 and all(len(u & v) == 3 for u,v in combinations(group,2)) for group in centers)
print('incidence_graph: center + 5 singletons + 10 pairs; degree=5')
print('resolving_four_sets=80; exactly 4-of-5 open neighborhoods')
print('exchange=16*K5; base_slides=0; complement_slides=160')
print('verification=PASS')
