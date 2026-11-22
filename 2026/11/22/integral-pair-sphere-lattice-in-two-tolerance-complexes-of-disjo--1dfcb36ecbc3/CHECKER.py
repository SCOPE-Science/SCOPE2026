#!/usr/bin/env python3
"""Finite cross-checks for top integral homology of triangle-block tolerance complexes.

The proof for arbitrary block number is in RESULT.md. This program does not
infer the infinite result from finite computations. Python 3 standard library.
"""
from collections import defaultdict
from itertools import combinations, permutations
from math import comb


def oriented_boundary(simplex):
    return [(simplex[:k] + simplex[k + 1:], (-1) ** k)
            for k in range(len(simplex))]


def add_boundary(chain):
    out = defaultdict(int)
    for simplex, coeff in chain.items():
        for face, sign in oriented_boundary(simplex):
            out[face] += coeff * sign
    return {face: coeff for face, coeff in out.items() if coeff}


def top_faces(r):
    n = 3 * r
    fs = set()
    for i in range(r):
        block = tuple(range(3*i, 3*i+3))
        others = [v for v in range(n) if v not in block]
        for a, b in combinations(others, 2):
            fs.add(tuple(sorted(block + (a, b))))
    return sorted(fs)


def pair_cycle(i, j):
    vertices = tuple(range(3*i, 3*i+3)) + tuple(range(3*j, 3*j+3))
    if i > j:
        raise ValueError('Use i<j')
    return dict(oriented_boundary(vertices))


def rank_mod_2(faces):
    rows = sorted({f for s in faces for f, _ in oriented_boundary(s)})
    rmap = {face: i for i, face in enumerate(rows)}
    pivots = {}
    for sigma in faces:
        v = 0
        for face, _ in oriented_boundary(sigma):
            v ^= 1 << rmap[face]
        while v:
            p = v.bit_length() - 1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    return len(pivots)


def signed_image(chain, vertex_map):
    ans = defaultdict(int)
    for simplex, coeff in chain.items():
        transformed = [vertex_map[v] for v in simplex]
        inversions = sum(transformed[k] > transformed[j]
                         for k in range(len(transformed))
                         for j in range(k + 1, len(transformed)))
        ans[tuple(sorted(transformed))] += coeff * (-1 if inversions % 2 else 1)
    return {s: c for s, c in ans.items() if c}


def sign_of_permutation(order):
    inversions = sum(order[i] > order[j]
                     for i in range(len(order)) for j in range(i+1, len(order)))
    return (-1) ** inversions


def symmetries_check(r):
    # Block relabeling and individual S_3 actions generate the full wreath product.
    for block_permutation in permutations(range(r)) if r <= 4 else [tuple(range(r))]:
        vertex_map = {3*i + a: 3*block_permutation[i] + a
                      for i in range(r) for a in range(3)}
        for i, j in combinations(range(r), 2):
            a, b = block_permutation[i], block_permutation[j]
            sign = 1 if a < b else -1
            target = pair_cycle(min(a,b), max(a,b))
            assert signed_image(pair_cycle(i,j), vertex_map) == {
                f: sign*v for f,v in target.items()}
    for block in range(r):
        vertex_map = {v:v for v in range(3*r)}
        vertex_map[3*block], vertex_map[3*block+1] = 3*block+1, 3*block
        for i, j in combinations(range(r), 2):
            sign = -1 if block in (i,j) else 1
            assert signed_image(pair_cycle(i,j), vertex_map) == {
                f:sign*c for f,c in pair_cycle(i,j).items()}


def check(r):
    faces = top_faces(r)
    assert len(faces) == r * comb(3*(r-1),2)
    top_set = set(faces)
    cofaces = defaultdict(list)
    for sigma in faces:
        for face, _ in oriented_boundary(sigma):
            cofaces[face].append(sigma)
    mixed_count = 0
    for sigma in faces:
        blocks = [sum(v//3 == i for v in sigma) for i in range(r)]
        assert sorted(x for x in blocks if x) in ([2,3],[1,1,3])
        if sorted(x for x in blocks if x) == [1,1,3]:
            mixed_count += 1
            i = blocks.index(3)
            face = tuple(v for v in sigma if v != 3*i)
            assert len(cofaces[face]) == 1
    assert mixed_count == r * (comb(3*(r-1),2) - (r-1)*3)
    pairs = list(combinations(range(r),2))
    supports = []
    for i,j in pairs:
        z = pair_cycle(i,j)
        assert set(z).issubset(top_set)
        assert len(z) == 6
        assert set(map(abs,z.values())) == {1}
        assert add_boundary(z) == {}
        supports.append(set(z))
    assert all(not a.intersection(b) for a,b in combinations(supports,2))
    rank = rank_mod_2(faces)
    assert len(faces) - rank == len(pairs)
    if r<=4:
        symmetries_check(r)
    print(f'r={r}: top_simplices={len(faces)}, mixed={mixed_count}, '
          f'boundary_rank_F2={rank}, pair_cycles={len(pairs)}; PASS')


if __name__ == '__main__':
    for r in range(2,9):
        check(r)
