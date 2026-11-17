#!/usr/bin/env python3
"""Exact integral and equivariant homology certificate for a graph cut complex.

Only the Python standard library is required; all incidence and chain data are
reconstructed from the fixed 11-vertex graph and are integer arithmetic.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations

N = 11
NEIGHBORS = {
    0: (1, 3, 4), 1: (2, 5, 6), 2: (3, 7), 3: (8, 9),
    4: (5, 9), 5: (10,), 6: (7, 10), 7: (8,),
    8: (10,), 9: (10,)
}
EDGES = {tuple(sorted((u, v))) for u, vs in NEIGHBORS.items() for v in vs}
ADJ = [0] * N
for u, v in EDGES:
    ADJ[u] |= 1 << v
    ADJ[v] |= 1 << u


def vertices(mask):
    return tuple(i for i in range(N) if mask & (1 << i))


def connected(mask):
    if mask == 0:
        return False
    reach = mask & -mask
    while True:
        new = reach
        for i in vertices(reach):
            new |= ADJ[i] & mask
        if new == reach:
            return new == mask
        reach = new


def dual_admissible(mask):
    return all(connected(sum(1 << v for v in trip))
               for trip in combinations(vertices(mask), 3))


def boundary_matrix(previous, current):
    idx = {f: i for i, f in enumerate(previous)}
    matrix = [[0] * len(current) for _ in previous]
    for col, mask in enumerate(current):
        for k, v in enumerate(vertices(mask)):
            matrix[idx[mask ^ (1 << v)]][col] = (-1) ** k
    return matrix


def unimodular_unit_pivots(matrix):
    """All operations are unimodular over Z; return unit pivots and residual."""
    m = [row[:] for row in matrix]
    rows = len(m)
    cols = len(m[0]) if rows else 0
    r = 0
    while r < min(rows, cols):
        loc = next(((i, j) for i in range(r, rows)
                    for j in range(r, cols) if abs(m[i][j]) == 1), None)
        if loc is None:
            break
        i, j = loc
        m[i], m[r] = m[r], m[i]
        for row in m:
            row[j], row[r] = row[r], row[j]
        pivot = m[r][r]
        for i in range(r + 1, rows):
            coeff = m[i][r] // pivot
            if coeff:
                for j in range(r, cols):
                    m[i][j] -= coeff * m[r][j]
        # Complete diagonalization by integral column operations; these do
        # not alter the lower-right remainder after the row elimination.
        for j in range(r + 1, cols):
            coeff = m[r][j] // pivot
            if coeff:
                for i in range(rows):
                    m[i][j] -= coeff * m[i][r]
        r += 1
    residual = max((abs(m[i][j]) for i in range(r, rows)
                    for j in range(r, cols)), default=0)
    return r, residual


def rank_mod_p(matrix, p):
    x = [[entry % p for entry in row] for row in matrix]
    rows = len(x)
    cols = len(x[0]) if rows else 0
    r = 0
    for c in range(cols):
        i = next((i for i in range(r, rows) if x[i][c]), None)
        if i is None:
            continue
        x[r], x[i] = x[i], x[r]
        inverse = pow(x[r][c], -1, p)
        x[r] = [(z * inverse) % p for z in x[r]]
        for i in range(rows):
            if i != r and x[i][c]:
                q = x[i][c]
                x[i] = [(a - q * b) % p for a, b in zip(x[i], x[r])]
        r += 1
        if r == rows:
            break
    return r


def mod_p_in_image(matrix, vector, p):
    return rank_mod_p(matrix, p) == rank_mod_p(
        [row + [v] for row, v in zip(matrix, vector)], p)


def rank_over_two_from_faces(lower, upper):
    """Separate F2 column reduction using bitset incidence columns."""
    idx = {face: k for k, face in enumerate(lower)}
    basis = {}
    for simplex in upper:
        col = 0
        for v in vertices(simplex):
            col ^= (1 << idx[simplex ^ (1 << v)])
        while col:
            pivot = col.bit_length() - 1
            if pivot in basis:
                col ^= basis[pivot]
            else:
                basis[pivot] = col
                break
    return len(basis)


def perm_sign(ordered):
    inversions = sum(a > b for i, a in enumerate(ordered)
                     for b in ordered[i + 1:])
    return (-1) ** inversions


def cycle_type(g):
    seen = set()
    lengths = []
    for v in range(N):
        if v in seen:
            continue
        w = v
        length = 0
        while w not in seen:
            seen.add(w)
            w = g[w]
            length += 1
        lengths.append(length)
    return tuple(sorted(Counter(lengths).items()))


def signed_trace(faces, g):
    total = 0
    for mask in faces:
        seq = [g[v] for v in vertices(mask)]
        if tuple(sorted(seq)) == vertices(mask):
            total += perm_sign(seq)
    return total


def all_automorphisms():
    high = (1, 3, 10)
    low = (4, 7)
    rest = tuple(sorted(set(range(N)) - set(high) - set(low)))
    def signature(v):
        adjacent_high = frozenset(w for w in high if ADJ[v] & (1 << w))
        adjacent_low = tuple(w for w in low if ADJ[v] & (1 << w))
        assert len(adjacent_high) == 2 and len(adjacent_low) == 1
        return adjacent_high, adjacent_low[0]
    inverse = {signature(v): v for v in rest}
    assert len(inverse) == 6
    result = []
    for hh in permutations(high):
        for ll in permutations(low):
            f = dict(zip(high, hh))
            f.update(zip(low, ll))
            for v in rest:
                a, z = signature(v)
                f[v] = inverse[frozenset(f[w] for w in a), f[z]]
            g = tuple(f[i] for i in range(N))
            assert len(set(g)) == N
            assert {tuple(sorted((g[u], g[v]))) for u, v in EDGES} == EDGES
            result.append(g)
    assert len(result) == 12 and len(set(result)) == 12
    return result


def main():
    assert len(EDGES) == 18
    disconnected_triples = []
    for combo in combinations(range(N), 3):
        mask = sum(1 << i for i in combo)
        if not connected(mask):
            disconnected_triples.append(mask)
    assert len(disconnected_triples) == 123
    # Ordinary cut complex generated by complements of disconnected triples.
    full = (1 << N) - 1
    cut_facets = [full ^ t for t in disconnected_triples]
    cut_faces = {s for f in cut_facets for s in range(1, 1 << N) if s & ~f == 0}
    count = tuple(sum(s.bit_count() == d + 1 for s in cut_faces) for d in range(8))
    assert count == (11, 55, 165, 330, 462, 462, 321, 123), count
    # Independent direct mod-two ranks on the full original cut complex.
    sorted_cut = {d: sorted(face for face in cut_faces if face.bit_count() == d + 1)
                  for d in range(8)}
    ranks_cut = tuple(rank_over_two_from_faces(sorted_cut[d-1], sorted_cut[d])
                      for d in range(1,8))
    assert ranks_cut == (10, 45, 120, 210, 252, 210, 110), ranks_cut
    # Alexander dual; record all sizes and prove no faces of cardinality >=5.
    dual_all = [s for s in range(1, 1 << N) if dual_admissible(s)]
    assert max(s.bit_count() for s in dual_all) == 4
    T = {d: sorted(s for s in dual_all if s.bit_count() == d + 1)
         for d in range(4)}
    assert tuple(len(T[d]) for d in range(4)) == (11, 55, 42, 9)
    B = {d: boundary_matrix(T[d - 1], T[d]) for d in range(1, 4)}
    pivots = {d: unimodular_unit_pivots(B[d]) for d in range(1, 4)}
    assert pivots == {1: (10, 0), 2: (32, 0), 3: (9, 0)}, pivots
    # Integer chain: 18 oriented triangles, coefficients all +/-1.
    cycle_terms = {
        (0, 1, 2): 1, (0, 2, 3): 1, (0, 1, 5): -1,
        (0, 4, 5): 1, (1, 2, 7): -1, (1, 6, 7): 1,
        (2, 3, 8): -1, (2, 7, 8): 1, (6, 7, 8): -1,
        (0, 3, 9): 1, (0, 4, 9): -1, (1, 5, 10): 1,
        (4, 5, 10): -1, (1, 6, 10): -1, (3, 8, 10): 1,
        (6, 8, 10): -1, (3, 9, 10): -1, (4, 9, 10): 1
    }
    z = [cycle_terms.get(vertices(s), 0) for s in T[2]]
    assert sum(abs(a) for a in z) == 18
    assert all(sum(a * b for a, b in zip(row, z)) == 0 for row in B[2])
    assert not mod_p_in_image(B[3], z, 3)
    # Character table: cycle type -> (number, H6 character, H7 character).
    expected = {
        ((1, 11),): (1, 1, 13),
        ((1, 5), (2, 3)): (3, 1, -5),
        ((1, 3), (2, 4)): (1, -1, -1),
        ((1, 1), (2, 5)): (3, -1, 1),
        ((1, 2), (3, 3)): (2, 1, 1),
        ((2, 1), (3, 1), (6, 1)): (2, -1, -1)
    }
    classes = defaultdict(list)
    for g in all_automorphisms():
        g_z = [0] * len(z)
        pos = {s: i for i, s in enumerate(T[2])}
        for mask, coeff in zip(T[2], z):
            if coeff == 0:
                continue
            mapped_vertices = [g[v] for v in vertices(mask)]
            mapped = sum(1 << v for v in mapped_vertices)
            g_z[pos[mapped]] += perm_sign(mapped_vertices) * coeff
        is_plus = mod_p_in_image(B[3], [(x - y) % 3 for x, y in zip(g_z, z)], 3)
        is_minus = mod_p_in_image(B[3], [(x + y) % 3 for x, y in zip(g_z, z)], 3)
        assert is_plus != is_minus
        char_h2_dual = 1 if is_plus else -1
        alt_trace_dual = sum((-1)**d * signed_trace(T[d], g) for d in range(4)) - 1
        char_h1_dual = char_h2_dual - alt_trace_dual
        char_h6 = perm_sign(g) * char_h2_dual
        char_h7 = perm_sign(g) * char_h1_dual
        # Independently check the stated rational irreducible decomposition
        # for the product of the 3-point and 2-point permutation actions.
        sign_A = perm_sign([g[v] for v in (1, 3, 10)])
        sign_Z = perm_sign([g[v] for v in (4, 7)])
        standard_A = sum(g[v] == v for v in (1, 3, 10)) - 1
        assert char_h6 == sign_Z
        assert char_h7 == (2 * sign_A + 2 * standard_A) + \
            sign_Z * (3 * sign_A + 2 * standard_A)
        # Independently use traces on all faces of original cut complex.
        signed_lef_cut = sum((-1)**(mask.bit_count() - 1) *
                             (perm_sign([g[v] for v in vertices(mask)]))
                             for mask in cut_faces
                             if tuple(sorted(g[v] for v in vertices(mask))) == vertices(mask)) - 1
        assert signed_lef_cut == char_h6 - char_h7, (g, signed_lef_cut, char_h6, char_h7)
        classes[cycle_type(g)].append((char_h6, char_h7))
    observed = {key: (len(vals), *vals[0]) for key, vals in classes.items()}
    assert all(set(vals) == {vals[0]} for vals in classes.values())
    assert observed == expected, (observed, expected)
    assert sum(c * a for c, a, b in expected.values()) == 0
    assert sum(c * b for c, a, b in expected.values()) == 0
    print('HERSCHEL_GRAPH vertices=11 edges=18 automorphisms=12')
    print('CUT_COMPLEX facets=123 faces=1929 f_vector=' + str(count))
    print('ORIGINAL_CUT_MOD2_BOUNDARY_RANKS ' + str(ranks_cut))
    print('ALEXANDER_DUAL f_vector=(11,55,42,9) no_higher_faces=YES')
    print('INTEGER_UNIT_PIVOTS ' + str(pivots))
    print('DUAL_HOMOLOGY H1=Z^13 H2=Z other_reduced=0 torsion=none')
    print('CUT_HOMOLOGY H6=Z H7=Z^13 other_reduced=0 torsion=none')
    for key in sorted(expected):
        print('AUTOMORPHISM_CLASS cycle_type=' + str(key) + ' size,H6,H7=' + str(expected[key]))
    print('INVARIANT_DIMENSIONS H6=0 H7=0')
    print('EXACT_INTEGER_CYCLE terms=18 mod3_nonboundary=YES')
    print('DIRECT_CUT_LEFSCHETZ all_12=PASS')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
