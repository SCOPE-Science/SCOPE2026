#!/usr/bin/env python3
"""Exact signed Aztec-diamond order-three Walsh spectrum verification.

Standard-library-only, exhaustive for all gauge classes. Vertex coordinates
represent square centers shifted by (1/2,1/2). All arithmetic is integer.
"""
from collections import Counter
from fractions import Fraction


def geometry(n=3):
    vertices = sorted((i, j) for i in range(-n, n) for j in range(-n, n)
                      if abs(2*i+1) + abs(2*j+1) <= 2*n)
    index = {v: a for a, v in enumerate(vertices)}
    edges = [(a, index[q]) for a, v in enumerate(vertices)
             for q in ((v[0]+1, v[1]), (v[0], v[1]+1)) if q in index]
    return vertices, edges


def matchings(vertices, edges):
    neighbors = [[] for _ in vertices]
    for k, (a, b) in enumerate(edges):
        neighbors[a].append((b, k))
        neighbors[b].append((a, k))
    ans = []
    def visit(left, mask):
        if not left:
            ans.append(mask)
            return
        a = min(left)
        for b, k in neighbors[a]:
            if b in left:
                visit(left - {a, b}, mask | (1 << k))
    visit(set(range(len(vertices))), 0)
    return ans


def gauge_free_edges(vertices, edges):
    parent = list(range(len(vertices)))
    def find(a):
        while a != parent[a]:
            a = parent[a]
        return a
    fixed = set()
    for k, (a, b) in enumerate(edges):
        a, b = find(a), find(b)
        if a != b:
            parent[a] = b
            fixed.add(k)
    assert len(fixed) == len(vertices) - 1
    return [k for k in range(len(edges)) if k not in fixed]


def det_bareiss(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    sign, prior = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            substitute = next((r for r in range(k+1, n) if a[r][k]), None)
            if substitute is None:
                return 0
            a[k], a[substitute] = a[substitute], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            ai = a[i]
            aik = ai[k]
            for j in range(k+1, n):
                numerator = ai[j]*pivot - aik*a[k][j]
                assert numerator % prior == 0
                ai[j] = numerator // prior
            ai[k] = 0
        prior = pivot
    return sign*a[n-1][n-1]


def walsh(values):
    h = list(values)
    count = len(h)
    assert count and count & (count-1) == 0
    step = 1
    while step < count:
        for start in range(0, count, 2*step):
            for j in range(step):
                a, b = h[start+j], h[start+j+step]
                h[start+j], h[start+j+step] = a+b, a-b
        step *= 2
    return h


def main():
    vertices, edges = geometry()
    assert (len(vertices), len(edges)) == (24, 36)
    all_matchings = matchings(vertices, edges)
    assert len(all_matchings) == 64 and len(set(all_matchings)) == 64
    assert all(m.bit_count() == 12 for m in all_matchings)
    assert all(len({v for k, (a, b) in enumerate(edges) if m >> k & 1
                    for v in (a, b)}) == 24 for m in all_matchings)

    # Integer signs of a bipartite planar Kasteleyn matrix:
    # vertical edges in odd columns have sign -1, horizontal edges +1.
    black = [v for v in range(24) if sum(vertices[v]) % 2 == 0]
    white = [v for v in range(24) if sum(vertices[v]) % 2 != 0]
    assert len(black) == len(white) == 12
    rb = {v:i for i,v in enumerate(black)}
    cw = {v:i for i,v in enumerate(white)}
    free = gauge_free_edges(vertices, edges)
    assert len(free) == 13
    free_index = {edge:i for i,edge in enumerate(free)}
    reduced = [sum(((m >> edge) & 1) << i for i,edge in enumerate(free))
               for m in all_matchings]
    assert len(set(reduced)) == 64

    def signed_matrix(mask):
        a = [[0]*12 for _ in range(12)]
        for edge, (u, v) in enumerate(edges):
            row, col = (rb[u], cw[v]) if u in rb else (rb[v], cw[u])
            vertical = vertices[u][0] == vertices[v][0]
            fixed_sign = -1 if vertical and vertices[u][0] % 2 else 1
            j = free_index.get(edge)
            if j is not None and mask & (1 << j):
                fixed_sign = -fixed_sign
            a[row][col] = fixed_sign
        return a

    multipliers = []
    for frequency in range(1 << 13):
        # Independent exact signed permanent by enumerating 64 matchings.
        matching_sum = sum(-1 if ((frequency & m).bit_count() & 1) else 1
                           for m in reduced)
        # A second, independent exact signed determinant calculation.
        determinant = det_bareiss(signed_matrix(frequency))
        assert matching_sum == determinant, (frequency, matching_sum, determinant)
        multipliers.append(matching_sum)

    expected = {
        -48:3, -40:8, -32:28, -24:50, -16:220, -8:1050,
        0:4781, 8:1486, 16:427, 24:86, 32:38,
        40:8, 48:6, 64:1
    }
    observed = dict(sorted(Counter(multipliers).items()))
    assert observed == expected, observed
    assert sum(expected.values()) == 8192
    assert sum(v*v for v in multipliers) == 8192*64  # Parseval
    assert min(abs(v) for v in multipliers if v) == 8
    # Vertex sign switches flip a Walsh eigenvalue's sign whenever
    # the switched vertex count is odd. Hence the full signed spectrum
    # symmetrizes the 8192 normalized determinant values.
    full_signed = {0: expected[0]*(1<<23)}
    for a in (8, 16, 24, 32, 40, 48, 64):
        frequency_count = (expected.get(a, 0) + expected.get(-a, 0))*(1<<22)
        full_signed[a] = frequency_count
        full_signed[-a] = frequency_count
    assert sum(full_signed.values()) == 1<<36

    # The range is the nonzero-multiplier Fourier span.
    indicator = [int(x != 0) for x in multipliers]
    assert sum(indicator) == 3411
    kernel_numerators = walsh(indicator)
    assert kernel_numerators[0] == 3411
    assert sum(abs(x) for x in kernel_numerators) == 164610
    sharp_norm = Fraction(sum(abs(x) for x in kernel_numerators), 8192)
    assert sharp_norm == Fraction(82305, 4096)
    # A second Fourier inversion: the projector's multiplier is an indicator.
    assert walsh(kernel_numerators) == [8192*x for x in indicator]

    # The first one-edge blind spots are exactly eight candidate positions.
    singleton_zeros = [k for k in range(len(edges))
                       if sum((-1 if m >> k & 1 else 1) for m in all_matchings) == 0]
    assert len(singleton_zeros) == 8, singleton_zeros

    print('Aztec order 3: 24 cells, 36 possible dominos, 64 tilings')
    print('Gauge quotient: 8192 normalized signed Fourier classes')
    print('All 8192 signed sums independently equal exact Kasteleyn determinants')
    print('Normalized signed spectral table:', observed)
    print('Full signed spectral table:', dict(sorted(full_signed.items())))
    print('Fourier rank quotient/full:', 3411, 3411*(1<<23))
    print('Fourier nullity quotient/full:', 4781, 4781*(1<<23))
    print('Minimum surviving magnitude: 8; condition number: 8')
    print('Sharp unrestricted endpoint projection norm:', sharp_norm)
    print('One-edge zeros:', len(singleton_zeros))
    print('PASS')

if __name__ == '__main__':
    main()
