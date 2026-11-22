"""Independent pairwise-comparison census. Python 3, no external packages.
Run: python3 check_python.py

A sensor set is valid iff every pair of locations has different sign vectors
of all ordered pairwise detector-distance comparisons. This program does not
construct ordered distance partitions or use the C++ program's BFS method.
"""
from itertools import combinations
from collections import Counter, deque
from math import comb

N = 16

def adjacent(which, x, y):
    if x == y:
        return False
    i, j = divmod(x, 4)
    k, l = divmod(y, 4)
    if which == 'rook':
        return i == k or j == l
    return ((k-i) % 4, (l-j) % 4) in {
        (1,0), (-1 % 4,0), (0,1), (0,-1 % 4), (1,1), (-1 % 4,-1 % 4)
    }

def run(which):
    # In these degree-six strongly regular graphs every nonedge is a two-step pair.
    graph = [[int(adjacent(which, x, y)) for y in range(N)] for x in range(N)]
    for x in range(N):
        assert sum(graph[x]) == 6
        for y in range(N):
            if x != y:
                assert sum(graph[x][z] * graph[y][z] for z in range(N)) == 2
    distance = lambda x, sensor: (0 if x == sensor else 1 if graph[x][sensor] else 2)
    good = bytearray(1 << N)
    counts = Counter()
    for mask in range(1 << N):
        sensors = [i for i in range(N) if mask & (1 << i)]
        pairs = list(combinations(sensors, 2))
        seen = set()
        ok = True
        for location in range(N):
            stamp = tuple(
                (distance(location, u) > distance(location, v)) -
                (distance(location, u) < distance(location, v))
                for u, v in pairs
            )
            if stamp in seen:
                ok = False
                break
            seen.add(stamp)
        good[mask] = int(ok)
        if ok:
            counts[len(sensors)] += 1

    expected = (
        [0,0,0,0,0,2112,7024,11248,12858,11440,8008,4368,1820,560,120,16,1]
        if which == 'rook' else
        [0,0,0,0,0,1728,6736,11152,12846,11440,8008,4368,1820,560,120,16,1]
    )
    assert [counts[i] for i in range(N+1)] == expected
    assert sum(counts.values()) == sum(expected)
    assert all(counts[i] == comb(N, i) for i in range(9, N+1))
    maxima = Counter()
    for mask in range(1 << N):
        if good[mask]:
            continue
        if all(good[mask | (1 << add)] for add in range(N) if not (mask >> add & 1)):
            maxima[mask.bit_count()] += 1
    assert dict(maxima) == (
        {4:144,6:72,7:96,8:12} if which == 'rook' else
        {4:48,6:24,7:96,8:24}
    )
    bases = {mask for mask in range(1 << N) if mask.bit_count() == 5 and good[mask]}
    edges = 0
    degree_hist = Counter()
    neigh = {}
    for mask in bases:
        e = set()
        for i in range(N):
            if mask & (1 << i):
                for j in range(N):
                    if not (mask & (1 << j)):
                        altered = mask ^ (1 << i) ^ (1 << j)
                        if altered in bases:
                            e.add(altered)
        degree_hist[len(e)] += 1
        edges += len(e)
        neigh[mask] = e
    assert edges % 2 == 0
    assert edges // 2 == (30624 if which == 'rook' else 22176)
    known = set()
    cc_sizes = []
    for s in bases:
        if s in known:
            continue
        q = [s]
        known.add(s)
        for u in q:
            for v in neigh[u]:
                if v not in known:
                    known.add(v)
                    q.append(v)
        cc_sizes.append(len(q))
    assert cc_sizes == [len(bases)]
    # Exact distances by exploring each BFS: an independent check of diameter 5.
    ecc = Counter()
    for root in bases:
        dd = {root:0}
        q = deque([root])
        while q:
            u = q.popleft()
            for v in neigh[u]:
                if v not in dd:
                    dd[v] = dd[u] + 1
                    q.append(v)
        assert len(dd) == len(bases)
        ecc[max(dd.values())] += 1
    assert dict(ecc) == {5:len(bases)}
    print(which, 'coefficients',expected,'maximal failure sets',sorted(maxima.items()))
    print(which, 'edges',edges//2,'degrees',sorted(degree_hist.items()),'eccentricities', sorted(ecc.items()))

if __name__ == '__main__':
    run('rook')
    run('shrikhande')
    print('ALL CHECKS PASS')
