#!/usr/bin/env python3
"""Independent direct-subset and explicit-construction checks for prism connected domination."""
from itertools import combinations
from collections import Counter


def graph(n):
    adj = []
    for layer in (0, 1):
        for j in range(n):
            adj.append((1 << (layer*n + (j-1)%n)) |
                       (1 << (layer*n + (j+1)%n)) |
                       (1 << ((1-layer)*n + j)))
    return adj


def connected_and_dominating(bits, adj):
    if not bits:
        return False
    cover = bits
    reach = bits & -bits
    frontier = reach
    while frontier:
        t = frontier & -frontier
        frontier -= t
        j = t.bit_length() - 1
        cover |= adj[j]
        grown = adj[j] & bits & ~reach
        reach |= grown
        frontier |= grown
    return reach == bits and (cover | bits) == (1 << len(adj)) - 1


def counted_doubles(bits, n):
    return sum(bool(bits & (1 << j)) and bool(bits & (1 << (n+j))) for j in range(n))


def predicted(n):
    if n == 3:
        return {1: 3}
    if n == 4:
        return {0: 2, 1: 24, 2: 4}
    return {0: 2, 1: 2*n*(n-1), 2: 2*n}


def explicit_sets(n):
    if n == 3:
        return {(1 << j) | (1 << (n+j)) for j in range(n)}
    output = set()
    for layer in (0, 1):
        output.add(sum(1 << (layer*n+j) for j in range(n)))
    for start_empty in range(n):
        occupied = [((start_empty + j) % n) for j in range(1, n)]
        for bridge_index in range(n - 1):
            for first_layer in (0, 1):
                bits = 0
                for idx, col in enumerate(occupied):
                    if idx == bridge_index:
                        bits |= (1 << col) | (1 << (n + col))
                    else:
                        lyr = first_layer if idx < bridge_index else 1-first_layer
                        bits |= (1 << (lyr*n + col))
                output.add(bits)
    for start_empty in range(n):
        occupied = [(start_empty + j) % n for j in range(2, n)]
        if n == 4:
            variants = (0,)
        else:
            variants = (0, 1)
        for lyr in variants:
            bits = 0
            for idx, col in enumerate(occupied):
                if idx in (0, len(occupied)-1):
                    bits |= (1 << col) | (1 << (n+col))
                else:
                    bits |= 1 << (lyr*n + col)
            output.add(bits)
    return output


def verify():
    checked = 0
    reached = 0
    for n in range(3, 11):
        adj = graph(n)
        wanted = explicit_sets(n)
        inferred = set()
        for bits in range(1, 1 << (2*n)):
            checked += 1
            if connected_and_dominating(bits, adj):
                reached += 1
                if n == 3 and bits.bit_count() == 2 or n >= 4 and bits.bit_count() == n:
                    inferred.add(bits)
                if n == 3:
                    assert bits.bit_count() >= 2
                else:
                    assert bits.bit_count() >= n
        assert inferred == wanted, (n, len(inferred), len(wanted), len(inferred ^ wanted))
        counts = dict(Counter(counted_doubles(b, n) for b in inferred))
        assert counts == predicted(n), (n, counts, predicted(n))
        print('n', n, 'min_size', 2 if n == 3 else n, 'minimum_count', len(inferred), 'double_profile', counts)
    constructions = 0
    for n in range(11, 41):
        adj = graph(n)
        sets = explicit_sets(n)
        assert len(sets) == sum(predicted(n).values()), (n, len(sets))
        for bits in sets:
            assert bits.bit_count() == n
            assert connected_and_dominating(bits, adj)
        constructions += len(sets)
    print('VERIFY_OK exhaustive_orders=3..10 nonempty_subsets='+str(checked),
          'connected_dominating_subsets='+str(reached),
          'explicit_sets_orders=11..40 '+str(constructions),
          'minimum_set_profiles=PASS disjoint_construction=PASS')


if __name__ == '__main__':
    verify()
