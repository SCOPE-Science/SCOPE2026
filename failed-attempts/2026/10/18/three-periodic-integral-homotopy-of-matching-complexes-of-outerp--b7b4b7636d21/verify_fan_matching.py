#!/usr/bin/env python3
"""Reproduce finite matching-homology checks for cone-over-path fan graphs.

Dependency-free. Integer bitsets implement boundary reductions over F_2.
The all-n sphere-wedge statement is proved separately, not by these tests.
"""


def edges(n):
    return [(i, i + 1) for i in range(n - 1)] + [(n, i) for i in range(n)]


def tiers(n):
    es = edges(n)
    vertex_masks = [(1 << a) | (1 << b) for a, b in es]
    out = [[0]]
    for degree in range(1, (n + 1) // 2 + 1):
        now = []
        for mask in out[-1]:
            occupied = 0
            for j, edge_v in enumerate(vertex_masks):
                if mask & (1 << j):
                    occupied |= edge_v
            for j in range(mask.bit_length(), len(es)):
                if not occupied & vertex_masks[j]:
                    now.append(mask | (1 << j))
        if not now:
            break
        assert len(now) == len(set(now))
        out.append(now)
    return out


def ranks_mod2(rows):
    ranks = []
    for k in range(1, len(rows)):
        indices = {face: j for j, face in enumerate(rows[k - 1])}
        basis = {}
        for simplex in rows[k]:
            remaining = simplex
            column = 0
            while remaining:
                bit = remaining & -remaining
                remaining ^= bit
                column ^= 1 << indices[simplex ^ bit]
            while column:
                pivot = column.bit_length() - 1
                if pivot not in basis:
                    basis[pivot] = column
                    break
                column ^= basis[pivot]
        ranks.append(len(basis))
    return ranks


def reduced_betti(rows, ranks):
    beta = []
    for j in range(1, len(rows)):
        incoming = ranks[j - 1]
        outgoing = ranks[j] if j < len(ranks) else 0
        value = len(rows[j]) - incoming - outgoing
        assert value >= 0
        beta.append(value)
    return beta


def predicted(n):
    q, r = divmod(n, 3)
    if r == 0:
        return q - 1, q + 1
    if r == 1:
        return q, q
    return q, 2 * q + 2


def path_matching_polynomial(m):
    # A matching of P_m either skips vertex m-1 or uses its last edge.
    a, b = [1], [1]
    for _ in range(2, m + 1):
        c = [0] * (max(len(b), len(a) + 1))
        for i, v in enumerate(b):
            c[i] += v
        for i, v in enumerate(a):
            c[i + 1] += v
        a, b = b, c
    return b if m >= 1 else a


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def fan_polynomial(n):
    result = list(path_matching_polynomial(n))
    for i in range(1, n + 1):
        component = mul(path_matching_polynomial(i - 1), path_matching_polynomial(n - i))
        for j, count in enumerate(component, 1):
            if j >= len(result):
                result.extend([0] * (j + 1 - len(result)))
            result[j] += count
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


if __name__ == '__main__':
    for n in range(2, 16):
        rows = tiers(n)
        ranks = ranks_mod2(rows)
        observed = reduced_betti(rows, ranks)
        dimension, multiplicity = predicted(n)
        expected = [multiplicity if d == dimension else 0 for d in range(len(observed))]
        assert observed == expected, (n, observed, expected)
        poly = fan_polynomial(n)
        assert [len(t) for t in rows] == poly, (n, [len(t) for t in rows], poly)
        reduced_euler = -sum(((-1) ** j) * count for j, count in enumerate(poly))
        assert reduced_euler == ((-1) ** dimension) * multiplicity
        print(f'n={n:2d} degree={dimension} spheres={multiplicity:2d} '
              f'face_counts={poly} mod2_betti={observed}')
    print('PASS: independent chain-rank, face-polynomial and Euler checks for n=2..15.')
