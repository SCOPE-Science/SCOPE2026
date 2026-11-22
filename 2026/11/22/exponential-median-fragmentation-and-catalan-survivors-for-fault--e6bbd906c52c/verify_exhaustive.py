#!/usr/bin/env python3
"""Finite crosschecks for fault-avoiding shortest-route reconfiguration.

Only standard-library code. The infinite-family proof is in RESULT.md.
"""
from collections import defaultdict, deque
from itertools import combinations, product


def all_routes(a, b):
    N = a + b
    for ee in combinations(range(N), a):
        sequence = ['N'] * N
        for j in ee:
            sequence[j] = 'E'
        word = ''.join(sequence)
        x = y = 0
        vertices = [(0, 0)]
        h = []
        for c in word:
            if c == 'E':
                x += 1
            else:
                h.append(x)
                y += 1
            vertices.append((x, y))
        yield word, frozenset(vertices), tuple(h)


def neighbors(word, words):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            continue
        other = word[:i] + word[i + 1] + word[i] + word[i + 2:]
        if other in words:
            yield other


def shortest_graph_distances(start, wordset):
    distances = {start: 0}
    queue = deque([start])
    while queue:
        word = queue.popleft()
        for nxt in neighbors(word, wordset):
            if nxt not in distances:
                distances[nxt] = distances[word] + 1
                queue.append(nxt)
    return distances


def check(a, b, fault_set, full, stats):
    failures = tuple(sorted(fault_set))
    valid = {w: h for w, verts, h in full if not verts.intersection(failures)}
    words = set(valid)
    groups = defaultdict(set)
    for word, verts, h in full:
        if word not in words:
            continue
        x_at_t = []
        x = 0
        x_at_t.append(x)
        for step in word:
            if step == 'E':
                x += 1
            x_at_t.append(x)
        signature = tuple(-1 if x_at_t[i + j] < i else 1 for i, j in failures)
        assert all(x_at_t[i + j] != i for i, j in failures)
        groups[signature].add(word)

    # Independent graph search, with no use of signatures.
    components = []
    yet = words.copy()
    while yet:
        start = next(iter(yet))
        reachable = shortest_graph_distances(start, words)
        comp = set(reachable)
        assert comp <= yet
        components.append(comp)
        yet -= comp
    assert sorted(map(sorted, components)) == sorted(map(sorted, groups.values())), (a,b,failures)

    # In each signature fiber, the full path-lattice order interval is present.
    for group in groups.values():
        profiles = [valid[w] for w in group]
        lower = tuple(map(min, zip(*profiles))) if b else ()
        upper = tuple(map(max, zip(*profiles))) if b else ()
        interval = {
            word for word, verts, h in full
            if all(l <= k <= u for l, k, u in zip(lower, h, upper))
        }
        assert interval == group, (a,b,failures,lower,upper)
        assert list(lower) == sorted(lower) and list(upper) == sorted(upper)
        for word in group:
            reach = shortest_graph_distances(word, group)
            assert len(reach) == len(group)
            for other in group:
                expected = sum(abs(u - v) for u, v in zip(valid[word], valid[other]))
                assert reach[other] == expected, (a,b,failures,word,other,reach[other],expected)
                stats['pairs_checked'] += 1
    stats['instances_checked'] += 1
    stats['nonempty_components'] += len(components)


def main():
    stats = {'instances_checked':0,'nonempty_components':0,'pairs_checked':0}
    for a, b in product(range(1, 5), repeat=2):
        full = list(all_routes(a, b))
        interior = [(x, y) for x in range(1, a) for y in range(1, b)]
        boundary = [(x, y) for x in range(a + 1) for y in range(b + 1)
                    if (x, y) not in ((0, 0), (a, b)) and (x, y) not in interior]
        for r in range(min(3, len(interior)) + 1):
            for subset in combinations(interior, r):
                check(a, b, subset, full, stats)
        for one in boundary:
            check(a, b, (one,), full, stats)
        for two in combinations(boundary, 2):
            check(a, b, two, full, stats)
    print('VERIFY_EXHAUSTIVE_OK',stats)


if __name__ == '__main__':
    main()
