#!/usr/bin/env python3
"""Independent finite tests of the VC formula for maximal grid antichains.

Run: python3 verify_maximal_antichain_grid.py
No external packages or input files are required.
"""
from itertools import combinations


def comparable(a, b):
    return ((a[0] <= b[0] and a[1] <= b[1])
            or (b[0] <= a[0] and b[1] <= a[1]))


def concepts(m, n):
    grid = [(i, j) for i in range(m) for j in range(n)]
    output = []
    for size in range(1, min(m, n) + 1):
        for rows in combinations(range(m), size):
            for cols in combinations(range(n), size):
                A = tuple(zip(rows, reversed(cols)))
                # No cell can be added without violating incomparability.
                if all(any(comparable(p, a) for a in A) for p in grid):
                    output.append(frozenset(A))
    return output


def is_shattered(support, hypotheses):
    patterns = {tuple(int(s in A) for s in support) for A in hypotheses}
    return len(patterns) == (1 << len(support))


def dimension_bruteforce(m, n):
    H = concepts(m, n)
    best = 0
    checked = 0
    # Every shattered support is an antichain: all-positive labeling.
    for k in range(1, min(m, n) + 1):
        any_support = False
        for rows in combinations(range(m), k):
            for cols in combinations(range(n), k):
                support = tuple(zip(rows, reversed(cols)))
                checked += 1
                if is_shattered(support, H):
                    any_support = True
        if not any_support:
            break
        best = k
    return best, len(H), checked


def local_gadget_tests():
    H = concepts(2, 3)
    S = ((0, 2), (1, 0))
    patterns = {tuple(int(s in A) for s in S) for A in H}
    assert patterns == {(0, 0), (0, 1), (1, 0), (1, 1)}
    H1 = concepts(1, 2)
    assert {int((0, 0) in A) for A in H1} == {0, 1}
    return 'local_gadgets_ok'


def main():
    local_gadget_tests()
    examined = 0
    for m in range(1, 8):
        for n in range(m, 8):
            dim, nh, examined_supports = dimension_bruteforce(m, n)
            predicted = min(m, n, 2 * (m + n) // 5)
            assert dim == predicted, (m, n, dim, predicted)
            examined += examined_supports
            if m == n == 7:
                assert nh == 817
            print(f'{m}x{n}: concepts={nh}, VC={dim}, checked_antichains={examined_supports}')
    print(f'GRID_MAXIMAL_ANTICHAIN_VC_PASS: 28_rectangles; '
          f'{examined}_candidate_supports; local_gadgets_ok')


if __name__ == '__main__':
    main()
