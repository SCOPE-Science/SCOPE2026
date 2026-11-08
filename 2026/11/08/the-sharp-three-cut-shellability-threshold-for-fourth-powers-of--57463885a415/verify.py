#!/usr/bin/env python3
"""Exact finite verification of three-cut complexes of fourth powers of cycles.

Run with Python >= 3.9 from any directory. All inputs are carried next to this file.
No optional dependencies. Orders consist of triples whose complements are facets.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter

ROOT = Path(__file__).resolve().parent


def edges(n):
    return [set(j for j in range(n) if j != i and min((j-i) % n, (i-j) % n) <= 4)
            for i in range(n)]


def connected_three(t, nbr):
    """Independent DFS, without using edge-count shortcuts."""
    seen = {t[0]}
    stack = [t[0]]
    while stack:
        u = stack.pop()
        for v in t:
            if v not in seen and v in nbr[u]:
                seen.add(v)
                stack.append(v)
    return len(seen) == 3


def bad_triples(n):
    nbr = edges(n)
    return set(t for t in combinations(range(n), 3) if not connected_three(t, nbr))


def check_shelling(n):
    universe = bad_triples(n)
    lines = (ROOT / f'p4_n{n}_order.txt').read_text(encoding='utf-8').splitlines()
    order = [tuple(int(v) for v in line.split(',')) for line in lines]
    assert len(order) == len(universe) and len(order) == len(set(order))
    assert set(order) == universe and all(tuple(sorted(t)) == t for t in order)
    preceding = []
    spanning = 0
    for j, t in enumerate(order):
        T = set(t)
        ridges = set()
        for q in preceding:
            D = set(q) - T
            if len(D) == 1:
                ridges.update(D)
        if j > 0:
            assert ridges, ('missing ridge', n, j)
            # Every intersection with an earlier facet lies in one old ridge.
            for q in preceding:
                assert (set(q) - T) & ridges, ('nonpure shelling intersection', n, j, t, q)
        if len(ridges) == n - 3:
            spanning += 1
        preceding.append(t)
    predicted = (n - 8) * (n - 9) // 2 - 35
    assert spanning == predicted, (n, spanning, predicted)
    print(f'SHELLING_OK n={n} facets={len(order)} spanning={spanning}')


def rank_mod2(columns):
    """Gaussian elimination on complete GF(2) boundary columns, as Python integers."""
    lead = {}
    for column in columns:
        c = column
        while c:
            k = c.bit_length() - 1
            if k not in lead:
                lead[k] = c
                break
            c ^= lead[k]
    return len(lead)


def check_dual_homology(n, expected_dim, expected_rank):
    # Alexander dual of the three-cut complex comprises exactly those vertex
    # subsets that contain no disconnected triple.
    forbidden = [sum(1 << a for a in t) for t in bad_triples(n)]
    faces = [[] for _ in range(n + 1)]
    for face in range(1 << n):
        if all(face & b != b for b in forbidden):
            faces[face.bit_count()].append(face)
    assert faces[0] == [0] and len(faces[1]) == n
    # Augmented boundary to the empty face computes reduced H_0 directly.
    ranks = [0] * (n + 1)
    for k in range(1, n + 1):
        if not faces[k]:
            continue
        ids = {face: a for a, face in enumerate(faces[k-1])}
        columns = []
        for f in faces[k]:
            col = 0
            bit_rem = f
            while bit_rem:
                b = bit_rem & -bit_rem
                bit_rem -= b
                col ^= 1 << ids[f ^ b]
            columns.append(col)
        ranks[k] = rank_mod2(columns)
    betti = {}
    for k in range(1, n + 1):
        b = len(faces[k]) - ranks[k] - ranks[k+1] if k < n else len(faces[k]) - ranks[k]
        if b:
            betti[k-1] = b
    assert betti == {expected_dim: expected_rank}, (n,betti)
    dual_dim = n - expected_dim - 3
    assert dual_dim < n - 4
    # Independent Euler check of the calculated ranks.
    chi_faces = sum((-1)**(k-1) * len(faces[k]) for k in range(1,n+1)) - 1
    chi_betti = sum((-1)**i * b for i,b in betti.items())
    assert chi_faces == chi_betti
    print(f'DUAL_HOMOLOGY_OK n={n} nonzero_K_degree={expected_dim} rank={expected_rank} Delta_degree={dual_dim}')


def main():
    assert not bad_triples(9) and not bad_triples(10)
    print('VOID_OK n=9,10')
    lower = {11:(5,1),12:(3,6),13:(3,40),14:(3,15),15:(3,1),16:(2,3)}
    for n,(q,b) in lower.items():
        check_dual_homology(n,q,b)
    for n in (17,18,19,20):
        check_shelling(n)
    print('ALL_VERIFY_OK')

if __name__ == '__main__':
    main()
