#!/usr/bin/env python3
"""Exact linear-algebra checker for dihedral/quaternion modular ideal lattices.
This program does not use a computer algebra system or any external packages.
"""
from collections import Counter
from itertools import combinations, product


def group_table(m, quaternion):
    assert m >= 4 and m & (m - 1) == 0
    elts = [(a, b) for b in range(2) for a in range(m)]
    idx = {g: i for i, g in enumerate(elts)}
    table = []
    for a, b in elts:
        table.append([])
        for c, d in elts:
            exponent = (a + (c if b == 0 else -c) + (m // 2 if quaternion and b and d else 0)) % m
            table[-1].append(idx[(exponent, (b + d) % 2)])
    return table


def canonical_subspaces(n):
    """Every binary subspace has one RREF basis; enumerate all of them."""
    for dim in range(n + 1):
        for pivots in combinations(range(n), dim):
            free = [(i, j) for i, p in enumerate(pivots)
                    for j in range(p + 1, n) if j not in pivots]
            for choices in product((0, 1), repeat=len(free)):
                rows = [1 << p for p in pivots]
                for (i, j), choice in zip(free, choices):
                    if choice:
                        rows[i] |= 1 << j
                yield tuple(rows), pivots


def contains(vector, rows, pivots):
    for row, pivot in zip(rows, pivots):
        if (vector >> pivot) & 1:
            vector ^= row
    return vector == 0


def permutation_action(word, perm):
    result = 0
    for j in range(len(perm)):
        if (word >> j) & 1:
            result ^= 1 << perm[j]
    return result


def augmentation_to_groupword(row):
    return (row << 1) | (row.bit_count() & 1)


def groupword_to_augmentation(word):
    assert word.bit_count() % 2 == 0
    return word >> 1


def both_sided_ideals(m, quaternion):
    """Exhaustive only for m=4; all ideals lie inside the 7-space J except kG."""
    assert m == 4
    tab = group_table(m, quaternion)
    left = [[tab[g][x] for x in range(8)] for g in (1, m)]
    right = [[tab[x][g] for x in range(8)] for g in (1, m)]
    result, left_hist, all_seen = {}, Counter(), 0
    for rows, pivots in canonical_subspaces(7):
        all_seen += 1
        def closed(permutations):
            return all(contains(groupword_to_augmentation(permutation_action(
                augmentation_to_groupword(row), perm)), rows, pivots)
                for row in rows for perm in permutations)
        is_left = closed(left)
        is_right = closed(right)
        if is_left:
            left_hist[len(rows)] += 1
        if is_left and is_right:
            result[rows] = len(rows)
    assert all_seen == 29212
    left_hist[8] += 1  # whole ring
    return result, left_hist


def closure_under_two_sided_products(table, word):
    """Return binary span of all g*word*h, expressed as canonical basis masks."""
    n = len(table)
    basis = {}
    for g in range(n):
        for h in range(n):
            v = 0
            for x in range(n):
                if (word >> x) & 1:
                    v ^= 1 << table[table[g][x]][h]
            while v:
                pivot = v.bit_length() - 1
                if pivot not in basis:
                    basis[pivot] = v
                    break
                v ^= basis[pivot]
    return tuple(sorted(basis.items()))


def equal_spans(a, b):
    def member(v, basis):
        for p, w in reversed(basis):
            if (v >> p) & 1:
                v ^= w
        return v == 0
    return all(member(v, b) for p,v in a) and all(member(v, a) for p,v in b)


def run():
    d, dleft = both_sided_ideals(4, False)
    q, qleft = both_sided_ideals(4, True)
    assert d == q, ('different two-sided ideal sets', set(d)^set(q))
    assert sorted(Counter(d.values()).items()) == [(0,1),(1,1),(2,3),(3,1),(4,3),(5,1),(6,3),(7,1)]
    assert tuple(dleft[i] for i in range(9)) == (1,1,3,5,11,5,3,1,1)
    assert tuple(qleft[i] for i in range(9)) == (1,1,3,1,3,1,3,1,1)
    print('F2[D8] left-by-dimension',tuple(dleft[i] for i in range(9)))
    print('F2[Q8] left-by-dimension',tuple(qleft[i] for i in range(9)))
    print('D8 and Q8 exact two-sided ideals inside the radical:',len(d))
    for m in (8, 16):
        for mask in [1, 3, 5, 17, 43, 127, 129, (1 << m) + 1,
                     (1 << (2*m-1)) | (1 << (m//2)) | 1]:
            a = closure_under_two_sided_products(group_table(m, False), mask)
            b = closure_under_two_sided_products(group_table(m, True), mask)
            assert equal_spans(a, b), (m, mask, a, b)
        print('checked principal two-sided ideal generators at group order',2*m)
    print('DIHEDRAL_QUATERNION_TWO_SIDED_LATTICE_DIRECT_CHECK_PASS')


if __name__ == '__main__':
    run()
