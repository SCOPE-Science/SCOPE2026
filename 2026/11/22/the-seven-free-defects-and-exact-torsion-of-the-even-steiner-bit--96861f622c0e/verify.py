#!/usr/bin/env python3
"""Reproduce the integral incidence theorem for a marked Cayley octad.

Requires Python 3 standard library. Run as
    python3 verify.py certificate.json
The certificate consists of reversible elementary integer row and column operations.
"""
from itertools import combinations
from collections import Counter
import json
import sys

PAIRS = list(combinations(range(8), 2))
HALVES = list(c for c in combinations(range(8), 4) if 0 in c)
assert len(PAIRS) == 28 and len(HALVES) == 35


def theta_q(v):
    """Parity quadratic form on even-size subsets modulo complementation."""
    assert len(v) % 2 == 0
    return (len(v) // 2) % 2


def pairing(a, b):
    return len(set(a) & set(b)) % 2


def incidence(half, pair):
    # A bitangent is in the Steiner complex exactly if theta(v) = 0.
    # With the chosen even theta origin, theta(v) = q(v) + <pair,v>.
    return int((theta_q(half) + pairing(pair, half)) % 2 == 0)


def matrix():
    return [[incidence(h, e) for e in PAIRS] for h in HALVES]


def rank_mod_p(a, p):
    b = [[v % p for v in row] for row in a]
    m, n = len(b), len(b[0]); k = 0
    for j in range(n):
        pi = next((i for i in range(k, m) if b[i][j]), None)
        if pi is None:
            continue
        b[k], b[pi] = b[pi], b[k]
        inv = pow(b[k][j], -1, p)
        b[k] = [(v * inv) % p for v in b[k]]
        for i in range(k + 1, m):
            t = b[i][j]
            if t:
                b[i] = [(x - t * y) % p for x, y in zip(b[i], b[k])]
        k += 1
        if k == m:
            break
    return k


def apply(a, op):
    kind, i, *rest = op
    m, n = len(a), len(a[0])
    if kind == 'Rswap':
        j, = rest
        assert 0 <= i < m and 0 <= j < m
        a[i], a[j] = a[j], a[i]
    elif kind == 'Cswap':
        j, = rest
        assert 0 <= i < n and 0 <= j < n
        for row in a:
            row[i], row[j] = row[j], row[i]
    elif kind == 'Radd':
        j, t = rest
        assert 0 <= i < m and 0 <= j < m and i != j and isinstance(t, int)
        a[i] = [x + t * y for x, y in zip(a[i], a[j])]
    elif kind == 'Cadd':
        j, t = rest
        assert 0 <= i < n and 0 <= j < n and i != j and isinstance(t, int)
        for row in a:
            row[i] += t * row[j]
    elif kind == 'Rneg':
        assert not rest and 0 <= i < m
        a[i] = [-x for x in a[i]]
    else:
        raise ValueError('Unknown operation')


def main(filename):
    m = matrix()
    assert [sum(row) for row in m] == [12] * 35
    assert [sum(m[i][j] for i in range(35)) for j in range(28)] == [15] * 28
    assert all(incidence(h, e) == int(len(set(h) & set(e)) in (0, 2))
               for h in HALVES for e in PAIRS)
    # Exact Gram entries: two equal pairs, pairs sharing a vertex,
    # and disjoint pairs give 15, 5, and 7 respectively.
    gram = [[sum(row[i] * row[j] for row in m)
             for j in range(28)] for i in range(28)]
    for i, e in enumerate(PAIRS):
        for j, f in enumerate(PAIRS):
            assert gram[i][j] == (15 if i == j else
                                  5 if len(set(e) & set(f)) == 1 else 7)
    # Rational 7-dimensional kernel, witnessed by zero-sum vertex weights.
    for k in range(7):
        a = [0] * 8; a[k] = 1; a[7] = -1
        weights = [a[i] + a[j] for i, j in PAIRS]
        assert all(sum(row[j] * weights[j] for j in range(28)) == 0 for row in m)
    # S_8 equivariance checked on generating adjacent transpositions.
    lookup_h = {h: i for i, h in enumerate(HALVES)}
    lookup_e = {e: i for i, e in enumerate(PAIRS)}
    for k in range(7):
        perm = list(range(8)); perm[k], perm[k+1] = perm[k+1], perm[k]
        for i, h in enumerate(HALVES):
            hh = tuple(sorted(perm[a] for a in h))
            if 0 not in hh: hh = tuple(sorted(set(range(8)) - set(hh)))
            ii = lookup_h[hh]
            for j, e in enumerate(PAIRS):
                jj = lookup_e[tuple(sorted(perm[a] for a in e))]
                assert m[ii][jj] == m[i][j]
    cert = json.load(open(filename, encoding='utf-8'))
    assert isinstance(cert, list) and len(cert) > 0
    b = [row[:] for row in m]
    for op in cert:
        apply(b, op)
    diag = [b[i][i] for i in range(28)]
    assert all(b[i][j] == 0 for i in range(35) for j in range(28) if i != j)
    assert diag == [1] * 7 + [2] * 13 + [6] + [0] * 7, diag
    assert rank_mod_p(m, 2) == 7
    assert rank_mod_p(m, 3) == 20
    assert rank_mod_p(m, 5) == 21
    print('VERIFIED: 35 even Steiner complexes, 28 bitangents; '
          'Smith=1^7 2^13 6 0^7; torsion=49152; '
          'Gram=(180^1,0^7,12^20); '
          f'{len(cert)} unimodular operations; ranks_mod_2_3_5=7_20_21')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python3 verify.py certificate.json')
    main(sys.argv[1])
