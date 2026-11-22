"""Independent finite checks for two-independence complexes of three-arm theta graphs.

The all-length proof is combinatorial and is supplied in RESULT.md; this file
checks the exact complexes, critical cells and finite-state boundary recurrence.
"""
from collections import Counter, deque
from itertools import combinations


def graph(length):
    assert length >= 3
    n = length + 3
    edges = {(0, 2), (1, 2), (0, 3), (1, 3)}
    path = [0] + list(range(4, n)) + [1]
    edges.update(tuple(sorted(e)) for e in zip(path, path[1:]))
    return n, sorted(edges)


def forbidden_triples(n, edges):
    es = {frozenset(e) for e in edges}
    return [sum(1 << x for x in triple) for triple in combinations(range(n), 3)
            if sum(frozenset(e) <= frozenset(triple) for e in es) >= 2]


def face_set(length):
    n, edges = graph(length)
    triples = forbidden_triples(n, edges)
    return n, {f for f in range(1 << n) if all(f & h != h for h in triples)}


def greedy_match(faces, order):
    unmatched = faces.copy()
    pairs = []
    for v in order:
        bit = 1 << v
        candidates = [(x, x | bit) for x in unmatched
                      if not x & bit and (x | bit) in unmatched]
        for lo, hi in candidates:
            unmatched.remove(lo)
            unmatched.remove(hi)
        pairs.extend(candidates)
    return unmatched, pairs


def expected(length):
    if length % 4 == 3:
        return ((length - 1) // 2, 1)
    if length % 4 == 0:
        return (length // 2, 1)
    if length % 4 == 1:
        return ((length + 1) // 2, 3)
    return (length // 2, 5)


def acyclic_hasse(faces, pairs, n):
    # Reverse each matched Hasse edge and topologically sort the result.
    flipped = set(pairs)
    indeg = {f: 0 for f in faces}
    graph = {f: [] for f in faces}
    incidence = 0
    for upper in faces:
        for i in range(n):
            bit = 1 << i
            if not upper & bit:
                continue
            lower = upper ^ bit
            if (lower, upper) in flipped:
                source, target = lower, upper
            else:
                source, target = upper, lower
            graph[source].append(target)
            indeg[target] += 1
            incidence += 1
    q = deque(f for f in faces if indeg[f] == 0)
    done = 0
    while q:
        x = q.popleft()
        done += 1
        for y in graph[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
    assert done == len(faces), (done, len(faces))
    return incidence


def residual_path(m, left, right):
    allowed = set()
    for x in range(1 << m):
        if any(((x >> j) & 7) == 7 for j in range(m - 2)):
            continue
        if left == 'S' and x & 1:
            continue
        if left == 'D' and (x & 3) == 3:
            continue
        if right == 'S' and (x >> (m - 1)) & 1:
            continue
        if right == 'D' and ((x >> (m - 2)) & 3) == 3:
            continue
        allowed.add(x)
    critical, _ = greedy_match(allowed, range(m))
    return critical


def compare_component_enumeration(length, faces):
    n, edges = graph(length)
    nbrs = [set() for _ in range(n)]
    for u, v in edges:
        nbrs[u].add(v)
        nbrs[v].add(u)
    for f in range(1 << n):
        included = {i for i in range(n) if (f >> i) & 1}
        while included:
            todo = [included.pop()]
            size = 0
            while todo:
                v = todo.pop()
                size += 1
                for w in nbrs[v] & included:
                    included.remove(w)
                    todo.append(w)
            if size > 2:
                assert f not in faces
                break
        else:
            assert f in faces


def main():
    patterns = {'F': 0b0110, 'S': 0b1100, 'D': 0b1010}
    # Index 0 is the leftmost path vertex: the four prefix bits are 0,1,1,0 etc.
    # Their bit masks are 0110, 1100, 1010 in little-endian notation.
    states = 'FSD'
    comparisons = 0
    for m in range(7, 17):
        for left in states:
            for right in states:
                previous = residual_path(m - 4, left, right)
                predicted = {patterns[left] | (x << 4) for x in previous}
                assert residual_path(m, left, right) == predicted, (m, left, right)
                comparisons += 1
    print('Path four-step recurrences:', comparisons)

    for length in range(3, 15):
        n, faces = face_set(length)
        critical, pairs = greedy_match(faces, list(range(4, n)) + [2, 3, 0, 1])
        dimension, count = expected(length)
        counts = Counter(f.bit_count() - 1 for f in critical)
        assert counts == {dimension: count}, (length, counts)
        assert len(pairs) * 2 + len(critical) == len(faces)
        if length <= 11:
            incidence = acyclic_hasse(faces, pairs, n)
        else:
            incidence = -1
        if length <= 10:
            compare_component_enumeration(length, faces)
        print('theta', length, 'faces', len(faces), 'pairs', len(pairs),
              'critical', count, 'dimension', dimension, 'hasse', incidence)
    print('ALL FINITE CHECKS PASSED')


if __name__ == '__main__':
    main()
