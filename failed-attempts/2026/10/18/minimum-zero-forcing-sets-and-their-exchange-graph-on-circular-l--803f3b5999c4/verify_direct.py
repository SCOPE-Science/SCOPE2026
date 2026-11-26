"""Exhaustive ordinary zero-forcing verification for small circular ladders.

Run: python3 verify_direct.py
Only the Python standard library is needed.
"""
from collections import Counter, deque
from hashlib import sha256
from itertools import combinations
import json


def actual_forcing(n, seed):
    neighbours = []
    for row in (0, 1):
        for i in range(n):
            neighbours.append((row*n+(i-1)%n, row*n+(i+1)%n, (1-row)*n+i))
    black = set(seed)
    while True:
        additions = set()
        for vertex in tuple(black):
            remaining = [w for w in neighbours[vertex] if w not in black]
            if len(remaining) == 1:
                additions.add(remaining[0])
        if not additions:
            return len(black) == 2*n
        black.update(additions)


def patterns(n):
    out = set()
    for a in (0, 1):
        b = 1-a
        for i in range(n):
            u = lambda x: a*n+(x%n)
            v = lambda x: b*n+(x%n)
            out.add(frozenset(u(i+j) for j in range(4)))
            for x, y in ((1,2),(-1,-2),(1,-2),(-1,2)):
                out.add(frozenset((v(i),u(i),u(i+x),u(i+y))))
    for i in range(n):
        for delta in (-1,0,1):
            out.add(frozenset((i,(i+1)%n,n+(i+delta)%n,n+(i+delta+1)%n)))
    return out


def verify(n):
    universe = range(2*n)
    assert all(not actual_forcing(n,s) for s in combinations(universe,3))
    forcing = {frozenset(s) for s in combinations(universe,4) if actual_forcing(n,s)}
    expected = patterns(n)
    assert forcing == expected, ('template discrepancy',n,forcing^expected)
    nodes = sorted(tuple(sorted(s)) for s in forcing)
    digest=sha256(json.dumps(nodes,separators=(',',':')).encode()).hexdigest()
    degree=Counter()
    adjacency = {}
    for s in forcing:
        neighbors = set()
        for outgoing in s:
            for incoming in universe:
                if incoming not in s:
                    t = frozenset((s - {outgoing}) | {incoming})
                    if t in forcing:
                        neighbors.add(t)
        adjacency[s] = neighbors
        degree[len(neighbors)]+=1
    assert all(s in adjacency[t] for s,adj in adjacency.items() for t in adj)
    start=next(iter(forcing))
    visited={start}
    stack=[start]
    for s in stack:
        for t in adjacency[s]:
            if t not in visited:
                visited.add(t)
                stack.append(t)
    assert len(visited)==len(forcing)
    if n>=6:
        assert len(forcing)==13*n
        assert dict(degree)=={5:4*n,8:8*n,12:n}
        assert sum(deg*count for deg,count in degree.items())//2==48*n
    return dict(n=n, minimum=4, state_count=len(forcing), edge_count=sum(deg*cnt for deg,cnt in degree.items())//2,
                degree_distribution={str(k):degree[k] for k in sorted(degree)},components=1,states_sha256=digest)


if __name__=='__main__':
    results=[verify(n) for n in range(5,14)]
    print(json.dumps(results,indent=2,sort_keys=True))
