#!/usr/bin/env python3
"""Exact integer and mod-two checks for the fourth-power 16-cycle open-neighborhood complex."""
from collections import defaultdict, deque
import json
import sys
from pathlib import Path

N, K = 16, 4


def bit_indices(mask):
    while mask:
        b = mask & -mask
        yield b.bit_length() - 1
        mask ^= b


def faces_from_facets():
    result = {0}
    facets = []
    for center in range(N):
        verts = sorted({(center + step) % N for step in range(-K, K + 1) if step != 0})
        facet = sum(1 << i for i in verts)
        facets.append(facet)
        for m in range(1, 1 << len(verts)):
            face = 0
            for j in bit_indices(m):
                face |= 1 << verts[j]
            result.add(face)
    assert len(facets) == len(set(facets)) == 16
    assert len(result) == 2713
    assert {m for m in range(1 << N) if m == 0 or any((m & f) == m for f in facets)} == result
    return result


def elementary_collapses(faces):
    remaining = set(faces)
    upcount = {face: 0 for face in remaining}
    for upper in remaining:
        for v in bit_indices(upper):
            upcount[upper ^ (1 << v)] += 1
    queue = deque(sorted(face for face, c in upcount.items() if face and c == 1))
    total = 0
    while queue:
        lower = queue.popleft()
        if lower not in remaining or upcount[lower] != 1:
            continue
        supers = [lower | (1 << v) for v in range(N)
                  if not (lower >> v & 1) and (lower | (1 << v)) in remaining]
        assert len(supers) == 1
        upper = supers[0]
        assert upcount[upper] == 0  # unique coface is maximal
        remaining.remove(lower)
        remaining.remove(upper)
        total += 1
        for deleted in (lower, upper):
            for v in bit_indices(deleted):
                face = deleted ^ (1 << v)
                upcount[face] -= 1
                if face and upcount[face] == 1:
                    queue.append(face)
    assert total == 999 and len(remaining) == 715
    assert all(sub in remaining for face in remaining for v in bit_indices(face)
               for sub in [face ^ (1 << v)])
    return remaining, total


def integral_unit_matrix(faces, degree):
    high = sorted(x for x in faces if x.bit_count() == degree + 1)
    low = sorted(x for x in faces if x.bit_count() == degree)
    lowpos = {x: i for i, x in enumerate(low)}
    columns = {j: {lowpos[face ^ (1 << v)]: (-1 if h % 2 else 1)
                   for h, v in enumerate(bit_indices(face))}
               for j, face in enumerate(high)}
    rows = defaultdict(set)
    for j, col in columns.items():
        for i in col:
            rows[i].add(j)
    rank, largest = 0, 1
    while True:
        unit_entries = ((len(rows[i]) * len(col), len(rows[i]) + len(col), i, j)
                        for j, col in columns.items() for i, coeff in col.items()
                        if abs(coeff) == 1)
        chosen = min(unit_entries, default=None)
        if chosen is None:
            break
        _, _, row, col = chosen
        pivot_column = columns[col]
        pivot = pivot_column[row]
        for other in list(rows[row] - {col}):
            q = columns[other]
            factor = q[row] // pivot
            for r, val in pivot_column.items():
                updated = q.get(r, 0) - factor * val
                if updated:
                    q[r] = updated
                    rows[r].add(other)
                    largest = max(largest, abs(updated))
                else:
                    q.pop(r, None)
                    rows[r].discard(other)
        for r in pivot_column:
            rows[r].discard(col)
        del rows[row]
        del columns[col]
        rank += 1
    assert not any(columns.values()), "Nonunit integer diagonal not resolved"
    return rank, largest


def echelon_columns(vectors):
    pivots, relations = {}, []
    for j, word in enumerate(vectors):
        expression = 1 << j
        while word:
            i = word.bit_length() - 1
            if i in pivots:
                old, repr_word = pivots[i]
                word ^= old
                expression ^= repr_word
            else:
                pivots[i] = (word, expression)
                break
        if not word:
            relations.append(expression)
    return pivots, relations


def reduce_word(word, pivots):
    while word:
        i = word.bit_length() - 1
        if i not in pivots:
            return word
        v = pivots[i]
        word ^= (v[0] if isinstance(v, tuple) else v)
    return 0


def mod_two_certificates(original):
    by = {degree: sorted(x for x in original if x.bit_count() == degree + 1)
          for degree in range(8)}
    pos = {degree: {face: j for j, face in enumerate(by[degree])}
           for degree in by}

    def boundary_columns(degree):
        return [sum(1 << pos[degree - 1][face ^ (1 << v)] for v in bit_indices(face))
                for face in by[degree]]

    def delta_rows(degree):
        return [sum(1 << pos[degree][face ^ (1 << v)] for v in bit_indices(face))
                for face in by[degree + 1]]

    for degree in range(2, 8):
        bc = boundary_columns(degree)
        prev = boundary_columns(degree - 1)
        for col in bc:
            residual = 0
            for j in bit_indices(col):
                residual ^= prev[j]
            assert residual == 0, f"Boundary square in dimension {degree}"

    ranks = {}
    for degree in range(1, 8):
        p, _ = echelon_columns(boundary_columns(degree))
        ranks[degree] = len(p)
    ranks[0] = 0
    betti = {degree: len(by[degree]) - ranks[degree] - ranks.get(degree + 1, 0)
             for degree in range(8)}
    assert [betti[d] for d in range(8)] == [1, 0, 7, 1, 1, 0, 0, 0]

    # A genuine nonbounding four-cycle, expressed in the original 4-chain basis.
    _, kernel4 = echelon_columns(boundary_columns(4))
    image5, _ = echelon_columns(boundary_columns(5))
    z4 = next(word for word in kernel4 if reduce_word(word, image5))
    check = 0
    b4 = boundary_columns(4)
    for j in bit_indices(z4):
        check ^= b4[j]
    assert check == 0 and reduce_word(z4, image5) != 0

    # Seven 2-cocycles, independent modulo the 1-coboundaries.
    rows = delta_rows(2)
    echelon_rows = {}
    for word in rows:
        while word:
            i = word.bit_length() - 1
            if i in echelon_rows:
                word ^= echelon_rows[i]
            else:
                echelon_rows[i] = word
                break
    representatives = []
    for j in sorted(set(range(len(by[2]))) - set(echelon_rows)):
        word = 1 << j
        for p in sorted(echelon_rows):
            if (echelon_rows[p] & word).bit_count() % 2:
                word ^= 1 << p
        assert all((row & word).bit_count() % 2 == 0 for row in rows)
        representatives.append(word)
    im_d1 = []
    for edge in by[1]:
        word = sum(1 << j for j, tri in enumerate(by[2]) if tri & edge == edge)
        im_d1.append(word)
    p1, _ = echelon_columns(im_d1)
    span = {p: x for p, (x, _) in p1.items()}
    assert len(span) == 105
    H2 = []
    for word in representatives:
        residue = reduce_word(word, span)
        if residue:
            span[residue.bit_length() - 1] = residue
            H2.append(word)
    assert len(H2) == 7
    assert len(representatives) == 112

    # Alexander-Whitney cup product of 2-cocycles against one generator of H_4.
    entries = []
    for j in bit_indices(z4):
        vertices = list(bit_indices(by[4][j]))
        tri1 = sum(1 << v for v in vertices[:3])
        tri2 = sum(1 << v for v in vertices[2:])
        entries.append((pos[2][tri1], pos[2][tri2]))
    pair = [[sum(((a >> x) & 1) * ((b >> y) & 1) for x, y in entries) % 2
             for b in H2] for a in H2]
    assert pair == [[0] * 7 for _ in range(7)]
    cert = {
        'graph_vertices': N, 'distance_steps': [1, 2, 3, 4],
        'face_vector': [len(by[d]) for d in range(8)],
        'mod_two_betti': [betti[d] for d in range(8)],
        'four_cycle_in_sorted_four_simplex_basis_hex': hex(z4),
        'two_cocycles_in_sorted_triangle_basis_hex': [hex(x) for x in H2],
        'four_cycle_support': z4.bit_count(),
        'cup_product_matrix_mod_two': pair,
    }
    return cert


def main():
    original = faces_from_facets()
    fv = [sum(x.bit_count() == d + 1 for x in original) for d in range(8)]
    assert fv == [16, 120, 432, 784, 784, 432, 128, 16]
    collapsed, removed_pairs = elementary_collapses(original)
    cvec = [sum(x.bit_count() == d + 1 for x in collapsed) for d in range(5)]
    assert cvec == [16, 98, 243, 255, 102]
    ranks = [integral_unit_matrix(collapsed, d) for d in range(1, 5)]
    assert [r for r, _ in ranks] == [15, 83, 153, 101]
    assert max(coeff for _, coeff in ranks) <= 2
    beta = [cvec[0] - ranks[0][0]] + [cvec[d] - ranks[d-1][0] - (ranks[d][0] if d<4 else 0) for d in range(1,5)]
    assert beta == [1, 0, 7, 1, 1]
    cert = mod_two_certificates(original)
    text = '\n'.join([
        'C16 FOURTH-POWER OPEN NEIGHBORHOOD COMPLEX: EXACT CHECKS',
        'Original nonempty faces: 2712',
        'Original dimensions 0..7: 16 120 432 784 784 432 128 16',
        'Elementary free-face pairs: 999',
        'Remaining dimensions 0..4: 16 98 243 255 102',
        'Integral unit Smith ranks d1..d4: 15 83 153 101',
        'All nonzero integer Smith factors: 1',
        'Integral Betti numbers degrees 0..4: 1 0 7 1 1',
        'Independent original mod-2 Betti numbers 0..7: 1 0 7 1 1 0 0 0',
        'Degree-four mod-2 cycle support: ' + str(cert['four_cycle_support']),
        'Two-dimensional cohomology basis size: 7',
        'Mod-2 degree-two cup pairing: zero 7-by-7 matrix',
        'VERIFY_OK',
    ]) + '\n'
    if len(sys.argv) > 1:
        certificate_path = Path(sys.argv[1])
        if certificate_path.exists():
            with certificate_path.open('r', encoding='utf-8') as fp:
                assert json.load(fp) == cert, 'Explicit certificate mismatch'
        else:
            with certificate_path.open('w', encoding='utf-8') as fp:
                json.dump(cert, fp, indent=2, sort_keys=True)
                fp.write('\n')
    print(text, end='')

if __name__ == '__main__':
    main()
