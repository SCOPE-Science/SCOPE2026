"""Finite validation of the exact truncated-factor signatures.

The proof for arbitrary dimensions and variable widths is mathematical;
these tests only check the finite coordinate-extension and intrinsic-colour lemmas.
Run: python check_rectangular_logic.py
"""
from collections import deque
from itertools import product


def realized_extensions(q, stationary):
    used = set(stationary)
    result = set()
    for new in range(q):
        result.add(tuple(int(new == old) for old in stationary))
    return result


def pattern(stationary):
    return tuple(tuple(int(x == y) for y in stationary) for x in stationary)


def check_coordinate_extensions():
    nchecks = 0
    for k in range(3, 7):
        for q in range(2, 9):
            for r in range(2, 9):
                if min(q, k) != min(r, k):
                    continue
                for s in range(k):
                    patterns_q = {}
                    patterns_r = {}
                    for tup in product(range(q), repeat=s):
                        patterns_q[pattern(tup)] = realized_extensions(q, tup)
                    for tup in product(range(r), repeat=s):
                        patterns_r[pattern(tup)] = realized_extensions(r, tup)
                    assert patterns_q == patterns_r, (k, q, r, s)
                    nchecks += 1
    return nchecks


def colored_graph(sizes, k):
    V = tuple(product(*(range(q) for q in sizes)))
    nbr = {x: set() for x in V}
    for x in V:
        for y in V:
            if sum(a != b for a, b in zip(x, y)) == 1:
                nbr[x].add(y)
    colors = {}
    for x in V:
        for y in nbr[x]:
            # The common neighbors and this edge form a clique in products of cliques.
            common = nbr[x].intersection(nbr[y])
            assert all(z in nbr[w] for z in common for w in common if z != w)
            clique_size = 2 + len(common)
            colors[x, y] = min(clique_size, k)
            index = next(i for i, (a, b) in enumerate(zip(x, y)) if a != b)
            assert colors[x, y] == min(sizes[index], k)
    return V, nbr, colors


def check_colored_diameters():
    tests = 0
    for sizes in [(2,), (3,), (4,), (2, 3), (2, 4), (3, 4),
                  (2, 3, 4), (2, 4, 5), (3, 4, 5), (2, 2, 3, 4)]:
        for k in (3, 4, 5):
            V, nbr, color = colored_graph(sizes, k)
            for label in range(2, k + 1):
                expected = sum(min(q, k) == label for q in sizes)
                diameter = 0
                for start in V:
                    dist = {start: 0}
                    Q = deque([start])
                    while Q:
                        x = Q.popleft()
                        for y in nbr[x]:
                            if color[x, y] == label and y not in dist:
                                dist[y] = dist[x] + 1
                                Q.append(y)
                    diameter = max(diameter, max(dist.values()))
                assert diameter == expected, (sizes, k, label, diameter, expected)
                tests += 1
    return tests


if __name__ == '__main__':
    a = check_coordinate_extensions()
    print('COORDINATE EXTENSION TABLES: PASS', a, 'parameter tests')
    b = check_colored_diameters()
    print('INTRINSIC COLOUR AND DIAMETERS: PASS', b, 'parameter tests')
    print('ALL CHECKS PASSED')
