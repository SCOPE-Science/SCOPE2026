#!/usr/bin/env python3
"""Reproduce the finite checks for the bubble-pass inverse-fiber theorem.

Pure Python standard library. The all-size proof is in RESULT.md; finite
checks are diagnostics and do not replace the mathematical argument.
"""
from itertools import permutations, product
from collections import Counter
from math import factorial


def bubble_pass(p):
    a = list(p)
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return tuple(a)


def record_positions(sigma):
    maximum = 0
    positions = []
    for i, value in enumerate(sigma):
        if value > maximum:
            maximum = value
            positions.append(i)
    return positions


def mask_fiber(sigma):
    records = record_positions(sigma)
    opt = {pos: j for j, pos in enumerate(records[:-1])}
    outputs = {}
    for mask in range(1 << (len(records)-1)):
        p = list(sigma)
        for i in range(len(sigma)-2, -1, -1):
            if i not in opt or (mask & (1 << opt[i])):
                p[i], p[i+1] = p[i+1], p[i]
        p = tuple(p)
        assert p not in outputs
        assert bubble_pass(p) == sigma
        outputs[p] = mask
    return records, outputs


def component_sizes(adjacency):
    todo = set(adjacency)
    sizes = []
    while todo:
        x = todo.pop()
        stack = [x]
        total = 1
        while stack:
            for y in adjacency[stack.pop()]:
                if y in todo:
                    todo.remove(y)
                    stack.append(y)
                    total += 1
        sizes.append(total)
    return sorted(sizes)


def block_lengths(records):
    # Record at the final input position has no selectable bit.
    m = len(records)-1
    starts = [0] + [j for j in range(1,m)
                    if records[j] > records[j-1]+1]
    return [b-a for a,b in zip(starts, starts[1:]+[m])]


def predicted_components(lengths):
    possible = [[(1 << h) for h in range(L)] + [1] for L in lengths[1:]]
    if not possible:
        return [1 << lengths[0]]
    return sorted((1 << lengths[0]) * __import__('math').prod(t)
                  for t in product(*possible))


def main():
    for n in range(1, 9):
        totals = Counter()
        for prefix in permutations(range(1,n)):
            sigma = prefix + (n,)
            records, fiber = mask_fiber(sigma)
            m = len(records)-1
            assert len(fiber) == (1 << m)
            mask_by_perm = fiber
            neighbor = {}
            edge_count_twice = 0
            for p, mask in fiber.items():
                actual = set()
                for i in range(n-1):
                    q = list(p)
                    q[i], q[i+1] = q[i+1], q[i]
                    if tuple(q) in mask_by_perm:
                        actual.add(mask_by_perm[tuple(q)])
                predicted = {mask ^ (1 << j) for j in range(m)
                             if j == 0 or
                             (records[j] == records[j-1]+1
                              and (mask & (1 << (j-1))) == 0)}
                assert actual == predicted, (sigma, mask, actual, predicted)
                neighbor[mask] = actual
                edge_count_twice += len(actual)
            assert edge_count_twice % 2 == 0
            adjacent_record_pairs = sum(records[j] == records[j-1]+1
                                        for j in range(1,m))
            predicted_edges = (1 << (m-1)) + (adjacent_record_pairs * (1 << (m-2))
                                              if m >= 2 else 0) if m else 0
            assert edge_count_twice // 2 == predicted_edges
            lengths = block_lengths(records) if m else [0]
            assert component_sizes(neighbor) == predicted_components(lengths)
            if len(component_sizes(neighbor)) == 1:
                totals['connected'] += 1
            totals['fibers'] += 1
            totals['vertices'] += len(fiber)
            totals['edges'] += edge_count_twice // 2
        expected_connected = (factorial(n-2) *
                              sum(1/factorial(j) for j in range(n-1)) if n >= 2 else 1)
        assert totals['connected'] == round(expected_connected)
        assert totals['vertices'] == factorial(n)
        print('n=%d images=%d connected=%d vertices=%d edges=%d PASS' %
              (n, totals['fibers'], totals['connected'],
               totals['vertices'], totals['edges']))
    # An additional exact-integer verification of the all-length count.
    for n in range(2, 251):
        c = sum(factorial(n-2)//factorial(j) for j in range(n-1))
        assert 1 <= c <= factorial(n-1)
    print('Connected-fiber enumerator checked through n=250: PASS')


if __name__ == '__main__':
    main()
