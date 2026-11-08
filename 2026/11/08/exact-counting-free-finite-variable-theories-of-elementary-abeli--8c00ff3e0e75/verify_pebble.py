#!/usr/bin/env python3
"""Finite orbit checks for bounded-variable logic of binary additive groups.

Uses linear-dependency kernels to enumerate tuples up to linear automorphism,
then checks the universal local-reply invariant. No external dependencies.
"""

from itertools import combinations


def dimension(values):
    pivots = {}
    for value in values:
        while value:
            lead = value.bit_length() - 1
            if lead in pivots:
                value ^= pivots[lead]
            else:
                pivots[lead] = value
                break
    return len(pivots)


def kernel(values):
    # Each mask describes a binary linear dependence among tuple entries.
    accum = {0: 0}
    for i, value in enumerate(values):
        for mask, partial in list(accum.items()):
            accum[mask | (1 << i)] = partial ^ value
    return frozenset(mask for mask, partial in accum.items() if not partial)


def orbit_representatives(k):
    representatives = {frozenset([0]): ()}
    for _ in range(k):
        new = {}
        for values in representatives.values():
            rank = dimension(values)
            span = {0}
            for item in values:
                span.update({x ^ item for x in tuple(span)})
            for new_item in span | {1 << rank}:
                next_values = values + (new_item,)
                new[kernel(next_values)] = next_values
        representatives = new
    return representatives


def local_moves(values, d, position, k):
    others = values[:position] + values[position + 1:]
    rank = dimension(others)
    span = {0}
    for item in others:
        span.update({x ^ item for x in tuple(span)})
    if d > rank:
        span.add(1 << k)  # An orbit representative outside the old span.
    result = set()
    for item in span:
        next_values = list(values)
        next_values[position] = item
        result.add(kernel(next_values))
    return result


def proper_signature(dependencies, k):
    # Preserve ALL equations supported on fewer than k pebbled positions.
    return frozenset(m for m in dependencies if m.bit_count() < k)


def check_pair(k, small, large):
    representations = orbit_representatives(k)
    left = {q: vals for q, vals in representations.items()
            if dimension(vals) <= small}
    right = {q: vals for q, vals in representations.items()
             if dimension(vals) <= large}
    right_sigs = {}
    for q in right:
        right_sigs.setdefault(proper_signature(q, k), []).append(q)

    pairs = [(q, p) for q in left
             for p in right_sigs.get(proper_signature(q, k), [])]
    assert pairs
    # This relation is a post-fixpoint: every move has a replying move
    # whose resulting kernel still belongs to the relation.
    move_cache = {}
    for side, collection, d in ((0, left, small), (1, right, large)):
        for q, vals in collection.items():
            for position in range(k):
                outcomes = local_moves(vals, d, position, k)
                move_cache[(side, q, position)] = {
                    proper_signature(outcome, k) for outcome in outcomes
                }
    total = 0
    for q, p in pairs:
        for pos in range(k):
            a = move_cache[(0, q, pos)]
            b = move_cache[(1, p, pos)]
            assert a == b, (k, small, large, q, p, pos, a ^ b)
            total += 1
    print(f"PASS k={k} dimensions=({small},{large}) "
          f"orbits=({len(left)},{len(right)}) "
          f"related_orbit_pairs={len(pairs)} "
          f"move_position_checks={total}")


def verify_formula_witness():
    # Six-variable formula for nonzero sum of five named vectors.
    # E5 means x1+x2+x3+x4+x5=0 in characteristic two:
    # exists z (R(x1,x2,z) & exists x1 (R(z,x3,x1)
    #                                    & R(x1,x4,x5))).
    n = 0
    for dim in (4, 5):
        basis = tuple(1 << j for j in range(min(dim, 5)))
        if dim == 5:
            assert len(basis) == 5
            for mask in range(1, 32):
                xor = 0
                for j in range(5):
                    if mask & (1 << j):
                        xor ^= basis[j]
                assert xor != 0
                n += 1
        else:
            subsets = list(combinations(range(1 << dim), 5))
            assert len(subsets) == 4368
            assert all(dimension(s) <= 4 for s in subsets)
            assert len(basis) == 4
        # Check the concrete 5-term formula on arbitrary sample tuples.
        samples = [(0, 0, 0, 0, 0), (1, 2, 4, 8, 15)]
        if dim == 5:
            samples.append((1, 2, 4, 8, 16))
        for x1, x2, x3, x4, x5 in samples:
            evaluated = any((x1 ^ x2 == z) and
                            any((z ^ x3 == overwritten_x1) and
                                (overwritten_x1 ^ x4 == x5)
                                for overwritten_x1 in range(1 << dim))
                            for z in range(1 << dim))
            assert evaluated == (x1 ^ x2 ^ x3 ^ x4 ^ x5 == 0)
    print(f"PASS five-independent-vector witness: {n} nonzero subset sums; "
          "six-variable addition-chain formula checked")


if __name__ == '__main__':
    check_pair(4, 3, 4)
    check_pair(5, 4, 5)
    check_pair(6, 5, 6)
    verify_formula_witness()
    print('ALL CHECKS PASS')
