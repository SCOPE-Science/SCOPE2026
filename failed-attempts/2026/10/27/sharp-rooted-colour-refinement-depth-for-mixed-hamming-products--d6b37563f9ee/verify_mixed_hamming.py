"""Exact integer checks for color refinement on rooted products of cliques.

No external libraries are required. This is finite corroboration of a separate
all-dimensions inductive proof, not an exhaustive proof over all parameter values.
"""
from collections import Counter
from itertools import combinations_with_replacement, product
from math import prod


def refine(colors, neighbours):
    signatures = []
    for v, row in enumerate(neighbours):
        count = Counter()
        for w, mult in row:
            count[colors[w]] += mult
        signatures.append((colors[v], tuple(sorted(count.items()))))
    newnames = {s: i for i, s in enumerate(sorted(set(signatures)))}
    return [newnames[s] for s in signatures]


def classify(colors, profiles):
    # Equality of partitions, not equality of arbitrary numeric color names.
    return all((colors[i] == colors[j]) == (profiles[i] == profiles[j])
               for i in range(len(colors)) for j in range(i + 1, len(colors)))


def depth(colors, neighbours):
    for t in range(len(colors)):
        updated = refine(colors, neighbours)
        if len(set(colors)) == len(set(updated)):
            return t, colors
        colors = updated
    raise AssertionError('refinement failed to stabilize')


def graph_case(qs):
    vertices = list(product(*(range(q) for q in qs)))
    locator = {v: i for i, v in enumerate(vertices)}
    neighbours = []
    for v in vertices:
        row = []
        for j, q in enumerate(qs):
            for a in range(q):
                if a != v[j]:
                    w = v[:j] + (a,) + v[j + 1:]
                    row.append((locator[w], 1))
        neighbours.append(row)
    sizes = sorted(set(qs))
    profiles = [tuple(sum(v[i] != 0 for i, q in enumerate(qs) if q == s)
                      for s in sizes) for v in vertices]
    initial = [0 if not any(v) else 1 for v in vertices]
    return initial, neighbours, profiles


def quotient_case(qs):
    sizes = sorted(set(qs))
    multiplicities = [qs.count(q) for q in sizes]
    profiles = list(product(*(range(m + 1) for m in multiplicities)))
    locate = {v: i for i, v in enumerate(profiles)}
    neighbours = []
    for vec in profiles:
        row = []
        for b, (q, m) in enumerate(zip(sizes, multiplicities)):
            j = vec[b]
            # Changing a nonzero symbol without changing its support.
            if j * (q - 2):
                row.append((locate[vec], j * (q - 2)))
            if j:
                v = list(vec)
                v[b] -= 1
                row.append((locate[tuple(v)], j))
            if m - j:
                v = list(vec)
                v[b] += 1
                row.append((locate[tuple(v)], (m - j) * (q - 1)))
        neighbours.append(row)
    initial = [0 if not any(v) else 1 for v in profiles]
    return initial, neighbours, profiles


def predicted(qs):
    return len(qs) - 1 if len(set(qs)) == 1 else len(qs)


def main():
    full = 0
    examples = {}
    for d in range(1, 6):
        for qs in combinations_with_replacement(range(2, 7), d):
            if prod(qs) > 3500:
                continue
            colors, neighbours, profiles = graph_case(qs)
            t, stable = depth(colors, neighbours)
            assert t == predicted(qs), (qs, t, predicted(qs))
            # independent full-graph type check by pairwise partition comparison
            assert classify(stable, profiles), (qs, 'orbit profile mismatch')
            full += 1
            examples[qs] = t
    test_patterns = [
        (2,) * 10,
        (2,) * 6 + (3,) * 4,
        (2, 3) * 5,
        (2, 3, 4, 5) * 3,
        (2, 3, 4, 5, 6, 7, 8, 9),
        (3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7),
        (2,) * 7 + (4,) * 5,
    ]
    quotient = 0
    for qs in test_patterns:
        colors, neighbours, profiles = quotient_case(qs)
        t, stable = depth(colors, neighbours)
        assert t == predicted(qs), (qs, t, predicted(qs))
        assert len(set(stable)) == len(profiles), (qs, 'quotient cells not separated')
        quotient += 1
    # Nontrivial example where a smaller punctured linear module need not
    # recover all rooted orbit indicators: the graph partition still does.
    assert examples[(2, 3)] == 2
    assert examples[(2, 3, 4)] == 3
    assert examples[(2, 2, 3, 3)] == 4
    assert examples[(3, 3, 3)] == 2
    print(f'FULL_GRAPH_CONFIGURATIONS={full}')
    print(f'WEIGHTED_QUOTIENT_CONFIGURATIONS={quotient}')
    print('SHARP_ROUNDS_AND_ORBITS=PASS')
    print('ALL_TESTS_PASS')


if __name__ == '__main__':
    main()
