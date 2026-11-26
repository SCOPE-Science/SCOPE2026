"""Exhaustively verify the top-dimensional Petersen configuration collapse."""
from collections import deque
from itertools import combinations


def boundary(cell, edges):
    movers, stopped = cell
    return [(movers[:j] + movers[j+1:], tuple(sorted((*stopped, v))))
            for j, e in enumerate(movers) for v in edges[e]]


def main():
    labels = [set(a) for a in combinations(range(5), 2)]
    originals = [(a,b) for a,b in combinations(range(10), 2)
                 if not labels[a] & labels[b]]
    assert len(originals) == 15
    adj = [{b if a == v else a for a,b in originals if v in (a,b)}
           for v in range(10)]
    assert all(len(a) == 3 for a in adj)
    assert all(not adj[a] & adj[b] for a,b in originals)
    assert all(len(adj[a] & adj[b]) <= 1 for a,b in combinations(range(10), 2))
    for k in range(3):
        for deleted in combinations(range(10), k):
            allowed = set(range(10)) - set(deleted)
            seen = {min(allowed)}
            while True:
                bigger = seen | (set.union(*(adj[a] for a in seen)) & allowed)
                if bigger == seen:
                    break
                seen = bigger
            assert seen == allowed
    print('Petersen graph: cubic, 3-vertex-connected, no cycles of length 3 or 4')

    edges = [(v,10+i) for i,e in enumerate(originals) for v in e]
    cells = [[] for _ in range(4)]
    for k in range(4):
        for moving in combinations(range(30), k):
            occupied = {v for e in moving for v in edges[e]}
            if len(occupied) == 2*k:
                avail = sorted(set(range(25)) - occupied)
                cells[k].extend((moving, stopped) for stopped in combinations(avail, 3-k))
    counts = tuple(map(len, cells))
    assert counts == (2300, 7590, 8190, 2880)
    print('Initial cell counts:', counts)
    assert all(len(a) == len(set(a)) for a in cells)
    index = [{c:i for i,c in enumerate(a)} for a in cells]
    down = [[], *[[[index[k-1][b] for b in boundary(c, edges)] for c in cells[k]]
                  for k in range(1,4)]]
    assert all(len(a) == len(set(a)) == 2*k
               for k in range(1,4) for a in down[k])
    stars = [set() for c in cells[2]]
    for j, faces in enumerate(down[3]):
        for i in faces:
            stars[i].add(j)
    free = deque(i for i,s in enumerate(stars) if len(s) == 1)
    active2 = set(range(counts[2]))
    active3 = set(range(counts[3]))
    while free:
        i = free.popleft()
        if i not in active2 or len(stars[i]) != 1:
            continue
        j = next(iter(stars[i]))
        assert j in active3 and i in down[3][j]
        active2.remove(i)
        active3.remove(j)
        for f in down[3][j]:
            stars[f].remove(j)
            if len(stars[f]) == 1:
                free.append(f)
    assert not active3 and all(not s for s in stars)
    assert len(active2) == counts[2] - counts[3]
    print('Free (2,3) pairs:', counts[3])
    print('Spine cell counts:', (*counts[:2], len(active2), 0))

    incident = [[] for c in cells[0]]
    for u,v in down[1]:
        incident[u].append(v)
        incident[v].append(u)
    frontier = [0]
    visited = {0}
    while frontier:
        for v in incident[frontier.pop()]:
            if v not in visited:
                visited.add(v)
                frontier.append(v)
    assert len(visited) == counts[0]
    chi = counts[0] - counts[1] + len(active2)
    assert chi == 20
    print('Connected 1-skeleton; Euler characteristic:', chi)


if __name__ == '__main__':
    main()
