#!/usr/bin/env python3
"""Independent finite checks for the stated constrained-permutation graph."""
from collections import Counter, deque
from itertools import permutations
from math import comb

def avoid231321(p):
    return all(not (p[j] > p[i] > p[k] or p[i] > p[j] > p[k])
               for i in range(len(p)) for j in range(i + 1, len(p))
               for k in range(j + 1, len(p)))

def decode(cuts):
    n = len(cuts) + 1
    ends = [i + 1 for i, b in enumerate(cuts) if b] + [n]
    out = []
    start = 0
    for end in ends:
        out.extend([end] + list(range(start + 1, end)))
        start = end
    return tuple(out)

def neighbors_east(x):
    for i in range(len(x)):
        if i == 0 or x[i - 1] == 1:
            y = list(x)
            y[i] = 1 - y[i]
            yield tuple(y)

def neighbors_perm(p, good):
    for i in range(len(p) - 1):
        q = p[:i] + (p[i+1], p[i]) + p[i+2:]
        if q in good:
            yield q

def distances(source, states):
    seen = {source: 0}
    Q = deque([source])
    while Q:
        x = Q.popleft()
        for y in neighbors_east(x):
            if y not in seen:
                seen[y] = seen[x] + 1
                Q.append(y)
    assert len(seen) == len(states)
    return seen

def gray(m):
    if m == 1:
        return [(0,), (1,)]
    smaller = gray(m - 1)
    return [x + (0,) for x in smaller] + [x + (1,) for x in reversed(smaller)]

def verify():
    direct_total = 0
    for n in range(2, 9):
        m = n - 1
        states = [tuple((mask >> i) & 1 for i in range(m)) for mask in range(1 << m)]
        good = set(p for p in permutations(range(1, n + 1)) if avoid231321(p))
        assert len(good) == 1 << m
        assert set(map(decode, states)) == good
        direct_total += len(good)
        freq = Counter()
        edges = 0
        for x in states:
            p = decode(x)
            neigh = set(neighbors_perm(p, good))
            expected = set(map(decode, neighbors_east(x)))
            assert neigh == expected, (n, x, p, neigh, expected)
            d = len(neigh)
            freq[d] += 1
            edges += d
        assert freq == Counter({d: 2 * comb(n - 2, d - 1) for d in range(1, n)})
        assert edges // 2 == n * (1 << (n - 3)) if n >= 3 else edges // 2 == 1
        diameter = max(max(distances(x, states).values()) for x in states)
        assert diameter == 2 * n - 3
        print('n=%d vertices=%d edges=%d diameter=%d degree_freq=%s' %
              (n, len(good), edges // 2, diameter, sorted(freq.items())))
    for m in range(1, 14):
        path = gray(m)
        assert len(path) == (1 << m) == len(set(path))
        assert path[0] == (0,) * m
        assert path[-1] == (0,) * (m - 1) + (1,)
        assert all(b in set(neighbors_east(a)) for a, b in zip(path, path[1:]))
        assert all(decode(x) != decode(y) for x,y in zip(path,path[1:]))
    print('PASS: %d direct pattern-avoiding permutations; all-pairs distances through n=8; Gray paths through n=14.' % direct_total)

if __name__ == '__main__':
    verify()
