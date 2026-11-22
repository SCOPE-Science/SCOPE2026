"""Exhaustive identifying-code exchange census for the 5 by 5 rook graph.
Uses combinations, row/column detector signatures, set-based exchange search.
Python 3.10+; run: python verify_py.py
"""
from collections import Counter, deque
from itertools import combinations

N = 5
EDGES = N*N
K = 7

def identifying(selection):
    # Signature coordinates are the actual board squares in the input set.
    row = [0]*N
    col = [0]*N
    for a, b in selection:
        index = N*a+b
        row[a] |= 1<<index
        col[b] |= 1<<index
    signatures = {row[a] | col[b] for a in range(N) for b in range(N)}
    return len(signatures) == EDGES and 0 not in signatures

optima = set()
for cells in combinations(range(EDGES), K):
    selected = [divmod(e,N) for e in cells]
    if identifying(selected):
        optima.add(sum(1<<e for e in cells))
assert len(optima) == 7200, len(optima)

neighbors = {}
for state in optima:
    selected = [j for j in range(EDGES) if state & (1<<j)]
    vacant = [j for j in range(EDGES) if not state & (1<<j)]
    neigh = set()
    for x in selected:
        reduced = state ^ (1<<x)
        for y in vacant:
            proposed = reduced | (1<<y)
            if proposed in optima:
                neigh.add(proposed)
    assert len(neigh) == 14, (state, len(neigh))
    neighbors[state] = neigh
assert sum(map(len, neighbors.values()))//2 == 50400

first = min(optima)
distance = {first:0}
queue=deque([first])
while queue:
    u=queue.popleft()
    for v in neighbors[u]:
        if v not in distance:
            distance[v] = distance[u] + 1
            queue.append(v)
assert len(distance) == len(optima)
shells = tuple(Counter(distance.values())[t] for t in range(max(distance.values())+1))
assert shells == (1,14,81,208,504,1024,1696,2184,1352,136), shells
assert max(distance.values()) == 9
print('PASS optima=7200 k=7 degree=14 edges=50400 connected=1 diameter=9')
print('shells',shells)
