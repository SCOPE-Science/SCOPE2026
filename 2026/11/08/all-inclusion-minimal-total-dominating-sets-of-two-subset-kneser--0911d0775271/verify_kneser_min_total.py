"""Exact finite obstruction census and independent Kneser total-domination check.

Run: python3 verify_kneser_min_total.py
Only the Python standard library is required.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb


def normalized(edges):
    verts = sorted({v for e in edges for v in e})
    m = {v: i for i, v in enumerate(verts)}
    return tuple(sorted(tuple(sorted((m[a], m[b]))) for a, b in edges))


def signature(edges):
    n = max(v for e in edges for v in e) + 1
    deg = [0] * n
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    return n, tuple(sorted(deg))


def isomorphic(E, F):
    n, dE = signature(E)
    nF, dF = signature(F)
    if n != nF or dE != dF:
        return False
    a = [0] * n
    b = [0] * n
    for u, v in E:
        a[u] |= 1 << v
        a[v] |= 1 << u
    for u, v in F:
        b[u] |= 1 << v
        b[v] |= 1 << u
    degA = [x.bit_count() for x in a]
    degB = [x.bit_count() for x in b]
    order = sorted(range(n), key=lambda u: (-degA[u], u))
    buckets = defaultdict(list)
    for v in range(n):
        buckets[degB[v]].append(v)
    mapping = [-1] * n

    def search(k, used):
        if k == n:
            return True
        u = order[k]
        for v in buckets[degA[u]]:
            if used & (1 << v):
                continue
            if any(((a[u] >> w) & 1) != ((b[v] >> mapping[w]) & 1)
                   for w in order[:k]):
                continue
            mapping[u] = v
            if search(k + 1, used | (1 << v)):
                return True
            mapping[u] = -1
        return False

    return search(0, 0)


def distinct(edgesets):
    buckets = defaultdict(list)
    for E in edgesets:
        E = normalized(E)
        bucket = buckets[signature(E)]
        if not any(isomorphic(E, F) for F in bucket):
            bucket.append(E)
    return [E for bucket in buckets.values() for E in bucket]


def all_unlabeled_edge_graphs(max_edges=6):
    layers = {1: [((0, 1),)]}
    for k in range(2, max_edges + 1):
        candidates = []
        for E in layers[k - 1]:
            n = max(v for e in E for v in e) + 1
            old = set(E)
            for a in range(n):
                for b in range(a + 1, n):
                    if (a, b) not in old:
                        candidates.append(E + ((a, b),))
                candidates.append(E + ((a, n),))
            candidates.append(E + ((n, n + 1),))
        layers[k] = distinct(candidates)
    return layers


def vertex_cover_at_most(edges, k):
    V = sorted({v for e in edges for v in e})
    for r in range(k + 1):
        for C in combinations(V, r):
            cover = set(C)
            if all(a in cover or b in cover for a, b in edges):
                return True
    return False


def critical_three(edges):
    if vertex_cover_at_most(edges, 2):
        return False
    return all(vertex_cover_at_most(edges[:i] + edges[i+1:], 2)
               for i in range(len(edges)))


def classify_graph(E):
    e, n = len(E), signature(E)[0]
    d = signature(E)[1]
    if (e, n, d) == (3, 6, (1,)*6):
        return 'three_disjoint_edges'
    if (e, n, d) == (4, 5, (1, 1, 2, 2, 2)):
        return 'triangle_and_edge'
    if (e, n, d) == (5, 5, (2,)*5):
        return 'five_cycle'
    if (e, n, d) == (6, 4, (3,)*4):
        return 'complete_four'
    return None


def census():
    layers = all_unlabeled_edge_graphs()
    sizes = [len(layers[i]) for i in range(1, 7)]
    assert sizes == [1, 2, 5, 11, 26, 68], sizes
    critical = Counter()
    for E in (E for layer in layers.values() for E in layer):
        if critical_three(E):
            label = classify_graph(E)
            assert label is not None, ('unexpected critical', E)
            critical[label] += 1
    assert dict(critical) == {
        'three_disjoint_edges': 1, 'triangle_and_edge': 1,
        'five_cycle': 1, 'complete_four': 1}, critical
    return sizes


def kneser_direct_check(n):
    pairs = list(combinations(range(n), 2))
    m = len(pairs)
    neighbors = []
    for a, b in pairs:
        bits = 0
        for j, (c, d) in enumerate(pairs):
            if a != c and a != d and b != c and b != d:
                bits |= 1 << j
        neighbors.append(bits)
    observed = Counter()
    total_dom = 0
    for S in range(1, 1 << m):
        if not all(S & adj for adj in neighbors):
            continue
        total_dom += 1
        if all(not all((S ^ (1 << j)) & adj for adj in neighbors)
               for j in range(m) if S & (1 << j)):
            observed[S.bit_count()] += 1
    expected = {
        3: 15 * comb(n, 6) if n >= 6 else 0,
        4: 10 * comb(n, 5) if n >= 5 else 0,
        5: 12 * comb(n, 5) if n >= 5 else 0,
        6: comb(n, 4),
    }
    expected = Counter({k: v for k, v in expected.items() if v})
    assert observed == expected, (n, observed, expected)
    return (1 << m) - 1, total_dom, sum(observed.values())


def main():
    sizes = census()
    stats = [kneser_direct_check(n) for n in range(4, 8)]
    assert sum(s[0] for s in stats) == 2**6 - 1 + 2**10 - 1 + 2**15 - 1 + 2**21 - 1
    print('VERIFY_OK critical_types=4 graph_types_by_edges=' + ','.join(map(str, sizes)) +
          ' kneser_n=4..7 checked_subsets=' + str(sum(s[0] for s in stats)) +
          ' total_dominating=' + str(sum(s[1] for s in stats)) +
          ' minimal=' + str(sum(s[2] for s in stats)) +
          ' coefficients=PASS no_external_dependencies=PASS')


if __name__ == '__main__':
    main()
