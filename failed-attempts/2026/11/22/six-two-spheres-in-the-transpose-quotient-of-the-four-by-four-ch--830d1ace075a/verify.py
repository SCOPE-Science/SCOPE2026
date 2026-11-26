#!/usr/bin/env python3
"""Exact finite computation for the transpose orbit of the 4-by-4 chessboard complex.

No external packages needed. The proof uses integral unit-pivot chain contractions;
this program only certifies the finite homology calculation, not simple connectivity.
"""
from collections import defaultdict
from itertools import combinations, permutations

N = 4

def transpose(mask):
    out = 0
    for i in range(N):
        for j in range(N):
            if mask & (1 << (N * i + j)):
                out |= 1 << (N * j + i)
    return out

def orbit_flag(flag):
    t = tuple(transpose(f) for f in flag)
    return min(flag, t)

def make_complex():
    faces = set()
    original_counts = []
    for size in range(1, N + 1):
        count = 0
        for rows in combinations(range(N), size):
            for cols in permutations(range(N), size):
                f = sum(1 << (N * r + c) for r, c in zip(rows, cols))
                assert f not in faces
                faces.add(f)
                count += 1
        original_counts.append(count)
    assert original_counts == [16, 72, 96, 24]
    # All strict subfaces, each a valid nonattacking-rook configuration.
    flags = {}
    for f in sorted(faces, key=lambda v: (v.bit_count(), v)):
        subfaces = [s for s in faces if s != f and s & f == s]
        flags[f] = [(f,)] + [c + (f,) for s in subfaces for c in flags[s]]
    orbit_cells = {orbit_flag(c) for family in flags.values() for c in family}
    cells = [sorted(c for c in orbit_cells if len(c) == k + 1)
             for k in range(N)]
    assert [len(c) for c in cells] == [125, 586, 768, 300]
    idx = [{c: i for i, c in enumerate(level)} for level in cells]
    boundaries = [{} for _ in range(N)]
    for k in range(1, N):
        for j, chain in enumerate(cells[k]):
            col = defaultdict(int)
            for t in range(k + 1):
                face = orbit_flag(chain[:t] + chain[t + 1:])
                col[idx[k - 1][face]] += (-1) ** t
            boundaries[k][j] = {i: a for i, a in col.items() if a}
    return boundaries, [len(c) for c in cells]

def boundary_square_zero(boundaries):
    for k in range(2, N):
        for c in boundaries[k].values():
            output = defaultdict(int)
            for i, coeff in c.items():
                for j, second in boundaries[k - 1][i].items():
                    output[j] += coeff * second
            assert all(v == 0 for v in output.values()), k

def rank_mod_two(columns):
    basis = {}
    for column in columns.values():
        mask = 0
        for i, a in column.items():
            if a % 2:
                mask ^= 1 << i
        while mask:
            pivot = mask.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = mask
                break
            mask ^= basis[pivot]
    return len(basis)

def contract_all_unit_pivots(boundaries, sizes):
    # Integral elementary basis changes split one Z -> Z isomorphism at a time.
    active = [set(range(s)) for s in sizes]
    canceled = defaultdict(int)
    for k in range(N - 1, 0, -1):
        while True:
            row_to_columns = defaultdict(set)
            for j, col in boundaries[k].items():
                for i in col:
                    row_to_columns[i].add(j)
            pivot = None
            best_cost = float('inf')
            for j, col in boundaries[k].items():
                for i, val in col.items():
                    if abs(val) == 1:
                        cost = (len(col) - 1) * (len(row_to_columns[i]) - 1)
                        if cost < best_cost:
                            best_cost = cost
                            pivot = (i, j, val)
            if pivot is None:
                break
            i, j, a = pivot
            source = boundaries[k][j]
            # Column elimination over the integers; the pivot is exactly a unit.
            for other in list(row_to_columns[i]):
                if other == j:
                    continue
                column = boundaries[k][other]
                q = column[i] // a
                for r, b in source.items():
                    new = column.get(r, 0) - q * b
                    if new:
                        column[r] = new
                    else:
                        column.pop(r, None)
            if k + 1 < N:
                for col in boundaries[k + 1].values():
                    col.pop(j, None)
            if k - 1 > 0:
                boundaries[k - 1].pop(i, None)
            boundaries[k].pop(j)
            active[k].remove(j)
            active[k - 1].remove(i)
            canceled[k] += 1
        boundary_square_zero(boundaries)
    remaining = [len(s) for s in active]
    assert dict(canceled) == {3: 300, 2: 462, 1: 124}
    assert remaining == [1, 0, 6, 0]
    assert all(not any(col.values()) for d in boundaries for col in d.values())
    return canceled, remaining

def fixed_chi():
    # Direct enumerate the equivariant rook-square orbits admitting an invariant face.
    squares = set(range(N * N))
    admissible_orbits = []
    while squares:
        a = min(squares)
        b = (a % N) * N + a // N
        orb = {a, b}
        squares -= orb
        rows = [x // N for x in orb]
        cols = [x % N for x in orb]
        if len(rows) == len(set(rows)) and len(cols) == len(set(cols)):
            admissible_orbits.append(tuple(sorted(orb)))
    f = [0] * N
    for k in range(1, N + 1):
        for chosen in combinations(admissible_orbits, k):
            union = [z for orbit in chosen for z in orbit]
            rows = [v // N for v in union]
            cols = [v % N for v in union]
            if len(rows) == len(set(rows)) and len(cols) == len(set(cols)):
                f[k - 1] += 1
    assert f == [10, 21, 10, 1]
    return sum((-1) ** i * v for i, v in enumerate(f))

def main():
    boundary, sizes = make_complex()
    boundary_square_zero(boundary)
    mod2 = [0] + [rank_mod_two(boundary[k]) for k in range(1, N)]
    assert mod2 == [0, 124, 462, 300]
    fixed_euler = fixed_chi()
    assert fixed_euler == -2
    original_euler = 16 - 72 + 96 - 24
    orbit_euler = sum((-1) ** k * n for k, n in enumerate(sizes))
    assert orbit_euler == (original_euler + fixed_euler) // 2 == 7
    canceled, remaining = contract_all_unit_pivots(boundary, sizes)
    print('original_faces: 16 72 96 24')
    print('quotient_barycentric_cells: 125 586 768 300')
    print('quotient_Euler: 7; independent_Burnside_Euler: 7')
    print('mod_2_boundary_ranks: 124 462 300')
    print('integral_unit_cancellations: 124 462 300 (degrees 1,2,3)')
    print('residual_integral_chain_ranks: 1 0 6 0')
    print('integral_homology: H0=Z, H2=Z^6, all_other=0')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
