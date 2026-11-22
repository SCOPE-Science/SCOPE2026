#!/usr/bin/env python3
"""Exact-integer checks for dyadic Haar mask projection in path variation.

All matrix entries are scaled by n, so there are no floating-point comparisons.
"""
from itertools import product


def basis(d):
    n = 1 << d
    nodes = []
    for lev in range(d):
        length = n >> lev
        for block in range(1 << lev):
            start = block * length
            signs = [0] * n
            for i in range(start, start + length // 2):
                signs[i] = 1
            for i in range(start + length // 2, start + length):
                signs[i] = -1
            parent = ((1 << (lev - 1)) - 1 + block // 2) if lev else -1
            nodes.append((parent, length, signs))
    return nodes


def scaled_jumps(d):
    n = 1 << d
    terms = []
    for parent, length, h in basis(d):
        dh = [h[i + 1] - h[i] for i in range(n - 1)]
        tail = [sum(h[j:]) for j in range(1, n)]
        q = n // length
        terms.append([q * a * b for a in dh for b in tail])
    return terms


def norm_num(m, n):
    return max(sum(abs(m[i * (n - 1) + j]) for i in range(n - 1))
               for j in range(n - 1))


def exact_exhaustion(d):
    n = 1 << d
    k = n - 1
    terms = scaled_jumps(d)
    parents = [item[0] for item in basis(d)]
    mat = [0] * (k * k)
    prev = 0
    non_tree_min = 10 ** 12
    checked = 0
    hereditary_count = 0
    for step in range(1 << k):
        mask = step ^ (step >> 1)
        if step:
            idx = (mask ^ prev).bit_length() - 1
            delta = 1 if mask & (1 << idx) else -1
            mat = [x + delta * y for x, y in zip(mat, terms[idx])]
        prev = mask
        hereditary = all(
            parents[i] < 0 or (mask & (1 << parents[i]))
            for i in range(k) if mask & (1 << i)
        )
        val = norm_num(mat, n)
        if hereditary:
            hereditary_count += 1
            assert val == (n if mask else 0), (d, mask, val)
        else:
            assert val >= 3 * n // 2, (d, mask, val)
            non_tree_min = min(val, non_tree_min)
        checked += 1
    if d >= 2:
        assert non_tree_min == 3 * n // 2, (d, non_tree_min)
    return checked, hereditary_count, (None if d == 1 else f'{non_tree_min}/{n}')


def witness_each_depth():
    for d in range(2, 10):
        n = 1 << d
        # Select just the left child of the root.
        length = n // 2
        h = [1] * (length // 2) + [-1] * (length // 2) + [0] * length
        dh = [h[i + 1] - h[i] for i in range(n - 1)]
        tail = [sum(h[j:]) for j in range(1, n)]
        projected = [(n // length) * a * b for a in dh for b in tail]
        assert norm_num(projected, n) == 3 * n // 2, d
        j = length // 2
        assert sum(abs(dh[i] * tail[j - 1] * (n // length))
                   for i in range(n - 1)) == 3 * n // 2
    print('EXACT_ISOLATED_CHILD_GAP_SHARPNESS_PASS depths_2_to_9')


def main():
    for d in (1, 2, 3, 4):
        n_masks, rooted, floor = exact_exhaustion(d)
        print(f'EXACT_MASK_EXHAUSTION_PASS depth={d} masks={n_masks} rooted={rooted} nonrooted_min={floor}')
    witness_each_depth()
    print('ALL_HAAR_TREE_VARIATION_CHECKS_PASS')


if __name__ == '__main__':
    main()
