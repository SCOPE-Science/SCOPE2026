#!/usr/bin/env python3
"""Exact finite verification of the bidirected theta multipath complex.

Python 3 standard library only. All faces and Hasse incidences are checked;
no random tests, floating-point ranks, or external certificates are used.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import permutations
import json

M, N = 2, 3
VERTICES = tuple([('A', a) for a in range(M)] + [('B', b) for b in range(N)])
ARCS = tuple((('A', a), ('B', b)) if direction == 0
             else (('B', b), ('A', a))
             for a in range(M) for b in range(N) for direction in range(2))
NUM_ARCS = len(ARCS)
assert NUM_ARCS == 12


def selected_indices(mask):
    return [i for i in range(NUM_ARCS) if (mask >> i) & 1]


def oriented_boundary(face):
    """Ordinary simplicial boundary over the integers, indexed by arc order."""
    for pos, bit in enumerate(selected_indices(face)):
        yield face ^ (1 << bit), (-1 if pos % 2 else 1)


def path_faces_directed():
    """Exhaustive criterion: at most one in/out at every vertex; no directed cycles."""
    faces = set()
    for mask in range(1 << NUM_ARCS):
        incoming, outgoing = {}, {}
        valid = True
        for i in selected_indices(mask):
            source, target = ARCS[i]
            if source in outgoing or target in incoming:
                valid = False
                break
            outgoing[source] = target
            incoming[target] = source
        if not valid:
            continue
        for starting_vertex in outgoing:
            current = starting_vertex
            visited = set()
            while current in outgoing:
                if current in visited:
                    valid = False
                    break
                visited.add(current)
                current = outgoing[current]
            if not valid:
                break
        if valid:
            faces.add(mask)
    return faces


def path_faces_union_find():
    """Independent enumeration via collision-free directed forest and union-find."""
    faces = set()
    for mask in range(1 << NUM_ARCS):
        parent = {v: v for v in VERTICES}
        def find(v):
            while parent[v] != v:
                v = parent[v]
            return v
        sources, targets = set(), set()
        valid = True
        for i in selected_indices(mask):
            source, target = ARCS[i]
            if source in sources or target in targets:
                valid = False
                break
            sources.add(source)
            targets.add(target)
            a, b = find(source), find(target)
            if a == b:
                valid = False
                break
            parent[a] = b
        if valid:
            faces.add(mask)
    return faces


def matching(faces):
    """Coordinate-matching filtration, ignoring the empty face."""
    rest = faces - {0}
    pairs = []
    for bit in range(NUM_ARCS):
        bitmask = 1 << bit
        round_pairs = [(low, low | bitmask)
                       for low in sorted(rest)
                       if not (low & bitmask) and (low | bitmask) in rest]
        for low, high in round_pairs:
            rest.remove(low)
            rest.remove(high)
        pairs.extend(round_pairs)
    return pairs, rest


def oriented_hasse_acyclic(faces, pairs):
    matched = set(pairs)
    graph = {face: [] for face in faces if face}
    indegree = {face: 0 for face in graph}
    covering = 0
    for face in graph:
        for codimension_one, _ in oriented_boundary(face):
            if not codimension_one:
                continue
            covering += 1
            source, target = ((codimension_one, face)
                              if (codimension_one, face) in matched
                              else (face, codimension_one))
            graph[source].append(target)
            indegree[target] += 1
    q = deque(k for k, v in indegree.items() if v == 0)
    seen = 0
    while q:
        v = q.popleft()
        seen += 1
        for w in graph[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                q.append(w)
    assert covering == 276
    assert seen == len(graph), (seen, len(graph))
    return covering


def boundary_ranks_mod_two(faces):
    by_dim = {d: sorted(f for f in faces if f.bit_count() - 1 == d)
              for d in range(4)}
    ranks = {}
    for d in range(1, 4):
        idx = {f: i for i, f in enumerate(by_dim[d - 1])}
        pivots = {}
        for face in by_dim[d]:
            col = 0
            for facet, _ in oriented_boundary(face):
                col ^= 1 << idx[facet]
            while col:
                lead = col.bit_length() - 1
                if lead not in pivots:
                    pivots[lead] = col
                    break
                col ^= pivots[lead]
        ranks[d] = len(pivots)
    assert ranks == {1: 11, 2: 30, 3: 12}, ranks
    return ranks


def morse_projection(pairs, crit):
    paired_up = {low: high for low, high in pairs}
    paired_down = {high: low for low, high in pairs}
    @lru_cache(maxsize=None)
    def project(face):
        if face in crit:
            return {face: 1}
        if face in paired_down:
            return {}
        if face not in paired_up:
            raise AssertionError(('face not matched or critical', face))
        upper = paired_up[face]
        oriented_facets = list(oriented_boundary(upper))
        incidence = next(s for f, s in oriented_facets if f == face)
        result = {}
        for facet, sign in oriented_facets:
            if facet == face:
                continue
            for critical, value in project(facet).items():
                result[critical] = result.get(critical, 0) - incidence * sign * value
                if not result[critical]:
                    del result[critical]
        return result
    return project


def morse_differential(crit, proj):
    coefficients = {}
    for cell in sorted(crit):
        if cell.bit_count() <= 1:
            continue
        image = {}
        for facet, sign in oriented_boundary(cell):
            for lower_cell, value in proj(facet).items():
                image[lower_cell] = image.get(lower_cell, 0) + sign * value
                if not image[lower_cell]:
                    del image[lower_cell]
        coefficients[cell] = image
    assert all(not image for image in coefficients.values()), coefficients
    return coefficients


def sign_of_permutation(indices):
    count = sum(indices[i] > indices[j]
                for i in range(len(indices)) for j in range(i + 1, len(indices)))
    return (-1) ** count


def symmetry_action(row_permutation, leaf_permutation, reversal):
    arc_index = {arc: i for i, arc in enumerate(ARCS)}
    def transform_vertex(v):
        kind, j = v
        return ((kind, row_permutation[j]) if kind == 'A'
                else (kind, leaf_permutation[j]))
    perm = []
    for a, b in ARCS:
        p, q = (transform_vertex(b), transform_vertex(a)) if reversal else (transform_vertex(a), transform_vertex(b))
        perm.append(arc_index[(p, q)])
    assert sorted(perm) == list(range(NUM_ARCS))
    return perm


def transform_simplex(face, action):
    dest = [action[i] for i in selected_indices(face)]
    return sum(1 << j for j in dest), sign_of_permutation(dest)


def one_cycle_and_cocycle(faces, pairs, crit, proj):
    unique_critical_edge = next(face for face in crit if face.bit_count() == 2)
    matched_edges = [(low, high) for low, high in pairs
                     if low.bit_count() == 1 and high.bit_count() == 2]
    assert len(matched_edges) == NUM_ARCS - 1
    graph = {i: [] for i in range(NUM_ARCS)}
    for vertex, edge in matched_edges:
        i, j = selected_indices(edge)
        graph[i].append((j, edge))
        graph[j].append((i, edge))
    i, j = selected_indices(unique_critical_edge)
    q = deque([(i, [])])
    visited = {i}
    path = None
    while q:
        v, steps = q.popleft()
        if v == j:
            path = steps
            break
        for w, edge in graph[v]:
            if w not in visited:
                visited.add(w)
                q.append((w, steps + [(v, w, edge)]))
    assert path is not None
    one_cycle = {unique_critical_edge: 1}
    for v, w, edge in path:
        s = 1 if selected_indices(edge) == [v, w] else -1
        one_cycle[edge] = one_cycle.get(edge, 0) - s
    def chain_boundary(chain):
        result = {}
        for face, coefficient in chain.items():
            for facet, sign in oriented_boundary(face):
                result[facet] = result.get(facet, 0) + coefficient * sign
        return {cell: value for cell, value in result.items() if value}
    assert not chain_boundary(one_cycle)
    def cocycle(edge):
        return proj(edge).get(unique_critical_edge, 0)
    assert sum(coefficient * cocycle(edge) for edge, coefficient in one_cycle.items()) == 1
    for triangle in (f for f in faces if f.bit_count() == 3):
        assert sum(sign * cocycle(edge) for edge, sign in oriented_boundary(triangle)) == 0
    return one_cycle, cocycle


def compute_characters(faces, one_cycle, cocycle):
    characters = {}
    class_counts = Counter()
    for row in permutations(range(M)):
        for leaf in permutations(range(N)):
            for reverse in range(2):
                action = symmetry_action(row, leaf, reverse)
                assert all(transform_simplex(f, action)[0] in faces for f in faces)
                trace1 = sum(value * cocycle(transform_simplex(edge, action)[0]) * transform_simplex(edge, action)[1]
                             for edge, value in one_cycle.items())
                reduced_lefschetz = sum((-1) ** (f.bit_count() - 1) * transform_simplex(f, action)[1]
                                        for f in faces if f and transform_simplex(f, action)[0] == f) - 1
                trace2 = reduced_lefschetz + trace1
                kind = ('id' if leaf == (0, 1, 2)
                        else '3cycle' if all(leaf[i] != i for i in range(3))
                        else 'transposition')
                key = (int(row != (0, 1)), kind, reverse)
                if key in characters:
                    assert characters[key] == (trace1, trace2), (key, characters[key], (trace1, trace2))
                characters[key] = (trace1, trace2)
                class_counts[key] += 1
    assert len(characters) == 12
    assert sum(class_counts.values()) == 24
    # Character table of the rational representations, computed independently
    # from the irreducible characters 1, sign and standard of S3.
    for (hub_swap, leaf_class, reversal), (h1, h2) in characters.items():
        std = {'id': 2, 'transposition': 0, '3cycle': -1}[leaf_class]
        sign = -1 if leaf_class == 'transposition' else 1
        chi = (-1) ** (hub_swap ^ reversal)
        assert h1 == sign
        assert h2 == (1 + std) + chi * (sign + std)
    assert characters == {
        (0, 'id', 0): (1, 6), (0, 'id', 1): (1, 0),
        (0, 'transposition', 0): (-1, 0), (0, 'transposition', 1): (-1, 2),
        (0, '3cycle', 0): (1, 0), (0, '3cycle', 1): (1, 0),
        (1, 'id', 0): (1, 0), (1, 'id', 1): (1, 6),
        (1, 'transposition', 0): (-1, 2), (1, 'transposition', 1): (-1, 0),
        (1, '3cycle', 0): (1, 0), (1, '3cycle', 1): (1, 0),
    }, characters
    return characters


def main():
    faces = path_faces_directed()
    assert faces == path_faces_union_find()
    fvector = {str(d): sum(f.bit_count() - 1 == d for f in faces)
               for d in [-1, 0, 1, 2, 3]}
    assert fvector == {'-1': 1, '0': 12, '1': 42, '2': 48, '3': 12}
    assert len(faces) == 115
    assert all((f ^ (1 << i)) in faces for f in faces for i in selected_indices(f))
    pairs, crit = matching(faces)
    assert len(pairs) == 53 and len(crit) == 8
    critical_by_dim = {str(d): sum(f.bit_count() - 1 == d for f in crit) for d in range(4)}
    assert critical_by_dim == {'0': 1, '1': 1, '2': 6, '3': 0}
    hasse_count = oriented_hasse_acyclic(faces, pairs)
    mod2_ranks = boundary_ranks_mod_two(faces)
    projection = morse_projection(pairs, crit)
    morse = morse_differential(crit, projection)
    cycle, cocycle = one_cycle_and_cocycle(faces, pairs, crit, projection)
    characters = compute_characters(faces, cycle, cocycle)
    print(json.dumps({
        'face_vector': fvector,
        'nonempty_faces': len(faces) - 1,
        'hasse_incidences': hasse_count,
        'matched_pairs': len(pairs),
        'critical_cells': critical_by_dim,
        'critical_masks': sorted(crit),
        'nonzero_morse_boundary_coefficients': sum(len(x) for x in morse.values()),
        'mod2_boundary_ranks': {str(k): v for k, v in mod2_ranks.items()},
        'one_cycle_support': len(cycle),
        'automorphisms_checked': 24,
        'conjugacy_characters': [
            {'hub_swap': h, 'leaf_class': leaf, 'arc_reversal': r, 'H1_trace': characters[(h, leaf, r)][0], 'H2_trace': characters[(h, leaf, r)][1]}
            for h in range(2) for leaf in ['id', 'transposition', '3cycle'] for r in range(2)
        ],
        'status': 'ALL_EXACT_CHECKS_PASSED'
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
