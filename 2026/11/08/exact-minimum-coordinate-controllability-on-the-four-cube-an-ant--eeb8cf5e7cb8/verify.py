#!/usr/bin/env python3
"""Exact arithmetic certificate for minimum coordinate actuation on the four-cube.

A 6-by-6 sign matrix has determinant of magnitude at most 6**3=216
(Hadamard's inequality). Thus every relevant minor vanishes over Q iff it
vanishes modulo 257. All ranks in this program are exact.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb

P = 257
D = 4
VERTICES = range(1 << D)


def rank_mod(rows, prime=P):
    a = [[int(z) % prime for z in row] for row in rows]
    nr, nc = len(a), len(a[0])
    pivot_row = 0
    for j in range(nc):
        pivot = next((i for i in range(pivot_row, nr) if a[i][j]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        inv = pow(a[pivot_row][j], -1, prime)
        a[pivot_row] = [z * inv % prime for z in a[pivot_row]]
        for i in range(pivot_row + 1, nr):
            if a[i][j]:
                c = a[i][j]
                a[i] = [(v - c*w) % prime for v, w in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == min(nr, nc):
            break
    return pivot_row


CHARS = {
    k: [sum(1 << j for j in J) for J in combinations(range(D), k)]
    for k in range(D + 1)
}


def level_rank(leaders, k):
    return rank_mod([
        [1 - 2 * ((x & mask).bit_count() & 1) for mask in CHARS[k]]
        for x in leaders
    ])


def pb_h_valid(leaders):
    return all(level_rank(leaders,k) == comb(D,k) for k in range(D+1))


PAIRS = tuple(range(8))  # x in 0..7 indexes antipodal class {x, x xor 15}


def structural(leaders):
    used = {min(x, x ^ 15) for x in leaders}
    if len(used) != 6:
        return False
    omitted = set(PAIRS) - used
    return len(omitted) == 2 and sum(x.bit_count() & 1 for x in omitted) == 1


def transform(leaders, perm, flip):
    return tuple(sorted(
        sum(1 << perm[j] for j in range(D) if (x >> j) & 1) ^ flip
        for x in leaders
    ))


def main():
    good = []
    total = 0
    for L in combinations(VERTICES, 6):
        total += 1
        exact = pb_h_valid(L)
        claim = structural(L)
        assert exact == claim, ('PBH and parity criterion differ', L)
        if exact:
            good.append(L)
    assert total == 8008
    assert len(good) == 1024

    # Independent direct test of the eigenspace lower bound for all sizes < 6.
    assert comb(4,2) == 6

    unvisited = set(good)
    perms = tuple(permutations(range(D)))
    orbits = []
    while unvisited:
        seed = min(unvisited)
        orb = {transform(seed, sigma, t) for sigma in perms for t in VERTICES}
        assert len(orb) <= 384 and orb <= unvisited
        unvisited.difference_update(orb)
        orbits.append((min(orb), len(orb)))
    orbits.sort(key=lambda a: (a[1], a[0]))
    sizes = sorted(size for rep, size in orbits)
    assert len(orbits) == 8
    assert sizes == [32,32,96,96,192,192,192,192]
    assert sum(sizes) == len(good)
    print('All 8008 six-subsets: modular PBH criterion agrees with parity test.')
    print('Controllable minimal leader sets:', len(good))
    print('Automorphism orbits:', len(orbits), '; sizes:', sizes)
    print('Canonical orbit representatives (decimal binary labels):')
    for rep, size in orbits:
        print(f'  {size:3d}  {rep}')
    print('EXACT VERIFICATION PASS')


if __name__ == '__main__':
    main()
