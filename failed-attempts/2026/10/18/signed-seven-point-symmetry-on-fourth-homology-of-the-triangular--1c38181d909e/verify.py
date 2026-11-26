#!/usr/bin/env python3
"""Exact integral cellular reduction and natural S_7 action on top homology.

Run with Python 3.10+; no third-party dependencies or external files.
The complex is the open-neighborhood complex of the triangular graph L(K_7).
"""
from collections import Counter, defaultdict
from heapq import heappop, heappush
from itertools import combinations
from math import factorial

N = 7
EDGE = tuple(combinations(range(N), 2))
EDGE_INDEX = {e: i for i, e in enumerate(EDGE)}


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask -= bit


def boundary(mask):
    return {mask ^ (1 << b): (-1 if i % 2 else 1)
            for i, b in enumerate(bits(mask))}


def add_scaled(chain, key, coeff):
    a = chain.get(key, 0) + coeff
    if a:
        chain[key] = a
    else:
        chain.pop(key, None)


def complex_faces():
    faces = {0}
    for u, v in EDGE:
        nb = sum((1 << j) for j, (a, b) in enumerate(EDGE)
                 if (a, b) != (u, v) and (u in (a, b) or v in (a, b)))
        sub = nb
        while sub:
            faces.add(sub)
            sub = (sub - 1) & nb
    return faces


def simplicial_collapses(faces):
    # A free codimension-one face t has exactly one codimension-one coface s.
    # When free, s is necessarily maximal. Every pair is an elementary collapse.
    live = set(faces)
    upper = defaultdict(set)
    for face in faces:
        for b in bits(face):
            upper[face ^ (1 << b)].add(face)
    heap = [(-f.bit_count(), f) for f in faces if len(upper[f]) == 1]
    from heapq import heapify
    heapify(heap)
    pairs = []
    while heap:
        _, t = heappop(heap)
        if t not in live or len(upper[t]) != 1:
            continue
        s = next(iter(upper[t]))
        assert s in live and s.bit_count() == t.bit_count() + 1 and not upper[s]
        pairs.append((t, s))
        for f in (t, s):
            live.remove(f)
            for b in bits(f):
                r = f ^ (1 << b)
                if r in live:
                    upper[r].remove(f)
                    if len(upper[r]) == 1:
                        heappush(heap, (-r.bit_count(), r))
    return live, pairs


def integer_kernel_basis(top, codim_one):
    row_index = {f: i for i, f in enumerate(codim_one)}
    pivots = {}
    cycles, free_columns = [], []
    for col, f in enumerate(top):
        d = {row_index[k]: v for k, v in boundary(f).items()}
        rep = {col: 1}
        while d:
            row = min(d)
            if row not in pivots:
                unit = d[row]
                assert unit in (-1, 1), (col, row, unit)
                pivots[row] = ({k: unit * v for k, v in d.items()},
                               {k: unit * v for k, v in rep.items()})
                break
            bd, brep = pivots[row]
            scalar = d[row]
            for k, v in bd.items():
                add_scaled(d, k, -scalar * v)
            for k, v in brep.items():
                add_scaled(rep, k, -scalar * v)
        if not d:
            cycles.append(rep)
            free_columns.append(col)
    assert len(cycles) == len(free_columns) == len(top) - len(pivots)
    assert all(all((1 if j == i else 0) == z.get(free_columns[j], 0)
                   for j in range(len(free_columns)))
               for i, z in enumerate(cycles))
    for z in cycles:
        bd = {}
        for j, v in z.items():
            for face, coeff in boundary(top[j]).items():
                add_scaled(bd, face, v * coeff)
        assert not bd
    return len(pivots), cycles, free_columns


def oriented_image(mask, permutation):
    indices = []
    for j in bits(mask):
        u, v = EDGE[j]
        e = tuple(sorted((permutation[u], permutation[v])))
        indices.append(EDGE_INDEX[e])
    inversions = sum(indices[i] > indices[j]
                     for i in range(len(indices)) for j in range(i + 1, len(indices)))
    image = sum(1 << k for k in indices)
    return image, (-1 if inversions % 2 else 1)


def project_4(chain, pairs):
    # Cellular chain map for each elementary collapse (t subset s):
    # p_4(t) = t - [t:s]^{-1} boundary(s) if dim(t)=4;
    # p_4(s) = 0 if dim(s)=4; all other degree-four basis chains fixed.
    for t, s in pairs:
        dim_t = t.bit_count() - 1
        if dim_t == 4 and t in chain:
            old = chain[t]
            sign = boundary(s)[t]
            for face, v in boundary(s).items():
                add_scaled(chain, face, -old * sign * v)
        elif dim_t == 3:
            chain.pop(s, None)
    return chain


def image_matrix(permutation, top, top_index, cycles, free, pairs):
    columns = []
    for z in cycles:
        img = {}
        for j, coeff in z.items():
            simplex, sgn = oriented_image(top[j], permutation)
            add_scaled(img, simplex, coeff * sgn)
        project_4(img, pairs)
        assert all(f in top_index for f in img)
        columns.append([img.get(top[k], 0) for k in free])
    return [[columns[j][i] for j in range(len(cycles))]
            for i in range(len(cycles))]


def partitions(n, upper=None):
    if n == 0:
        yield ()
    else:
        for k in range(min(n, upper if upper is not None else n), 0, -1):
            for rest in partitions(n-k, k):
                yield (k,) + rest


def cycle_type_perm(lam):
    perm = []
    begin = 0
    for length in lam:
        perm += list(range(begin + 1, begin + length)) + [begin]
        begin += length
    return perm


def parity(perm):
    return (-1 if sum(perm[i] > perm[j] for i in range(N)
                      for j in range(i + 1, N)) % 2 else 1)


def matrix_multiply(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def main():
    all_faces = complex_faces()
    rem, pairs = simplicial_collapses(all_faces)
    shape = tuple(Counter(f.bit_count() - 1 for f in rem)[i] for i in range(-1, 5))
    assert len(all_faces) == 18495 and len(pairs) == 7962
    assert shape == (1, 21, 210, 881, 1194, 264), shape
    top = sorted(f for f in rem if f.bit_count() == 5)
    facets3 = sorted(f for f in rem if f.bit_count() == 4)
    rank, cycles, free = integer_kernel_basis(top, facets3)
    assert rank == 257 and len(cycles) == 7
    assert all(abs(v) == 1 for z in cycles for v in z.values())
    index = {f: k for k, f in enumerate(top)}
    character = {}
    for lam in partitions(7):
        perm = cycle_type_perm(lam)
        matrix = image_matrix(perm, top, index, cycles, free, pairs)
        trace = sum(matrix[i][i] for i in range(7))
        expected = parity(perm) * sum(perm[i] == i for i in range(7))
        assert trace == expected, (lam, trace, expected)
        character[lam] = trace
    # Independent structural check: integer matrices of simple transpositions
    # obey all Coxeter relations for S_7.
    simple = []
    for i in range(N-1):
        p = list(range(N))
        p[i], p[i + 1] = p[i + 1], p[i]
        simple.append(image_matrix(p, top, index, cycles, free, pairs))
    eye = [[int(i == j) for j in range(7)] for i in range(7)]
    for i, s in enumerate(simple):
        assert matrix_multiply(s, s) == eye
        for j in range(i+1, len(simple)):
            a, b = s, simple[j]
            if j == i + 1:
                assert matrix_multiply(matrix_multiply(a,b),a) == matrix_multiply(matrix_multiply(b,a),b)
            else:
                assert matrix_multiply(a,b) == matrix_multiply(b,a)
    print('PASS: 18,495 augmented faces; 7,962 elementary collapses; 264 surviving 4-cells.')
    print('PASS: integral degree-four boundary rank 257 by unit-pivot elimination; exact H_4 = Z^7.')
    print('PASS: S_7 homology character sign times natural seven-point permutation character.')
    print('PASS: 15 conjugacy classes; six generators satisfy Coxeter relations over Z.')
    print('CHARACTERS:', ' '.join(f'{lam}:{character[lam]}' for lam in partitions(7)))


if __name__ == '__main__':
    main()
