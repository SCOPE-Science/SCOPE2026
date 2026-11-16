#!/usr/bin/env python3
"""Exact rank-incidence certificate for 5x5 restrictions of the order-15 DFT.

Usage: python3 verify_f15_five.py [f15_five_incidence.json]
Python standard library only. No external inputs are needed to regenerate the ranks.
"""
from itertools import combinations, permutations
from collections import Counter
import json
import sys

N, K = 15, 5
PHI = (1, -1, 0, 1, -1, 1, 0, -1, 1)
EXPECTED = {2: 360, 3: 24480, 4: 880920, 5: 8112249}


def roots_in_integer_basis():
    roots = []
    for t in range(N):
        p = [0] * 15
        p[t] = 1
        for degree in range(14, 7, -1):
            v = p[degree]
            if v:
                for j in range(8):
                    p[degree - 8 + j] -= v * PHI[j]
                p[degree] = 0
        roots.append(tuple(p[:8]))
    assert all(roots[(t + N) % N] == roots[t] for t in range(N))
    return roots


ROOT = roots_in_integer_basis()
SIGNED = {}
for d in range(1, K + 1):
    SIGNED[d] = []
    for perm in permutations(range(d)):
        parity = sum(perm[i] > perm[j] for i in range(d)
                     for j in range(i + 1, d))
        SIGNED[d].append((perm, -1 if parity % 2 else 1))


def is_zero_minor(rows, cols):
    d = len(rows)
    assert d == len(cols)
    counts = [0] * N
    for perm, sign in SIGNED[d]:
        exponent = sum(rows[i] * cols[perm[i]] for i in range(d)) % N
        counts[exponent] += sign
    return all(sum(counts[t] * ROOT[t][j] for t in range(N)) == 0
               for j in range(8))


def exact_rank(rows, cols):
    if not is_zero_minor(rows, cols):
        return 5
    for i in range(5):
        r = rows[:i] + rows[i + 1:]
        for j in range(5):
            c = cols[:j] + cols[j + 1:]
            if not is_zero_minor(r, c):
                return 4
    for ii in combinations(range(5), 3):
        r = tuple(rows[i] for i in ii)
        for jj in combinations(range(5), 3):
            c = tuple(cols[j] for j in jj)
            if not is_zero_minor(r, c):
                return 3
    # Prove the residual lower bound, rather than assuming rank >= 2.
    for ii in combinations(range(5), 2):
        r = tuple(rows[i] for i in ii)
        for jj in combinations(range(5), 2):
            c = tuple(cols[j] for j in jj)
            if not is_zero_minor(r, c):
                return 2
    return 1


def translation_orbits():
    unseen = set(combinations(range(N), K))
    out = []
    while unseen:
        rep = min(unseen)
        orbit = {tuple(sorted((x + t) % N for x in rep))
                 for t in range(N)}
        assert orbit <= unseen
        unseen.difference_update(orbit)
        out.append((rep, len(orbit)))
    assert len(out) == 201
    assert Counter(size for _, size in out) == {15: 200, 3: 1}
    assert sum(w for _, w in out) == 3003
    return out


def rank_mod(matrix, p):
    a = [list(row) for row in matrix]
    k = 0
    for c in range(5):
        pivot = next((i for i in range(k, 5) if a[i][c]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        mult = pow(a[k][c], p - 2, p)
        a[k] = [(v * mult) % p for v in a[k]]
        for i in range(k + 1, 5):
            if a[i][c]:
                t = a[i][c]
                a[i] = [(v - t * w) % p for v, w in zip(a[i], a[k])]
        k += 1
    return k


def crosscheck_modular(orbits, ranks):
    # Both primes split X^15-1; modular ranks can only UNDERestimate
    # complex ranks. The maximum of the two ranks matches exact ranks.
    lower = [[0] * 201 for _ in range(201)]
    for p, g in ((31, 3), (61, 2)):
        omega = pow(g, (p - 1) // N, p)
        assert pow(omega, N, p) == 1
        assert all(pow(omega, N // q, p) != 1 for q in (3, 5))
        roots = [pow(omega, t, p) for t in range(N)]
        for i, (r, _) in enumerate(orbits):
            for j, (c, _) in enumerate(orbits):
                mat = [[roots[x * y % N] for y in c] for x in r]
                a = rank_mod(mat, p)
                assert a <= ranks[i][j]
                lower[i][j] = max(lower[i][j], a)
    assert lower == ranks


def rank2_structural(r, c):
    h = lambda a: len({v % 3 for v in a}) == 1
    two = lambda a: len({v % 5 for v in a}) == 2
    return (h(r) and two(c)) or (h(c) and two(r))


def certify():
    orbits = translation_orbits()
    matrix = []
    counts = Counter()
    count2_pairs = 0
    rank1 = 0
    for r, wr in orbits:
        row = []
        for c, wc in orbits:
            rank = exact_rank(r, c)
            row.append(rank)
            counts[rank] += wr * wc
            if rank == 2:
                count2_pairs += 1
            if rank == 1:
                rank1 += wr * wc
            assert (rank == 2) == rank2_structural(r, c)
        matrix.append(row)
    assert rank1 == 0
    assert count2_pairs == 8
    assert counts == EXPECTED
    assert sum(counts.values()) == 3003 * 3003
    assert all(matrix[i][j] == matrix[j][i] for i in range(201) for j in range(201))
    crosscheck_modular(orbits, matrix)
    cert = {
        'order': N, 'minor_order': K,
        'orbit_type': 'translation',
        'orbit_representatives': [list(a) for a, _ in orbits],
        'orbit_sizes': [w for _, w in orbits],
        'rank_incidence': matrix,
        'global_rank_counts': {str(k): counts[k] for k in sorted(counts)},
    }
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding='utf-8') as f:
            assert json.load(f) == cert
    print('EXACT_F15_FIVE_CERTIFICATE_OK')
    print('ORBIT_COUNT', len(orbits), 'ORBIT_PAIRS', len(orbits) ** 2)
    print('RANK_TOTALS', dict(sorted(counts.items())))
    print('MODULAR_LOWER_BOUNDS_AGREE', [31, 61])
    return cert


if __name__ == '__main__':
    result = certify()
    if len(sys.argv) == 1:
        with open('f15_five_incidence.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, separators=(',', ':'))
            f.write('\n')
