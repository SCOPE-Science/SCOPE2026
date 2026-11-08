#!/usr/bin/env python3
"""Independent finite-type and labelled-graph checks for a minimum-set classification.

Uses only the Python standard library.  Run: python verify.py
"""

from itertools import combinations, product
from math import comb

GROUP_NEIGHBORS = ((2, 3), (2, 4), (0, 1), (0, 4), (1, 3))
CORE = {
    (1, 1, 1, 1, 1),
    (1, 1, 2, 0, 1),
    (2, 0, 1, 1, 1),
    (2, 0, 2, 0, 1),
    (2, 0, 2, 1, 0),
    (2, 1, 2, 0, 0),
}


def expected_profiles(a, b):
    return CORE | ({(3, 0, 1, 0, 1)} if a == 4 else set()) | (
        {(1, 0, 3, 0, 1)} if b == 4 else set()
    )


def class_sizes(a, b):
    return a, a, b, b, 1


def dominates_type(a, b, x):
    size = class_sizes(a, b)
    return all(x[i] == size[i] or any(x[j] for j in GROUP_NEIGHBORS[i])
               for i in range(5))


def secure_type(a, b, x):
    size = class_sizes(a, b)
    if not dominates_type(a, b, x):
        return False
    for i in range(5):
        if x[i] == size[i]:
            continue
        found = False
        for j in GROUP_NEIGHBORS[i]:
            if not x[j]:
                continue
            y = list(x)
            y[i] += 1
            y[j] -= 1
            if dominates_type(a, b, y):
                found = True
                break
        if not found:
            return False
    return True


def type_spectrum(a, b, k):
    size = class_sizes(a, b)
    return {x for x in product(*(range(min(v, k) + 1) for v in size))
            if sum(x) == k and secure_type(a, b, x)}


def count_formula(a, b):
    return (a*a*b*b + a*a*comb(b, 2) + b*b*comb(a, 2)
            + (a+b+1)*comb(a, 2)*comb(b, 2)
            + (comb(a, 3)*b if a == 4 else 0)
            + (a*comb(b, 3) if b == 4 else 0))


def count_from_profiles(a, b, patterns):
    return sum(comb(a, x[0])*comb(a, x[1])*comb(b, x[2])*comb(b, x[3])
               for x in patterns)


def labelled_graph(a, b):
    """Construct the graph from original vertices, shadows and an apex."""
    n = 2*(a+b)+1
    original_a = tuple(range(a))
    original_b = tuple(range(a, a+b))
    shadow_a = tuple(range(a+b, 2*a+b))
    shadow_b = tuple(range(2*a+b, 2*a+2*b))
    apex = n-1
    adjacency = [set() for _ in range(n)]

    def edge(u, v):
        adjacency[u].add(v)
        adjacency[v].add(u)

    for u in original_a:
        for v in original_b + shadow_b:
            edge(u, v)
    for u in shadow_a:
        for v in original_b:
            edge(u, v)
    for u in shadow_a + shadow_b:
        edge(u, apex)
    return adjacency, (original_a, shadow_a, original_b, shadow_b, (apex,))


def graph_secure(adjacency, selection):
    """Check the original vertex-level dominating and swap conditions."""
    n = len(adjacency)
    chosen = set(selection)

    def dominating(s):
        return all(u in s or bool(s.intersection(adjacency[u])) for u in range(n))

    if not dominating(chosen):
        return False
    for u in range(n):
        if u in chosen:
            continue
        if not any(dominating((chosen-{v}) | {u})
                   for v in chosen.intersection(adjacency[u])):
            return False
    return True


def verify():
    # The symbolic proof shows that no secure set of size at most five
    # can select four vertices from one non-apex class.  Therefore class
    # sizes 4 and 5 represent every possible boundary phenomenon.
    for a, b in product((4, 5), repeat=2):
        assert type_spectrum(a, b, 5) == expected_profiles(a, b)
        for k in range(5):
            assert not type_spectrum(a, b, k)
    print('FOUR_THRESHOLD_REGIMES_EXHAUSTIVE_OK')

    for a in range(4, 12):
        for b in range(4, 12):
            found = type_spectrum(a, b, 5)
            assert found == expected_profiles(a, b)
            assert count_from_profiles(a, b, found) == count_formula(a, b)
    print('UNRESTRICTED_FORMULA_SPOTCHECK_OK', 64)

    for a, b in ((4, 4), (4, 5), (5, 4), (5, 5), (4, 6)):
        graph, groups = labelled_graph(a, b)
        actual = set()
        counted = 0
        for selected in combinations(range(len(graph)), 5):
            if graph_secure(graph, selected):
                counted += 1
                sel = set(selected)
                actual.add(tuple(len(sel.intersection(g)) for g in groups))
        assert actual == expected_profiles(a, b)
        assert counted == count_formula(a, b)
        print('LABELLED_VERTEX_CHECK_OK', a, b, counted)
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
