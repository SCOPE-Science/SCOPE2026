#!/usr/bin/env python3
"""Reproduce the integral discrete-Morse certificate for Ind(C_11 x K_3).

Requires only Python 3.10+ and the adjacent morse_matrices.json. Enumerates
all faces, constructs two opposite-order acyclic matchings, computes their
signed Morse boundaries, and performs exact elementary integral operations.
"""
from array import array
from collections import Counter, defaultdict, deque
from functools import lru_cache
from pathlib import Path
import json

LENGTH = 11
COLORS = 3
N = LENGTH * COLORS
ADJ = [sum(1 << (q * COLORS + d)
           for q in ((r - 1) % LENGTH, (r + 1) % LENGTH)
           for d in range(COLORS) if d != c)
       for r in range(LENGTH) for c in range(COLORS)]


def faces():
    out = [0]
    for i in range(N):
        bit = 1 << i
        out += [s | bit for s in out if not (s & ADJ[i])]
    return out


def boundary(face):
    original, index = face, 0
    while face:
        bit = face & -face
        yield original ^ bit, (-1 if index % 2 else 1)
        face -= bit
        index += 1


def stage_matching(face_list, vertex_order):
    present, partners = set(face_list), {}
    pairs = 0
    for i in vertex_order:
        bit = 1 << i
        for lower in face_list:
            if lower == 0 or lower & bit or lower in partners:
                continue
            upper = lower | bit
            if upper in present and upper not in partners:
                partners[lower] = upper
                partners[upper] = lower
                pairs += 1
    critical = [s for s in face_list if s not in partners]
    return partners, critical, pairs


def check_acyclic(face_list, partners):
    """Kahn topological sort on every Hasse incidence, reversed on pairs."""
    where = {f: i for i, f in enumerate(face_list)}
    indegrees = array('i', [0]) * len(face_list)
    incidences = 0
    for s in face_list:
        for t, _ in boundary(s):
            if partners.get(s) == t:
                indegrees[where[s]] += 1
            else:
                indegrees[where[t]] += 1
            incidences += 1
    ready = deque(i for i, v in enumerate(indegrees) if v == 0)
    visited = 0
    while ready:
        index = ready.popleft()
        s = face_list[index]
        visited += 1
        for t, _ in boundary(s):
            if partners.get(s) != t:
                j = where[t]
                indegrees[j] -= 1
                if indegrees[j] == 0:
                    ready.append(j)
        upper = partners.get(s)
        if upper is not None and upper.bit_count() > s.bit_count():
            j = where[upper]
            indegrees[j] -= 1
            if indegrees[j] == 0:
                ready.append(j)
    assert visited == len(face_list), (visited, len(face_list))
    return incidences


def signed_morse_boundary(critical, partners):
    rows = sorted(s for s in critical if s.bit_count() == 7)
    cols = sorted(s for s in critical if s.bit_count() == 8)
    crit = set(critical)
    row_set = set(rows)

    @lru_cache(maxsize=None)
    def projection(s):
        if s in crit:
            return {s: 1} if s in row_set else {}
        partner = partners[s]
        if s.bit_count() > partner.bit_count():
            return {}
        bd = list(boundary(partner))
        coefficient = next(c for t, c in bd if t == s)
        result = defaultdict(int)
        for t, sign in bd:
            if t == s:
                continue
            for basis, value in projection(t).items():
                result[basis] -= coefficient * sign * value
        return {basis: value for basis, value in result.items() if value}

    matrix = [[0] * len(cols) for _ in rows]
    for j, upper in enumerate(cols):
        result = defaultdict(int)
        for lower, sign in boundary(upper):
            for basis, value in projection(lower).items():
                result[basis] += sign * value
        for i, basis in enumerate(rows):
            matrix[i][j] = result[basis]
    return rows, cols, matrix


def unit_diagonal_reduction(matrix):
    """Integral row and column elementary operations; diagonal is Smith 1's.

    Every pivot is plus or minus one. Swaps, sign changes and integer
    additions preserve the isomorphism class of the integer cokernel.
    """
    a = [row[:] for row in matrix]
    m, n = len(a), len(a[0])
    rank = 0
    for k in range(min(m, n)):
        choice = next(((i, j) for i in range(k, m) for j in range(k, n)
                       if abs(a[i][j]) == 1), None)
        if choice is None:
            break
        i, j = choice
        a[k], a[i] = a[i], a[k]
        for row in a:
            row[k], row[j] = row[j], row[k]
        if a[k][k] == -1:
            a[k] = [-x for x in a[k]]
        for i in range(m):
            if i != k and a[i][k]:
                c = a[i][k]
                a[i] = [x - c * y for x, y in zip(a[i], a[k])]
        for j in range(n):
            if j != k and a[k][j]:
                c = a[k][j]
                for i in range(m):
                    a[i][j] -= c * a[i][k]
        rank += 1
    assert all(a[i][j] == (1 if i == j and i < rank else 0)
               for i in range(m) for j in range(n)), a
    return rank


def transfer_count():
    """Independent cyclic row-state transfer count; no simplicial enumeration."""
    compatible = lambda a, b: a == 0 or b == 0 or (a == b and a in (1, 2, 4))
    counts = [0] * (N + 1)
    for first in range(8):
        states = {first: [0] * (N + 1)}
        states[first][first.bit_count()] = 1
        for _ in range(1, LENGTH):
            new_states = {}
            for previous, polynomial in states.items():
                for current in range(8):
                    if not compatible(previous, current):
                        continue
                    dest = new_states.setdefault(current, [0] * (N + 1))
                    shift = current.bit_count()
                    for degree, coefficient in enumerate(polynomial[:N + 1 - shift]):
                        if coefficient:
                            dest[degree + shift] += coefficient
            states = new_states
        for last, polynomial in states.items():
            if compatible(last, first):
                for degree, coefficient in enumerate(polynomial):
                    counts[degree] += coefficient
    return counts


def verify():
    expected = json.loads((Path(__file__).resolve().parent / 'morse_matrices.json').read_text('utf-8'))
    assert len(expected) == 2
    assert all(ADJ[i] & (1 << i) == 0 for i in range(N))
    assert all((ADJ[i] >> j) & 1 == (ADJ[j] >> i) & 1 for i in range(N) for j in range(N))
    assert sum(x.bit_count() for x in ADJ) // 2 == 66
    all_faces = faces()
    face_sizes = Counter(s.bit_count() for s in all_faces)
    assert sum(face_sizes.values()) == 732802
    assert [face_sizes[i] for i in range(N + 1)] == transfer_count()
    outputs = []
    for name, order, certificate in zip(('ascending', 'descending'),
                                        (range(N), range(N - 1, -1, -1)), expected):
        partners, critical, pairs = stage_matching(all_faces, order)
        assert 2 * pairs + len(critical) == len(all_faces)
        assert pairs == 366383
        profile = Counter(s.bit_count() - 1 for s in critical)
        assert dict(profile) == {-1: 1, 0: 1, 6: 18, 7: 16}
        assert 0 in critical
        assert sum(1 for s in critical if s.bit_count() == 1) == 1
        incidences = check_acyclic(all_faces, partners)
        assert incidences == 5573766
        rows, cols, mat = signed_morse_boundary(critical, partners)
        assert certificate['label'] == name
        assert rows == certificate['rows']
        assert cols == certificate['columns']
        assert mat == certificate['matrix']
        assert certificate['faces'] == len(all_faces)
        assert certificate['pairs'] == pairs
        assert certificate['incidences'] == incidences
        assert {int(k): v for k,v in certificate['f_vector'].items()} == dict(Counter(s.bit_count()-1 for s in all_faces))
        assert {int(k): v for k,v in certificate['critical'].items()} == dict(profile)
        rank = unit_diagonal_reduction(mat)
        assert rank == 15
        assert certificate['smith'] == [1] * rank
        outputs.append({'matching': name, 'matched_pairs': pairs,
                        'critical_dimensions': dict(sorted(profile.items())),
                        'hasse_incidences_checked': incidences,
                        'morse_boundary_shape': [len(rows), len(cols)],
                        'integral_unit_pivots': rank,
                        'free_homology_ranks': {'6': len(rows) - rank, '7': len(cols) - rank}})
    return {'result': 'C11_K3_INDEPENDENCE_INTEGRAL_WEDGE_VERIFIED',
            'graph_vertices': N, 'graph_edges': 66, 'faces_including_empty': len(all_faces),
            'face_count_by_cardinality': {str(i): face_sizes[i] for i in range(N+1) if face_sizes[i]},
            'independent_transfer_agreement': True, 'certificates': outputs}


if __name__ == '__main__':
    print(json.dumps(verify(), sort_keys=True, separators=(',', ':')))
