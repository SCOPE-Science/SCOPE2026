#!/usr/bin/env python3
"""Exact full-symmetry quotient collapse of the cube matching complex.

Requires Python 3.9+ standard library only. No external file is needed beyond
collapse_certificate.json. All finite spaces are rebuilt from definitions.
"""
import itertools
import json
from collections import Counter
from pathlib import Path
import sys


def cube_edges():
    return tuple((u, u ^ (1 << j)) for u in range(8) for j in range(3)
                 if not (u & (1 << j)))


def cube_edge_automorphisms(edges):
    index = {e: i for i, e in enumerate(edges)}
    perms = set()
    for coordinate_perm in itertools.permutations(range(3)):
        for shift in range(8):
            vertex_map = [shift ^ sum(((u >> j) & 1) << coordinate_perm[j]
                                       for j in range(3)) for u in range(8)]
            edge_perm = tuple(index[tuple(sorted((vertex_map[a], vertex_map[b])))]
                              for a, b in edges)
            perms.add(edge_perm)
    assert len(perms) == 48
    assert all(set(p) == set(range(12)) for p in perms)
    return sorted(perms)


def matching_masks(edges):
    masks = []
    for mask in range(1, 1 << len(edges)):
        endpoints = []
        for i, edge in enumerate(edges):
            if (mask >> i) & 1:
                endpoints.extend(edge)
        if len(endpoints) == len(set(endpoints)):
            masks.append(mask)
    assert len(masks) == 107
    return masks


def all_chains(matchings):
    strict_supersets = {m: [n for n in matchings
                            if m != n and (m & n) == m] for m in matchings}
    result = []
    def visit(chain):
        result.append(tuple(chain))
        for m in strict_supersets[chain[-1]]:
            visit(chain + [m])
    for m in matchings:
        visit([m])
    assert len(result) == 1385
    return result


def orbit_complex():
    edges = cube_edges()
    assert len(edges) == 12
    group = cube_edge_automorphisms(edges)
    matchings = matching_masks(edges)
    chains = all_chains(matchings)
    image = {}
    def transform(m, p):
        key = (m, p)
        if key not in image:
            image[key] = sum(1 << p[i] for i in range(12) if (m >> i) & 1)
        return image[key]
    memo = {}
    def canonical(chain):
        chain = tuple(chain)
        if chain not in memo:
            memo[chain] = min(tuple(transform(m, p) for m in chain) for p in group)
        return memo[chain]
    cells = sorted(set(canonical(c) for c in chains), key=lambda x: (len(x), x))
    assert len(cells) == 55
    assert Counter(len(c)-1 for c in cells) == {0:9, 1:21, 2:19, 3:6}
    ids = {c: i for i, c in enumerate(cells)}
    facets = {ids[c]: tuple(ids[canonical(c[:j]+c[j+1:])]
                        for j in range(len(c))) for c in cells if len(c) > 1}
    # All barycentric simplex face orbits are present.
    assert all(len(facets[i]) == len(cells[i]) for i in facets)
    assert all(i not in facets[i] for i in facets)
    return cells, facets


def verify_collapse(cells, facets, pairs):
    active = set(range(len(cells)))
    assert len(pairs) == 27
    for step, item in enumerate(pairs, 1):
        assert isinstance(item, list) and len(item) == 2, (step, item)
        free, top = item
        assert free in active and top in active, (step, free, top)
        assert len(cells[top]) == len(cells[free]) + 1
        # The face must occur exactly once in the ENTIRE active boundary,
        # including repeated incidences of a single orbit simplex.
        incidences = [c for c in active if c in facets
                      for f in facets[c] if f == free]
        assert incidences == [top], (step, free, top, incidences)
        # The corresponding top simplex must be maximal, not a face of another.
        assert not any(top in facets[c] for c in active if c in facets), (step, top)
        active.difference_update((free, top))
        # Every surviving simplex keeps every codimension-one face.
        assert all(all(f in active for f in facets[c]) for c in active
                   if c in facets), (step, 'noncomplex residual')
    assert len(active) == 1 and len(cells[next(iter(active))]) == 1
    return next(iter(active))


def make_certificate(cells, facets):
    active = set(range(len(cells)))
    pairs = []
    while len(active) > 1:
        possibilities = []
        for top in sorted(active):
            if top not in facets:
                continue
            if any(top in facets[c] for c in active if c in facets):
                continue
            for face in facets[top]:
                if face not in active:
                    continue
                frequency = sum(facets[c].count(face) for c in active if c in facets)
                if frequency == 1:
                    possibilities.append((face, top))
        assert possibilities, ('stalled', len(active))
        free, top = min(possibilities, key=lambda ft: (-len(cells[ft[0]]), ft))
        pairs.append([free, top])
        active.difference_update((free, top))
    return pairs


def main():
    cells, facets = orbit_complex()
    path = Path(__file__).resolve().parent / 'collapse_certificate.json'
    if len(sys.argv) > 1 and sys.argv[1] == '--make':
        obj = {'description':'Cube matching-complex quotient: elementary CW collapses',
               'edge_order':list(map(list,cube_edges())),
               'orbit_cells':len(cells),'facet_count_by_dimension':[9,21,19,6],
               'pairs':make_certificate(cells, facets)}
        path.write_text(json.dumps(obj, sort_keys=True, indent=2) + '\n',encoding='utf-8')
    obj = json.loads(path.read_text(encoding='utf-8'))
    assert obj['orbit_cells'] == len(cells)
    assert obj['edge_order'] == list(map(list, cube_edges()))
    assert obj['facet_count_by_dimension'] == [9,21,19,6]
    remaining = verify_collapse(cells, facets, obj['pairs'])
    print('CUBE_MATCHING_FULL_QUOTIENT_COLLAPSES_OK',
          f'group=48 matchings=107 flags=1385 cells=55 pairs=27 last_vertex={remaining}')

if __name__=='__main__':
    main()
