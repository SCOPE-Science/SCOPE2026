#!/usr/bin/env python3
"""Exact elementary-operation certificate for a three-order incomparability kernel.

Usage: python3 VERIFY.py CERTIFICATE.json
Only the Python standard library is required.
"""
import itertools
import json
import sys


def kernel(n):
    triples = list(itertools.product(range(n + 1), repeat=3))
    return [
        [int(not (all(a < b for a, b in zip(x, y)) or
                  all(a > b for a, b in zip(x, y)))) for y in triples]
        for x in triples
    ]


def apply(A, op):
    t, i, j, c = op
    m = len(A)
    assert 0 <= i < m
    if t in ('R', 'C', 'S', 'T'):
        assert 0 <= j < m
    if t == 'S':
        A[i], A[j] = A[j], A[i]
    elif t == 'T':
        for row in A:
            row[i], row[j] = row[j], row[i]
    elif t == 'N':
        assert c == -1
        A[i] = [-a for a in A[i]]
    elif t == 'R':
        assert i != j and isinstance(c, int)
        A[i] = [x + c*y for x, y in zip(A[i], A[j])]
    elif t == 'C':
        assert i != j and isinstance(c, int)
        for row in A:
            row[i] += c * row[j]
    else:
        raise ValueError(t)


def test_rule(n):
    # Independent feasibility test: compare with all allowed order-sign choices.
    triples = list(itertools.product(range(n + 1), repeat=3))
    M = kernel(n)
    for i, x in enumerate(triples):
        for j, y in enumerate(triples):
            allowed = [((1,) if a < b else (-1,) if a > b else (-1, 1))
                       for a, b in zip(x, y)]
            possible = any(min(o) < 0 < max(o)
                           for o in itertools.product(*allowed))
            assert bool(M[i][j]) == possible
    return len(triples) ** 2



def rank_mod(A, p):
    B = [[x % p for x in row] for row in A]
    m = len(B)
    pivot = 0
    for j in range(m):
        k = next((i for i in range(pivot, m) if B[i][j]), None)
        if k is None:
            continue
        B[k], B[pivot] = B[pivot], B[k]
        inv = pow(B[pivot][j], -1, p)
        B[pivot] = [(inv * v) % p for v in B[pivot]]
        for i in range(pivot + 1, m):
            if B[i][j]:
                coeff = B[i][j]
                B[i] = [(a - coeff*b) % p for a, b in zip(B[i], B[pivot])]
        pivot += 1
        if pivot == m:
            break
    return pivot

def main(path):
    with open(path, encoding='utf-8') as h:
        cert = json.load(h)
    assert cert['schema'] == 'elementary-unimodular-operations-v1'
    expected = {1: ([1]*3 + [0]*5),
                2: ([1]*15 + [2] + [0]*11),
                3: ([1]*44 + [3] + [0]*19)}
    comparisons = 0
    for record in cert['cases']:
        n = record['n']
        assert n in expected
        assert record['target_diagonal'] == expected[n]
        comparisons += test_rule(n)
        M = kernel(n)
        ranks = {p: rank_mod(M, p) for p in (2, 3, 5)}
        expected_ranks = {1: {2: 3, 3: 3, 5: 3},
                          2: {2: 15, 3: 16, 5: 16},
                          3: {2: 45, 3: 44, 5: 45}}
        assert ranks == expected_ranks[n]
        for op in record['operations']:
            apply(M, op)
        N = len(M)
        diag = [M[i][i] for i in range(N)]
        assert diag == expected[n]
        assert all(M[i][j] == 0 for i in range(N) for j in range(N) if i != j)
        print('n=', n, 'dimension=', N, 'unit factors=',diag.count(1),
              'nonunit factors=', [x for x in diag if x > 1],
              'free rank=',diag.count(0), 'ranks=',ranks, 'ops=',len(record['operations']))
    assert sorted(x['n'] for x in cert['cases']) == [1,2,3]
    print('INDEPENDENT_FEASIBILITY_COMPARISONS=',comparisons)
    print('CERTIFICATE_OK')

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'CERTIFICATE.json')
