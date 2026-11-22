#!/usr/bin/env python3
"""Exact finite verification of mod-two homology for two 16-vertex graph complexes.

The graphs are encoded independently by their coordinate adjacency rules.
No external modules are needed; all fields of order two are exact integer bit operations.
"""
from collections import Counter, defaultdict
from itertools import combinations, product

VERTICES = list(product(range(4), repeat=2))
N = len(VERTICES)
STEPS = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
EXPECTED = {
    "Shrikhande": {
        "faces": (1, 16, 120, 416, 672, 432, 144, 16),
        "ranks": (1, 15, 105, 311, 304, 128, 16),
        "betti": (0, 0, 0, 57, 0, 0, 0),
    },
    "Rook": {
        "faces": (1, 16, 120, 416, 632, 240, 16),
        "ranks": (1, 15, 105, 311, 223, 16),
        "betti": (0, 0, 0, 98, 1, 0),
    },
}


def graph(kind):
    def adjacent(u, v):
        x, y = VERTICES[u]
        xx, yy = VERTICES[v]
        if kind == 'Rook':
            return x == xx or y == yy
        return ((xx - x) % 4, (yy - y) % 4) in STEPS

    neighbors = [0] * N
    for i in range(N):
        for j in range(N):
            if i != j and adjacent(i, j):
                neighbors[i] |= 1 << j
    assert all(neighbors[i].bit_count() == 6 for i in range(N))
    for i in range(N):
        for j in range(i + 1, N):
            assert ((neighbors[i] & neighbors[j]).bit_count() == 2)
            assert bool(neighbors[i] & (1 << j)) == bool(neighbors[j] & (1 << i))
    return neighbors


def forbid_triples(neighbors):
    forbidden = []
    for a, b, c in combinations(range(N), 3):
        ne = int((neighbors[a] >> b) & 1) + int((neighbors[a] >> c) & 1) + int((neighbors[b] >> c) & 1)
        if ne == 2:
            forbidden.append((1 << a) | (1 << b) | (1 << c))
    assert len(forbidden) == 144
    return forbidden


def independent_clique_components(mask, neighbors):
    unseen = mask
    while unseen:
        root = unseen & -unseen
        visited = root
        frontier = root
        while frontier:
            vbit = frontier & -frontier
            frontier ^= vbit
            v = vbit.bit_length() - 1
            newly = neighbors[v] & unseen & ~visited
            visited |= newly
            frontier |= newly
        # Each connected component must be a clique.
        size = visited.bit_count()
        vmask = visited
        while vmask:
            vbit = vmask & -vmask
            vmask ^= vbit
            v = vbit.bit_length() - 1
            if (neighbors[v] & visited).bit_count() != size - 1:
                return False
        unseen &= ~visited
    return True


def enumerate_faces(neighbors):
    bad = forbid_triples(neighbors)
    valid = bytearray(1 << N)
    valid[0] = 1
    by_size = defaultdict(list)
    by_size[0].append(0)
    for mask in range(1, 1 << N):
        parent = mask & (mask - 1)
        if valid[parent] and all((mask & triple) != triple for triple in bad):
            valid[mask] = 1
            by_size[mask.bit_count()].append(mask)
    # Independent, graph-theoretic definition verifies every one of the 2^16 subsets.
    for mask in range(1 << N):
        assert bool(valid[mask]) == independent_clique_components(mask, neighbors), mask
    for sz, faces in by_size.items():
        if not sz:
            continue
        for face in faces:
            m = face
            while m:
                b = m & -m
                m ^= b
                assert valid[face ^ b]
    return by_size


def boundary_columns(upper, lower):
    lower_index = {face: pos for pos, face in enumerate(lower)}
    out = []
    for face in upper:
        col = 0
        bits = face
        while bits:
            b = bits & -bits
            bits ^= b
            col ^= 1 << lower_index[face ^ b]
        assert col.bit_count() == face.bit_count()
        out.append(col)
    return out


def rank_by_columns(columns):
    pivots = {}
    for c in columns:
        v = c
        while v:
            i = v.bit_length() - 1
            if i not in pivots:
                pivots[i] = v
                break
            v ^= pivots[i]
    return len(pivots)


def rank_by_rows(columns, nrows):
    # An independent transpose implementation performs elimination on row bitsets.
    rows = [0] * nrows
    for j, col in enumerate(columns):
        while col:
            bit = col & -col
            col ^= bit
            rows[bit.bit_length() - 1] ^= 1 << j
    pivot = {}
    for row in rows:
        while row:
            bit = row & -row
            k = bit.bit_length() - 1
            if k not in pivot:
                pivot[k] = row
                break
            row ^= pivot[k]
    return len(pivot)


def check(kind):
    neighbors = graph(kind)
    faces = enumerate_faces(neighbors)
    max_size = max(faces)
    dims = tuple(len(faces[k]) for k in range(max_size + 1))
    assert dims == EXPECTED[kind]['faces'], (kind, dims)
    ranks = []
    previous = None
    for size in range(1, max_size + 1):
        upper = faces[size]
        lower = faces[size-1]
        cols = boundary_columns(upper, lower)
        r1 = rank_by_columns(cols)
        r2 = rank_by_rows(cols, len(lower))
        assert r1 == r2, (kind, size, r1, r2)
        # For each size >=2, the composite consecutive mod-two boundaries vanish.
        if previous is not None:
            for col in cols:
                result = 0
                while col:
                    b = col & -col
                    col ^= b
                    result ^= previous[b.bit_length()-1]
                assert result == 0
        ranks.append(r1)
        previous = cols
    assert tuple(ranks) == EXPECTED[kind]['ranks'], (kind, ranks)
    betti = tuple(dims[k] - ranks[k-1] - (ranks[k] if k < len(ranks) else 0)
                  for k in range(1, len(dims)))
    assert betti == EXPECTED[kind]['betti'], (kind, betti)
    chi_tilde = sum((-1)**(sz-1) * len(faces[sz]) for sz in range(max_size+1))
    assert chi_tilde == sum((-1)**dim * count for dim, count in enumerate(betti))
    print(f'{kind}: f(size=0..{max_size})={dims}')
    print(f'{kind}: augmented boundary ranks (size=1..{max_size})={tuple(ranks)}')
    print(f'{kind}: reduced F2 Betti degrees 0..{max_size-1}={betti}')
    print(f'{kind}: reduced Euler characteristic={chi_tilde}; checks OK')


if __name__ == '__main__':
    for kind in ('Shrikhande', 'Rook'):
        check(kind)
    print('ALL CHECKS PASSED')
