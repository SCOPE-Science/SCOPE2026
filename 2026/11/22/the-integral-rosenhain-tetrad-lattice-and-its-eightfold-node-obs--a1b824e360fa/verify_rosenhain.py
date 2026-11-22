#!/usr/bin/env python3
"""Exact certificate for the node--Rosenhain tetrad incidence lattice.

Only Python's standard library is needed. Node labels are integers 0,...,15,
with their binary digits giving coordinates on the four-dimensional 2-torsion.
"""
from itertools import combinations
import csv
from pathlib import Path


def bitsum(a):
    return a.bit_count() % 2


def pairing(a, b):
    # B(a,b) = (sum a_i)(sum b_i) + sum a_i b_i in F_2.
    return bitsum(a) * bitsum(b) ^ bitsum(a & b)


def quadratic(a):
    return sum(((a >> i) & 1) * ((a >> j) & 1)
               for i in range(4) for j in range(i + 1, 4)) % 2


def tetrads():
    directions = set()
    for a, b in combinations(range(1, 16), 2):
        if pairing(a, b) == 1:
            directions.add(tuple(sorted((0, a, b, a ^ b))))
    assert len(directions) == 20
    out = {
        tuple(sorted(v ^ z for v in direction))
        for direction in directions
        for z in range(16)
    }
    assert len(out) == 80
    return sorted(out)


def determinant_bareiss(A):
    """Exact integer determinant; no floating point or external libraries."""
    a = [list(map(int, r)) for r in A]
    n = len(a)
    assert all(len(r) == n for r in a)
    sign, prev = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            for t in range(k + 1, n):
                if a[t][k]:
                    a[k], a[t] = a[t], a[k]
                    sign = -sign
                    break
            else:
                return 0
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                z = a[i][j] * pivot - a[i][k] * a[k][j]
                assert z % prev == 0
                a[i][j] = z // prev
        for i in range(k + 1, n):
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def certificate_rows():
    return [0, 3, 7, 12, 13, 24, 26, 35,
            42, 44, 49, 60, 68, 69, 70, 72]


def main():
    T = tetrads()
    # Each affine non-isotropic plane has four nodes and quadratic parity 1.
    for t in T:
        assert len(t) == 4
        assert sum(quadratic(v) for v in t) % 2 == 1
        assert all(sum((v >> i) & 1 for v in t) % 2 == 0
                   for i in range(4))
        a, b, c, d = t
        assert a ^ b ^ c ^ d == 0
        assert pairing(a ^ b, a ^ c) == 1
    A = [[int(v in t) for v in range(16)] for t in T]
    selected = certificate_rows()
    d1 = determinant_bareiss([A[i] for i in selected])
    d2 = determinant_bareiss([[A[i][v] for i in selected]
                              for v in range(16)])
    assert d1 == d2 and abs(d1) == 128, (d1, d2)
    # Characteristic signatures of the explicit quotient map:
    # Phi(e_0)=(1,0), Phi(e_{2^i}-e_0)=(0, standard_i).
    assert quadratic(0) == 0
    for i in range(4):
        assert quadratic(1 << i) == 0
    # Exact order of the class of each node: Phi(8e_v)=0, Phi(4e_v)!=0.
    for v in range(16):
        assert (8 - 32 * quadratic(v)) % 8 == 0
        assert (4 - 16 * quadratic(v)) % 8 == 4
    # Optional independent on-disk enumeration certificate, if alongside script.
    csv_path = Path(__file__).with_name('rosenhain_80.csv')
    if csv_path.exists():
        with csv_path.open(encoding='utf-8', newline='') as f:
            rows = list(csv.DictReader(f))
        assert [(int(r['node0']), int(r['node1']), int(r['node2']),
                 int(r['node3'])) for r in rows] == T
        assert [int(r['index']) for r in rows] == list(range(80))
        assert [int(r['index']) for r in rows if int(r['minor'])] == selected
    print('VERIFIED_80_ROSENHAIN_TETRADS_16_MINOR_INDEX_128_DET_%s' % d1)
    print('COORDINATE_MOMENTS_4_ZERO_QUADRATIC_MOMENT_ODD')
    print('QUOTIENT_Z8_PLUS_Z2_POWER4_NODE_ORDER8')


if __name__ == '__main__':
    main()
