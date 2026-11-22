#!/usr/bin/env python3
"""Standalone exhaustive checks of a restricted adjacent-swap metric.
Requires only the Python standard library. No external data or packages.
The all-length theorem relies on the proof in RESULT.md, not enumeration.
"""
from collections import deque
from itertools import combinations, permutations


def inversion_bits(p):
    n = len(p)
    return tuple(sum(p[i] > p[j] for j in range(i + 1, n)) for i in range(n - 1))


def avoids_patterns(p):
    n = len(p)
    for i, j, k in combinations(range(n), 3):
        if p[i] > p[j] > p[k] or p[i] > p[k] > p[j]:
            return False  # 321 or 312
    for i, j, k, ell in combinations(range(n), 4):
        if p[ell] < p[i] < p[j] < p[k]:
            return False  # 2341
    return True


def allowed_bit_word(x):
    return '111' not in x


def bit_neighbours(x):
    m = len(x)
    for i in range(m):
        if i + 1 < m and x[i + 1] == '1':
            continue
        y = x[:i] + str(1 - int(x[i])) + x[i + 1:]
        if allowed_bit_word(y):
            yield y


def predicted_distance(x, y):
    mismatch = {i for i in range(len(x)) if x[i] != y[i]}
    forced = set()
    active = set(mismatch)
    for i in range(len(x) - 1):
        if i in active and x[i + 1] == y[i + 1] == '1':
            forced.add(i + 1)
            active.add(i + 1)
    return len(mismatch) + 2 * len(forced)


def target_diameter(m):
    return m + (m + 1) // 3 if m >= 2 else m


def bfs(graph, src):
    d = {src: 0}
    todo = deque([src])
    while todo:
        v = todo.popleft()
        for w in graph[v]:
            if w not in d:
                d[w] = d[v] + 1
                todo.append(w)
    return d


def test_bit_graph():
    for m in range(1, 11):
        words = [format(x, f'0{m}b') for x in range(1 << m)
                 if allowed_bit_word(format(x, f'0{m}b'))]
        graph = {w: tuple(bit_neighbours(w)) for w in words}
        assert all(w in graph[v] for v in words for w in graph[v])
        observed = 0
        for v in words:
            distances = bfs(graph, v)
            assert len(distances) == len(words), (m, v)
            for w, d in distances.items():
                expected = predicted_distance(v, w)
                assert d == expected, (m, v, w, d, expected)
                observed = max(observed, d)
        assert observed == target_diameter(m), (m, observed)
        print(f'BIT_GRAPH m={m} vertices={len(words)} diameter={observed} PASS')


def test_permutation_model():
    for n in range(2, 9):
        ps = [p for p in permutations(range(1, n + 1)) if avoids_patterns(p)]
        pset = set(ps)
        pairs = {p: ''.join(map(str, inversion_bits(p))) for p in ps}
        code_set = set(pairs.values())
        words = {format(x, f'0{n-1}b') for x in range(1 << (n - 1))
                 if allowed_bit_word(format(x, f'0{n-1}b'))}
        assert len(ps) == len(code_set) and code_set == words, n
        for p in ps:
            actual = set()
            for i in range(n - 1):
                swapped = p[:i] + (p[i + 1], p[i]) + p[i + 2:]
                if swapped in pset:
                    actual.add(pairs[swapped])
            expected = set(bit_neighbours(pairs[p]))
            assert actual == expected, (n, p, actual, expected)
        print(f'PERMUTATIONS n={n} vertices={len(ps)} exact_edges=PASS')


if __name__ == '__main__':
    test_permutation_model()
    test_bit_graph()
    print('ALL TESTS PASSED')
