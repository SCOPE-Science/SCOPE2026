#!/usr/bin/env python3
"""Check the integral three-particle top-homology certificate for GP(12,5)."""

import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


def main(witness_path):
    W = json.loads(Path(witness_path).read_text(encoding="utf-8"))
    V = tuple(range(24))
    neighbors = {}
    for v in V:
        layer, i = divmod(v, 12)
        step = 1 if layer == 0 else 5
        neighbors[v] = sorted([
            12 * layer + (i + step) % 12,
            12 * layer + (i - step) % 12,
            (v + 12) % 24,
        ])
    assert all((v % 12 + v // 12 - u % 12 - u // 12) % 2
               for v in V for u in neighbors[v])

    # Use the least vertex as start and the lesser of its two cycle neighbors
    # as the second vertex. Enumerate even short cycles without assuming girth.
    circles = []

    def visit(path):
        for u in neighbors[path[-1]]:
            if u == path[0] and len(path) >= 3 and path[1] < path[-1]:
                circles.append(path)
            elif u > path[0] and u not in path and len(path) < 12:
                visit(path + (u,))

    for v in V:
        visit((v,))
    circles.sort(key=lambda c: (len(c), c))
    counts = Counter(map(len, circles))
    assert counts == {6: 12, 8: 54, 10: 108, 12: 246}
    masks = [sum(1 << v for v in c) for c in circles]
    triples = set()
    for i, a in enumerate(masks):
        for j, b in enumerate(masks[:i]):
            if a & b == 0:
                for k in range(j):
                    if masks[k] & (a | b) == 0:
                        triples.add((k, j, i))
    profiles = Counter(tuple(len(circles[i]) for i in t) for t in triples)
    assert profiles == {(6, 6, 6): 16, (6, 6, 8): 72, (6, 8, 8): 36, (8, 8, 8): 6}

    # The witness indexes an older list with both orientations. Keep its
    # numbering but use only unoriented triples to check the full span.
    def canonical(c):
        return min(c, c[:1] + c[:0:-1])

    legacy = list(map(tuple, W['cycles_short']))
    assert Counter(map(canonical, legacy)) == {c: 2 for c in circles if len(c) <= 8}
    ids = {c: i for i, c in enumerate(circles)}
    assert len(W['torus_triples']) == 59
    assert all(tuple(sorted(ids[canonical(legacy[i])] for i in t)) in triples
               for t in W['torus_triples'])

    C = [tuple(zip(vertices, (bits >> j & 1 for j in range(3))))
         for vertices in combinations(V, 3) for bits in range(8)]
    assert len(C) == 16192

    def edge(v, u):
        return tuple(sorted((v, u)))

    def boundary(B):
        for j, (v, i) in enumerate(B):
            rest = B[:j] + B[j + 1:]
            sign = (-1) ** j
            yield (rest, edge(v, neighbors[v][0])), -sign
            yield (rest, edge(v, neighbors[v][i + 1])), sign

    # Rank in F3. The disjoint bitplanes X and Y store positions of 1 and 2.
    row_bits, pivots = {}, {}
    for B in C:
        X = Y = 0
        for row, sign in boundary(B):
            if row not in row_bits:
                row_bits[row] = 1 << len(row_bits)
            if sign == 1:
                X |= row_bits[row]
            else:
                Y |= row_bits[row]
        while X or Y:
            i = (X | Y).bit_length() - 1
            if i not in pivots:
                pivots[i] = (X, Y)
                break
            P, Q = pivots[i]
            if (X >> i & 1) == (P >> i & 1):
                P, Q = Q, P
            # X,Y <- (X,Y) + (P,Q) mod 3.
            X, Y = ((X & ~(P | Q)) | (Y & Q) | (P & ~(X | Y)),
                    (Y & ~(P | Q)) | (X & P) | (Q & ~(X | Y)))
    assert len(row_bits) == 39600 and len(pivots) == 16132

    def torus(cycles):
        factors = []
        for c in cycles:
            out = []
            for j, v in enumerate(c):
                for i, u in enumerate(neighbors[v][1:]):
                    if u == c[(j + 1) % len(c)]:
                        out.append(((v, i), 1))
                    elif u == c[j - 1]:
                        out.append(((v, i), -1))
            factors.append(out)
        return {tuple(sorted((a, b, c))): x * y * z * (-1) ** ((a > b) + (a > c) + (b > c))
                for (a, x), (b, y), (c, z) in product(*factors)}

    def check_cycle(chain):
        out = defaultdict(int)
        for B, n in chain.items():
            for row, sign in boundary(B):
                out[row] += n * sign
        assert not any(out.values())

    items = W['nonproduct_cycle']
    assert len(items) == len({i for i, _ in items}) == 5034
    assert all(0 <= i < len(C) and n != 0 for i, n in items)
    basis = [torus(legacy[i] for i in t) for t in W['torus_triples']]
    basis.append({C[i]: n for i, n in items})
    for z in basis:
        check_cycle(z)
    rows = W['minor_rows']
    assert len(rows) == len(set(rows)) == 60 and all(0 <= i < len(C) for i in rows)
    # Gauss-Jordan on the transpose of the minor: get its determinant and the
    # exact linear functional extracting the last coordinate in this basis.
    A = [[Fraction(z.get(C[i], 0)) for i in rows] + [Fraction(j == 59)]
         for j, z in enumerate(basis)]
    det = Fraction(1)
    for j in range(60):
        k = next(k for k in range(j, 60) if A[k][j])
        if k != j:
            A[j], A[k] = A[k], A[j]
            det = -det
        a = A[j][j]
        det *= a
        A[j] = [u / a for u in A[j]]
        for k in range(60):
            if k != j and A[k][j]:
                a = A[k][j]
                A[k] = [u - a * v for u, v in zip(A[k], A[j])]
    assert det == -1
    terms = [(C[i], cell[-1]) for i, cell in zip(rows, A) if cell[-1]]
    assert all(coeff.denominator == 1 for _, coeff in terms)
    for t in sorted(triples):
        z = torus(circles[i] for i in t)
        check_cycle(z)
        assert sum(int(coeff) * z.get(B, 0) for B, coeff in terms) == 0
    print('NAURU_THREE_PARTICLE_TOP_HOMOLOGY_OK')
    print('unoriented_simple_cycles:', dict(sorted(counts.items())))
    print('geometric_product_tori:', len(triples), 'integral_rank:', 59)
    print('degree_three_generators:', len(C), 'boundary_mod3_rank:', len(pivots))
    print('integral_cycle_basis:', len(basis), 'coordinate_minor_determinant:', det)
    print('nonproduct_cycle_terms:', len(items))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'NAURU_WITNESS.json')
