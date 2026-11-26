#!/usr/bin/env python3
"""Finite checks for the proper conflict-free coloring theorem of rook graphs.

Run with Python 3.9+: python verify_pcf_rook.py
This finite verification is auxiliary; the theorem is proved separately.
"""
from itertools import permutations, product


def is_proper(grid):
    m, n = len(grid), len(grid[0])
    return (all(len(set(row)) == n for row in grid)
            and all(len({grid[i][j] for i in range(m)}) == m for j in range(n)))


def directly_pcf(grid):
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            neighbors = [grid[i][k] for k in range(n) if k != j]
            neighbors += [grid[k][j] for k in range(m) if k != i]
            if not neighbors:
                continue
            if not any(neighbors.count(c) == 1 for c in set(neighbors)):
                return False
    return True


def palette_criterion(grid):
    m, n = len(grid), len(grid[0])
    return all(set(grid[i]) != {grid[k][j] for k in range(m)}
               for i in range(m) for j in range(n)) if m*n > 1 else True


def cyclic_construction(m, n):
    if m == n == 1:
        return ((0,),)
    if m < n:
        return tuple(tuple((i + j) % n for j in range(n)) for i in range(m))
    q = n + 2
    a = [x for x in range(q) if x not in (0, 1)]
    b = [x for x in range(q) if x not in (0, 2)]
    return tuple(tuple((x + y) % q for y in b) for x in a)


def exhaustive(m, n, q):
    count_proper = count_pcf = 0
    rows = tuple(permutations(range(q), n))
    for grid in product(rows, repeat=m):
        if not is_proper(grid):
            continue
        count_proper += 1
        a = directly_pcf(grid)
        b = palette_criterion(grid)
        assert a == b, (m, n, q, grid)
        count_pcf += a
    expected_possible = q >= (n if m < n else n + 2) if m*n > 1 else q >= 1
    # All tested palettes in the loops are large enough to allow a proper
    # grid whenever q>=n; for smaller palettes neither kind can exist.
    assert (count_pcf > 0) == expected_possible, (m, n, q, count_proper, count_pcf)
    return count_proper, count_pcf


def main():
    construction_sizes = 0
    for m in range(1, 14):
        for n in range(m, 14):
            grid = cyclic_construction(m, n)
            assert is_proper(grid) and directly_pcf(grid) and palette_criterion(grid)
            assert len({x for row in grid for x in row}) == (n if m<n else n+2) if m*n > 1 else True
            construction_sizes += 1
    checks = [
        (1, 1, 1), (1, 2, 2), (1, 4, 4),
        (2, 2, 2), (2, 2, 3), (2, 2, 4),
        (2, 3, 3), (2, 3, 4), (2, 4, 4), (2, 5, 5),
        (3, 3, 3), (3, 3, 4), (3, 3, 5),
        (3, 4, 4), (3, 4, 5), (4, 4, 4),
    ]
    grand_total = grand_pcf = 0
    for m, n, q in checks:
        proper, pcf = exhaustive(m, n, q)
        print(f'K_{m} square K_{n}, palette {q}: {proper} proper; {pcf} PCF')
        grand_total += proper
        grand_pcf += pcf
    print(f'PASS: {construction_sizes} construction sizes; '
          f'{len(checks)} complete proper-coloring enumerations; '
          f'{grand_total} proper color arrays; {grand_pcf} PCF arrays')


if __name__ == '__main__':
    main()
