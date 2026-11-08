#!/usr/bin/env python3
"""Reproduce the geometric fixed-space Morse certificate for the Fano incidence graph.

Uses only Python's standard library. Run beside morse_certificate.json.
"""
import json
from collections import deque, defaultdict
from itertools import combinations
from pathlib import Path


def parity_dot(a, b):
    return (a & b).bit_count() % 2


def faces_of_orbit_complex(edge_labels):
    faces = {()}
    for k in range(1, len(edge_labels) + 1):
        for face in combinations(range(len(edge_labels)), k):
            occupied = set()
            valid = True
            for j in face:
                for p in set(edge_labels[j]):
                    if p in occupied:
                        valid = False
                        break
                    occupied.add(p)
                if not valid:
                    break
            if valid:
                faces.add(face)
    return faces


def full_incidence_matching_faces(incidences):
    result = {()}
    # Independent enumeration: extend edge matchings by increasing edge index.
    def recurse(current, used_points, used_lines, minimum):
        for j in range(minimum, len(incidences)):
            p, ell = incidences[j]
            if not ((used_points >> p) & 1 or (used_lines >> ell) & 1):
                extension = current + (j,)
                result.add(extension)
                recurse(extension, used_points | (1 << p),
                        used_lines | (1 << ell), j + 1)
    recurse((), 0, 0, 0)
    return result


def morse_matching(nonempty, order):
    unmatched = set(nonempty)
    pairs = []
    for index in order:
        for lower in sorted(unmatched, key=lambda f: (len(f), f)):
            if index in lower:
                continue
            upper = tuple(sorted(lower + (index,)))
            if upper in unmatched:
                unmatched.remove(lower)
                unmatched.remove(upper)
                pairs.append((lower, upper))
    return pairs, unmatched


def verify_acyclic(nonempty, pairs):
    pair_set = set(pairs)
    outgoing = {f: [] for f in nonempty}
    indegree = {f: 0 for f in nonempty}
    count = 0
    for upper in nonempty:
        for i in range(len(upper)):
            lower = upper[:i] + upper[i + 1:]
            if not lower:
                continue
            if (lower, upper) in pair_set:
                origin, target = lower, upper
            else:
                origin, target = upper, lower
            outgoing[origin].append(target)
            indegree[target] += 1
            count += 1
    frontier = deque(f for f in nonempty if indegree[f] == 0)
    visited = 0
    while frontier:
        f = frontier.popleft()
        visited += 1
        for g in outgoing[f]:
            indegree[g] -= 1
            if indegree[g] == 0:
                frontier.append(g)
    assert visited == len(nonempty), (visited, len(nonempty))
    return count, visited


def rank_two(columns):
    pivots = {}
    for col in columns:
        while col:
            high = col.bit_length() - 1
            if high in pivots:
                col ^= pivots[high]
            else:
                pivots[high] = col
                break
    return len(pivots)


def mod_two_ranks(nonempty):
    by_dim = defaultdict(list)
    for f in nonempty:
        by_dim[len(f) - 1].append(f)
    out = []
    for dim in range(1, 4):
        prior = {face: i for i, face in enumerate(by_dim[dim - 1])}
        columns = []
        for face in by_dim[dim]:
            col = 0
            for j in range(len(face)):
                col ^= 1 << prior[face[:j] + face[j + 1:]]
            columns.append(col)
        out.append(rank_two(columns))
    return [len(by_dim[i]) for i in range(4)], out


def main():
    c = json.loads(Path(__file__).with_name('morse_certificate.json').read_text(encoding='utf-8'))
    points = range(1, 8)
    # Heawood graph: p_a is incident with L_b iff a dot b = 0 in F_2^3.
    incidences = sorted((a, b) for a in points for b in points if parity_dot(a, b) == 0)
    assert len(incidences) == 21
    edge_to_index = {edge: index for index, edge in enumerate(incidences)}
    assert all(sum(parity_dot(a, b) == 0 for b in points) == 3 for a in points)
    # The polarity interchanges p_a and L_a, carrying edge (a,b) to edge (b,a).
    tau = [edge_to_index[b, a] for (a, b) in incidences]
    assert all(tau[tau[j]] == j for j in range(21))
    orbits = []
    seen = set()
    for j in range(len(incidences)):
        if j not in seen:
            orbit = tuple(sorted({j, tau[j]}))
            orbits.append(orbit)
            seen.update(orbit)
    assert len(orbits) == 12
    labels = [tuple(sorted(incidences[orbit[0]])) for orbit in orbits]
    assert sorted(labels) == sorted(tuple(t) for t in c['orbit_edge_labels'])
    # Reorder orbits canonically by the two endpoint labels, including loops.
    orbits = [orbit for _, orbit in sorted(zip(labels, orbits))]
    labels = sorted(labels)
    assert labels == [tuple(x) for x in c['orbit_edge_labels']]
    orbit_faces = faces_of_orbit_complex(labels)
    nonempty = orbit_faces - {()}
    assert len(nonempty) == 137

    # Build all original matching simplices (3461) without using orbit restrictions.
    original_faces = full_incidence_matching_faces(incidences)
    assert len(original_faces) == 3462
    original_invariant = set()
    for face in original_faces:
        if {tau[i] for i in face} == set(face):
            original_invariant.add(face)
    expanded = {tuple(sorted(i for orbit_id in face for i in orbits[orbit_id])) for face in orbit_faces}
    assert original_invariant == expanded
    assert len(original_invariant) == 138

    order = c['toggle_order']
    assert sorted(order) == list(range(12))
    pairs, critical = morse_matching(nonempty, order)
    expected = {tuple(x) for x in c['critical_faces']}
    assert critical == expected
    assert len(pairs) == 66
    assert sorted(len(f) for f in critical) == [1, 3, 3, 3, 3]
    assert not set(f for pair in pairs for f in pair) & critical
    cover_count, visited = verify_acyclic(nonempty, pairs)
    f_vector, ranks = mod_two_ranks(nonempty)
    assert f_vector == [12, 45, 59, 21]
    assert ranks == [11, 34, 21]
    assert c['expected_face_vector'] == f_vector
    assert c['expected_boundary_ranks_mod2'] == ranks
    print('POLARITY_HEAWOOD_FIXED_MORSE_OK')
    print('heawood_edges=21 edge_orbits=12 original_matching_faces_including_empty=3462')
    print('fixed_faces_including_empty=138 face_vector=' + str(f_vector))
    print('morse_pairs=66 critical_dimensions=[0,2,2,2,2] hasse_covers=' + str(cover_count))
    print('complete_acyclicity_sort=' + str(visited) + '/137 mod2_boundary_ranks=' + str(ranks))
    print('geometric_fixed_homotopy=wedge_of_four_2_spheres')


if __name__ == '__main__':
    main()
