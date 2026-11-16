#!/usr/bin/env python3
"""Exact integer verification of Fourier convolution for order-three Latin squares.

All loops are finite and cover the stated parameter, with no external modules.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product

N = 3
DIM = N ** 3

def incidence(rows):
    return sum(1 << (9 * i + 3 * j + rows[i][j])
               for i in range(N) for j in range(N))

def alpha_beta_squares():
    return {incidence(tuple(tuple((a * i + b * j + c) % 3
                                  for j in range(N)) for i in range(N)))
            for a in (1, 2) for b in (1, 2) for c in range(N)}

def independent_squares():
    perms = list(permutations(range(N)))
    return {incidence(rows) for rows in product(perms, repeat=N)
            if all(len({rows[i][j] for i in range(N)}) == N
                   for j in range(N))}

def xor_basis(vectors):
    echelon = {}
    inserted = []
    for v in vectors:
        while v:
            pivot = v.bit_length() - 1
            if pivot in echelon:
                v ^= echelon[pivot]
            else:
                echelon[pivot] = v
                inserted.append(v)
                break
    return inserted

def fwht(a):
    arr = list(a)
    step = 1
    while step < len(arr):
        for pos in range(0, len(arr), 2*step):
            for offset in range(step):
                k, ell = pos+offset, pos+offset+step
                x, y = arr[k], arr[ell]
                arr[k], arr[ell] = x+y, x-y
        step *= 2
    return arr

def char(u, x):
    return -1 if ((u & x).bit_count() % 2) else 1

def main():
    first = independent_squares()
    second = alpha_beta_squares()
    assert first == second and len(first) == 12
    # Sort by the order of the independent enumeration, not arbitrary set order.
    perms = list(permutations(range(N)))
    squares = [incidence(rows) for rows in product(perms, repeat=N)
               if all(len({rows[i][j] for i in range(N)}) == N
                      for j in range(N))]
    assert set(squares) == first and len(squares) == 12
    anchor = squares[0]
    basis = xor_basis([p ^ anchor for p in squares])
    assert len(basis) == 8
    assert basis == [62512128,14355888,102264240,219051,7299499,110808,13851,27702]
    d = len(basis)
    # Build the entire affine span, tracking each point's unique coordinates.
    expansion = {}
    for z in range(1 << d):
        v = 0
        for i, b in enumerate(basis):
            if (z >> i) & 1:
                v ^= b
        assert v not in expansion
        expansion[v] = z
    assert len(expansion) == 1 << d
    assert anchor not in expansion  # the affine support does not pass through zero
    support = [expansion[p ^ anchor] for p in squares]
    assert len(set(support)) == 12
    assert sorted(support) == [0,1,3,4,11,18,40,124,137,220,228,250]
    # First character-sum route: direct sum on the 12 quotient points.
    direct = [sum(char(u, x) for x in support) for u in range(1 << d)]
    # Second independent route: Walsh transform of a 0-1 array.
    mask = [int(x in support) for x in range(1 << d)]
    via_fwht = fwht(mask)
    assert direct == via_fwht
    # Third route: recover a representative of every ambient linear functional.
    evaluations = [sum(((b >> j) & 1) << i for i,b in enumerate(basis))
                   for j in range(DIM)]
    dual = {0: 0}
    for j, vec in enumerate(evaluations):
        for y, representative in tuple(dual.items()):
            target = y ^ vec
            if target not in dual:
                dual[target] = representative ^ (1 << j)
    assert len(dual) == 1 << d
    for u in range(1 << d):
        rep = dual[u]
        assert all(((rep & b).bit_count() % 2) == ((u >> i) & 1)
                   for i,b in enumerate(basis))
        explicit = sum(char(rep, x) for x in squares)
        assert explicit == char(rep, anchor) * direct[u]
    signed = Counter(direct)
    assert signed == {-8:2,-4:45,0:108,4:90,8:10,12:1}
    assert sum(x*x for x in direct) == (1 << d) * len(squares)
    nonzero = [int(x != 0) for x in direct]
    kernel = fwht(nonzero)
    # Independent, explicit sum for the projection kernel.
    assert kernel == [sum(char(x,u) for u in range(1<<d) if nonzero[u])
                      for x in range(1<<d)]
    kernel_hist = Counter(abs(h) for h in kernel)
    assert kernel_hist == {0:12,4:81,8:108,12:54,148:1}
    assert sum(h*h for h in kernel) == (1 << d) * sum(nonzero)
    assert sum(nonzero) == 148
    norm = Fraction(sum(abs(v) for v in kernel),1<<d)
    assert norm == Fraction(31,4)
    ambient_dim = DIM
    ambient_freq = 1 << ambient_dim
    lifts = 1 << (ambient_dim-d)
    assert ambient_freq == 134217728 and 148*lifts == 77594624
    assert (ambient_freq - 148*lifts) == 56623104
    print('LATIN3_WALSH_RANGE_PASS latin=12 dimension=8 quotient=256 '
          'rank=77594624 zero=56623104 norm=31/4')
    print('signed=', sorted(signed.items()))
    print('projection_abs=', sorted(kernel_hist.items()))

if __name__ == '__main__':
    main()
