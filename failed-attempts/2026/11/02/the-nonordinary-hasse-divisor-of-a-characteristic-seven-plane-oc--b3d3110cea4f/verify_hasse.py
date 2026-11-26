#!/usr/bin/env python3
"""Exact Hasse-Witt coefficient computation for the smooth plane-octic pencil.

Uses only the Python standard library, with all arithmetic in F_7[lambda].
The coefficient formula is applied to the 21 degree-five residue forms.
"""
from collections import defaultdict
from itertools import combinations_with_replacement
from math import comb, factorial

P = 7
DEG = 5
BASIS = [(i, j, DEG-i-j) for i in range(DEG+1) for j in range(DEG+1-i)]
assert len(BASIS) == 21


def trim(poly):
    z = list(poly)
    while z and z[-1] == 0:
        z.pop()
    return tuple(z)


def add(a, b):
    return trim([((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % P
                 for i in range(max(len(a), len(b)))])


def mul(a, b):
    if not a or not b:
        return ()
    out = [0]*(len(a)+len(b)-1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i+j] = (out[i+j]+u*v) % P
    return trim(out)


def scale(a, c):
    return trim([(v*c) % P for v in a])


def determinant(matrix):
    n = len(matrix)
    assert all(len(row) == n for row in matrix)
    if n == 0:
        return (1,)
    if n == 1:
        return matrix[0][0]
    result = ()
    for j, elem in enumerate(matrix[0]):
        sub = [row[:j]+row[j+1:] for row in matrix[1:]]
        term = mul(elem, determinant(sub))
        result = add(result, scale(term, (-1)**j))
    return result


def evaluate(poly, x):
    return sum(c*pow(x, i, P) for i,c in enumerate(poly)) % P


def rank(matrix, lam):
    a = [[evaluate(t, lam) for t in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot = 0
    for j in range(cols):
        k = next((k for k in range(pivot, rows) if a[k][j]), None)
        if k is None:
            continue
        a[pivot], a[k] = a[k], a[pivot]
        inv = pow(a[pivot][j], -1, P)
        a[pivot] = [(inv*t)%P for t in a[pivot]]
        for h in range(rows):
            if h != pivot:
                factor = a[h][j]
                if factor:
                    a[h] = [(u-factor*v)%P for u,v in zip(a[h],a[pivot])]
        pivot += 1
        if pivot == rows:
            break
    return pivot


def build_matrix():
    # F = Y^8 - X^7 Z - X Z^7 - lambda*(Y^2-2XZ)^4.
    terms = [((0,8,0), 1, 0), ((7,0,1), -1, 0), ((1,0,7), -1, 0)]
    for k in range(5):
        terms.append(((k,8-2*k,k), -comb(4,k)*(-2)**k, 1))
    coeff = defaultdict(lambda: [0]*7)
    for multiset in combinations_with_replacement(range(len(terms)), 6):
        counts = [multiset.count(i) for i in range(len(terms))]
        multinom = factorial(6)
        exponent = [0,0,0]
        constant = 1
        ldegree = 0
        for idx,c in enumerate(counts):
            if not c:
                continue
            multinom //= factorial(c)
            mono, factor, ld = terms[idx]
            exponent = [e+c*u for e,u in zip(exponent, mono)]
            constant *= factor**c
            ldegree += ld*c
        coeff[tuple(exponent)][ldegree] = (
            coeff[tuple(exponent)][ldegree] + multinom*constant) % P
    # For each pair of canonical monomials v (row), u (column),
    # obtain the coefficient of exponent 7*(u+1)-(v+1) in F^6.
    return [[trim(coeff.get(tuple(7*(b+1)-(a+1) for a,b in zip(v,u)), [0]*7))
             for u in BASIS] for v in BASIS]


def blocks(matrix):
    parent = list(range(42))
    def root(z):
        while z != parent[z]:
            z = parent[z]
        return z
    for i in range(21):
        for j in range(21):
            if matrix[i][j]:
                parent[root(i)] = root(21+j)
    components = defaultdict(list)
    for z in range(42):
        components[root(z)].append(z)
    groups = []
    for comp in components.values():
        rows = sorted(v for v in comp if v < 21)
        cols = sorted(v-21 for v in comp if v >= 21)
        assert len(rows) == len(cols)
        groups.append((rows,cols))
    return sorted(groups, key=lambda t:t[0][0])


def main():
    H = build_matrix()
    groups = blocks(H)
    assert [len(rows) for rows,cols in groups] == [1,1,2,2,3,3,3,2,2,1,1]
    for rows,cols in groups:
        sub = [[H[i][j] for j in cols] for i in rows]
        determinant_block = determinant(sub)
        size = len(rows)
        if size == 1:
            assert determinant_block == (0,1)
        else:
            # -lambda^size(lambda^2-2) = 2 lambda^size-lambda^(size+2).
            expected = (0,)*size+(2,0,6)
            assert determinant_block == expected, (rows,determinant_block,expected)
        assert rank(sub,3) == size if size==1 else rank(sub,3)==size-1
        assert rank(sub,4) == size if size==1 else rank(sub,4)==size-1
    det = (1,)
    for rows,cols in groups:
        det = mul(det, determinant([[H[i][j] for j in cols] for i in rows]))
    L = (0,1)
    expected = (1,)
    for _ in range(21):expected = mul(expected,L)
    for _ in range(7):expected = mul(expected,(5,0,1))
    expected = scale(expected, -1)
    assert det == expected
    for lam in range(7):
        desired = 0 if lam == 0 else (14 if lam in (3,4) else 21)
        assert rank(H,lam) == desired, (lam,rank(H,lam),desired)
    print('HASSE_OCTIC_21x21_BLOCK_DETERMINANT_AND_RANKS_OK')
    print('det(H)=-lambda^21*(lambda^2-2)^7 over F7; block sizes 1^4 2^4 3^3')


if __name__ == '__main__':
    main()
