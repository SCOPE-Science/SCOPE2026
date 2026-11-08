#!/usr/bin/env python3
"""Exact finite verification of the ordinary matching complex of M_16.

The graph uses residues modulo 16, the cyclic edges and eight antipodal
edges. All matching faces, the acyclic matching, its integral Morse chain
complex and independent mod-2 simplicial homology are rebuilt from scratch.
Run: python3 verify_m16.py  (requires sympy for Smith normal form).
"""
from collections import Counter, defaultdict, deque
from pathlib import Path
import json
from functools import lru_cache
from sympy import Matrix, zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form


def graph_edges(n=8):
    size = 2 * n
    return tuple(sorted({tuple(sorted((i, (i + 1) % size))) for i in range(size)} |
                        {tuple(sorted((i, i + n))) for i in range(n)}))


def face_complex(edges):
    conflicts = []
    for i, (a, b) in enumerate(edges):
        conflicts.append(sum(1 << j for j, (c, d) in enumerate(edges)
                             if i != j and ({a, b} & {c, d})))
    faces = {0}
    for i in range(len(edges)):
        faces.update({m | (1 << i) for m in list(faces) if not (m & conflicts[i])})
    for m in faces:
        used = set()
        for i, (a, b) in enumerate(edges):
            if m & (1 << i):
                assert a not in used and b not in used
                used.add(a)
                used.add(b)
    return faces


def lower_faces(mask):
    return tuple((mask ^ (1 << i), (-1) ** j)
                 for j, i in enumerate(i for i in range(mask.bit_length()) if mask & (1 << i)))


def verified_acyclic_matching(faces, vertex_count):
    remaining = set(faces)
    pairs = []
    for i in range(vertex_count):
        stage = [(a, a | (1 << i)) for a in sorted(remaining)
                 if not (a & (1 << i)) and (a | (1 << i)) in remaining]
        for a, b in stage:
            assert a in remaining and b in remaining
            assert b.bit_count() == a.bit_count() + 1
            remaining.remove(a)
            remaining.remove(b)
        pairs.extend(stage)
    critical = set(remaining)
    assert 2 * len(pairs) + len(critical) == len(faces)

    paired = set(pairs)
    indegree = dict.fromkeys(faces, 0)
    adjacency = {face: [] for face in faces}
    incidence_count = 0
    for upper in faces:
        for lower, sign in lower_faces(upper):
            assert lower in faces and abs(sign) == 1
            source, target = (lower, upper) if (lower, upper) in paired else (upper, lower)
            adjacency[source].append(target)
            indegree[target] += 1
            incidence_count += 1
    queue = deque(face for face, d in indegree.items() if d == 0)
    processed = 0
    while queue:
        source = queue.popleft()
        processed += 1
        for target in adjacency[source]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    assert processed == len(faces), 'Directed Hasse graph has a cycle'
    return pairs, critical, incidence_count


def morse_differentials(critical, pairs):
    up = dict(pairs)
    upper = set(up.values())

    @lru_cache(None)
    def projection(face):
        if face in critical:
            return {face: 1}
        if face in upper:
            return {}
        matched_upper = up[face]
        signed_faces = dict(lower_faces(matched_upper))
        pivot = signed_faces[face]
        assert pivot in (-1, 1)
        result = defaultdict(int)
        for alternate, sign in signed_faces.items():
            if alternate == face:
                continue
            for c, coefficient in projection(alternate).items():
                result[c] -= pivot * sign * coefficient
        return {c: coefficient for c, coefficient in result.items() if coefficient}

    by_dim = {k: sorted(face for face in critical if face.bit_count() == k + 1)
              for k in range(-1, 9)}
    diff = {}
    for k in range(0, 9):
        rows, cols = by_dim[k - 1], by_dim[k]
        row_idx = {face: i for i, face in enumerate(rows)}
        D = zeros(len(rows), len(cols))
        for j, simplex in enumerate(cols):
            for face, sign in lower_faces(simplex):
                for critical_face, coefficient in projection(face).items():
                    assert critical_face in row_idx
                    D[row_idx[critical_face], j] += sign * coefficient
        diff[k] = D
    for k in range(1, 9):
        assert diff[k - 1] * diff[k] == zeros(diff[k - 1].rows, diff[k].cols)
    return by_dim, diff


def smith(D):
    if D.rows == 0 or D.cols == 0:
        return ()
    S = smith_normal_form(D, domain=ZZ)
    return tuple(abs(int(S[i, i])) for i in range(min(S.rows, S.cols)) if S[i, i] != 0)


def mod_two_homology(faces):
    by_dim = {k: sorted(face for face in faces if face.bit_count() == k + 1)
              for k in range(-1, 9)}
    ranks = {}
    for k in range(0, 9):
        rows = {face: i for i, face in enumerate(by_dim[k - 1])}
        pivot_map = {}
        for simplex in by_dim[k]:
            bits = 0
            for face, _ in lower_faces(simplex):
                bits ^= 1 << rows[face]
            while bits:
                pivot = bits.bit_length() - 1
                if pivot not in pivot_map:
                    pivot_map[pivot] = bits
                    break
                bits ^= pivot_map[pivot]
        ranks[k] = len(pivot_map)
    return {k: len(by_dim[k]) - ranks[k] - ranks[k + 1]
            for k in range(0, 8)}


def main():
    edges = graph_edges()
    assert len(edges) == 24
    faces = face_complex(edges)
    f_vector = {k: sum(face.bit_count() == k + 1 for face in faces)
                for k in range(-1, 8)}
    assert f_vector == {-1: 1, 0: 24, 1: 228, 2: 1096, 3: 2834,
                        4: 3880, 5: 2588, 6: 696, 7: 47}
    assert len(faces) == 11394
    pairs, critical, incidences = verified_acyclic_matching(faces, len(edges))
    assert len(pairs) == 5673
    critical_counts = Counter(m.bit_count() - 1 for m in critical)
    assert critical_counts == {3: 2, 4: 23, 5: 23}
    assert incidences == sum((k + 1) * c for k, c in f_vector.items() if k >= 0)
    cells, diff = morse_differentials(critical, pairs)
    d4, d5 = diff[4], diff[5]
    assert d4.shape == (2, 23) and d5.shape == (23, 23)
    assert d4 * d5 == zeros(2, 23)
    assert smith(d4) == (1, 1)
    assert smith(d5) == (1,) * 19
    certificate_path = Path(__file__).with_name('morse_certificate.json')
    if certificate_path.is_file():
        certificate = json.loads(certificate_path.read_text(encoding='utf-8'))
        assert certificate['edges'] == [list(e) for e in edges]
        assert certificate['matching_pairs'] == [list(p) for p in pairs]
        assert certificate['critical_masks'] == sorted(critical)
        assert certificate['d4'] == d4.tolist()
        assert certificate['d5'] == d5.tolist()
    betti = mod_two_homology(faces)
    assert betti == {0: 0, 1: 0, 2: 0, 3: 0, 4: 2, 5: 4, 6: 0, 7: 0}
    print('GRAPH_EDGES', len(edges))
    print('SIMPLEX_VECTOR', [f_vector[k] for k in range(-1, 8)])
    print('TOTAL_FACES', len(faces))
    print('HASSE_INCIDENCES', incidences)
    print('MATCHED_PAIRS', len(pairs))
    print('CRITICAL_CELLS', dict(sorted(critical_counts.items())))
    print('MORSE_D4_SMITH', smith(d4))
    print('MORSE_D5_SMITH', smith(d5))
    print('MORSE_DIFFERENTIAL_PRODUCT_ZERO', d4 * d5 == zeros(2, 23))
    print('DIRECT_SIMPLICIAL_MOD2_BETTI', betti)
    print('ALL_VERIFY_OK')

if __name__ == '__main__':
    main()
