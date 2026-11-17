#!/usr/bin/env python3
"""Finite sanity checks for quotient flags and collapses; no infinite proof is delegated to enumeration."""
from itertools import combinations, permutations
from collections import Counter


def verify_dimension(d):
    vertices = range(1 << d)
    edges = [(u, u ^ (1 << j)) for u in vertices for j in range(d)
             if u < (u ^ (1 << j))]
    cells = []
    for u, v in combinations(vertices, 2):
        cells.append((('v', u), ('v', v)))
    for u, v in edges:
        for w in vertices:
            if w not in (u, v):
                cells.append(tuple(sorted((('e', u, v), ('v', w)))))
    for (u, v), (w, z) in combinations(edges, 2):
        if len({u, v, w, z}) == 4:
            cells.append(tuple(sorted((('e', u, v), ('e', w, z)))))
    cell_index = {c: i for i, c in enumerate(cells)}
    codim1 = []
    for cell in cells:
        boundary = []
        for j, part in enumerate(cell):
            if part[0] == 'e':
                for endpoint in part[1:]:
                    sub = tuple(sorted(cell[:j] + (('v', endpoint),) + cell[j+1:]))
                    boundary.append(cell_index[sub])
        codim1.append(boundary)
    flags = set((i,) for i in range(len(cells)))
    for i in range(len(cells)):
        for j in codim1[i]:
            flags.add((j, i))
            for k in codim1[j]:
                flags.add((k, j, i))
                flags.add((k, i))
    flags = sorted(flags, key=lambda x: (len(x), x))
    flag_index = {f: i for i, f in enumerate(flags)}
    group = []
    for p in permutations(range(d)):
        for b in vertices:
            group.append(tuple(sum(((x >> j) & 1) << p[j] for j in range(d)) ^ b
                               for x in vertices))
    assert len(group) == (1 << d) * __import__('math').factorial(d)
    orbit = [-1] * len(flags)
    for k, flag in enumerate(flags):
        if orbit[k] >= 0:
            continue
        for g in group:
            mapped = []
            for idx in flag:
                parts = []
                for part in cells[idx]:
                    if part[0] == 'v':
                        parts.append(('v', g[part[1]]))
                    else:
                        parts.append(('e',) + tuple(sorted((g[part[1]], g[part[2]]))))
                mapped.append(cell_index[tuple(sorted(parts))])
            orbit[flag_index[tuple(mapped)]] = k
    assert all(x >= 0 for x in orbit)
    reps = {k: flags[k] for k in sorted(set(orbit))}
    levels = [{k for k, x in reps.items() if len(x) == n} for n in (1, 2, 3)]
    assert tuple(map(len, levels)) == (4*d-4, 10*d-15, 6*d-10)

    def suborbit(flag):
        return orbit[flag_index[flag]]

    triangles = set(levels[2]); links = set(levels[1]); points = set(levels[0])
    triangle_pairs = 0
    while True:
        incidences = {e: [] for e in links}
        for t in triangles:
            tri = reps[t]
            for j in range(3):
                e = suborbit(tri[:j] + tri[j+1:])
                if e in incidences:
                    incidences[e].append(t)
        free = next(((e, ts[0]) for e, ts in sorted(incidences.items())
                     if len(ts) == 1), None)
        if free is None:
            break
        e, t = free
        triangles.remove(t); links.remove(e); triangle_pairs += 1
    assert not triangles and triangle_pairs == 6*d-10

    edge_pairs = 0
    while True:
        incidences = {v: [] for v in points}
        for edge in links:
            for idx in reps[edge]:
                incidences[suborbit((idx,))].append(edge)
        free = next(((v, es[0]) for v, es in sorted(incidences.items())
                     if len(es) == 1), None)
        if free is None:
            break
        v, e = free
        points.remove(v); links.remove(e); edge_pairs += 1
    assert len(points) == 1 and not links and edge_pairs == 4*d-5

    # Directly check the stabilizers of a parallel pair and a perpendicular pair.
    for r in range(1, d):
        y = sum(1 << j for j in range(1, r+1))
        e1 = (0, 1); e2 = (y, y+1)
        assert stabilizer_size(group, e1, e2) == 4
    for r in range(1, d-1):
        y = sum(1 << j for j in range(2, r+2))
        e1 = (0, 1); e2 = (y, y+2)
        assert stabilizer_size(group, e1, e2) == 2
    return len(cells), len(flags), tuple(map(len, levels)), triangle_pairs, edge_pairs


def stabilizer_size(group, e1, e2):
    # Kernel permutations of unused coordinates may stabilize the cell.
    # Count *distinct parameter actions*, not stabilizer group elements.
    actions = set()
    original = {tuple(sorted(e1)), tuple(sorted(e2))}
    for g in group:
        images = {tuple(sorted((g[e1[0]], g[e1[1]]))),
                  tuple(sorted((g[e2[0]], g[e2[1]])))}
        if images != original:
            continue
        action = []
        for a, b in ((0, 0), (0, 1), (1, 0), (1, 1)):
            u, v = g[e1[a]], g[e2[b]]
            action.append((e1.index(u) if u in e1 else e1.index(v),
                           e2.index(v) if v in e2 else e2.index(u)))
        actions.add(tuple(action))
    return len(actions)


if __name__ == '__main__':
    for dimension in range(2, 6):
        cells, flags, fvector, t, e = verify_dimension(dimension)
        print(f'd={dimension}: cubical_cells={cells}, flags={flags}, '
              f'quotient_f={fvector}, collapses=({t},{e}): PASS')
    print('HYPERCUBE_TWO_POINT_QUOTIENT_CHECK_OK')
