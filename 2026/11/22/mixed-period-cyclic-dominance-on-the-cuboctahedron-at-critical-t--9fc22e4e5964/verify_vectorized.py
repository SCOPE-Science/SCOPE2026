#!/usr/bin/env python3
"""Independent exhaustive three-color threshold-two cuboctahedral dynamics check.
Requires Python 3 and NumPy; does not read external data files.
"""
from collections import Counter, deque
from itertools import permutations
import numpy as np

EDGES = [(u, v) for u in range(8) for v in range(u + 1, 8)
         if (u ^ v).bit_count() == 1]
assert len(EDGES) == 12
ADJ = [tuple(j for j, (w, z) in enumerate(EDGES)
             if i != j and (u in (w, z) or v in (w, z)))
       for i, (u, v) in enumerate(EDGES)]
assert all(len(a) == 4 for a in ADJ)
POW = [3 ** j for j in range(12)]
N = 3 ** 12
D = np.array([(np.arange(N, dtype=np.int32) // p) % 3 for p in POW],
             dtype=np.uint8)


def transition(ghm=False):
    transformed = np.zeros(N, dtype=np.int32)
    for i in range(12):
        c = D[i]
        n = (c + 1) % 3
        matches = sum((D[j] == n) for j in ADJ[i])
        if ghm:
            new = np.where(c == 0, (matches >= 2).astype(np.uint8), n)
        else:
            new = np.where(matches >= 2, n, c)
        transformed += new.astype(np.int32) * POW[i]
    assert np.min(transformed) >= 0 and np.max(transformed) < N
    return transformed


def census(successor):
    indegree = np.bincount(successor, minlength=N).astype(np.int32)
    queue = deque(np.flatnonzero(indegree == 0).tolist())
    removed = []
    while queue:
        u = queue.popleft()
        removed.append(u)
        v = int(successor[u])
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
    assert all(indegree[u] == 0 for u in removed)
    orbit = np.full(N, -1, dtype=np.int32)
    period = np.zeros(N, dtype=np.uint8)
    depth = np.zeros(N, dtype=np.uint8)
    cycles = []
    for initial in np.flatnonzero(indegree > 0):
        initial = int(initial)
        if orbit[initial] >= 0:
            continue
        i = len(cycles)
        points = []
        u = initial
        while orbit[u] < 0:
            orbit[u] = i
            points.append(u)
            u = int(successor[u])
        assert u == initial
        for v in points:
            period[v] = len(points)
        cycles.append(tuple(points))
    for u in reversed(removed):
        v = int(successor[u])
        orbit[u] = orbit[v]
        period[u] = period[v]
        depth[u] = depth[v] + 1
    assert np.all(orbit >= 0)
    basin_sizes = np.bincount(orbit, minlength=len(cycles))
    basin = {}
    for i, points in enumerate(cycles):
        basin[(len(points), int(basin_sizes[i]))] = basin.get(
            (len(points), int(basin_sizes[i])), 0) + 1
    depth_period = Counter((int(d), int(p)) for d, p in zip(depth, period))
    return cycles, basin, depth_period, int(depth.max()), period, basin_sizes, depth


def symmetry_classes(cycles, allow_color_shift, basin_sizes):
    edges_by_key = {edge: i for i, edge in enumerate(EDGES)}
    maps = set()
    for axes in permutations(range(3)):
        for flips in range(8):
            def f(u):
                return sum(((((u >> ax) & 1) ^ ((flips >> i) & 1)) << i)
                           for i, ax in enumerate(axes))
            maps.add(tuple(edges_by_key[tuple(sorted((f(u), f(v))))]
                           for u, v in EDGES))
    assert len(maps) == 48
    rep_for_state = {int(s): min(cyc) for cyc in cycles for s in cyc}
    by_rep = {min(cyc): len(cyc) for cyc in cycles}
    size_by_rep = {min(cyc): int(basin_sizes[i]) for i, cyc in enumerate(cycles)}
    unclassified = set(by_rep)
    result = Counter()
    while unclassified:
        rep = min(unclassified)
        digits = [(rep // p) % 3 for p in POW]
        group_orbit = set()
        for mapping in maps:
            for shift in range(3 if allow_color_shift else 1):
                image = sum(((digits[j] + shift) % 3) * POW[mapping[j]]
                            for j in range(12))
                group_orbit.add(rep_for_state[image])
        assert group_orbit <= unclassified
        assert len({size_by_rep[k] for k in group_orbit}) == 1
        result[(by_rep[rep], len(group_orbit), size_by_rep[rep])] += 1
        unclassified -= group_orbit
    return result


def show(label, result):
    cycles, basin, depth_period, max_depth, state_period, basin_sizes, state_depth = result
    print(label)
    print('orbit counts:', sorted(Counter(map(len, cycles)).items()))
    print('basin spectrum:', sorted(basin.items()))
    print('entry-depth-period:', sorted(depth_period.items()))
    print('maximum entry depth:', max_depth)
    print('symmetry classes (period, class-size, basin-size)->count:',
          sorted(symmetry_classes(cycles, label == 'CCA', basin_sizes).items()))
    assert sum(len(cyc) for cyc in cycles) == sum(
        n for (depth, period), n in depth_period.items() if depth == 0)
    assert sum(n * size for (period, size), n in basin.items()) == N


if __name__ == '__main__':
    cca = census(transition(False))
    ghm = census(transition(True))
    show('CCA', cca)
    show('GHM', ghm)
    assert Counter(map(len, cca[0])) == Counter({1:81,3:8,6:8,8:36,12:8})
    assert cca[3] == 8
    assert Counter(map(len, ghm[0])) == Counter({1:1,3:8})
    assert ghm[3] == 6
    assert int(cca[6][31727]) == 8
    assert int(ghm[6][16188]) == 6
    for witness, per in [(84774, 3), (37134, 6), (455, 8), (8638, 12)]:
        assert int(cca[4][witness]) == per and int(cca[6][witness]) == 0
    pair_counts = Counter(zip(cca[4].tolist(), ghm[4].tolist()))
    print('joint eventual periods (CCA, GHM)->states:', sorted(pair_counts.items()))
    print('PASS')
