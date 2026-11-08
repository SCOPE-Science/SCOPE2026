#!/usr/bin/env python3
"""Exact finite-state checks for a binary five-site cellular automaton.

Only Python's standard library is required. All arithmetic is integral.
"""
from collections import deque
from math import comb, factorial, gcd


def reverse_maps():
    maps = []
    for label in (0, 1):
        arr = []
        for state in range(16):
            a, b, c, d = ((state >> k) & 1 for k in (3, 2, 1, 0))
            predecessor_bit = label ^ c ^ (a & (1 ^ b) & d)
            arr.append((predecessor_bit << 3) | (state >> 1))
        maps.append(tuple(arr))
    return tuple(maps)


def make_edges(maps):
    states = tuple(range(16))
    fibers = {
        (a, b): tuple(sorted({maps[a][maps[b][x]] for x in states}))
        for a in (0, 1) for b in (0, 1)
    }
    assert all(len(fiber) == 8 for fiber in fibers.values())
    edges = {}
    for source, fiber in fibers.items():
        for symbol in (0, 1):
            target = (symbol, source[0])
            ranks = {state: i for i, state in enumerate(fibers[target])}
            permutation = tuple(ranks[maps[symbol][state]] for state in fiber)
            assert sorted(permutation) == list(range(8))
            edges[(source, symbol)] = (target, permutation)
    return fibers, edges


def walk(vertex, symbols, edges):
    perm = tuple(range(8))
    for symbol in symbols:
        vertex, edge = edges[(vertex, symbol)]
        perm = tuple(edge[perm[i]] for i in range(8))
    return vertex, perm


def compose(a, b):
    return tuple(a[b[i]] for i in range(8))


def permutation_order(perm):
    identity = tuple(range(8))
    state = identity
    for n in range(1, 40321):
        state = compose(perm, state)
        if state == identity:
            return n
    raise AssertionError('Order too large')


def subgroup_cardinality(generators):
    identity = tuple(range(8))
    reached = {identity}
    queue = deque([identity])
    while queue:
        p = queue.popleft()
        for generator in generators:
            q = compose(generator, p)
            if q not in reached:
                reached.add(q)
                queue.append(q)
    return len(reached)


def cyclic_output(x, n):
    bits = [(x >> i) & 1 for i in range(n)]
    output = 0
    for i in range(n):
        v = bits[i] ^ bits[(i + 3) % n] ^ (
            bits[(i + 1) % n] & (1 ^ bits[(i + 2) % n]) & bits[(i + 4) % n]
        )
        output |= v << i
    return output


def fiber_count_from_perm(y, n, edges):
    bits = [(y >> i) & 1 for i in range(n)]
    v = (bits[0], bits[1 % n])
    final, p = walk(v, reversed(bits), edges)
    assert final == v
    return sum(i == x for i, x in enumerate(p))


def main():
    maps = reverse_maps()
    fibers, edges = make_edges(maps)
    expected_fibers = {
        (0, 0): (0, 2, 5, 6, 9, 11, 12, 15),
        (0, 1): (0, 2, 4, 6, 9, 11, 13, 15),
        (1, 0): (1, 3, 4, 7, 8, 10, 13, 14),
        (1, 1): (1, 3, 5, 7, 8, 10, 12, 14),
    }
    assert fibers == expected_fibers
    root = (0, 0)
    va, a = walk(root, (0,), edges)
    vb, b = walk(root, (1, 0, 0), edges)
    vc, c = walk(root, (1, 0, 0, 0, 0), edges)
    assert va == vb == vc == root
    assert a == (0, 4, 1, 5, 6, 2, 3, 7)
    assert b == (1, 0, 3, 6, 4, 5, 7, 2)
    assert permutation_order(a) == 6
    assert permutation_order(c) == 7
    assert gcd(6, 5 * 7) == 1
    group_size = subgroup_cardinality((a, b))
    assert group_size == factorial(8)

    checks = 0
    for n in range(2, 14):
        hist = bytearray(1 << n)
        for x in range(1 << n):
            hist[cyclic_output(x, n)] += 1
        assert sum(hist) == (1 << n)
        for y, direct in enumerate(hist):
            via_permutation = fiber_count_from_perm(y, n, edges)
            assert direct == via_permutation, (n, y, direct, via_permutation)
            assert direct != 7
            checks += 1
    derangements = [sum((-1) ** j * factorial(m) // factorial(j) for j in range(m + 1))
                   for m in range(9)]
    rencontres = tuple(comb(8, j) * derangements[8 - j] for j in range(9))
    assert rencontres == (14833, 14832, 7420, 2464, 630, 112, 28, 0, 1)
    assert sum(rencontres) == factorial(8)
    print('VERIFY_OK group_order=%d lifted_cycle_lengths=6,35 cyclic_targets=%d limit_numerators=%s' %
          (group_size, checks, ','.join(map(str, rencontres))))


if __name__ == '__main__':
    main()
