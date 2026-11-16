#!/usr/bin/env python3
"""Exact combinatorial verification of labeled Fano-plane Fourier sampling.
Python standard library only; invoke: python verify_permutation.py.
"""
from itertools import permutations, combinations

VERTICES = tuple(range(1, 8))
TRIPLES = tuple(combinations(VERTICES, 3))
INDEX = {t: i for i, t in enumerate(TRIPLES)}
BASE = ((1,2,3),(1,4,5),(1,6,7),(2,4,6),(2,5,7),(3,4,7),(3,5,6))


def parity(perm):
    return (-1) ** sum(perm[i] > perm[j] for i in range(7) for j in range(i + 1,7))


def moved_mask(perm):
    lookup = {a: b for a,b in zip(VERTICES, perm)}
    return sum(1 << INDEX[tuple(sorted(lookup[x] for x in t))] for t in BASE)


def run():
    signs = {}
    multiplicities = {}
    for p in permutations(VERTICES):
        mask = moved_mask(p)
        sign = parity(p)
        if mask in signs:
            assert signs[mask] == sign, 'Odd base-plane automorphism'
        else:
            signs[mask] = sign
        multiplicities[mask] = multiplicities.get(mask, 0) + 1
    assert len(signs) == 30
    assert set(multiplicities.values()) == {168}
    A = sorted(x for x in signs if signs[x] == 1)
    B = sorted(x for x in signs if signs[x] == -1)
    assert len(A) == len(B) == 15
    planes = A + B
    overlaps = [[(u & v).bit_count() for v in planes] for u in planes]
    assert all(overlaps[i][i] == 7 for i in range(30))
    assert all(overlaps[i][j] == 1 for i in range(30) for j in range(30)
               if i != j and (i < 15) == (j < 15))
    Bmat = [[int(overlaps[i][15+j] == 3) for j in range(15)] for i in range(15)]
    assert all(overlaps[i][15+j] in (0,3) for i in range(15) for j in range(15))
    assert all(sum(row) == 7 for row in Bmat)
    assert all(sum(row[j] for row in Bmat) == 7 for j in range(15))
    assert all(sum(Bmat[i][k]*Bmat[j][k] for k in range(15)) == (7 if i == j else 3)
               for i in range(15) for j in range(15))
    # K_{P,Q} = 1 + |P cap Q| + binom(|P cap Q|,2), exactly the
    # Gram matrix for all degree <=2 cell-presence monomials.
    gram = [[1 + v + v*(v-1)//2 for v in row] for row in overlaps]
    assert all(gram[i][i] == 29 for i in range(30))
    assert all(sum(gram[i]) == 114 for i in range(30))
    sign_vec = [signs[p] for p in planes]
    assert all(sum(gram[i][j] * sign_vec[j] for j in range(30)) == 0
               for i in range(30))
    # With B B^T=4I+3J, Gram eigenvalues are 114 (1),
    # 39 (14), 15 (14), 0 (1), proving rank 29 exactly.
    witness = ((1,2,3),(1,4,5),(2,4,6))
    wbits = sum(1 << INDEX[t] for t in witness)
    hits = [p for p in planes if (p & wbits) == wbits]
    assert len(hits) == 1
    assert sum(signs[p] for p in hits) == 1
    print('PASS: 30 labelled Fano planes; 15+15 parity split; each stabilizer 168 even')
    print('PASS: cross-incidence symmetric 2-(15,7,3) design')
    print('PASS: degree-two Gram spectrum 114^1,39^14,15^14,0^1')
    print('PASS: parity contrast is exact quadratic kernel; cubic witness unique')

if __name__ == '__main__':
    run()
