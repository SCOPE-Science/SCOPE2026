"""Independent exhaustive graph-distance verification for small binary cubes.

Run: python3 verify_independent.py
Only Python's standard library is required.
"""
from collections import Counter, deque
from itertools import combinations


def cube(d):
    n = 1 << d
    graph = [[x ^ (1 << j) for j in range(d)] for x in range(n)]
    distances = []
    for root in range(n):
        row = [-1] * n
        row[root] = 0
        q = deque([root])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if row[v] < 0:
                    row[v] = row[u] + 1
                    q.append(v)
        distances.append(row)
    edges = [(u, v) for u in range(n) for v in graph[u] if u < v]
    return distances, edges


def valid(S, distances, edges):
    signatures = [tuple(min(distances[s][a], distances[s][b]) for s in S)
                  for a, b in edges]
    resolving = len(set(signatures)) == len(edges)
    dominated = all(any(min(distances[s][a], distances[s][b]) <= 1 for s in S)
                    for a, b in edges)
    return resolving, dominated


def expected(d):
    n = 1 << d
    full = n - 1
    result = set()
    def add(v):
        assert len(set(v)) == len(v)
        result.add(frozenset(v))
    if d == 2:
        for x in range(n):
            for j in range(d):
                add([x, x ^ (1 << j)])
    elif d == 3:
        for parity in (0, 1):
            side = [x for x in range(n) if x.bit_count() % 2 == parity]
            for t in combinations(side, 3):
                add(t)
        for x in range(n):
            for a, b in combinations([x ^ (1 << j) for j in range(d)], 2):
                add([a, x, b])
    elif d == 4:
        for j in range(d):
            for fixed in (0, 1):
                for parity in (0, 1):
                    add([x for x in range(n) if (x >> j) & 1 == fixed
                         and x.bit_count() % 2 == parity])
        for center in range(n):
            ne = [center ^ (1 << j) for j in range(d)]
            for absent in ne:
                add([center ^ full] + [x for x in ne if x != absent])
        for a in range(n):
            b = a ^ full
            if a > b:
                continue
            rest = [x for x in range(n) if x != a and x != b
                    and (x.bit_count() - a.bit_count()) % 2 == 0]
            for c, e in combinations(rest, 2):
                if c ^ e != full:
                    add([a, b, c, e])
    elif d == 5:
        for center in range(n):
            ne = [center ^ (1 << j) for j in range(d)]
            for absent in ne:
                add([center ^ full] + [x for x in ne if x != absent])
    return result


for d, target, count, expected_lower_res, expected_lower_dom in [
    (2, 2, 4, 0, 4),
    (3, 3, 32, 0, 16),
    (4, 4, 176, 64, 112),
    (5, 5, 160, 1280, 80),
]:
    distances, edges = cube(d)
    if d >= 4:
        assert sum(valid(S, distances, edges)[0]
                   for S in combinations(range(1 << d), target - 2)) == 0
    lower_counts = Counter()
    for S in combinations(range(1 << d), target - 1):
        r, v = valid(S, distances, edges)
        lower_counts['resolving'] += r
        lower_counts['ve_dominating'] += v
        lower_counts['joint'] += r and v
    assert lower_counts['resolving'] == expected_lower_res, (d, lower_counts)
    assert lower_counts['ve_dominating'] == expected_lower_dom, (d, lower_counts)
    assert lower_counts['joint'] == 0, (d, lower_counts)
    bases = set()
    for S in combinations(range(1 << d), target):
        r, v = valid(S, distances, edges)
        if r and v:
            bases.add(frozenset(S))
    geometries = expected(d)
    assert len(bases) == count and bases == geometries, (d, len(bases), len(geometries))
    print(f'Q{d}: lower_res={lower_counts["resolving"]} '
          f'lower_ve={lower_counts["ve_dominating"]} '
          f'lower_joint=0, minimum={target}, bases={len(bases)}, family_equal=True')
print('CUBE_VE_EDGE_PY_OK')
