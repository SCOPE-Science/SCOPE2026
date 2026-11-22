#!/usr/bin/env python3
"""Finite exact checks for two-independence on a cycle with one pendant vertex.

The all-parameter theorem is proved separately; this verifier is a finite check.
Only Python's standard library is required.
"""
from collections import Counter, deque
from itertools import combinations
import json


def graph(n):
    """Cycle vertices 0,..,n-1; leaf n attached to vertex 0."""
    vertices = n + 1
    neighbors = [0] * vertices
    for a, b in ([(j, (j + 1) % n) for j in range(n)] + [(0, n)]):
        neighbors[a] |= 1 << b
        neighbors[b] |= 1 << a
    return neighbors


def faces(n):
    adj = graph(n)
    N = n + 1
    forbidden = []
    for t in combinations(range(N), 3):
        a, b, c = t
        mask = (1 << a) | (1 << b) | (1 << c)
        # Connected induced triples have at least two internal edges.
        edges = ((adj[a] & mask).bit_count() + (adj[b] & mask).bit_count()
                 + (adj[c] & mask).bit_count()) // 2
        if edges >= 2:
            forbidden.append(mask)
    fs = [mask for mask in range(1 << N)
          if all(mask & t != t for t in forbidden)]
    # Independent BFS check, not using the forbidden-triple representation.
    for f in fs:
        unseen = f
        while unseen:
            seed = unseen & -unseen
            seen = seed
            fringe = seed
            while fringe:
                v = (fringe & -fringe).bit_length() - 1
                fringe &= fringe - 1
                new = adj[v] & f & ~seen
                seen |= new
                fringe |= new
            assert seen.bit_count() <= 2
            unseen &= ~seen
    return fs


def matching(fs, n):
    remaining = set(fs)
    pair = {}
    # The pendant-leaf pivot precedes the cycle pivots.
    for vertex in [n] + list(range(n)):
        v = 1 << vertex
        for lower in sorted(remaining):
            upper = lower | v
            if not lower & v and upper in remaining:
                remaining.remove(lower)
                remaining.remove(upper)
                pair[lower] = upper
    assert 0 in pair and pair[0] == 1 << n
    # Empty face is not part of the ordinary non-augmented face poset.
    pair.pop(0)
    nonempty = set(fs) - {0}
    critical = nonempty - set(pair) - set(pair.values())
    assert all((upper & lower) == lower and
               (upper.bit_count() == lower.bit_count() + 1) for lower, upper in pair.items())
    assert all(x in nonempty for x in pair for x in (x, pair[x]))
    assert len(nonempty) == 2 * len(pair) + len(critical)
    return pair, critical


def check_acyclic(fs, pair):
    nonempty = set(fs) - {0}
    indegree = {f: 0 for f in nonempty}
    arrows = {f: [] for f in nonempty}
    covers = 0
    for top in nonempty:
        vbits = top
        while vbits:
            bit = vbits & -vbits
            vbits ^= bit
            low = top ^ bit
            if low == 0:
                continue
            covers += 1
            if pair.get(low) == top:
                a, b = low, top
            else:
                a, b = top, low
            arrows[a].append(b)
            indegree[b] += 1
    queue = deque(x for x, d in indegree.items() if d == 0)
    visited = 0
    while queue:
        x = queue.popleft()
        visited += 1
        for y in arrows[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                queue.append(y)
    assert visited == len(nonempty), 'A directed cycle was found'
    return covers


def expected(n):
    k = (n + 1) // 4 if n % 4 == 3 else n // 4
    if n % 4 in (0, 3):
        return {0: 1, 2 * k - 1: 2}
    return {0: 1}


def main():
    output = []
    for n in range(3, 17):
        fs = faces(n)
        pairs, crit = matching(fs, n)
        covers = check_acyclic(fs, pairs)
        count = dict(sorted(Counter(f.bit_count() - 1 for f in crit).items()))
        assert count == expected(n), (n, count, expected(n))
        output.append({'cycle_length': n, 'faces_including_empty': len(fs),
                       'pairs_nonempty': len(pairs), 'face_poset_covers': covers,
                       'critical_cell_dimensions': {str(k): v for k, v in count.items()},
                       'acyclic': True})
    print(json.dumps({'range': [3, 16], 'checks': output}, ensure_ascii=False,
                     sort_keys=True, separators=(',', ':')))

if __name__ == '__main__':
    main()
