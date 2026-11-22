"""Reproducible finite checks for acyclic path-semigroup commutation formulas.

Run with Python 3.9 or later; no third-party libraries are required.
The finite computations illustrate, but do not prove, the general theorem.
"""
from itertools import product


def paths(n, edges):
    outgoing = [[] for _ in range(n)]
    for edge_id, (u, v) in enumerate(edges):
        assert 0 <= u < v < n
        outgoing[u].append((edge_id, v))
    result = [((), i, i) for i in range(n)]

    def extend(start, here, seq):
        for edge_id, end in outgoing[here]:
            new_seq = seq + (edge_id,)
            result.append((new_seq, start, end))
            extend(start, end, new_seq)

    for i in range(n):
        extend(i, i, ())
    return result


def multiply(x, y):
    if x is None or y is None or x[2] != y[1]:
        return None
    return (x[0] + y[0], x[1], y[2])


def cut_families(n, path_list):
    index = {p: i for i, p in enumerate(path_list)}
    families = set()
    for colors in product(range(3), repeat=n):
        sources = {v for v, c in enumerate(colors) if c == 1}
        targets = {v for v, c in enumerate(colors) if c == 2}
        chosen = {
            p for p in path_list
            if (not p[0] and p[1] not in sources | targets)
            or (p[0] and p[1] in sources and p[2] in targets)
        }
        realized_sources = {p[1] for p in chosen if p[0]}
        realized_targets = {p[2] for p in chosen if p[0]}
        if realized_sources == sources and realized_targets == targets:
            families.add(frozenset(index[p] for p in chosen))
    return families


def enumerate_maximal_commuting(path_list):
    n = len(path_list)
    noncommuting = [0] * n
    for i, a in enumerate(path_list):
        for j, b in enumerate(path_list):
            if multiply(a, b) != multiply(b, a):
                noncommuting[i] |= 1 << j
    full = (1 << n) - 1
    families = set()
    for mask in range(1 << n):
        chosen = [i for i in range(n) if mask & (1 << i)]
        if any(noncommuting[i] & mask for i in chosen):
            continue
        blocked = mask
        for i in chosen:
            blocked |= noncommuting[i]
        if blocked == full:
            families.add(frozenset(chosen))
    return families


def check(n, edges):
    all_paths = paths(n, edges)
    by_vertex_pair = {(u, v): 0 for u in range(n) for v in range(n)}
    for p in all_paths:
        by_vertex_pair[p[1], p[2]] += 1
    total = len(all_paths)
    incoming = [sum(by_vertex_pair[u, v] for u in range(n)) for v in range(n)]
    outgoing = [sum(by_vertex_pair[v, w] for w in range(n)) for v in range(n)]

    for p in all_paths:
        actual = 1 + sum(multiply(p, q) == multiply(q, p) for q in all_paths)
        predicted = (total - incoming[p[1]] - outgoing[p[2]] +
                     (3 if not p[0] else 1))
        assert actual == predicted, (n, edges, p, actual, predicted)

    actual_families = enumerate_maximal_commuting(all_paths)
    expected_families = cut_families(n, all_paths)
    assert actual_families == expected_families, (n, edges)
    return len(all_paths), len(actual_families)


def main():
    count = 0
    for n in range(1, 5):
        possible = [(u, v) for u in range(n) for v in range(u+1, n)]
        for bits in product((0, 1), repeat=len(possible)):
            edges = [e for e, b in zip(possible, bits) if b]
            check(n, edges)
            count += 1
    cases = [
        (3, [(0, 1), (0, 1), (1, 2), (1, 2)]),
        (4, [(0, 1), (0, 1), (1, 2), (2, 3)]),
        (5, [(0, 1), (1, 2), (2, 3), (3, 4)]),
        (5, [(0, 1), (1, 3), (2, 3), (3, 4)]),
    ]
    for n, edges in cases:
        check(n, edges)
        count += 1
    for n in range(1, 7):
        line = [(i, i+1) for i in range(n-1)]
        actual = cut_families(n, paths(n, line))
        expected = 1 + (3**n - 2*n - 1)//4
        assert len(actual) == expected
        maximum = max(len(f) + 1 for f in actual)  # add zero
        assert maximum == max(n + 1, 1 + n*n//4)
        print(f'line n={n}: {expected} maximal families, largest size {maximum}')
    print(f'PASS: {count} DAG instances; all maximal families and individual centralizers')


if __name__ == '__main__':
    main()
