"""Exact finite checker for alternating-permutation Kendall codes, Python 3.9+."""

from collections import Counter, defaultdict
from itertools import combinations, permutations
from pathlib import Path


def orientation(p):
    if len(p) < 2:
        return 1
    signs = tuple(a < b for a, b in zip(p, p[1:]))
    if not all(a != b for a, b in zip(signs, signs[1:])):
        return 0
    return 1 if signs[0] else -1


def adjacent_ball(p):
    yield p
    for i in range(len(p) - 1):
        x = list(p)
        x[i], x[i + 1] = x[i + 1], x[i]
        yield tuple(x)


def conflicts(words):
    buckets = defaultdict(list)
    for i, p in enumerate(words):
        for output in adjacent_ball(p):
            buckets[output].append(i)
    return sorted({edge for group in buckets.values() for edge in combinations(group, 2)})


def graph_components(words, edges):
    adj = [set() for _ in words]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
    unseen = set(range(len(words)))
    comps = []
    while unseen:
        comp = [unseen.pop()]
        for i in comp:
            for j in adj[i] & unseen:
                unseen.remove(j)
                comp.append(j)
        comps.append(comp)
    return comps, adj


def independence_enumerator(indices, adj):
    best = -1
    num = 0
    for mask in range(1 << len(indices)):
        size = bin(mask).count('1')
        if size < best:
            continue
        chosen = {i for k, i in enumerate(indices) if (mask >> k) & 1}
        if all(not (adj[i] & chosen) for i in chosen):
            if size > best:
                best, num = size, 0
            num += 1
    return best, num


EULER = [0, 1, 1, 2, 5, 16, 61, 272, 1385]
RESULTS = [(0, 0), (1, 1), (1, 2), (2, 2), (5, 4), (16, 9216),
           (80, 2**42), (502, 2**42), (2770, 1)]
EDGES_EXPECTED = [0, 0, 1, 4, 10, 22, 42, 42, 0]

for n in range(1, 9):
    words = [p for p in permutations(range(1, n + 1)) if orientation(p)]
    assert len(words) == (1 if n == 1 else 2 * EULER[n])
    edges = conflicts(words)
    assert len(edges) == EDGES_EXPECTED[n]
    comps, adj = graph_components(words, edges)
    if n == 3:
        assert len(comps) == 1 and len(comps[0]) == 4
        assert all(len(a) == 2 for a in adj)
    if n == 4:
        assert len(comps) == 1 and len(comps[0]) == 10
    if n == 5:
        degree_sequences = Counter(tuple(sorted(len(adj[i]) for i in comp)) for comp in comps)
        assert degree_sequences == Counter({(1, 1): 6, (1, 1, 2, 2): 2, (1, 1, 2, 2, 2, 2): 2})
    if n <= 5:
        opt, num = 0, 1
        for comp in comps:
            size, count = independence_enumerator(comp, adj)
            opt += size
            num *= count
    else:
        assert max(map(len, adj)) <= 1
        opt, num = len(words) - len(edges), 2**len(edges)
    assert (opt, num) == RESULTS[n]

    if n in (6, 7):
        path = Path(__file__).with_name('optimal_%d.txt' % n)
        code = [tuple(map(int, line.strip())) for line in path.read_text().splitlines() if line.strip()]
        assert len(code) == opt and len(set(code)) == opt
        index = {p: i for i, p in enumerate(words)}
        assert all(p in index for p in code)
        chosen = {index[p] for p in code}
        assert all(i not in chosen or j not in chosen for i, j in edges)
        profiles = Counter()
        for i, j in edges:
            p, q = words[i], words[j]
            assert orientation(p) * orientation(q) == -1
            centers = []
            for a, b in combinations(range(1, n), 2):
                if b == a + 1:
                    continue
                x = list(p)
                x[a-1], x[a] = x[a], x[a-1]
                x[b-1], x[b] = x[b], x[b-1]
                if tuple(x) == q:
                    centers.append((a, b))
            assert len(centers) == 1
            profiles[centers[0]] += 1
        expected = {(1, 4): 12, (2, 4): 18, (2, 5): 12} if n == 6 else {(2, 5): 42}
        assert dict(profiles) == expected

    print('n', n, 'source', len(words), 'conflicts', len(edges),
          'max_code', opt, 'opt_codebooks', num)
print('VERIFY_OK')
