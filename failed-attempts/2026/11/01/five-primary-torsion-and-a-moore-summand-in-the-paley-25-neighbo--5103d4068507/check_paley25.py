#!/usr/bin/env python3
"""Exact integral Morse calculation for the open-neighborhood complex of Paley(25).

Requires Python 3.10+ and SymPy (tested 1.13.1). Run from the same directory
as paley25_certificate.json. Uses integer arithmetic throughout.
"""
import hashlib
import json
import sys
from collections import Counter, defaultdict, deque
from functools import lru_cache
from pathlib import Path
from itertools import combinations
from sympy import zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def enc(a, b):
    return a % 5 + 5 * (b % 5)


def add(x, y):
    return enc(x % 5 + y % 5, x // 5 + y // 5)


def neg(x):
    return enc(-(x % 5), -(x // 5))


def mul(x, y):
    a, b, c, d = x % 5, x // 5, y % 5, y // 5
    return enc(a * c + 2 * b * d, a * d + b * c)


def boundary(mask):
    original = mask
    i = 0
    while mask:
        bit = mask & -mask
        mask -= bit
        yield original ^ bit, 1 if i % 2 == 0 else -1
        i += 1


def graph_and_faces():
    residues = {mul(x, x) for x in range(1, 25)}
    assert len(residues) == 12 and -1 % 5 in residues
    neighbors = []
    for x in range(25):
        row = [y for y in range(25)
               if y != x and add(y, neg(x)) in residues]
        assert len(row) == 12
        neighbors.append(row)
    for x in range(25):
        for y in range(25):
            assert (y in neighbors[x]) == (x in neighbors[y])
            if x != y:
                assert len(set(neighbors[x]) & set(neighbors[y])) == (5 if y in neighbors[x] else 6)
    graph_four_cliques = sum(1 for C in combinations(range(25), 4)
                             if all(b in neighbors[a] for a, b in combinations(C, 2)))
    assert graph_four_cliques == 75
    faces = set()
    for row in neighbors:
        full = 1 << len(row)
        for sub in range(1, full):
            bits = 0
            for i, vertex in enumerate(row):
                if (sub >> i) & 1:
                    bits |= 1 << vertex
            faces.add(bits)
    assert len(faces) == 93350
    expected = [25, 300, 2200, 9475, 18750, 22950,
                19800, 12375, 5500, 1650, 300, 25]
    assert [sum(f.bit_count() == k + 1 for f in faces)
            for k in range(len(expected))] == expected
    return faces, expected


def staged_matching(faces, order=range(25), verify_primary=True):
    remain = set(faces)
    pairs = {}
    for v in order:
        bit = 1 << v
        # Loop order is inessential: each admissible pair is disjoint.
        for f in sorted(remain):
            u = f | bit
            if f in remain and f != u and u in remain:
                pairs[u] = f
                remain.remove(f)
                remain.remove(u)
    if verify_primary:
        assert len(pairs) == 46529
        assert len(remain) == 292
        assert Counter(f.bit_count() - 1 for f in remain) == {0: 1, 3: 246, 4: 45}
    return pairs, remain


def verify_acyclic(faces, pairs):
    # Reverse matched covering edges; retain every other covering edge downwards.
    # An acyclic matching is exactly an acyclic resulting orientation.
    index = {f: i for i, f in enumerate(sorted(faces))}
    outgoing = [[] for _ in range(len(index))]
    indeg = [0] * len(index)
    incidence_count = 0
    for u in faces:
        for f, _ in boundary(u):
            if f not in index:
                continue
            a, b = (index[f], index[u]) if pairs.get(u) == f else (index[u], index[f])
            outgoing[a].append(b)
            indeg[b] += 1
            incidence_count += 1
    work = deque(i for i, x in enumerate(indeg) if x == 0)
    visited = 0
    while work:
        i = work.popleft()
        visited += 1
        for j in outgoing[i]:
            indeg[j] -= 1
            if indeg[j] == 0:
                work.append(j)
    assert visited == len(index), (visited, len(index))
    return incidence_count


def morse_boundary(pairs, remain):
    critical3 = sorted(f for f in remain if f.bit_count() == 4)
    critical4 = sorted(f for f in remain if f.bit_count() == 5)
    critical3_index = {mask: k for k, mask in enumerate(critical3)}
    up = {lower: upper for upper, lower in pairs.items()
          if upper.bit_count() == 5}

    @lru_cache(None)
    def project(face):
        # Quotient by the 3--4 matching relations. A face paired down to
        # a two-face represents 0 in the critical three-chain quotient.
        if face in critical3_index:
            return {critical3_index[face]: 1}
        if face not in up:
            return {}
        upper = up[face]
        incidence = dict(boundary(upper))[face]
        result = defaultdict(int)
        for lower, sign in boundary(upper):
            if lower != face:
                for i, coeff in project(lower).items():
                    result[i] -= incidence * sign * coeff
        return {i: v for i, v in result.items() if v}

    columns = []
    for upper in critical4:
        result = defaultdict(int)
        for face, sign in boundary(upper):
            for i, coeff in project(face).items():
                result[i] += sign * coeff
        columns.append([[i, int(v)] for i, v in sorted(result.items()) if v])
    return critical3, critical4, columns


def rank_mod(cols, nrow, p):
    # Sparse Gaussian elimination with pivot rows and rational-free arithmetic.
    pivots = {}
    for entries in cols:
        work = {i: val % p for i, val in entries if val % p}
        while work:
            pivot = min(work)
            coeff = work[pivot]
            if pivot not in pivots:
                inverse = pow(coeff, -1, p)
                pivots[pivot] = {i: (val * inverse) % p for i, val in work.items()}
                break
            row = pivots[pivot]
            for i, val in row.items():
                z = (work.get(i, 0) - coeff * val) % p
                if z:
                    work[i] = z
                else:
                    work.pop(i, None)
    return len(pivots)


def main():
    faces, f_vector = graph_and_faces()
    pairs, critical = staged_matching(faces)
    incidences = verify_acyclic(faces, pairs)
    critical3, critical4, columns = morse_boundary(pairs, critical)
    assert len(critical3) == 246 and len(critical4) == 45
    assert sum(len(c) for c in columns) == 1051
    matrix = zeros(246, 45)
    for j, column in enumerate(columns):
        for i, val in column:
            matrix[i, j] = val
    smith = smith_normal_form(matrix, domain=ZZ)
    diag = [int(abs(smith[i, i])) for i in range(45) if smith[i, i]]
    assert Counter(diag) == {1: 40, 5: 1}, Counter(diag)
    modular_ranks = {str(p): rank_mod(columns, 246, p) for p in [2, 3, 5, 7, 11]}
    assert modular_ranks == {'2': 41, '3': 41, '5': 40, '7': 41, '11': 41}
    # Independent staged matching order, with different critical-cell counts.
    alternate_order = list(range(0, 25, 2)) + list(range(1, 25, 2))
    alternate_pairs, alternate_critical = staged_matching(
        faces, order=alternate_order, verify_primary=False)
    assert verify_acyclic(faces, alternate_pairs) == incidences
    alt3, alt4, alternate_columns = morse_boundary(alternate_pairs, alternate_critical)
    assert (len(alt3), len(alt4)) == (237, 36)
    alt_matrix = zeros(len(alt3), len(alt4))
    for j, col in enumerate(alternate_columns):
        for i, val in col:
            alt_matrix[i, j] = val
    alt_smith = smith_normal_form(alt_matrix, domain=ZZ)
    alt_diag = [int(abs(alt_smith[i, i])) for i in range(len(alt4))
                if alt_smith[i, i]]
    assert Counter(alt_diag) == {1: 31, 5: 1}, Counter(alt_diag)
    assert len(alt3) - len(alt_diag) == 205
    assert len(alt4) - len(alt_diag) == 4
    pair_data = [[int(upper), int(lower)] for upper, lower in sorted(pairs.items())]
    pair_sha = hashlib.sha256(json.dumps(pair_data, separators=(',', ':')).encode()).hexdigest()
    cert = {
        'field_model': 'GF(5)[t]/(t^2-2); a+bt encoded as a+5b',
        'graph_order': 25,
        'graph_degree': 12,
        'graph_parameters': [25, 12, 5, 6],
        'four_cliques': 75,
        'simplicial_face_vector': f_vector,
        'nonempty_faces': len(faces),
        'hasse_incidences': incidences,
        'matching_pairs': len(pairs),
        'matching_pairs_sha256': pair_sha,
        'critical_face_counts': [1, 0, 0, 246, 45],
        'critical_3_masks': critical3,
        'critical_4_masks': critical4,
        'morse_boundary_sparse_columns': columns,
        'nonzero_morse_boundary_entries': sum(len(c) for c in columns),
        'smith_nonzero_invariants': diag,
        'modular_ranks': modular_ranks,
        'alternate_vertex_order': alternate_order,
        'alternate_critical_3': len(alt3),
        'alternate_critical_4': len(alt4),
        'alternate_smith_nonzero_invariants': alt_diag,
        'homology': {'H3': 'Z^205 plus Z/5', 'H4': 'Z^4', 'other_reduced': '0'}
    }
    path = Path(__file__).with_name('paley25_certificate.json')
    serialized = json.dumps(cert, ensure_ascii=False, sort_keys=True, indent=2) + '\n'
    if '--write-certificate' in sys.argv:
        path.write_text(serialized, encoding='utf-8')
    else:
        assert path.read_text(encoding='utf-8') == serialized, 'certificate mismatch'
    print('PALEY25_NEIGHBORHOOD_INTEGRAL_5_TORSION_MORSE_OK')
    print('facevector', f_vector, 'incidences', incidences,
          'pairs', len(pairs), 'critical3', len(critical3), 'critical4', len(critical4))
    print('SNF', Counter(diag), 'ranks', modular_ranks,
          'alternate', Counter(alt_diag))


if __name__ == '__main__':
    main()
