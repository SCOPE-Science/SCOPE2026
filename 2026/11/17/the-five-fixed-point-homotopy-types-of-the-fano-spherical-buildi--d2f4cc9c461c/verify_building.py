#!/usr/bin/env python3
"""Exact subgroup and geometric-fixed-space census for the Fano incidence building.

Run: python verify_building.py --census census.json
Only the Python standard library is required.
"""
import argparse
import itertools
import json
from collections import Counter


def classify():
    points = range(1, 8)
    lines = sorted({tuple(sorted((a, b, a ^ b))) for a in points for b in points if a != b})
    line_index = {line: i for i, line in enumerate(lines)}
    assert len(lines) == 7 and all(len(line) == 3 for line in lines)

    # All invertible three-column binary matrices, represented by their action
    # on the seven nonzero vectors, supply the 168 type-preserving symmetries.
    seven_actions = []
    for a, b, c in itertools.product(points, repeat=3):
        if len({a, b, c, a ^ b, a ^ c, b ^ c, a ^ b ^ c}) == 7:
            seven_actions.append(tuple((a if i & 1 else 0) ^
                                       (b if i & 2 else 0) ^
                                       (c if i & 4 else 0) for i in points))
    seven_actions = sorted(set(seven_actions))
    assert len(seven_actions) == 168

    collineations = [
        tuple(p[i - 1] - 1 for i in points) +
        tuple(7 + line_index[tuple(sorted(p[i - 1] for i in line))] for line in lines)
        for p in seven_actions
    ]
    perpendicular = lambda x, y: (x & y).bit_count() % 2 == 0
    perpendicular_line = {
        x: line_index[tuple(i for i in points if perpendicular(x, i))]
        for x in points
    }
    line_normal = {j: next(x for x in points if perpendicular_line[x] == j)
                   for j in range(7)}
    polarity = (tuple(7 + perpendicular_line[x] for x in points) +
                tuple(line_normal[j] - 1 for j in range(7)))
    compose = lambda p, q: tuple(p[q[i]] for i in range(14))
    identity = tuple(range(14))
    assert compose(polarity, polarity) == identity
    group = sorted(set(collineations + [compose(polarity, p) for p in collineations]))
    index = {p: i for i, p in enumerate(group)}
    assert len(group) == 336
    e = index[identity]
    multiplication = [[index[compose(p, q)] for q in group] for p in group]
    inverse = [next(j for j in range(336) if multiplication[i][j] == e)
               for i in range(336)]

    flags = sorted((x - 1, 7 + j) for j, line in enumerate(lines) for x in line)
    flag_set = {frozenset(edge) for edge in flags}
    assert len(flags) == 21
    # Independent incidence verification for every one of the 336 permutations.
    assert all(frozenset([g[u], g[v]]) in flag_set
               for g in group for u, v in flags)

    # Enumerate *all* subgroups of the 168-element colour-preserving normal
    # subgroup by adjoining every available element to every discovered group.
    colour_preserving = frozenset(index[g] for g in collineations)
    colour_reversing = sorted(set(range(336)) - colour_preserving)
    small = {frozenset([e])}
    queue = [frozenset([e])]
    for H in queue:
        for t in colour_preserving:
            if t in H:
                continue
            moves = tuple(H) + (t,)
            generated, todo = {e}, [e]
            while todo:
                x = todo.pop()
                for y in moves:
                    z = multiplication[x][y]
                    if z not in generated:
                        generated.add(z)
                        todo.append(z)
            K = frozenset(generated)
            if K not in small:
                small.add(K)
                queue.append(K)
    assert len(small) == 179

    # Every subgroup meeting the other coset is H union Ht, where
    # H lies in the normal index-two group, t^2 lies in H, and t normalizes H.
    subgroups = set(small)
    for H in small:
        for t in colour_reversing:
            if multiplication[t][t] not in H:
                continue
            if any(multiplication[multiplication[t][h]][inverse[t]] not in H
                   for h in H):
                continue
            K = frozenset(set(H) | {multiplication[h][t] for h in H})
            assert len(K) == 2 * len(H)
            subgroups.add(K)
    assert len(subgroups) == 413
    assert all(inverse[x] in H for H in subgroups for x in H)
    assert all(multiplication[x][y] in H for H in subgroups for x in H for y in H)

    # Exact conjugacy partition by the full 336-element group.
    remaining = set(subgroups)
    classes = []
    while remaining:
        H = min(remaining, key=lambda h: (len(h), tuple(sorted(h))))
        conjugates = {
            frozenset(multiplication[multiplication[g][h]][inverse[g]] for h in H)
            for g in range(336)
        }
        assert conjugates <= remaining
        remaining -= conjugates
        # A deterministic representative: lexicographically minimum element set.
        H = min(conjugates, key=lambda h: tuple(sorted(h)))
        classes.append((H, len(conjugates)))
    assert len(classes) == 23

    def fixed_graph(H):
        fixed_vertices = [x for x in range(14)
                          if all(group[g][x] == x for g in H)]
        fixed_flags = [(u, v) for u, v in flags
                       if all(frozenset((group[g][u], group[g][v])) ==
                              frozenset((u, v)) for g in H)]
        # Fixed vertices of the barycentric subdivision are original vertices
        # fixed individually and flag midpoints fixed setwise. Fixed edges are
        # the incidences from fixed original vertices to fixed flag midpoints.
        fset = set(fixed_vertices)
        adjacencies = [(x, j) for j, edge in enumerate(fixed_flags)
                       for x in edge if x in fset]
        nv = len(fixed_vertices) + len(fixed_flags)
        parent = list(range(nv))

        def root(i):
            while i != parent[i]:
                i = parent[i]
            return i

        vmap = {x: i for i, x in enumerate(fixed_vertices)}
        for x, j in adjacencies:
            parent[root(vmap[x])] = root(len(fixed_vertices) + j)
        b0 = len({root(i) for i in range(nv)})
        b1 = len(adjacencies) - nv + b0
        assert b1 >= 0
        if nv == 0:
            kind = 'empty'
        elif b0 == 1 and b1 == 0:
            kind = 'contractible'
        elif b0 == 2 and b1 == 0:
            kind = 'S0'
        elif b0 == 3 and b1 == 0:
            kind = 'three_points'
        elif b0 == 1 and b1 == 8 and len(H) == 1:
            kind = 'wedge_8_circles'
        else:
            raise AssertionError(('Unexpected fixed-space type', nv, b0, b1))
        return (len(fixed_vertices), len(fixed_flags), len(adjacencies),
                b0, b1, kind)

    counts = Counter()
    census = []
    for H, class_size in classes:
        data = fixed_graph(H)
        reversed_type = any(group[g][0] >= 7 for g in H)
        # Independently check every conjugate subgroup (not just representatives).
        conjugates = {frozenset(multiplication[multiplication[g][h]][inverse[g]]
                                for h in H) for g in range(336)}
        assert len(conjugates) == class_size
        for K in conjugates:
            assert fixed_graph(K)[-1] == data[-1]
            counts[data[-1]] += 1
        census.append({
            'subgroup_order': len(H), 'conjugacy_class_size': class_size,
            'contains_duality': reversed_type,
            'representative_group_indices': sorted(H),
            'fixed_original_vertices': data[0], 'fixed_flag_midpoints': data[1],
            'fixed_barycentric_edges': data[2], 'components': data[3],
            'first_betti_number': data[4], 'homotopy_type': data[5]
        })
    assert sum(counts.values()) == 413
    assert dict(counts) == {
        'wedge_8_circles': 1, 'contractible': 210, 'S0': 56,
        'three_points': 28, 'empty': 118
    }
    census.sort(key=lambda row: (row['contains_duality'],
                                 row['subgroup_order'],
                                 row['homotopy_type'],
                                 row['representative_group_indices']))
    return {'group_order': len(group), 'type_preserving_subgroups': len(small),
            'all_subgroups': len(subgroups), 'conjugacy_classes': len(classes),
            'type_counts': dict(sorted(counts.items())), 'census': census}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--census', help='write the exact 23-conjugacy-class JSON census')
    args = ap.parse_args()
    result = classify()
    if args.census:
        with open(args.census, 'w', encoding='utf8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2, sort_keys=True)
            f.write('\n')
    for key in ('group_order', 'type_preserving_subgroups', 'all_subgroups', 'conjugacy_classes'):
        print(f'{key}={result[key]}')
    for kind, count in sorted(result['type_counts'].items()):
        print(f'{kind}={count}')
    print('FANO_BUILDING_FULL_SUBGROUP_FIXED_SPACES_PASS')


if __name__ == '__main__':
    main()
