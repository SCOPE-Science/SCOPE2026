#!/usr/bin/env python3
"""Direct labelled-vertex check independent of support-type reduction."""
from itertools import product
from collections import Counter

SIZES = [(1,1,1), (1,1,2), (1,2,2), (2,2,2), (1,2,3),
         (2,2,3), (1,3,3), (1,1,1,1), (2,1,1,1),
         (2,2,1,1), (2,2,2,1), (2,2,2,2), (1,1,1,1,1),
         (2,2,1,1,1), (2,2,2,1,1), (1,1,1,1,1,1),
         (3,3,3), (3,3,2,1), (2,2,2,2,1)]


def inspect(sizes):
    parts = tuple(i for i, size in enumerate(sizes) for _ in range(size))
    n = len(parts)
    neighbours = tuple(tuple(j for j in range(n) if parts[i] != parts[j]) for i in range(n))
    def advance(z):
        return tuple((z[i] if z[i] == 2 and any(z[j] == 1 for j in neighbours[i])
                      else (z[i]+1) % 3) for i in range(n))
    census = Counter()
    for start in product(range(3), repeat=n):
        states = []
        visited = {}
        z = start
        while z not in visited:
            visited[z] = len(states)
            states.append(z)
            z = advance(z)
            assert len(states) <= 20
        t = visited[z]
        p = len(states) - t
        recurrent = states[t]
        sync = len(set(recurrent)) == 1
        assert p in (3,4)
        assert t <= 6
        assert t == 0 or (p == 3 and sync)
        assert advance(advance(advance(advance(advance(advance(z)))))) == z if p == 3 else True
        census[t, p, sync] += 1
    U2 = [2**m-2 for m in sizes]
    U3 = [3**m-3*2**m+3 for m in sizes]
    period_4 = 2 * sum(U2[i]*U2[j] for i in range(len(sizes)) for j in range(i+1,len(sizes)))
    period_3_asynchronous = sum(U3)
    assert census[(0,3,False)] == period_3_asynchronous
    assert census[(0,4,False)] == period_4
    assert census[(0,3,True)] == 3
    assert sum(census.values()) == 3**n
    expected_max = 3 if max(sizes)==1 else 6
    assert max(t for t,p,sy in census) == expected_max
    return sum(census.values()), census[(0,4,False)], census[(0,3,False)]


def main():
    total = 0
    for sizes in SIZES:
        count, p4, p3 = inspect(sizes)
        total += count
        print('GRAPH_OK sizes=%s states=%d period4=%d async3=%d' % (sizes,count,p4,p3))
    print('DIRECT_OK graphs=%d configurations=%d' % (len(SIZES),total))

if __name__ == '__main__':
    main()
