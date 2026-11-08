"""Exact finite checks for two adjacent elongated distances, using only Python stdlib.

Run: python check_adjacent_stretch.py
The universal theorem is proved analytically; these are exhaustive small-size checks.
"""
from itertools import product


def metric2(n, t2):
    """Return doubled distances, with exceptional edges 0-1 and 1-2."""
    return {(i, j): (t2 if (i, j) in {(0, 1), (1, 2)} else 2)
            for i in range(n) for j in range(i + 1, n)}


def is_connected_tight(f, d):
    adj = [[] for _ in f]
    for (i, j), dij in d.items():
        if abs(f[i] - f[j]) == dij:
            adj[i].append(j)
            adj[j].append(i)
    seen = {1}
    stack = [1]
    while stack:
        for v in adj[stack.pop()]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == len(f)


def count_exact(n, t2):
    # f(1)=0. Every vertex has a tight spanning tree, hence its
    # doubled values are integers. The bound |f(i)-f(1)|<=d(i,1)
    # gives the following finite, exhaustive grid for every vertex.
    d = metric2(n, t2)
    choices = {i: range(-d[min(i, 1), max(i, 1)],
                         d[min(i, 1), max(i, 1)] + 1)
               for i in range(n) if i != 1}
    indices = tuple(choices)
    total = 0
    for coords in product(*(choices[i] for i in indices)):
        f = [0] * n
        for i, x in zip(indices, coords):
            f[i] = x
        if any(abs(f[i] - f[j]) > dij for (i, j), dij in d.items()):
            continue
        if is_connected_tight(f, d):
            total += 1
    return total


def formula(n, t2):
    if t2 == 2:  # t=1
        return 2 ** n - 2
    if t2 == 4:  # t=2
        return 2 ** n - 4
    return 7 * 2 ** (n - 2) - 10


if __name__ == '__main__':
    tests = 0
    for n in range(4, 7):
        for t2 in (2, 3, 4):
            actual = count_exact(n, t2)
            predicted = formula(n, t2)
            assert actual == predicted, (n, t2, actual, predicted)
            tests += 1
    print(f'EXACT_VERTEX_ENUMERATION_PASS: {tests} cases')
    print('ALL_ADJACENT_STRETCH_CHECKS_PASSED')
